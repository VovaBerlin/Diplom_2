import pytest
import requests
import allure
from data import Urls, Handlers, ResponseText
from tools import RegData


class TestCreateUser:
    @allure.title('Создание нового пользователя.')
    def test_create_new_user(self):
        response = requests.post(f'{Urls.URL}{Handlers.CREATE_USER}', json=RegData.create_user())
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Проверка создания пользователя, который уже зарегистрирован.')
    def test_create_double_user_error(self):
        response = requests.post(f'{Urls.URL}{Handlers.CREATE_USER}', json=RegData.reg_double_user)
        assert response.status_code == 403 and ResponseText.USER_ALREADY_EXISTS in response.text

    @allure.title('Проверка регистриции пользователя с незаполненными обязательными полями.')
    @pytest.mark.parametrize('reg_data', [RegData.reg_without_name, RegData.reg_without_email, RegData.reg_without_pswd])
    def test_create_user_without_data_error(self, reg_data):
        response = requests.post(f'{Urls.URL}{Handlers.CREATE_USER}', data=reg_data)
        assert response.status_code == 403 and ResponseText.REG_WITHOUT_DATA in response.text

