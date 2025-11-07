from django.urls import path, include
from .views import *
urlpatterns = [
    path('', login, name="login"),
    path('logout/', logout, name="logout"),
    path('home/', home , name='home'),
    path('teste/', teste, name='teste')
]