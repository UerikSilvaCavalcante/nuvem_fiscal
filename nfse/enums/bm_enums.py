from django.db import models
from django.utils.translation import gettext_lazy as _

class TPBM(models.IntegerChoices):
    ALIQUOTA_DIFERENCIAL = 1, _("Alíquota Diferencial")
    RED_BC = 2, _("Redução da Base de Cálculo")
    ISENTO = 3, _("Isento")
    