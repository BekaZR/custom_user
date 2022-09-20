
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin,
    )

from mainapp.managers import CustomAccountManager


class User(AbstractBaseUser,PermissionsMixin,):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now(), )
    about = models.TextField(_('about'), max_length=500, blank=True, )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name',]
    
    def __str__(self):
        return f'{self.user_name} {self.email}'


