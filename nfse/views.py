from django.shortcuts import render, redirect
from nfse.forms import (
    EmitNFSeForm,
    InfDPSForm,
    PrestForm,
    TomaForm,
    ServForm,
    ValoresForm,
)
import json


# Create your views here.
def emit_nfse(request):
    nfse_form = EmitNFSeForm(prefix="nfse")
    infDPS_form = InfDPSForm(prefix="infDPS")
    prest_form = PrestForm(prefix="prest")
    toma_form = TomaForm(prefix="toma")
    serv_form = ServForm(prefix="serv")
    valores_form = ValoresForm(prefix="valores")
    if request.method == "POST":
        nfse_form = EmitNFSeForm(request.POST, prefix="nfse")
        infDPS_form = InfDPSForm(request.POST, prefix="infDPS")
        prest_form = PrestForm(request.POST, prefix="prest")
        toma_form = TomaForm(request.POST, prefix="toma")
        serv_form = ServForm(request.POST, prefix="serv")
        valores_form = ValoresForm(request.POST, prefix="valores")
        if all(
            [
                nfse_form.is_valid(),
                infDPS_form.is_valid(),
                prest_form.is_valid(),
                toma_form.is_valid(),
                serv_form.is_valid(),
                valores_form.is_valid(),
            ]
        ):
            print(
                f"NFSe: {nfse_form.cleaned_data}",
                f"InfDPS: {infDPS_form.cleaned_data}",
                f"Prest: {prest_form.cleaned_data}",
                f"Toma: {toma_form.cleaned_data}",
                f"Serv: {serv_form.cleaned_data}",
                f"Valores: {valores_form.cleaned_data}",
            )
            return redirect("emit_nfse")

    return render(
        request,
        "nfse/emit_nfse.html",
        {
            "nfse_form": nfse_form,
            "infDPS_form": infDPS_form,
            "prest_form": prest_form,
            "toma_form": toma_form,
            "serv_form": serv_form,
            "valores_form": valores_form,
        },
    )
