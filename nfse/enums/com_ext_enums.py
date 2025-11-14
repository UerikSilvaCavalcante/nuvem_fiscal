from django.db import models
from django.utils.translation import gettext_lazy as _


class MDPRESTACAO(models.IntegerChoices):
    DESCONHECIDO = 0, _("Desconhecido")
    TRANSFRONTEIRICO = 1, _("Transfronteiriço")
    CONSUMO_NO_PAIS = 2, _("Consumo no Brasil")
    PRESENCA = 3, _("Presença Física no Brasil")
    MOVIMENTO = 4, _("Movimento de Temporário de Pessoas Físicas")


class VINCPREST(models.IntegerChoices):
    SEM_VINCULO = 0, _("Sem Vínculo")
    CONTROLADA = 1, _("Controlada")
    CONTROLADORA = 2, _("Controladora")
    COLIGADA = 3, _("Coligada")
    MATRIZ = 4, _("Matriz")
    FILIAL = 5, _("Filial ou sucursale")
    OUTRO = 6, _("Outro")


class MECAFCOMEXP(models.TextChoices):
    DESCONHECIDO = "00", _("Desconhecido")
    NENHUM = "01", _("Nenhum")
    ACC = "02", _("Acordo Comercial com Países da CPLP")
    ACE = "03", _("Acordo Comercial com a União Europeia")
    BNDES_POS = "04", _("Exim Pós-Embarque - Serviços")
    BNDES_PRE = "05", _("Exim Pré-Embarque - Serviços")
    FGE = "06", _("Fundo de Garantia à Exportação - FGE")
    PROEX_EQU = "07", _("Equalização - PROEX")
    PROEX_FIN = "08", _("Financiamento - PROEX")


class MECAFCOMEXT(models.TextChoices):
    DESCONHECIDO = "00", _("Desconhecido")
    NENHUM = "01", _("Nenhum")
    ADM = "02", _("Adm. Pública e Repr. Internacional")
    ALUGUEL = "03", _("Alugueis e Arrend. Mercantil de maquinas")
    ARRENDAMENTO = "04", _(
        "Arrendamento Mercantil de aeronave para empresa de transporte aéreo público"
    )
    COMISSAO = "05", _("Comissão a agentes externos na exportação")
    DESPESAS = "06", _(
        "Despesas de armazenagem, mov. e transporte de carga no exterior"
    )
    FIFA_SUBS = "07", _("Eventos FIFA (subsidiária)")
    FIFA = "08", _("Eventos FIFA")
    FRETE = "09", _("Frete Internacional")
    MATERIAL = "10", _("Materiais Aeronáuticos")
    PROM_BENS = "11", _("Promoção de Bens e Serviços no Exterior")
    PROM_DEST = "12", _("Promoção de Destinos Turísticos no Exterior")
    PROM_BRASIL = "13", _("Promoção do Brasil no Exterior")
    PROM_SERV = "14", _("Promoção de Serviços no Exterior")
    RECINE = "15", _("Recine")
    RECOPA = "16", _("Recopa")
    REGISTRO = "17", _("Registro de Marcas e Patentes no Exterior")
    REICOMP = "18", _("ReiComp")
    REIDI = "19", _("Reidi")
    REPENEC = "20", _("Repene")
    REPES = "21", _("Repes")
    RETAERO = "22", _("Retenção de Aeronave no Exterior")
    RETIDO = "23", _("Retido no Exterior")
    ROYALTIES = "24", _("Royalties e Direitos de Propriedade Intelectual")
    SERVICOS = "25", _("Serviços Técnicos e Profissionais no Exterior")
    ZPE = "26", _("Zona de Processamento de Exportação - ZPE")


class MOVTEMPBENS(models.IntegerChoices):
    DESCONHECIDO = 0, _("Desconhecido")
    NAO = 1, _("Não")
    VINCULADA_IMP = 2, _("Vinculada à Importação")
    VINCULADA_EXP = 3, _("Vinculada à Exportação")
