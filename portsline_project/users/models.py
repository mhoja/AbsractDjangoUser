
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(max_length=14)
    is_verified= models.BooleanField(default=False)
    email_token=models.CharField(max_length=100, null=True, blank=True)
    forget_password =models.CharField(max_length=100, null=True, blank=True)
    last_login_time =models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # spouse_name = models.CharField(blank=True, max_length=100)
    # date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.email