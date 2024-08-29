Social Networking Application

Overview

This project is a social networking application developed using Django Rest Framework. It includes functionalities for user authentication, friend requests, and user searches. The application supports login and signup, searches users by email or name, handles friend requests, and lists friends and pending requests.

Features:

User Authentication:

    * Signup with email only.
    * Login with email and password (case insensitive).
    * Logout functionality.

User Search:
    
    * Search users by email (exact match) or name (partial match).
    * Pagination of search results (up to 10 records per page).

Friend Requests:

    * Send, accept, and reject friend requests.
    * List friends who have accepted requests.
    * List pending friend requests.
    * Rate limit: No more than 3 friend requests per minute.

Installation
    
    Python 3.x
    Django 4.x
    Django REST Framework 3.x  
    PostgreSQL (or any other preferred database)

Setup:

    1) Clone the Repository.
    2) Create and Activate a Virtual Environment.
    3) Install Dependencies (pip install -r requirements.txt)
    4) Configure Database:
           Update the DATABASES settings in settings.py to match your database configuration.
    5) Apply Migrations.
    6) Run the Development Server.(python manage.py runserver)
          