from dotenv import load_dotenv
import requests
import os


def get_empresas(user):
    load_dotenv()
    url = str(os.getenv("BASE_URL"))
    headers = {"Authorization": f"Bearer {user.token}"}
    res = requests.get(f"{url}/empresas", headers=headers)
    data = res.json()
    return data["data"]
