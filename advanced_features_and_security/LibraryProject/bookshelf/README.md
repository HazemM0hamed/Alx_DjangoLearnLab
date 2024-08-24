## Permissions and Groups Setup

### Custom Permissions

- `can_view`: Permission to view a book.
- `can_create`: Permission to create a new book.
- `can_edit`: Permission to edit an existing book.
- `can_delete`: Permission to delete a book.

### Groups and Permissions

- **Editors**: Has `can_edit` and `can_create` permissions.
- **Viewers**: Has `can_view` permission.
- **Admins**: Has all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

### Implementing Permissions

Use decorators such as `@permission_required('bookshelf.can_edit', raise_exception=True)` in your views to enforce permissions.
