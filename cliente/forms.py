from django.forms import ModelForm
from django import forms
from .models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        exclude = ["token"]


class LoginForm(forms.Form):
    nome_login = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-user",
                "placeholder": "Entre com seu Usuario",
            }
        ),
    )
    password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-user",
                "placeholder": "Entre com sua Senha",
            }
        ),
    )
