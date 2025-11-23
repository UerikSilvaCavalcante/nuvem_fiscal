import requests
import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))

db = client["nfse_false_db"]


def get_cancelamento_situacao(token, nfse_id):
    base_url = str(os.getenv("BASE_URL"))
    endpoint = f"nfse/{nfse_id}/cancelamento"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    try:
        # response = requests.get(f"{base_url}{endpoint}", headers=headers)
        data = db.cancelamento.find_one({"id": nfse_id})
        response = {"data": data}
        return response
    except Exception as e:
        raise Exception(f"Erro ao obter as cidades atendidas: {str(e)}")
