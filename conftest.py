import pytest
import requests

from data import Urls, Handlers
from tools import RegData


@pytest.fixture(scope="function")
def setup_user():
    payload = RegData.create_user()
    response = requests.post(f"{Urls.URL}{Handlers.CREATE_USER}", data=payload)
    auth_token = response.json()["accessToken"]
    yield auth_token
    requests.delete(f"{Urls.URL}{Handlers.DELETE_USER}", headers={'Authorization': f'{auth_token}'})

