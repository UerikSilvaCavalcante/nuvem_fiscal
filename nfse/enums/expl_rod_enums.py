from django.db import models
from django.utils.translation import gettext_lazy as _


class CATEGVEICENUM(models.TextChoices):
    N_INFO = "00", _("tipo não informado na nota de origem")
    AUTOMOVEL = "01", _("Automóvel")
    CAMINHONETE = "02", _("Caminhonete")
    AUTOMOVEL_SEMIRREBOQUE = "03", _("Automóvel com semirreboque")
    CAMINHAO = "04", _("Caminhão")
    AUTOMOVEL_REBOQUE = "05", _("Automóvel com reboque")
    CAMINHAO_REBOQUE = "06", _("Caminhão com reboque")
    CAMINHAO_TRATOR = "07", _("Caminhão trator")
    MOTOCICLETA = "08", _("Motocicleta")
    VEIC_ESPECIAL = "09", _("Veículo especial")
    ISENTO = "10", _("Veiculo Isento")
