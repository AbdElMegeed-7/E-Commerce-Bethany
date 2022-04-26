from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False, blank=False
    )
    phone_field = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.user.username
