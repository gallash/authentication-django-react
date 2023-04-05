# User Authentication on a Django-React environment

## Forewords
In this repo, I will build the implementation of three authentication systems between Django-React:
1. Django's built-in authentication system (axios)
2. Token based authentication (dj-rest-auth)
3. OAuth 2.0 authentication (django-allauth)


The main objectives of this repo are:
1. develop a reusable framework with which I can easily replicate my Django-React user authentications
2. manage permissions with this authentication system
3. explore alternative authentication systems

## Structure of this project
### Front-end
The web app will have a couple of important pages. Their intent is to check how flexible and reliable
are the different registration methods that I chose to test.

The Home Page will have two tabs. The main tab is the Auth Methods page. The second one is the Check
Access page.

Unauthenticated viewers will only see the Auth Methods page.

The web app will have a primary page where the user can select the method of signing in.
The central part will be divided into three sections:
1. Django's built-in auth system
2. Token based auth system
3. OAuth 2.0 auth system

This page allows for registration as well as authentication. Here, the platform will allow the
user to create an account with higher privileges. 

Whichever method selected, the user will be brought into a new page, to perform the signing in.

Then, the user will be sent back to the Home Page, but new information should appear if he has been
successfully signed in.

There will also be another button, "Log out". Pressing this button will redirect the user back to the 
Auth Methods page, without being logged in.

### Back-end
