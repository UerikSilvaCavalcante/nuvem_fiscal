from django.shortcuts import render, redirect
from nfse.forms import (
    EmitNFSeForm,
    InfDPSForm,
    TomaForm,
    ServForm,
    ValoresForm,
)
from nfse.use_case.aply_retencoes_fed import AplyRetencoesFederais
from nfse.models import (
    NFSe,
    Serv,
    Toma,
    InfDPS,
    Valores,
    Contato,
    Identificacao,
    CServ,
    VServPreset,
    VDescCondIcond,
    Trib,
    TribFed,
    TribMun,
    Piscofins,
)
from nfse.service.helper.trata_decimal import DecimalEncoder
from value_objects.endereco import Endereco, EndExt
from value_objects.email import Email
from nfse.service.serializers.emit_nfse_serializer import NfseSerializaer
import json
from nfse.service.api.get_cidades_atendidas import get_cidades_atendidas
from nfse.service.api.get_nfses import get_nfses
from empresa.service.api.get_config_nfse import get_config_nfse


# Create your views here.
def emit_nfse(request):
    nfse_form = EmitNFSeForm(prefix="nfse")
    infDPS_form = InfDPSForm(prefix="infDPS")
    toma_form = TomaForm(prefix="toma")
    serv_form = ServForm(prefix="serv")
    valores_form = ValoresForm(prefix="valores")
    cidades_atendidas = get_cidades_atendidas(request.user.token)

    if request.method == "POST":
        nfse_form = EmitNFSeForm(request.POST, prefix="nfse")
        infDPS_form = InfDPSForm(request.POST, prefix="infDPS")
        toma_form = TomaForm(request.POST, prefix="toma")
        serv_form = ServForm(request.POST, prefix="serv")
        valores_form = ValoresForm(request.POST, prefix="valores")
        if all(
            [
                nfse_form.is_valid(),
                infDPS_form.is_valid(),
                toma_form.is_valid(),
                serv_form.is_valid(),
                valores_form.is_valid(),
            ]
        ):

            if valores_form.cleaned_data["aplica_trib_fed"]:
                impostos = AplyRetencoesFederais().execute(
                    valores_form.cleaned_data["vServ"],
                )

            # print(
            #     f"NFSe: {nfse_form.cleaned_data}",
            #     f"InfDPS: {infDPS_form.cleaned_data}",
            #     f"Toma: {toma_form.cleaned_data}",
            #     f"Serv: {serv_form.cleaned_data}",
            #     f"Valores: {valores_form.cleaned_data}",
            #     sep="\n",
            # )

            nfse_model = NFSe(
                **nfse_form.cleaned_data,
            )

            toma_model = Toma(
                contato=Contato(
                    email=Email(address=toma_form.cleaned_data["email"]),
                    fone=toma_form.cleaned_data["fone"],
                ),
                identificacao=Identificacao(
                    cnpj=toma_form.cleaned_data["cnpj"],
                    cpf=toma_form.cleaned_data["cpf"],
                    nif=toma_form.cleaned_data["nif"],
                    xNome=toma_form.cleaned_data["xNome"],
                ),
                end=Endereco(
                    xLgr=toma_form.cleaned_data["xLgr"],
                    nro=toma_form.cleaned_data["nro"],
                    xCpl=toma_form.cleaned_data["xCpl"],
                    xBairro=toma_form.cleaned_data["xBairro"],
                    cMun=toma_form.cleaned_data["cMun"],
                    cep=toma_form.cleaned_data["cep"],
                    endExt=None,
                ),
                dadosFiscais=None,
            )

            serv_model = Serv(
                cLocPrestacao=serv_form.cleaned_data["cLocPrestacao"],
                cPaisPrestacao=serv_form.cleaned_data["cPaisPrestacao"],
                cServ=CServ(
                    CNAE=serv_form.cleaned_data["CNAE"],
                    cNBS=serv_form.cleaned_data["cNBS"],
                    cTribMun=serv_form.cleaned_data["cTribMun"],
                    cTribNac=serv_form.cleaned_data["cTribNac"],
                    xDescServ=serv_form.cleaned_data["xDescServ"],
                ),
            )

            valores_model = Valores(
                vServPreset=VServPreset(
                    vReceb=valores_form.cleaned_data["vReceb"],
                    vServ=valores_form.cleaned_data["vServ"],
                ),
                vDescCondIncond=(
                    VDescCondIcond(
                        vDescIncond=valores_form.cleaned_data["vDescIncond"],
                        vDescCond=valores_form.cleaned_data["vDescCond"],
                    )
                    if valores_form.cleaned_data["vDescIncond"]
                    else None
                ),
                trib=Trib(
                    tribMun=TribMun(
                        cLocIncid=valores_form.cleaned_data["cLocIncid"],
                        cPaisResult=valores_form.cleaned_data["cPaisResult"],
                        pAliq=valores_form.cleaned_data["pAliq"],
                        tpImunidade=valores_form.cleaned_data["tpImunidade"],
                        tpRetISSQN=valores_form.cleaned_data["tpRetISSQN"],
                        tribISSQN=valores_form.cleaned_data["tribISSQN"],
                    ),
                    tribFed=(
                        TribFed(
                            piscofins=Piscofins(
                                CST=impostos.get("CST", ""),  # type: ignore
                                vPis=impostos.get("vPis", 0),  # type: ignore
                                vCofins=impostos.get("vCofins", 0),  # type: ignore
                                tpRetPisCofins=impostos.get("tpRetPisCofins", 0),  # type: ignore
                            ),
                            vRetCSLL=impostos.get("vRetCSLL", 0),  # type: ignore
                        )
                        if valores_form.cleaned_data.get("aplica_trib_fed")  # type: ignore
                        else None
                    ),
                ),
            )

            infDPS_model = InfDPS(
                dCompet=infDPS_form.cleaned_data["dhCompet"],
                dhEmi=infDPS_form.cleaned_data["dhEmi"],
                tpAmb=infDPS_form.cleaned_data["tpAmb"],
                serv=serv_model,
                toma=toma_model,
                valores=valores_model,
            )

            nfse_serializer = NfseSerializaer(
                nfse=nfse_model,
                infDPS=infDPS_model,
            ).serialize()

            print(json.dumps(nfse_serializer, indent=4, cls=DecimalEncoder))
            return redirect("emit_nfse")
    return render(
        request,
        "nfse/emit_nfse.html",
        {
            "nfse_form": nfse_form,
            "infDPS_form": infDPS_form,
            "toma_form": toma_form,
            "serv_form": serv_form,
            "valores_form": valores_form,
            "cidades": cidades_atendidas["data"],
        },
    )


def listar_nfse(request):
    config_nfse = get_config_nfse(request.user.token, "10247520000157")
    nfses = get_nfses(request.user.token, "10247520000157", "homologacao")

    return render(request, "nfse/listar_nfse.html", {"nfses": nfses.get("data")})
