from django import forms


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
            cep = cep.strip()
            if not cep.isdigit():
                raise forms.ValidationError("O CEP deve conter apenas números.")
            elif len(cep) != 8:
                raise forms.ValidationError("O CEP deve conter 8 números.")
            else:
                return cep


class EmpresaForm(forms.Form):
    """
    Formulario da Empresa
    """

    cpf_cnpj = forms.CharField(required=True, label="CNPJ ou CPF", max_length=14)
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
    telefone = forms.CharField(required=False, label="Telefone", max_length=20)
    email = forms.EmailField(required=True, label="Email", max_length=100)

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
            cpf_cnpj = cpf_cnpj.strip()
            if not cpf_cnpj.isdigit():
                raise forms.ValidationError("O CPF/CNPJ deve conter apenas números.")
            elif len(cpf_cnpj) != 11 and len(cpf_cnpj) != 14:
                raise forms.ValidationError("O CPF/CNPJ deve conter 11 ou 14 números.")
            else:
                return cpf_cnpj

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
