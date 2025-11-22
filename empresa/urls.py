from django.urls import path
from .views import *

urlpatterns = [
    path("", consultar_empresa, name="consultar_empresa"),
    path("add/", cad_empresa, name="cad_empresa"),
    path("info/<int:id>/", info_empresa, name="info_empresa"),
    path("cad_certificado/<int:cpf_cnpj>", cad_certificado, name="cad_certificado"),
    path("config_nfse_form/<int:cpf_cnpj>", config_nfse, name="config_nfse"),
    path("edit/<int:id>", edit_empresa, name="edit_empresa"),
]
