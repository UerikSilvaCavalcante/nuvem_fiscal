import os
import requests
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["nfse_false_db"]


def post_cancelar_nfse(token: str, id: str, cancelamento: dict):
    base_url = str(os.getenv("BASE_URL"))
    endpoint = f"nfse/{id}/cancelamento"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    data = cancelamento
    try:
        # response = requests.post(f"{base_url}{endpoint}", headers=headers, data=data)
        data = db.cancelamento.insert_one(cancelamento)
        return {"data": data}
    except Exception as e:
        raise Exception(f"Erro ao obter as cidades atendidas: {str(e)}")
