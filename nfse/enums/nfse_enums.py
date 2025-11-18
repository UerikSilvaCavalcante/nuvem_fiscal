from django.db import models


class PROVEDOR(models.TextChoices):
    PRADAO = "padrao", "Padrão"
    NACIONAL = "nacional", "Nacional"


class AMBIENTE(models.TextChoices):
    PROD = "producao", "Produção", 
    HOMO = "homologacao", "Homologação"
