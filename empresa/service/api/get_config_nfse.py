import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_config_nfse(token, empresa_id):
    """
    Função para obter a configuração de NFSe de uma empresa específica.
    """
    base_url = str(os.getenv("BASE_URL"))
    endpoint = f"/empresas/{empresa_id}/nfse"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    try:
        response = requests.get(f"{base_url}{endpoint}", headers=headers)
        return response.json()
    except Exception as e:
        raise Exception(f"Erro ao obter a configuração de NFSe: {str(e)}")
