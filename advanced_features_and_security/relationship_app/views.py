from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Book, Library, UserProfile
from .forms import BookForm

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Query to get all books
    return render(request, 'relationship_app/book_list.html', {'books': books})  # Render the book list template

# Function-based view to view a single book
def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship_app/book_detail.html', {'book': book})

# Function-based view to add a new book
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if not request.user.has_perm('relationship_app.can_add_book'):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# Function-based view to edit an existing book
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    if not request.user.has_perm('relationship_app.can_change_book'):
        return HttpResponseForbidden()
    
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

# Function-based view to delete a book
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    if not request.user.has_perm('relationship_app.can_delete_book'):
        return HttpResponseForbidden()
    
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library  # Specify the model to use
    template_name = 'relationship_app/library_detail.html'  # Specify the template to use
    context_object_name = 'library'  # The context variable that will be passed to the template

# Function-based view to handle user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# User role-based views
def check_role(user, role):
    return user.userprofile.role == role

@user_passes_test(lambda user: check_role(user, 'Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda user: check_role(user, 'Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda user: check_role(user, 'Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Class-based views with mixins for role-based access
class LibrarianRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.userprofile.role == 'Librarian'

class LibrarianView(LibrarianRequiredMixin, TemplateView):
    template_name = 'relationship_app/librarian_view.html'

class MemberRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.userprofile.role == 'Member'

class MemberView(MemberRequiredMixin, TemplateView):
    template_name = 'relationship_app/member_view.html'
