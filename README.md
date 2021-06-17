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

### Signin page

![Screenshot (201)](https://user-images.githubusercontent.com/62867903/122433620-07642a80-cfb4-11eb-9dc5-cfdf91291903.png)

![Screenshot (202)](https://user-images.githubusercontent.com/62867903/122433636-0af7b180-cfb4-11eb-9daf-79a64bfba7b1.png)

### Customer Page 

![Screenshot (203)](https://user-images.githubusercontent.com/62867903/122433671-10ed9280-cfb4-11eb-82e4-a7b5394de637.png)

#### new order 

![Screenshot (205)](https://user-images.githubusercontent.com/62867903/122433711-19de6400-cfb4-11eb-9127-5e4bb80aeee5.png)

#### Payment Gateway

![Screenshot (206)](https://user-images.githubusercontent.com/62867903/122433749-206cdb80-cfb4-11eb-9a3e-2ce247f057be.png)

![Screenshot (207)](https://user-images.githubusercontent.com/62867903/122433762-24006280-cfb4-11eb-8f78-000633e94b16.png)

#### Old Transactions

![Screenshot (208)](https://user-images.githubusercontent.com/62867903/122433768-25ca2600-cfb4-11eb-9314-ac9afcb039ff.png)

### Shopkeeper Page


![Screenshot (209)](https://user-images.githubusercontent.com/62867903/122434843-15667b00-cfb5-11eb-984b-89b571a2575b.png)

#### Recent Orders


![Screenshot (210)](https://user-images.githubusercontent.com/62867903/122434855-18616b80-cfb5-11eb-883c-ced3a3dce73b.png)


![Screenshot (211)](https://user-images.githubusercontent.com/62867903/122434863-1ac3c580-cfb5-11eb-9ae2-2749858ab5e9.png)
