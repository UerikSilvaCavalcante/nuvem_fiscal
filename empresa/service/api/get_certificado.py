import requests
import os
from dotenv import load_dotenv


def get_certificado(token, empresa_id):
    """
    Função para obter o certificado de uma empresa específica.
    """
    load_dotenv()
    base_url = str(os.getenv("BASE_URL"))
    endpoint = f"/empresas/{empresa_id}/certificado"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    try:
        response = requests.get(f"{base_url}{endpoint}", headers=headers)

        return response.json()
    except Exception as e:
        raise Exception(f"Erro ao obter o certificado: {str(e)}")
