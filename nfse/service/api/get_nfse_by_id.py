import requests
import json
import os
from dotenv import load_dotenv
import pymongo

load_dotenv()

from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_URI"))
db = client["nfse_false_db"]


def get_nfse_by_id(token: str, id: str):
    base_url = str(os.getenv("BASE_URL"))
    endpoint = f"nfse/{id}"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    try:
        # response = requests.get(f"{base_url}{endpoint}", headers=headers)
        data = db.nfse.find_one({"id": id})
        response = {"data": data}
        return response
    except Exception as e:
        raise Exception(f"Erro ao obter as NFSes: {str(e)}")
