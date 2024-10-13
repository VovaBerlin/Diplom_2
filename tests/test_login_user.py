import allure
import requests

from data import Urls, Handlers, ResponseText
from tools import RegData


class TestLogin:
    @allure.title('Авторизация с корректными данными.')
    def test_login_success(self):
        response = requests.post(f'{Urls.URL}{Handlers.LOGIN}', data=RegData.correct_user)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Авторизация с некорректным логином или паролем.')
    def test_login_with_incorrect_data_error(self):
        response = requests.post(f'{Urls.URL}{Handlers.LOGIN}', data=RegData.incorrect_user)
        assert response.status_code == 401 and ResponseText.INCORRECT_LOGIN in response.text