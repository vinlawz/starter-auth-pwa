from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class User(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(
        _("email address"), 
        unique=True,
        db_index=True
    )
    
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True)
    is_verified = models.BooleanField(
        default=False,
        help_text=_("Designates whether this user has verified their email.")
    )
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
