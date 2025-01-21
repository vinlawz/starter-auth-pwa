from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class User(AbstractUser, PermissionsMixin):
    class Types(models.TextChoices):
        STAFF = "STAFF", "Staff"
        ENDUSER = "ENDUSER", "EndUser"
        
    username = None
    email = models.EmailField(
        _("email address"), 
        unique=True,
        db_index=True
    )
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True)
    type = models.CharField(
        _("User Type"),
        max_length=50,
        choices=Types.choices,
        default=Types.STAFF,
    )
    is_verified = models.BooleanField(
        default=False,
        help_text=_("Designates whether this user has verified their email.")
    )
    is_custom_admin = models.BooleanField(
        default=False,
        help_text=_("Designates whether this user has dashboard access to the site.")
    )
    date_joined = models.DateTimeField(default=timezone.now)
    # add additional fields here

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class StaffUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add additional fields here
    
    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "Staff Profile"
        verbose_name_plural = "Staff Profiles"

class EndUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add additional fields here
    
    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "End User Profile"
        verbose_name_plural = "End User Profiles"
        
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.type == User.Types.STAFF:
            StaffUserProfile.objects.create(user=instance)
        else:
            EndUserProfile.objects.create(user=instance)
    else:
        if instance.type == User.Types.STAFF:
            StaffUserProfile.objects.update_or_create(user=instance)
            EndUserProfile.objects.filter(user=instance).delete()
        else:
            EndUserProfile.objects.update_or_create(user=instance)
            StaffUserProfile.objects.filter(user=instance).delete()