from django.conf import settings
from django.db import models

class FCMToken(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="fcm_token"
    )
    firebase_token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - FCM Token"  # Fixed issue with None username

    class Meta:
        verbose_name = "FCM Token"
        verbose_name_plural = "FCM Tokens"
