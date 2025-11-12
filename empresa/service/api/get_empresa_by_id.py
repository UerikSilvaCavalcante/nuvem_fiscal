import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_empresa_by_id(token, cpf_cnpj):
    """
    Função para obter os dados de uma empresa específica pelo ID
    """
    url = str(os.getenv("BASE_URL"))
    headers = {"Authorization": f"Bearer {token}"}
    try:

        data = requests.get(f"{url}/empresas/{cpf_cnpj}", headers=headers)
        return data.json()
    except Exception as e:
        raise Exception(f"Erro ao obter empresa")