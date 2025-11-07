from django.db import models
from django.contrib.auth.models import AbstractUser


class Cliente(AbstractUser):
    client_id = models.CharField(blank=False, null=False)
    client_secret = models.CharField(blank=False, null=False)
    scope = models.CharField(blank=False, null=False)
    token = models.CharField(blank=True, null=True)


# Create your models here.
