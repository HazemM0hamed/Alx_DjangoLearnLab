from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
from rest_framework.test import APIClient
from django.test import TestCase

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Create a sample book
        self.book = Book.objects.create(title='Sample Book', author='Author', publication_year=2023)

    def test_get_books_authenticated(self):
        # Send GET request to the books endpoint
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_authenticated(self):
        # Send POST request to create a new book
        response = self.client.post('/api/books/', {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2024
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class BookAPITests(APITestCase):

    def setUp(self):
        """Set up initial data for the tests."""
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )

    def test_create_book(self):
        """Test creating a book."""
        url = reverse('book-list')  # Ensure the URL name corresponds to the routing in urls.py
        data = {
            'title': 'New Book',
            'publication_year': 2020,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, 'New Book')

    def test_list_books(self):
        """Test listing all books."""
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Harry Potter and the Philosopher\'s Stone')

    def test_update_book(self):
        """Test updating a book."""
        url = reverse('book-detail', args=[self.book.id])
        data = {
            'title': 'Updated Title',
            'publication_year': 2001,
            'author': self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')
        self.assertEqual(self.book.publication_year, 2001)

    def test_delete_book(self):
        """Test deleting a book."""
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_search_books(self):
        """Test searching for a book by title."""
        url = f'{reverse("book-list")}?search=Harry'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Harry Potter and the Philosopher\'s Stone')

    def test_filter_books_by_author(self):
        """Test filtering books by author."""
        url = f'{reverse("book-list")}?author__name=J.K. Rowling'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author']['name'], 'J.K. Rowling')

    def test_order_books_by_year(self):
        """Test ordering books by publication year."""
        url = f'{reverse("book-list")}?ordering=publication_year'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more books and test ordering later
