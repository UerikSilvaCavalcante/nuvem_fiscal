import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def get_metadados_cidade(token: str, cod_ibge: str):
    base_url = str(os.getenv("BASE_URL"))
    endpoint = f"nfse/cidades/{cod_ibge}"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    try:
        response = requests.get(f"{base_url}{endpoint}", headers=headers)
        return response.json()
    except Exception as e:
        raise Exception(f"Erro ao obter as cidades atendidas: {str(e)}")
