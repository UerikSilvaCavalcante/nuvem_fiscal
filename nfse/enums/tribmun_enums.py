from django.db import models
from django.utils.translation import gettext_lazy as _


class TRIBISSQN(models.IntegerChoices):
    OP_TRIBUTAVEL = 1, _("Operação Tributável")
    OP_IMUNE = 2, _("Imunidade")
    OP_EXP_SERV = 3, _("Exportação de Serviços")
    OP_ISENTA = 4, _("Não Incidência")


class TPIMUNIDADE(models.IntegerChoices):
    IMUNIDADE = 0, _("Imunidade")
    PATRIMONIO = 1, _("Patrimônio")
    TEMPLOS = 2, _("Templos de qualquer culto")
    PATRIMONIO_POLI = 3, _("Patrimônio Político")
    LIVROS = 4, _("Livros, jornais, periódicos e o papel destinado à sua impressão")

class TPRETISSQN(models.IntegerChoices):
    N_RETIDNO = 1, _("Não Retido")
    RETIDO_TOMADOR = 2, _("Retido pelo Tomador")
    RETIDO_INTERMEDIARIO = 3, _("Retido pelo Intermediário")