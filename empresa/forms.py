from django import forms
from value_objects.cep import CEP
from value_objects.cnpj import CNPJ
from value_objects.cpf import CPF
from pydantic import ValidationError
from empresa.models import Certificado
from empresa.enums.config_nfse_enums import *


class EnderecoForm(forms.Form):
    """
    Formulário para cadastro de endereço
    """

    cep = forms.CharField(
        required=True,
        label="CEP",
        max_length=8,
        widget=forms.TextInput(attrs={"placeholder": "Ex.:00000-000"}),
    )
    logradouro = forms.CharField(
        required=True,
        label="Logradouro",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: Rua da empresa"}),
    )
    complemento = forms.CharField(
        required=False,
        label="Complemento",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: Quadra 00 / Lt 00"}),
    )
    bairro = forms.CharField(
        required=True,
        label="Bairro",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: Bairro da empresa"}),
    )
    cidade = forms.CharField(
        required=False,
        label="Cidade",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: Cidade da empresa"}),
    )
    uf = forms.CharField(
        required=True,
        label="UF",
        max_length=2,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: SP"}),
    )
    numero = forms.CharField(
        required=True,
        label="Número",
        max_length=10,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: 0000"}),
    )
    codigo_pais = forms.CharField(
        required=False, label="Código do Pais", initial="1058"
    )
    pais = forms.CharField(required=False, label="Pais", initial="Brasil")

    def __init__(self, *args, **kwargs):
        """
        Aplica a estilização do formulario
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-user"})

    def clean_cep(self):
        """
        Valida CEP
        """
        cep = self.cleaned_data.get("cep")
        if cep:
            try:
                valid_cep = CEP(value=cep.strip())
                return valid_cep
            except ValidationError as e:
                mensagens = [err["msg"] for err in e.errors()]
                raise forms.ValidationError(f"CEP inválido: {mensagens[0]}")


class EmpresaForm(forms.Form):
    """
    Formulario da Empresa
    """

    cpf_cnpj = forms.CharField(
        required=True,
        label="CNPJ ou CPF",
        max_length=14,
    )
    created_at = forms.DateField(required=False, widget=forms.HiddenInput())
    updated_at = forms.DateField(required=False, widget=forms.HiddenInput())
    inscricao_estadual = forms.CharField(required=False, label="Inscrição Estadual")
    inscricao_municipal = forms.CharField(required=False, label="Inscrição Municipal")
    nome_razao_social = forms.CharField(
        required=True, label="Razão Social", max_length=100
    )
    nome_fantasia = forms.CharField(
        required=True, label="Nome Fantasia", max_length=100
    )
    fone = forms.CharField(required=False, label="Telefone", max_length=20)
    email = forms.EmailField(
        required=True,
        label="Email",
        max_length=100,
    )

    def __init__(self, *args, **kwargs):
        """
        Aplica a estilização do formulario
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-user"})

    def clean_cpf_cnpj(self):
        """
        Valida CPF ou CNPJ
        """
        cpf_cnpj = self.cleaned_data.get("cpf_cnpj")
        if cpf_cnpj:
            try:
                valid_cpf = CPF(value=cpf_cnpj.strip())
                return valid_cpf.get()
            except:
                try:
                    valid_cnpj = CNPJ(value=cpf_cnpj.strip())
                    return valid_cnpj.get()
                except ValidationError as e:
                    mensagens = [err["msg"] for err in e.errors()]
                    raise forms.ValidationError(f"CPF ou CNPJ inválido: {mensagens[0]}")

    def clean_telefone(self):
        """
        Valida telefone
        """
        telefone = self.cleaned_data.get("telefone")
        if telefone:
            telefone = telefone.strip()
            if not telefone.isdigit():
                raise forms.ValidationError("O telefone deve conter apenas números.")
            else:
                return telefone


class CertificadoForm(forms.Form):
    """
    form de cadastro ou atualização do certificado
    """

    certificado = forms.FileField(required=True, label="Certificado", max_length=100)

    password = forms.CharField(required=True, label="Senha", max_length=100)

    def __init__(self, *args, **kwargs):
        """
        Aplica a estilização do formulario
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-user"})

    def clean_certificado(self):
        certificado = self.cleaned_data.get("certificado")
        if certificado:
            try:
                certificado_valid = Certificado(certificado=certificado, password="123")
            except ValidationError as e:
                mensagens = [err["msg"] for err in e.errors()]
                raise forms.ValidationError(
                    f"Certificado inválido: {str(mensagens[0])}"
                )
            return certificado


class ConfigNFSeForm(forms.Form):
    opSimpNac = forms.ChoiceField(
        required=False,
        choices=opSimpNacEnum.choices,
        label="Situação perante o Simples Nacional",
    )

    regApTribSN = forms.ChoiceField(
        required=False,
        choices=regApTribSNEnum.choices,
        label="Regime especial de tributação social",
    )

    regEspTrib = forms.ChoiceField(
        required=False,
        choices=regEspTribEnum.choices,
        label="Regime especial de tributação",
    )

    lote = forms.IntegerField(required=True, label="Lote")
    serie = forms.CharField(required=True, label="Serie")
    numero = forms.IntegerField(required=True, label="Numero")
    login = forms.CharField(required=False, label="Login")
    senha = forms.CharField(required=False, label="Senha", widget=forms.PasswordInput())
    token = forms.CharField(required=False, label="Token")
    incentivo_fical = forms.BooleanField(required=False, label="Incentivo Fiscal")
    ambiente = forms.ChoiceField(required=True, choices=AmbienteEnum.choices)

    def __init__(self, *args, **kwargs):
        """
        Aplica a estilização do formulario
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-user"})
