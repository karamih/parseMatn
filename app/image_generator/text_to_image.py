import requests
from app.config import settings

API_URL = settings.api_url
headers = {'Authorization': settings.headers}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content
