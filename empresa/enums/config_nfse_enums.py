from enum import Enum, StrEnum, auto
from django.db import models
from django.utils.translation import gettext_lazy as _


class opSimpNacEnum(models.IntegerChoices):
    NAO_OPTANTE = 1, _("Não optante")
    OPTANTE_MEI = 2, _("Optante - Microempreendedor Individual (MEI)")
    OPTANTE_ME = 3, _("Optante - Microempresa ou Empresa de Pequeno Porte (ME/EPP)")


class regApTribSNEnum(models.IntegerChoices):
    REG_SN = 1, _("Regime de apuração dos tributos federais e municipal pelo SN")
    REG_SN_ISSQN = 2, _(
        "Regime de apuração dos tributos federais pelo SN e ISSQN por fora do SN conforme respectiva legislação municipal do tributo"
    )
    REG_NO_SN = 3, _(
        "Regime de apuração dos tributos federais e municipal por fora do SN conforme respectivas legilações federal e municipal de cada tributo"
    )


class regEspTribEnum(models.IntegerChoices):
    NENHUM = 0, _("Nenhum")
    ATO_COOP = 1, _("Atos cooperativos")
    ESTIMATIVA = 2, _("Estimativa")
    MICROEMPRESA = 3, _("Microempresa Municipal")
    NOT_REGIS = 4, _("Notário ou Registrador")
    PROF_AUT = 5, _("Profissional Autonomo")
    SOC_PROF = 6, _("Sociedade Profissional")


class AmbienteEnum(models.TextChoices):
    PRODUCAO = "producao"
    HOMOLOGACAO = "homologacao"
