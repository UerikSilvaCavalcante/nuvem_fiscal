from django.shortcuts import render, redirect
from .forms import EmpresaForm, EnderecoForm, CertificadoForm, ConfigNFSeForm
from empresa.service.serializers.empresa_serializer import EmpresaSerializer
from empresa.service.serializers.certificado_serializer import CertificadoSerializer
from empresa.service.serializers.config_nfse_serializer import ConfigNFSeSerializer
from .service.api.get_empresa_by_id import get_empresa_by_id
from .service.api.get_empresas import get_empresas
from .service.api.get_certificado import get_certificado
from .service.api.get_config_nfse import get_config_nfse
import json
from django.contrib import messages
from empresa.models import Empresa, Endereco, Certificado, ConfigNFSe


# Create your views here.
def consultar_empresa(request):
    data = get_empresas(request.user)
    return render(request, "empresa/consultar_empresa.html", {"data": data})


def cad_empresa(request):
    """
    Rota de Cadastrar empresa
    """
    empresa_form = EmpresaForm(prefix="empresa")
    endereco_form = EnderecoForm(prefix="endereco")
    if request.method == "POST":
        empresa_form = EmpresaForm(request.POST, prefix="empresa")
        endereco_form = EnderecoForm(request.POST, prefix="endereco")

        if empresa_form.is_valid() and endereco_form.is_valid():
            empresa_serializer = EmpresaSerializer(
                Empresa(**empresa_form.cleaned_data),
                Endereco(**endereco_form.cleaned_data),
            )

            print(
                json.dumps(
                    empresa_serializer.serialize(),
                    indent=4,
                    ensure_ascii=False,
                )
            )
            return redirect("home")

    return render(
        request,
        "empresa/cad_empresa.html",
        {"empresa_form": empresa_form, "endereco_form": endereco_form},
    )


def info_empresa(request, id):
    """
    Rota de Informações da empresa
    """
    user = request.user
    try:
        empresa_info = get_empresa_by_id(user.token, id)
        certificado = get_certificado(user.token, id)
        config_nfse = get_config_nfse(user.token, id)

        return render(
            request,
            "empresa/info_empresa.html",
            {
                "empresa": empresa_info,
                "certificado": certificado,
                "config_nfse": config_nfse,
            },
        )
    except Exception as e:
        print(e)
        messages.error(request, "Erro ao buscar informações sobre a empresa.")
        return redirect("consultar_empresa")


def cad_certificado(request, cpf_cnpj: str):
    certificado_form = CertificadoForm()

    if request.method == "POST":
        certificado_form = CertificadoForm(request.POST, request.FILES)
        if certificado_form.is_valid():
            new_certificado = Certificado(**certificado_form.cleaned_data)
            new_certificado_serializer = CertificadoSerializer(new_certificado)
            print(json.dumps(new_certificado_serializer.serialize(), indent=4))
            return redirect("info_empresa", id=cpf_cnpj)

    return render(
        request,
        "empresa/cad_certificado.html",
        {"certificado_form": certificado_form, "cpf_cnpj": cpf_cnpj},
    )


def config_nfse(request, cpf_cnpj: str):
    config_nfse_form = ConfigNFSeForm()

    if request.method == "POST":
        config_nfse_form = ConfigNFSeForm(request.POST)
        if config_nfse_form.is_valid():
            config_nfse_valid = ConfigNFSe(**config_nfse_form.cleaned_data)
            config_nfse_serializer = ConfigNFSeSerializer(config_nfse_valid)
            print(json.dumps(config_nfse_serializer.serialize(), indent=4))
            return redirect("info_empresa", id=cpf_cnpj)
    return render(
        request,
        "empresa/config_nfse.html",
        {"config_nfse_form": config_nfse_form, "cpf_cnpj": cpf_cnpj},
    )
