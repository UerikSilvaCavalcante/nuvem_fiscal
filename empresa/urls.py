from django.urls import path
from .views import *
urlpatterns = [
    path('', consultar_empresa, name='consultar_empresa'),
    path('add/', cad_empresa, name='cad_empresa'),
]
