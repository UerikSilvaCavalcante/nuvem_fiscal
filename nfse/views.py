from django.shortcuts import render
from nfse.forms import EmitNFSeForm, InfDPSForm, PrestForm, TomaForm, ServForm, ValoresForm


# Create your views here.
def emit_nfse(request):
    nfse_form = EmitNFSeForm()
    infDPS_form = InfDPSForm()
    prest_form = PrestForm()
    toma_form = TomaForm()
    serv_form = ServForm()
    valores_form = ValoresForm()
    
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
