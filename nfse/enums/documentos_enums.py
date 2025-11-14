from django.db import models
from django.utils.translation import gettext_lazy as _


class TPDEDRED(models.IntegerChoices):
    ALIMENTACAO = 1, _("Alimentação")
    MATERIAIS = 2, _("Materiais")
    PRODUCAO = 3, _("Produção")
    REEMBOLSO = 4, _("Reembolso de despesas")
    REPASSE_CONSORCIADO = 5, _("Repasse a terceiros")
    REPASSE_PLANO_SAUDE = 6, _("Repasse a plano de saúde")
    SERVICOS = 7, _("Serviços")
    SUBEMPREITADO = 8, _("Subempreitado")
    OUTRAS = 99, _("Outras")
