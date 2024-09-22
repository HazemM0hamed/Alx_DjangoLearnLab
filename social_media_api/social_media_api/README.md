# README for Social Media API

## Overview

This project is a Social Media API built with Django and Django REST Framework, featuring user authentication and profile management.

## Prerequisites

- Python 3.x
- Django
- Django REST Framework

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd social_media_api
   ```

2. **Create a virtual environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install django djangorestframework djangorestframework-authtoken
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## User Registration and Authentication

### Registration

POST to `/register/` with:
```json
{
    "username": "your_username",
    "password": "your_password",
    "email": "your_email@example.com"
}
```

### Login

POST to `/login/` with:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

## User Model Overview

The custom user model includes:
- **bio**: Biography text.
- **profile_picture**: User's profile image.
- **followers**: Many-to-many relationship for following other users.

## Testing the API

Use Postman or curl to test endpoints:
- Register: `/register/`
- Login: `/login/`
- Access profile: `/profile/` (include token in headers).

---
Overview
Documenting your API is essential for developers to understand how to interact with it. This documentation will cover the available endpoints, their methods, required parameters, and example requests and responses.
Endpoint Documentation Structure
Base URL: Specify the base URL for your API.
Example: http://127.0.0.1:8000/api/
Authentication: Describe the authentication method (e.g., token-based).
Example: "Use Bearer token for authentication in the header."
Endpoints:
List each endpoint with details about its functionality.
Example Endpoints
Posts
POST /posts/
Description: Create a new post.
Request Body:
json
{
    "title": "Post Title",
    "content": "Post content."
}

Response:
json
{
    "id": 1,
    "author": 1,
    "title": "Post Title",
    "content": "Post content.",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
}

GET /posts/
Description: Retrieve a list of posts.
Response:
json
[
    {
        "id": 1,
        "author": 1,
        "title": "Post Title",
        "content": "Post content.",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z"
    }
]

GET /posts/{id}/
Description: Retrieve a specific post by ID.
PUT /posts/{id}/
Description: Update a specific post by ID.
DELETE /posts/{id}/
Description: Delete a specific post by ID.
Comments
POST /comments/
Description: Create a new comment.
Request Body:
json
{
    "post": 1,
    "content": "Comment content."
}

Response:
json
{
    "id": 1,
    "post": 1,
    "author": 1,
    "content": "Comment content.",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
}

Tools for Documentation
Django REST Swagger or drf-spectacular can be integrated to generate interactive API documentation automatically from your views and serializers.
To set up drf-spectacular:
bash
pip install drf-spectacular

Update your settings.py to include:
python
INSTALLED_APPS = [
    ...
    'drf_spectacular',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

Add URL patterns for documentation in your main urls.py:
python
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    ...
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


1. Updated Models and Migrations
Description: This section includes all changes made to the CustomUser model in the accounts app, specifically the addition of the following fields:
Followers: A many-to-many relationship field allowing users to follow other users.
Profile Picture: An image field for storing user profile pictures.
Bio: A text field for user biographies.
Migrations: All new migrations created as a result of these model changes are included. The migration files ensure that the database schema is updated to reflect the new model structure.
Files Included:
accounts/models.py: Updated model definitions.
Migration files (e.g., 0002_auto_some_id.py): Files created to apply changes to the database schema.
2. Code Files for Views and Serializers
Description: This section contains the implementation of views and serializers that facilitate user follow management and post feed generation.
Follow Management:
Views for following and unfollowing users, ensuring proper permissions are enforced.
Feed Generation:
A view that generates a dynamic content feed based on posts from users that the current user follows.
Files Included:
accounts/views.py: Contains views for follow management.
posts/views.py: Contains views for generating the user feed.
posts/serializers.py: Serializers used for validating and formatting data related to posts.
3. URL Configurations
Description: This section outlines the new routes added to handle follow management and feed retrieval functionalities.
Follow Management Routes:
Endpoint for following a user: /follow/<int:user_id>/
Endpoint for unfollowing a user: /unfollow/<int:user_id>/
Feed Route:
Endpoint for retrieving the user's feed: /feed/
Files Included:
accounts/urls.py: Updated URL configurations for follow management.
posts/urls.py: Updated URL configurations for the feed endpoint.
4. Documentation
Description: Comprehensive API documentation covering all new functionalities, including details on how to manage follows and access the feed.
Contents of Documentation:
Overview of new endpoints with descriptions, required parameters, request and response examples.
Information on how to authenticate requests using tokens.
Files Included:
README.md: Updated documentation file containing instructions on using the new features, including examples of API requests and responses.
Additional markdown files (if any) that provide detailed API specifications.

API Documentation
Document the functionality and endpoints for likes and notifications:
Likes
POST /posts/<post_id>/like/: Allows a user to like a specific post.
Request Body: None required.
Response:
Success (201): { "message": "Post liked." }
Already liked (400): { "message": "You already liked this post." }
DELETE /posts/<post_id>/unlike/: Allows a user to unlike a specific post.
Response:
Success (204): { "message": "Post unliked." }
Not liked (400): { "message": "You have not liked this post." }
Notifications
GET /notifications/: Fetches all notifications for the authenticated user.
Response:
json
[
    {
        "id": 1,
        "actor": "<actor_user>",
        "verb": "liked your post",
        "target": "<target_post>",
        "timestamp": "2024-01-01T00:00:00Z",
        "is_read": false
    }
]
