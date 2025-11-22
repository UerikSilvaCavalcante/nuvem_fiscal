from django.db import models
from django.contrib.auth.models import AbstractUser


class Cliente(AbstractUser):
    client_id = models.CharField(blank=False, null=False)
    client_secret = models.CharField(blank=False, null=False)
    scope = models.CharField(blank=False, null=False)
    token = models.CharField(blank=True, null=True)

    cpf = models.CharField(
        blank=False, null=False, max_length=11, unique=True, default="00000000000"
    )
    cnpj = models.CharField(
        blank=False, null=False, max_length=14, unique=True, default="00000000000000"
    )
    regTrib = models.CharField(blank=False, null=False, max_length=2, default="01")

    def __str__(self) -> str:
        return f"{self.first_name.title()} {self.last_name}"


# Create your models here.
