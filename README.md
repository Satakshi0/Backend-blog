Project(Artizence) Documentation - Blog API

Introduction:
A blog API with CRUD operation and Authentication through which content will be uploaded to the database and the Front-end site can fetch the content info from the API with JWT Authentication.

Admin: Full control over all endpoints.
Manager: Can edit and post new content.
Content Creator: Can create and edit only the content they have created.


Project setup:
To set up the project, follow these steps:

Clone the project from the Git repository.
Create and activate a virtual environment.
Install the project dependencies from the requirements.txt file using pip.
Migrate the database.
Run the development server.


API Endpoints:

I have made the following API endpoints in the project:


Users

/api/users/ (GET, POST) - To View a list of all users or create a new user account.
/api/users/{id}/ (GET, PATCH, DELETE) - To Retrieve, update, or delete a specific user account.

Authentication

/api/auth/token/ (POST) -To Obtain an access token and a refresh token by providing a valid email and password.
/api/auth/token/refresh/ (POST) - To Obtain a new access token by providing a valid refresh token.



Blog Posts

/api/posts/ (GET, POST) - To View a list of all blog posts or create a new post.
/api/posts/{id}/ (GET, PATCH, DELETE) -To Retrieve, update, or delete a specific blog post.

API Authentication:
Here, The Blog API uses JWT authentication to protect certain endpoints that require user authorization. In order to obtain a token, send a POST request to /api/auth/token/ with a valid email and password. The response will contain an access token and a refresh token. Use the access token to access the protected endpoints. If the token expires, use the refresh token to obtain a new access token.

API Authorization:

The Blog API includes user roles and permissions to restrict access to certain endpoints. The following roles are available:

Admin: Full control over all endpoints.
Manager: Can edit and post new content.
Content Creator: Can create and edit only the content they have created.
I have created a permissions.py file that includes custom permission classes that check the user's role before allowing access to a certain endpoint.

