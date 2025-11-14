from django.db import models
from django.utils.translation import gettext_lazy as _


class TPRETPISCOFINS(models.IntegerChoices):
    RETIDO = 1, _("Retido")
    NAO_RETIDO = 2, _("Não retido")


class CST(models.TextChoices):
    NENHUM = "00", _("Nenhum")
    TRIBUTADO_BASICO = "01", _("Operação Tributável com Alíquota Básica")
    TRIBUTADO_DIFERENCIADA = "02", _("Operação Tributável com Alíquota Diferenciada")
    TRIBUTADO_UNIDADE_MEDIDA = "03", _(
        "Operação Tributável por Unidade de Medida de Produto"
    )
    TRIBUTADO_MONO = "04", _("Operação Tributável Monofásica - Revenda a Alíquota Zero")
    TRIBUTADO_SUBSTITUICAO = "05", _("Operação Tributável por Substituição Tributária")
    TRIBUTADO_ZERO = "06", _("Operação Tributável a Alíquota Zero")
    TRIBUTADO_CONTRIBUICAO = "07", _("Operação Tributável da Contribuição")
    OP_SEM_INCIDENCIA = "08", _("Operação sem Incidência da Contribuição")
    OP_COM_SUSPENSAO = "09", _("Operação com Suspensão da Contribuição")
