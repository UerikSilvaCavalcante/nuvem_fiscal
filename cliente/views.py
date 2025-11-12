from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
from dotenv import load_dotenv
import requests

load_dotenv()


# Create your views here.
def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form["nome_login"].value()
            password = form["password"].value()
            user = authenticate(request, username=username, password=password)
            if user:
                url = str(os.getenv("AUTH_URL"))
                scope = user.scope # type: ignore

                data = {
                    "grant_type": "client_credentials",
                    "client_id": user.client_id, # type: ignore
                    "client_secret": user.client_secret, # type: ignore
                    "scope": scope,
                }

                res = requests.post(
                    url,
                    headers={"ContenContent-Type": "application/x-www-form-urlencoded"},
                    data=data,
                )
                data = res.json()
                user.token = data["access_token"] # type: ignore
                
                login_user(request, user)
                user.save()
                user.refresh_from_db()
                return redirect("home")
            else:
                messages.error(request, "Usuario ou Senha incorretos")
                return redirect("login")

    form = LoginForm()
    return render(request, "client/login.html", {"form": form})


@login_required(login_url="/", redirect_field_name="login")
def home(request):
    return render(request, "client/home.html")


def teste(request):
    return render(request, "client/tables.html")


def logout(request):

    logout_user(request)
    return redirect("login")
