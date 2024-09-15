# Blog Post Management Features

## Overview
The blog post management system allows users to create, view, update, and delete blog posts. This functionality is essential for managing dynamic content on the blog.

## Implementation Details
### List View
- **Description**: Displays all blog posts.
- **URL**: `/posts/`
- **Template**: `post_list.html`
- **View**: `PostListView`

### Detail View
- **Description**: Shows details of a single post.
- **URL**: `/posts/<int:pk>/`
- **Template**: `post_detail.html`
- **View**: `PostDetailView`

### Create View
- **Description**: Allows users to create a new post.
- **URL**: `/posts/new/`
- **Template**: `post_form.html`
- **View**: `PostCreateView`

### Update View
- **Description**: Enables post editing.
- **URL**: `/posts/<int:pk>/edit/`
- **Template**: `post_form.html`
- **View**: `PostUpdateView`

### Delete View
- **Description**: Allows post deletion.
- **URL**: `/posts/<int:pk>/delete/`
- **Template**: `post_confirm_delete.html`
- **View**: `PostDeleteView`

## Form Configuration
The `PostForm` handles creating and updating posts with fields for `title` and `content`.

## Template Details
- **post_list.html**: Lists posts with links to details.
- **post_detail.html**: Shows full post content.
- **post_form.html**: Used for creating and editing posts.
- **post_confirm_delete.html**: Confirms deletion.

## URL Configuration
- **List View**: `path('', PostListView.as_view(), name='post-list')`
- **Detail View**: `path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail')`
- **Create View**: `path('post/new/', PostCreateView.as_view(), name='post-create')`
- **Update View**: `path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update')`
- **Delete View**: `path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')`

## Permissions and Access Control
- **Authentication Required**: Users must be logged in to create, edit, or delete posts.
- **Authorization**: Users can only modify posts they created.

## Testing
- **Create**: Verify post creation functionality.
- **Read**: Test listing and detail views.
- **Update**: Ensure post editing works.
- **Delete**: Confirm post deletion.

## Known Issues and Limitations
- **None**
