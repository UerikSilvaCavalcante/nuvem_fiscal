import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def get_nfses(token: str, cpf_cnpj: str, ambiente: str):
    base_url = str(os.getenv("BASE_URL"))
    endpoint = f"nfse/?cpf_cnpj={cpf_cnpj}&ambiente={ambiente}"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    try:
        response = requests.get(f"{base_url}{endpoint}", headers=headers)
        return response.json()
    except Exception as e:
        raise Exception(f"Erro ao obter as NFSes: {str(e)}")
