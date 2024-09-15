Authentication System Documentation for django_blog
This document explains the authentication system implemented in the django_blog project, covering the following features:

User Registration
User Login
User Logout
Profile Management
Each feature is described with instructions on how users interact with it and how to test the functionalities.

1. User Registration
Description:
User registration allows new users to create accounts by providing a username, email, and password. This functionality is implemented by extending Django’s built-in UserCreationForm.

Components Involved:
View: register view in blog/views.py
Form: UserRegisterForm (extends Django's UserCreationForm)
Template: register.html for the user registration form
URL: /register
User Interaction:
A new user navigates to /register.
The user fills in the registration form with a username, email, and password.
After form submission, if the form is valid, the user account is created, and the user is redirected to the login page.
Testing Instructions:
Navigate to /register.
Fill in the registration form with a username, email, password, and confirm the password.
Ensure that the form creates a new user in the database and redirects the user to the login page.
Check for error messages if the form submission fails (e.g., mismatched passwords).

2. User Login
Description:
The login functionality allows users to sign in using their credentials (username and password). It uses Django's built-in LoginView.

Components Involved:
View: Django's LoginView
Template: login.html for user login form
URL: /login
User Interaction:
A registered user navigates to /login.
The user enters their username and password.
If the credentials are valid, the user is authenticated and logged into the system.
Testing Instructions:
Navigate to /login.
Use a registered username and password to log in.
Ensure that the login is successful and the user is redirected to a home page or profile.
Test with incorrect credentials and confirm that an error message is displayed.

3. User Logout
Description:
The logout functionality allows users to log out from the application. It uses Django's LogoutView to log the user out and end their session.

Components Involved:
View: Django's LogoutView
URL: /logout
User Interaction:
A logged-in user navigates to /logout.
The user is logged out and their session is ended.
Testing Instructions:
Log into the system, then navigate to /logout.
Ensure that the user is successfully logged out and redirected to a confirmation page or login page.
Verify that the session is destroyed and no protected content is accessible after logging out.

4. Profile Management
Description:
Users can manage their profiles by updating their personal information. The profile management feature allows users to edit fields such as bio, profile picture, or email (depending on how the profile is extended).

Components Involved:
View: profile view in blog/views.py
Form: ProfileUpdateForm (for profile details)
Template: profile.html for displaying and editing profile information
URL: /profile
User Interaction:
A logged-in user navigates to /profile.
The user views their profile and updates information (e.g., profile picture or bio).
After form submission, the user's profile is updated.
Testing Instructions:
Log in and navigate to /profile.
Verify that the user’s current profile details are displayed.
Update profile details (e.g., change the profile picture or bio) and submit the form.
Ensure that the profile is successfully updated and changes are reflected in the user’s profile.

5. Security and Protection
Description:
The authentication system is secured by default with Django’s built-in mechanisms. Some key security features include:

CSRF Tokens: Each form submission is protected against Cross-Site Request Forgery (CSRF) attacks using CSRF tokens.
Password Hashing: User passwords are securely stored using Django's password hashing system.
User Authentication: Access to certain pages (like profile management) is restricted to authenticated users using Django’s login_required decorator.
Testing Instructions:
Test that CSRF tokens are present in all forms (registration, login, profile management) and verify that forms are submitted securely.
Ensure that users are required to log in before accessing protected pages (e.g., /profile).
Confirm that user passwords are not stored in plaintext in the database and that authentication is based on password hashing.

6. Testing the Full Authentication System
Steps:
Register: Create a new account by navigating to /register and completing the form.
Login: Use the registered credentials to log in at /login.
Profile Update: After logging in, navigate to /profile and update profile details.
Logout: Log out by navigating to /logout and confirm that you are logged out successfully.
Session Testing: After logging out, ensure you cannot access /profile or any other authenticated pages.
