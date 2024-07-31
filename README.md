# Django REST Framework Chat API

This repository provides a Django REST Framework application for user management and AI chat interactions. The application includes endpoints for user registration, login, sending messages to an AI chatbot, and checking token balances.

## Installation Guidelines

### Prerequisites

- **Python** (version 3.8 or higher)
- **pip** (Python package installer)
- **virtualenv** (optional, but recommended)

### Setting Up the Project

Follow these steps to install and set up the project:

#### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/shubham3451/Upnyx_Assignment.git
cd api
```

#### 2. Create a Virtual Environment

Create a virtual environment to manage project dependencies:

```bash
python -m venv env
```

Activate the virtual environment:

- **On Windows**:
  ```bash
  env\Scripts\activate
  ```

- **On macOS/Linux**:
  ```bash
  source env/bin/activate
  ```

#### 3. Install Required Packages

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

Ensure `requirements.txt` includes the following:

```
Django>=4.0,<5.0
django-cors-headers>=4.0,<5.0
djangorestframework>=3.14,<4.0
djangorestframework-simplejwt>=5.0,<6.0
```

#### 4. Apply Migrations

Set up the database schema by applying migrations:

```bash
python manage.py migrate
```

#### 5. Create a Superuser (Optional)

Create a superuser to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser account.

### Configuration

#### 1. Update `settings.py`

Ensure that the `settings.py` file is properly configured. Update the following settings:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'api',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Add JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
MIDDLEWARE = [
  
    'corsheaders.middleware.CorsMiddleware',
]
```


### Running the Application

Start the Django development server:

```bash
python manage.py runserver
```

The server will be available at `http://127.0.0.1:8000/`.

### Usage Instructions

#### User Registration

- **Endpoint**: `/api/register/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  - **201 Created**:
    ```json
    {
      "message": "User created successfully"
    }
    ```
  - **400 Bad Request**:
    ```json
    {
      "error": "Username already exists"
    }
    ```

#### User Login

- **Endpoint**: `/api/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "refresh": "string",
      "access": "string"
    }
    ```
  - **400 Bad Request**:
    ```json
    {
      "error": "Invalid credentials"
    }
    ```

#### Chat API

- **Endpoint**: `/api/chat/`
- **Method**: `POST`
- **Headers**:
  - **Authorization**: `Bearer <access_token>`
- **Request Body**:
  ```json
  {
    "message": "string"
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "user": "user_id",
      "message": "string",
      "response": "This is a dummy response from the AI.",
      "timestamp": "2024-07-31T12:34:56Z"
    }
    ```
  - **400 Bad Request**:
    ```json
    {
      "error": "Message is required"
    }
    ```
    or
    ```json
    {
      "error": "Insufficient tokens"
    }
    ```

#### Token Balance API

- **Endpoint**: `/api/tokens/`
- **Method**: `GET`
- **Headers**:
  - **Authorization**: `Bearer <access_token>`
- **Response**:
  - **200 OK**:
    ```json
    {
      "tokens": 4000
    }
    ```

