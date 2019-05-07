# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin #Allows add permissions to our user model
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Helps Django work with out custom user model. """

    def create_user(self, email, name, password=None):
        """ Creates a new user profile object """
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ Creates and save a new superuser with given details. """

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represents  a 'user profile' inside the system. """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects  = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']   # Because by defalt is required. So only name as additionally required field

    def get_full_name(self):
        """ Used to get a full name. """
        return self.name

    def get_short_name(self):     # In our case, both perform the same job
        """ Used to get a short name. """
        return self.name

    def __str__(self):
        """ Needs it to convert object to string. """
        return self.name + " " + self.email


class ProfileFeedItem(models.Model):
    """ Profile status update. """
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """ Return model as string """
        return self.status_text
