from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['username'].isalpha()) == False:
            if len(postData['username']) < 5:
                errors['username'] = "Username can not be shorter than 5 characters"

        if (postData['phone'].isalpha()) == False:
            if len(postData['phone']) < 9:
                errors['phone'] = "Phone number can not be shorter than 9 characters"

        if len(postData['password']) == 0:
            errors['password'] = "You must enter password"

        return errors

class User(models.Model):
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
# Create your models here.
