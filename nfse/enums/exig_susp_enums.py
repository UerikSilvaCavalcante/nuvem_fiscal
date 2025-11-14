from django.db import models
from django.utils.translation import gettext_lazy as _

class TPSUSP(models.IntegerChoices):
    EXIG_SUSPENSAO = 1, _("Exigibilidade Suspensa por Decisão Judicial")
    EXIG_SUSP_ADMIN = 2, _("Exigibilidade Suspensa por Decisão Administrativa")
