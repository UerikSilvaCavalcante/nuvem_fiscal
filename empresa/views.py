from django.shortcuts import render, redirect
from .forms import EmpresaForm, EnderecoForm
from .service.payloads.cad_empresa_payload import generate_payload
from .service.api.get_empresas import get_empresas
import json


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

            payload = generate_payload(empresa_form, endereco_form)
            print(
                json.dumps(
                    payload,
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
