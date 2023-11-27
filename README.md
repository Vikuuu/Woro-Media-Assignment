# Woro-Media-Assignment

### Cloning the repository

1. Clone the repository using this command:

```
git clone https://github.com/Vikuuu/Woro-Media-Assignment.git
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

# Social Media Login Setup

To use the social media login feature follow these steps to enable it

-->Navigate to `http://localhost:8000/admin/` and enter your super user credentials

-->Click on `"Social applications"`.

![image](https://github.com/Vikuuu/Woro-Media-Assignment/assets/125040659/f33d9545-c8ea-4ae3-b78a-2555e3596c3c)

-->Click on `"ADD SOCIAL APPLICATION"`.

![image](https://github.com/Vikuuu/Woro-Media-Assignment/assets/125040659/347df734-28e7-402a-86e3-c8c5fb010167)

-->In the provider dropdown, select the option `Google`.

![image](https://github.com/Vikuuu/Woro-Media-Assignment/assets/125040659/5fefcfd5-3d94-4951-bb28-5ed99d7ca47c)

-->In the `Name` field enter the name of your choice or enter "GOOGLE".

![image](https://github.com/Vikuuu/Woro-Media-Assignment/assets/125040659/2bc043cc-6bad-4bb1-8381-cd049d652d76)

-->Add the `Client ID` from the `.env.local` file.

![image](https://github.com/Vikuuu/Woro-Media-Assignment/assets/125040659/05a33e2f-aae0-40c2-bd25-e9f702a78873)

-->Add the `Secret Key` from the `.env.local` file.

![image](https://github.com/Vikuuu/Woro-Media-Assignment/assets/125040659/8dad4dc0-7332-4aa1-a9f1-4a4641e12044)

-->In `Sites` option double-click the `localhost:8000`.

![image](https://github.com/Vikuuu/Woro-Media-Assignment/assets/125040659/30f5de8f-aa8c-4a10-959d-527bcae9ad6a)

-->Click `Save` to save all the changes
![image](https://github.com/Vikuuu/Woro-Media-Assignment/assets/125040659/5e42a95c-4231-4bbf-b06f-bee59592a876)


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

