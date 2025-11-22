from django.contrib import admin
from .models import Cliente
from django.contrib.auth.admin import UserAdmin
from .forms import ClienteForm

# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(UserAdmin):
    list_display = ("username", "email", "client_id", "scope")
    add_form = ClienteForm

    fieldsets = UserAdmin.fieldsets + (
        (
            "Dados do Cliente",
            {
                "classes": ("wide"),
                "fields": (
                    "cpf",
                    "cnpj",
                    "regTrib",
                    "client_id",
                    "client_secret",
                    "scope",
                ),
            },
        ),
    )  # type: ignore
    add_fieldsets = UserAdmin.fieldsets + (
        (
            "Dados do Cliente",
            {
                "classes": ("wide"),
                "fields": (
                    "cpf",
                    "cnpj",
                    "regTrib",
                    "client_id",
                    "client_secret",
                    "scope",
                ),
            },
        ),
    )  # type: ignore
