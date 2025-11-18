from django.urls import path
from nfse.views import *

urlpatterns = [
    path("", emit_nfse, name="emit_nfse"),
]
