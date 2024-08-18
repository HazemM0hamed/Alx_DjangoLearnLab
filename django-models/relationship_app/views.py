from django.shortcuts import render
from .models import Book 
from .models import Library # Import the Book and Library models
from django.views.generic.detail import DetailView

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Query to get all books
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Render the list_books template

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library  # Specify the model to use
    template_name = 'relationship_app/library_detail.html'  # Specify the template to use
    context_object_name = 'library'  # The context variable that will be passed to the template

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

# You can also define a custom registration view if needed
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

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

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin

class LibrarianRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.userprofile.role == 'Librarian'

class LibrarianView(LibrarianRequiredMixin, TemplateView):
    template_name = 'librarian_view.html'
def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
class MemberRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.userprofile.role == 'Member'

class MemberView(MemberRequiredMixin, TemplateView):
    template_name = 'member_view.html'
