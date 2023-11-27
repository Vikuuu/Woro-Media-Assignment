# Woro-Media-Assignment

### Cloning the repository

1. Clone the repository using this command:

```
gh repo clone Vikuuu/Woro-Media-Assignment
```

2. Move into the project directory:

```
cd Woro-Media-Assignment
```

3. Create a new virtual environment:
```
# Let's first install the pipenv
pip install pipenv

#Now create the virtual environment
pipenv shell
```

4. Activate the environment:
```
# when called in the same directory as where virtual env is created,
# then it activates the virtual env
pipenv shell
```

5. Install the requirements
```
pipenv install -r requirements.txt
```

6. Create the cache table using:
```
py manage.py createcachetable
```

7. Run the migrations:
```
py manage.py migrate
```
### Run the App

Start the server: 
```
py manage.py runserver
```
⚠ Then, the development server will be started at `http://localhost:8000/`

Now you are good to go.


# API Documentation

```
routes = [
        {
            'Endpoint': 'auth/api/register/',
            'method': 'POST',
            'body': {"email":"","username":"","password": ""},
            'description': 'Creates a new user'
        },
        {
            'Endpoint': 'auth/api/verify-email'/<str:token>,
            'method': 'GET',
            'body': None,
            'description': 'Verify the user email'
        },
        {
            'Endpoint': '/auth/api/login/',
            'method': 'POST',
            'body': {"email": "", "password": ""},
            'description': 'Logs In the user, and returns the access and refresh tokens'
        },
        {
            'Endpoint': '/auth/api/login/refresh',
            'method': 'POST',
            'body': {"refresh": ""},
            'description': 'Returns the refresh and access token '
        },
        {
            'Endpoint': '/accounts/signup/',
            'method': 'GET',
            'body': None,
            'description': 'Use to signup with google'
        },
    ]
```

