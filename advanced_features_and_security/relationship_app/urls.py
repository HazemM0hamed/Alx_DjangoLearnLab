from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
]

from django.urls import path
from .views import admin_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),  # For function-based view
    
]
from django.urls import path
from .views import librarian_view, member_view, LibrarianView, MemberView

urlpatterns = [
    #path('librarian/', librarian_view, name='librarian_view'),  # For function-based view
    #path('librarian/', LibrarianView.as_view(), name='librarian_view'),  # For class-based view
    path('member/', member_view, name='member_view'),  # For function-based view
    #path('member/', MemberView.as_view(), name='member_view'),  # For class-based view
]

from django.urls import path
from .views import add_book, edit_book, delete_book, list_books

urlpatterns = [
    path("add_book/", add_book, name="add_book"),  # URL pattern for adding a book
    path("edit_book/<int:pk>/", edit_book, name="edit_book"),  # URL pattern for editing a book
    path("delete_book/<int:pk>/", delete_book, name="delete_book"),  # URL pattern for deleting a book
    path("list_books/", list_books, name="list_books"),  # URL pattern for listing books
]

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('books/<int:pk>/', views.view_book, name='view_book'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]


