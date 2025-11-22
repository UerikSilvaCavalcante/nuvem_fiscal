from django.urls import path
from nfse.views import *

urlpatterns = [
    path("", listar_nfse, name="listar_nfse"),
    path("emit_nfse/", emit_nfse, name="emit_nfse"),
]
