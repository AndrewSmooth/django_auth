# Django_my_auth
This is RESTful Django and DRF API for Authentication. The system supports user registration, authentication, token refresh, logout, and allow users to retrieve and update their personal information. Authentication utilizes Access and Refresh tokens.

# Tokens
Refresh Token – A UUID stored in the database, issued for 30 days by default.
Access Token – A JSON Web Token with a default lifespan of 30 seconds.
Tokens are encoded and decoded by [PyJWT library](https://pypi.org/project/PyJWT/)

# Details
Clients may request an Access Token refresh at any time, for instance, upon Access Token expiry by providing a valid Refresh Token. In this case, the service returns a new valid pair of Access and Refresh Tokens, resetting their lifespans.

# Run
1) Clone this repo
2) Install django, django rest framework and PyJWT library
3) Make config file
4) Create venv. Go to directory with `manage.py` and run:
`python manage.py runserver`

# Usage examples
## User registration
Endpoint: `/register/`
Method: `POST`
Body: `{"password": "password", "email": "user@example.com"}`
Response: `{"id": 1, "email": "user@example.com"}`

## Authentication
Endpoint: `/login/`
Method: `POST`
Body: `{"email": "user@example.com", "password": "password"}`
Response: `{"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsImV4cCI6MTcxMjE0NTk0NiwiaWF0IjoxNzEyMTQ1OTE2fQ.KX6LM66tC3p3bUCdkWRQkPvariP8tzUfWd8Z13akCPY", "refresh_token": "d952527b-caef-452c-8c93-1100214f82e5"}`

## Access token refresh 
Endpoint: `/refresh/`
Method: `POST`
Body: `{"refresh_token": "d952527b-caef-452c-8c93-1100214f82e5"}`
Response: `{"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInVzZXJuYW1lIjoiZXhhbXBsZVVzZXIiLCJleHAiOjE3MTIxNDYxNDd9.zKobBlRuOiJSxCmi-iYap1bejfnvK6M3qtnkT0ssDKA", "refresh_token": "eb0464c2-ed6e-4346-a709-042c33946154"}`

## Logout (Invalidating Refresh Token)
Endpoint: `/logout/`
Method: `POST`
Body: `{"refresh_token": "eb0464c2-ed6e-4346-a709-042c33946154"}`
Response: `{"success": "User logged out."}`

## Retrieving personal information 
Endpoint: `/me/`
Method: `GET`
Header: `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInVzZXJuYW1lIjoiZXhhbXBsZVVzZXIiLCJleHAiOjE3MTIxNDYxNDd9.zKobBlRuOiJSxCmi-iYap1bejfnvK6M3qtnkT0ssDKA`
Response: `{"id": 1, "username": "", "email": "user@example.com"}`

## Updating Personal Information
Endpoint: `/me/`
Method: `PUT`
Header: `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInVzZXJuYW1lIjoiZXhhbXBsZVVzZXIiLCJleHAiOjE3MTIxNDYxNDd9.zKobBlRuOiJSxCmi-iYap1bejfnvK6M3qtnkT0ssDKA`
Body: `{"username": "John Smith"}`
Response: `{"id": 1, "username": "John Smith", "email": "user@example.com"}`