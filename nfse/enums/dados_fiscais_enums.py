from django.db import models
from django.utils.translation import gettext_lazy as _


class CNAONIFENUM(models.IntegerChoices):
    N_INFO = 0, _("Não informado")
    DISPENSADO = 1, _("Dispensado de inscrição")
    N_EXIG = 2, _("Não exigido inscrição")
