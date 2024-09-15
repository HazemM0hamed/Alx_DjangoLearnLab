Commenting System Documentation
Overview
The commenting system allows users to interact with blog posts by adding, editing, and deleting comments. This feature enhances user engagement by enabling discussions and feedback on individual posts.

Features
Add Comments: Authenticated users can post comments on blog posts.
Edit Comments: Users can edit their own comments.
Delete Comments: Users can delete their own comments.
View Comments: All users can view comments associated with blog posts.
Models
Comment Model
The Comment model is defined in blog/models.py:

post: ForeignKey linking to the Post model (many-to-one relationship).
author: ForeignKey linking to Django’s User model (indicating the comment's author).
content: TextField for the comment’s text.
created_at: DateTimeField that records when the comment was made.
updated_at: DateTimeField that records the last update to the comment.
Forms
CommentForm
The CommentForm is a ModelForm used for creating and editing comments:

python
Copy code
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
Views
Adding Comments
View Name: add_comment
URL Pattern: /posts/<int:post_id>/comments/new/
Method: POST
Description: Allows authenticated users to add a comment to a specific blog post.
Editing Comments
View Name: edit_comment
URL Pattern: /comments/<int:comment_id>/edit/
Method: POST
Description: Allows authenticated users to edit their own comments.
Deleting Comments
View Name: delete_comment
URL Pattern: /comments/<int:comment_id>/delete/
Method: POST
Description: Allows authenticated users to delete their own comments.
Templates
Add Comment Template
File: blog/templates/blog/add_comment.html

html
Copy code
{% extends 'blog/base.html' %}
{% block content %}
  <h2>Add a Comment</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
  </form>
{% endblock %}
Edit Comment Template
File: blog/templates/blog/edit_comment.html

html
Copy code
{% extends 'blog/base.html' %}
{% block content %}
  <h2>Edit Comment</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Update</button>
  </form>
{% endblock %}
Delete Comment Template
File: blog/templates/blog/delete_comment.html

html
Copy code
{% extends 'blog/base.html' %}
{% block content %}
  <h2>Delete Comment</h2>
  <p>Are you sure you want to delete this comment?</p>
  <form method="post">
    {% csrf_token %}
    <button type="submit">Confirm</button>
  </form>
{% endblock %}
URL Patterns
Add Comment: posts/<int:post_id>/comments/new/ - view: add_comment
Edit Comment: comments/<int:comment_id>/edit/ - view: edit_comment
Delete Comment: comments/<int:comment_id>/delete/ - view: delete_comment
Permissions
Add Comments: Must be authenticated.
Edit/Delete Comments: Only the comment's author can edit or delete their own comments.
View Comments: Accessible to all users, whether authenticated or not.
Testing
Add Comments: Test by submitting a new comment on a blog post.
Edit Comments: Test by updating an existing comment.
Delete Comments: Test by removing an existing comment.
Permissions: Ensure that only the comment's author can edit or delete their own comments.
