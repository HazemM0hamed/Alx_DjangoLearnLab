# Delete Operation

```python
from bookshelf.models import Book

# Delete the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Try to retrieve the book again to confirm deletion
books = Book.objects.all()
print(books)

# Expected Output
# QuerySet[] or similar empty list, confirming deletion
