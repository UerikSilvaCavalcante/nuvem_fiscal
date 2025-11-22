from django.db import models
from django.utils.translation import gettext_lazy as _


class PROVEDOR(models.TextChoices):
    PRADAO = "padrao", _("Padrão")
    NACIONAL = "nacional", _("Nacional")


class AMBIENTE(models.TextChoices):
    PROD = "producao", _("Produção"),
    
    HOMO = "homologacao", _("Homologação")
