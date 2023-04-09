# Connecting the backend in Django with the frontend in React
In order to connect with the frontend, it is necessary to follow the following steps:

1. Install the necessary packages
    Create a Django project and an app for the API.

    In this case (using Django as the backend framework), I will need to use `djangorestframework` (Django REST Framework), 
    in order to make connections in REST. This tool has a myriad of different functions that make the construction of 
    RESTful APIs that much easier.
    
    It is also necessary to install `django-cors-headers` to allow the frontend URLs to connect.

2. Setup the settings.py correctly (watchout for the permissions)
    In the `settings.py` file, add `corsheaders`, `rest_framework` to the installed apps, 
    and `corsheaders.middleware.CorsMiddleware` to the middleware list

    And create the following lists:
    
    (For some reason, using the URL on my network [e.g., "http://192.168.0.11"], does not work).

    ```python
    CORS_ALLOWED_ORIGINS = [
        'http://localhost:3000'
    ]

    CSRF_TRUSTED_ORIGINS = [
        'http://localhost:3000'
    ]
    ```

    Later on, add the REST_FRAMEWORK dictionary. This is where we can set up the permissions, among other
    configurations of the functioning of the API.

3. Serializering the data to be transferred
    We are dealing with data being sent from one technology to another. We need to serialize the data so that it is readable
    for the target technology.
    
    Create a `serializers.py` file, where the Serializer class will be declared (use the `serializers` class from the `rest_framework` itself).

4. Fetching the data from the frontend
    Create a React App using Typescript as the template.

    Import the React hooks `useState` and `useEffect`.

    One of the most important aspects to consider when using `useState` is that the types must match the structure of the data that is being passed.
    Meaning, if the data being passed is an object with two fields, "item" (a string) and "value" (a number), declare it like as follows:
    ```typescript
    import { useState } from 'react';

    function App (){
        const [ data, setData ] = useState({ item: "", value: Number });

        ...
    }
    ...
    ```
    
    Use the `fetch` function to connect with the API.