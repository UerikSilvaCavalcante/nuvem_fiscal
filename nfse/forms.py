from django import forms
from nfse.enums import tribmun_enums
from nfse.enums.nfse_enums import PROVEDOR, AMBIENTE
from datetime import date
from value_objects.cpf import CPF
from value_objects.cep import CEP
from value_objects.cnpj import CNPJ
from pydantic import ValidationError


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

    cNBS = forms.CharField(
        required=False,
        label="NBS",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
    )

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

    def clean_cTribNac(self):
        cTribNac = self.cleaned_data.get("cTribNac")
        if cTribNac:
            if not cTribNac.isdigit():
                raise forms.ValidationError(
                    "O codigo tributario nacional deve ser um numero"
                )
            else:
                return cTribNac

    def clean_cTribMun(self):
        cTribMun = self.cleaned_data.get("cTribMun")
        if cTribMun:
            if not cTribMun.isdigit():
                raise forms.ValidationError(
                    "O codigo tributario municipal deve ser um numero"
                )
            else:
                return cTribMun


class TomaForm(forms.Form):
    cnpj = forms.CharField(
        required=True,
        label="CNPJ",
        max_length=14,
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
    )
    cpf = forms.CharField(
        required=True,
        label="CPF",
        max_length=11,
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

    nif = forms.CharField(
        required=False,
        label="NIF (Número de Identificação Fiscal fornecido por órgão de administração tributária no exterior)",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
    )

    cep = forms.CharField(
        required=True,
        label="CEP",
        widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
        max_length=8,
    )

    # cMun = forms.CharField(
    #     required=True,
    #     label="Codigo do municipio",
    # )

    cMun = forms.CharField(
        required=True,
        label="Codigo do municipio",
        widget=forms.TextInput(attrs={"list": "cidades"}),
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

    def clean_cpf(self):
        cpf = self.cleaned_data.get("cpf")
        if cpf:
            try:
                valid_cpf = CPF(value=cpf.strip())
                return valid_cpf
            except ValidationError as e:
                mensagens = [err["msg"] for err in e.errors()]
                raise forms.ValidationError(f"CPF inválido: {mensagens[0]}")

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get("cnpj")
        if cnpj:
            try:
                valid_cnpj = CNPJ(value=cnpj.strip())
                return valid_cnpj
            except ValidationError as e:
                mensagens = [err["msg"] for err in e.errors()]
                raise forms.ValidationError(f"CNPJ inválido: {mensagens[0]}")

    def clean_cep(self):
        cep = self.cleaned_data.get("cep")
        if cep:
            try:
                valid_cep = CEP(value=cep.strip())
                return valid_cep
            except ValidationError as e:
                mensagens = [err["msg"] for err in e.errors()]
                raise forms.ValidationError(f"CEP inválido: {mensagens[0]}")

    def clean_cMun(self):
        cMun = self.cleaned_data.get("cMun")
        if cMun:
            if not cMun.isdigit():
                raise forms.ValidationError("O municipio deve conter apenas números.")
            else:
                return cMun

    def __init__(self, *args, **kwargs):
        """
        Aplica a estilização do formulario
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-user"})


# class PrestForm(forms.Form):
#     cnpj = forms.CharField(
#         required=False,
#         label="CNPJ",
#         max_length=14,
#         widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
#     )

#     cpf = forms.CharField(
#         required=False,
#         label="CPF",
#         max_length=11,
#         widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
#     )

#     xNome = forms.CharField(
#         required=True,
#         label="Nome",
#         widget=forms.TextInput(attrs={"class": "form-control form-control-user"}),
#     )

#     regTrib = forms.IntegerField(
#         required=True,
#         label="Regime Tributário",
#         widget=forms.NumberInput(
#             attrs={"class": "form-control form-control-user"},
#         ),
#     )

#     def clean_cnpj(self):
#         cnpj = self.cleaned_data.get("cnpj")
#         if cnpj:
#             try:
#                 valid_cnpj = CNPJ(value=cnpj.strip())
#                 return valid_cnpj.get()
#             except ValidationError as e:
#                 mensagens = [err["msg"] for err in e.errors()]
#                 raise forms.ValidationError(f"CNPJ inválido: {mensagens[0]}")

#     def clean_cep(self):
#         cep = self.cleaned_data.get("cep")
#         if cep:
#             try:
#                 valid_cep = CEP(value=cep.strip())
#                 return valid_cep
#             except ValidationError as e:
#                 mensagens = [err["msg"] for err in e.errors()]
#                 raise forms.ValidationError(f"CEP inválido: {mensagens[0]}")


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


class ValoresForm(forms.Form):
    vReceb = forms.DecimalField(
        required=False,
        label="Valor Recebido",
        widget=forms.NumberInput(attrs={"class": "form-control form-control-user"}),
    )
    vServ = forms.DecimalField(
        required=True,
        label="Valor do Servico",
        widget=forms.NumberInput(attrs={"class": "form-control form-control-user"}),
    )

    vDescCond = forms.DecimalField(
        required=False,
        label="Desconto Condicional",
        widget=forms.NumberInput(attrs={"class": "form-control form-control-user"}),
    )

    vDescIncond = forms.DecimalField(
        required=False,
        label="Desconto Incondicional",
        widget=forms.NumberInput(attrs={"class": "form-control form-control-user"}),
    )

    # tribMun
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
        initial="0",
    )

    pAliq = forms.DecimalField(
        required=False,
        label="Porcentagem Aliquota",
    )

    tpRetISSQN = forms.ChoiceField(
        required=False,
        label="Tipo de Retencao ISSQN",
        choices=tribmun_enums.TPRETISSQN.choices,
    )

    # tribFed

    aplica_trib_fed = forms.BooleanField(
        label="Aplicar retenção Federal (PIS/COFINS/IR/CSLL)", required=False
    )

    # totTrib
    vTotTrib = forms.DecimalField(
        label="Valor monetário dos tributos federais",
        required=False,
    )

    vTotTribEst = forms.DecimalField(
        label="Valor monetário dos tributos estaduais",
        required=False,
    )

    vTotTribMun = forms.DecimalField(
        label="Valor monetário dos tributos municipais",
        required=False,
    )

    pTotTribFed = forms.DecimalField(
        label="Percentual dos tributos federais",
        required=False,
    )

    pTotTribEst = forms.DecimalField(
        label="Percentual dos tributos estaduais",
        required=False,
    )

    pTotTribMun = forms.DecimalField(
        label="Percentual dos tributos municipais",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        """
        Aplica a estilização do formulario
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-user"})
        # Desabilita tpImunidade se tribISSQN não for "imune"
        if self.data and self.data.get("tribISSQN") != tribmun_enums.TRIBISSQN.OP_IMUNE:
            self.fields["tpImunidade"].disabled = True


class InfDPSForm(forms.Form):
    tpAmb = forms.ChoiceField(
        required=True,
        label="Ambiente",
        choices=AMBIENTE.choices,
    )

    dhEmi = forms.DateField(
        required=True,
        label="Data de Emissão",
        widget=forms.DateInput(attrs={"class": "form-control form-control-user"}),
        initial=date.today,
    )
    dhCompet = forms.DateField(
        required=True,
        label="Data de Competência",
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
            choices=PROVEDOR.choices,
            attrs={"class": "form-control form-control-user"},
        ),
        initial=PROVEDOR.PRADAO,
    )

    ambiente = forms.CharField(
        required=True,
        label="Ambiente",
        initial=AMBIENTE.HOMO,
        widget=forms.Select(
            choices=AMBIENTE.choices,
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
