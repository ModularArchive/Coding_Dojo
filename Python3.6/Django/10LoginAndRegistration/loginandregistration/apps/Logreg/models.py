from __future__ import unicode_literals

from django.db import models

 # https://docs.python.org/3/library/re.html#module-re           
import bcrypt
class UserManager(models.Manager):
    def validation(self, postData):
        errors = {}
        if len(postData['first_name']) < 1: #If length of the posted data "first_name" is less than one the following code will execute
            errors['first_name'] = "Please enter a First Name." #Error holds the messages and information of what went wrong to be posted via message
        elif len(postData['first_name']) < 2: #If length of posted data "first_name" is less than 2 the following code will execute
            errors['first_name'] = "First name must be at least 2 characters long."
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Please enter a Last Name."
        elif len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long."
        if len(postData['email']) < 1:
            errors['email'] = "Please enter a Email."
        elif User.objects.filter(email=postData['email']):
            errors['email'] = "Email is already taken"
        if len(postData['password']) < 1:
            errors['password'] = "Please enter a Password."
        elif len(postData['password']) < 8:
            errors['password'] = "Your password must be at least 8 characters long"
        if postData['pw_confirm'] != postData['password']:
            errors['pw_confirm'] = "Passwords do not match."
        return errors

    def login_validation(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors['email'] = "Please enter your email."
        elif not User.objects.filter(email=postData['email']):
            errors['email'] = "Incorrect email."
        if len(postData['password']) < 1:
            errors['password'] = "Incorrect password."
        elif not bcrypt.checkpw(postData['password'].encode(), User.objects.get(email=postData['email']).password.encode()):
            errors['password'] = "Incorrect password."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()