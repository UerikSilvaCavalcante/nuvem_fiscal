import json


def generate_payload(empresa, endereco):
    """
        Gera e retorna o Payload para mandar para a API
    """

    payload = dict()

    keys = empresa.fields.keys()
    for key in keys:
        payload[key] = empresa.cleaned_data[key]

    payload['endereco'] = dict()
    keys = endereco.fields.keys()
    for key in keys:
        payload['endereco'][key] = endereco.cleaned_data[key]    

    return payload