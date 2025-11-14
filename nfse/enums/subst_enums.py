from django.db import models
from django.utils.translation import gettext_lazy as _


class CMOTIVO(models.TextChoices):
    DESENQUADRAMENTO = "01", _("Desenquadramento de NFS-e do Simples Nacional")
    ENQUADRAMENTO = "02", _("Enquadramento de NFS-e no Simples Nacional")
    INCLUSAO = "03", _("Inclusão Retroativa de Imunidade/Isenção para NFS-e")
    EXCLUSAO = "04", _("Exclusão Retroativa de Imunidade/Isenção para NFS-e")
    REJEICAO = "05", _("Rejeição de NFS-e")
    OUTROS = "99", _("Outros")
