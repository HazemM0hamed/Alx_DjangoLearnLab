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
