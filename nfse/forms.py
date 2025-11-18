from django import forms
from nfse.enums import nfse_enums, tribmun_enums
from datetime import date


class EnderecoForm(forms.Form):
    cMun = forms.CharField(
        required=True,
        label="Codigo do municipio",
    )
    cep = (
        forms.CharField(
            required=True,
            label="CEP",
            max_length=8,
            widget=forms.TextInput(attrs={"placeholder": "Ex.:00000-000"}),
        ),
    )

    xLgr = forms.CharField(
        required=True,
        label="Logradouro",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: Rua da empresa"}),
    )
    nro = forms.CharField(
        required=True,
        label="Numero",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: 01"}),
    )
    xCpl = forms.CharField(
        required=False,
        label="Complemento",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: Quadra 00 / Lt 00"}),
    )
    xBairro = forms.CharField(
        required=True,
        label="Bairro",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: Bairro da empresa"}),
    )

    def __init__(self, *args, **kwargs):
        """
        Aplica a estilização do formulario
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-user"})


class cServForm(forms.Form):
    cTribNac = forms.CharField(
        required=True,
        label="Codigo Tributario Nacional",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
        max_length=6,
    )

    cTribMun = forms.CharField(
        required=False,
        label="Codigo Tributario Municipal",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
    )

    CNAE = forms.CharField(
        required=False,
        label="CNAE",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
    )

    xDescServ = forms.CharField(
        required=True,
        label="Descricao do Servico",
        widget=forms.Textarea(attrs={"class": "form-control form-control-user"}),
    )


class InfoComplForm(forms.Form):
    idDocTec = forms.CharField(
        required=False,
        label="Identificador do Documento Tecnico",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
    )

    docRef = forms.CharField(
        required=False,
        label="Documento Referencia",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
    )

    xInfComp = forms.CharField(
        required=False,
        label="Informacoes Complementares",
        widget=forms.Textarea(attrs={"class": "form-control form-control-user"}),
    )


class ServForm(forms.Form):
    cLocPrestacao = forms.CharField(
        required=True,
        label="Local de Prestação",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
    )
    cPaisPrestacao = forms.CharField(
        required=False,
        label="Pais",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
        initial="1058",
    )
    cServ = cServForm()


class TomaForm(forms.Form):
    cnpj = forms.CharField(
        required=False,
        label="CNPJ",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
    )
    cpf = forms.CharField(
        required=False,
        label="CPF",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
    )

    xNome = forms.CharField(
        required=True,
        label="Nome",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
    )

    fone = forms.CharField(
        required=False,
        label="Telefone",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
    )

    email = forms.EmailField(
        required=False,
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control form-control-user"}),
    )

    end = EnderecoForm()


class PrestForm(forms.Form):

    regTrib = forms.IntegerField(
        required=True,
        label="Regime Tributário",
        widget=forms.NumberInput(
            attrs={"class": "form-control form-control-user"},
        ),
    )


class TribMunForm(forms.Form):
    tribISSQN = forms.ChoiceField(
        required=True,
        label="Tributacao ISSQN sobre o serviço prestado",
        choices=tribmun_enums.TRIBISSQN.choices,
    )
    cLocIncid = forms.CharField(
        required=False,
        label="Local de Incidência",
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-user"},
        ),
    )
    cPaisResult = forms.CharField(
        required=False,
        label="Codigo Pais Resultante",
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-user"},
        ),
        initial="1058",
    )

    tpImunidade = forms.ChoiceField(
        required=False,
        label="Tipo de Imunidade",
        choices=tribmun_enums.TPIMUNIDADE.choices,
    )

    vBC = forms.DecimalField(
        required=False,
        label="Base de Calculo",
    )

    pAliq = forms.DecimalField(
        required=False,
        label="Aliquota",
    )

    vISSQN = forms.DecimalField(
        required=False,
        label="Valor ISSQN",
    )

    tpRetISSQN = forms.ChoiceField(
        required=False,
        label="Tipo de Retencao ISSQN",
        choices=tribmun_enums.TPRETISSQN.choices,
    )

    vLiq = forms.DecimalField(
        required=False,
        label="Valor Liquido",
    )

    def __init__(self, *args, **kwargs):
        """
        Aplica a estilização do formulario
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-user"})


class vTotTribForm(forms.Form):
    vTotTribFed = forms.DecimalField(
        required=True,
        label="Valor Total Tributos Federais",
    )
    vTotTribEst = forms.DecimalField(
        required=True,
        label="Valor Total Tributos Estaduais",
    )
    vTotTribMun = forms.DecimalField(
        required=True,
        label="Valor Total Tributos Municipais",
    )

    def __init__(self, *args, **kwargs):
        """
        Aplica a estilização do formulario
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-user"})


class pTotTribForm(forms.Form):
    pTotTribFed = forms.DecimalField(
        required=True,
        label="Percentual Total Tributos Federais",
    )
    pTotTribEst = forms.DecimalField(
        required=True,
        label="Percentual Total Tributos Estaduais",
    )
    pTotTribMun = forms.DecimalField(
        required=True,
        label="Percentual Total Tributos Municipais",
    )

    def __init__(self, *args, **kwargs):
        """
        Aplica a estilização do formulario
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-user"})


class TotTribForm(forms.Form):
    vTotTrib = vTotTribForm()
    pTotTrib = pTotTribForm()
    indTotTrib = forms.IntegerField(
        required=True, label="Indicador Total Tributos", initial=0
    )

    def __init__(self, *args, **kwargs):
        """
        Aplica a estilização do formulario
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-user"})


class TribForm(forms.Form):
    tribMun = TribMunForm()
    totTrib = TotTribForm()


class vServPrestForm(forms.Form):
    vReceb = forms.DecimalField(
        required=True,
        label="Valor Recebido",
        widget=forms.NumberInput(attrs={"class": "form-control form-control-user"}),
    )
    vServ = forms.DecimalField(
        required=True,
        label="Valor do Servico",
        widget=forms.NumberInput(attrs={"class": "form-control form-control-user"}),
    )


class ValoresForm(forms.Form):
    vServPrest = vServPrestForm()
    trib = TribForm()


class InfDPSForm(forms.Form):
    tpAmb = forms.IntegerField(
        required=True,
        label="Ambiente",
        widget=forms.Select(
            choices=nfse_enums.AMBIENTE.choices,
            attrs={"class": "form-control form-control-user"},
        ),
    )

    dhEmi = forms.DateField(
        required=True,
        label="Data de Emissão",
        widget=forms.DateInput(attrs={"class": "form-control form-control-user"}),
        initial=date.today,
    )

    def __init__(self, *args, **kwargs):
        """
        Aplica a estilização do formulario
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-user"})


class EmitNFSeForm(forms.Form):
    provedor = forms.CharField(
        required=True,
        label="Provedor",
        widget=forms.Select(
            choices=nfse_enums.PROVEDOR.choices,
            attrs={"class": "form-control form-control-user"},
        ),
        initial=nfse_enums.PROVEDOR.PRADAO,
    )

    ambiente = forms.CharField(
        required=True,
        label="Ambiente",
        initial=nfse_enums.AMBIENTE.HOMO,
        widget=forms.Select(
            choices=nfse_enums.AMBIENTE.choices,
            attrs={"class": "form-control form-control-user"},
        ),
    )
    referencia = forms.CharField(
        required=False,
        label="Referencia",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
    )

    def __init__(self, *args, **kwargs):
        """
        Aplica a estilização do formulario
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-user"})
