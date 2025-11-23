from django.urls import path
from nfse.views import *

urlpatterns = [
    path("", listar_nfse, name="listar_nfse"),
    path("emit_nfse/", emit_nfse, name="emit_nfse"),
    path("info_nfse/<str:nfse_id>/", info_nfse, name="info_nfse"),
    path(
        "cancelamento_sit/<str:nfse_id>/",
        cancelamento_situacao,
        name="cancelamento_sit",
    ),
    path(
        "cancelar_nfse/<str:nfse_id>/",
        cancelar_nfse,
        name="cancelar_nfse",
    ),
]
