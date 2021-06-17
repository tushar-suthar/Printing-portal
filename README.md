# Printing-portal
A printing portal website developed using Django Framework,where user can upload his/her document to be printed and can pay respective amount using integrated epayment gateway.
The website includes seperate login system for general users and shopkeeper authenticated with microsoft auth.

## Installation
python and django need to be installed

```bash
pip install django
```
##Usage

Go to the Printing-Portal folder and run 

```bash
python manage.py runserver
```

Then go to the browser and enter the url **http://loaclhost:8000**

## Login

The login page is common for customer and shopkeeper.  
The username is their microsoft outlook email-id and password is thier respective email password.

You can access the django admin page at **http://127.0.0.1:8000/admin**, after creating new admin user by following command

```bash
python manage.py createsuperuser
```
## User
There is no need to create any user from admin page.

The email of shopkeeper need to be defined at function store_user in authhelper file under tutorial folder.

Also the email of shopkeeper need to be defined at place order function in views file under task folder 

## Screenshots

###Signin page


