from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token
from .manager import UserManager
from django import forms

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    password1 = models.CharField(max_length=1000)
    password2 = models.CharField(max_length=1000)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','date_of_birth','gender','password1']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.username

    
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class RegisterForm(forms.Form): 
    username = forms.CharField(max_length=200)
    date_of_birth = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=10)
    email = forms.CharField()
    password1 = forms.CharField(max_length=200)
    password2 = forms.CharField(max_length=200)

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(max_length=200)
        


        
    
   
        