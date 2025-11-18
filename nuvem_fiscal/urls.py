from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cliente.urls")),
    path("empresa/", include("empresa.urls")),
    path("nfse/", include("nfse.urls")),
]
