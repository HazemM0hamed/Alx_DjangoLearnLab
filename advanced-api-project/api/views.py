from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.urls import reverse
from datetime import date
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Author
from django.contrib.auth.models import User
from django_filters import rest_framework
from rest_framework.permissions import AllowAny

# ListView: Retrieve all books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    
    # Add filtering options
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author__name', 'publication_year']  # Filter by title, author name, and publication year
    filter_backends = [filters.SearchFilter]  # Add SearchFilter
    search_fields = ['title', 'author__name']  # Allow searching by title or author's name
    filter_backends = [filters.OrderingFilter]  # Add OrderingFilter
    ordering_fields = ['title', 'publication_year']  # Users can order by title or publication year
    ordering = ['title']
    
    #This view handles retrieving and creating Book instances. It includes the following advanced query capabilities:
    
    #- Filtering: Users can filter books by title, author name, and publication year.Example: /books/?title=Example&author__name=John&publication_year=2022
    
    #- Searching: Users can perform text searches on the title and author name fields.Example: /books/?search=Example
    
    #- Ordering: Users can order the results by title or publication year.Example: /books/?ordering=title or /books/?ordering=-publication_year (for descending order)

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create
    
    def perform_create(self, serializer):
        # Custom validation: Ensure publication year is not in the future
        publication_year = serializer.validated_data['publication_year']
        current_year = datetime.date.today().year
        
        if publication_year > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        
        # If validation passes, save the book instance
        serializer.save()

# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update
    
    def perform_update(self, serializer):
        # Custom validation: Ensure publication year is not in the future
        publication_year = serializer.validated_data['publication_year']
        current_year = datetime.date.today().year
        
        if publication_year > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        
        # If validation passes, update the book instance
        serializer.save()

# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete

#  This view handles the creation of new Book instances. It is restricted to authenticated users, and it includes custom validation logic to ensure that the publication year is valid.

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test author
        self.author = Author.objects.create(name='Author 1')

        # Create some test books
        self.book1 = Book.objects.create(title='Book 1', publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title='Book 2', publication_year=2019, author=self.author)

        # Set up the API client
        self.client = APIClient()

    def authenticate(self):
        self.client.login(username='testuser', password='testpassword')

    def test_create_book(self):
        # Authenticate the user
        self.authenticate()

        # Data for creating a new book
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id
        }

        response = self.client.post(reverse('book-create'), data, format='json')

        # Check the status code and data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # 2 books from setUp, plus the new one
        self.assertEqual(Book.objects.get(id=3).title, 'New Book')

    def test_retrieve_book_list(self):
        response = self.client.get(reverse('book-list'), format='json')
        
        # Check status code and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should return 2 books

    def test_filter_books_by_title(self):
        response = self.client.get(reverse('book-list'), {'title': 'Book 1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book 1')

    def test_search_books_by_author(self):
        response = self.client.get(reverse('book-list'), {'search': 'Author 1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_publication_year(self):
        response = self.client.get(reverse('book-list'), {'ordering': 'publication_year'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book 2')  # Oldest book first

    def test_update_book(self):
        self.authenticate()

        data = {
            'title': 'Updated Book',
            'publication_year': 2020,
            'author': self.author.id
        }

        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book1.pk}), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_delete_book(self):
        self.authenticate()

        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book1.pk}))

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Only 1 book should remain

    def test_create_book_without_authentication(self):
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2022,
            'author': self.author.id
        }

        response = self.client.post(reverse('book-create'), data, format='json')

        # Ensure that a 403 Forbidden status is returned
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#This class contains unit tests for the Book API endpoints, including:
    
 #   - Test the CRUD operations for the Book model.
  #  - Test filtering, searching, and ordering of books.
   # - Test permission and authentication rules on endpoints.
    
    #Each test simulates an API request and checks the response's status code, 
    #response data integrity, and the correct functioning of advanced query features.