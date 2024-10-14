import allure
import pytest
import requests

from data import Urls, Handlers, ResponseText
from tools import RegData


class TestChangingUserData:

    @allure.title("Успешное изменение имени авторизованного пользователя")
    def test_update_user_name_with_auth(self, setup_user):
        new_name = {'name': RegData.create_user()["name"]}
        auth_token = {'Authorization': setup_user}
        response = requests.patch(f"{Urls.URL}{Handlers.UPDATE_USER}", headers=auth_token, data=new_name)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Успешное изменение email авторизованного пользователя")
    def test_update_user_email_with_auth(self, setup_user):
        new_email = {'email': RegData.create_user()["email"]}
        auth_token = {'Authorization': setup_user}
        response = requests.patch(f"{Urls.URL}{Handlers.UPDATE_USER}", headers=auth_token, data=new_email)
        assert response.status_code == 200 and response.json()['user']['email'] == new_email["email"]

    @allure.title("Успешное изменение пароля авторизованного пользователя")
    def test_update_user_password_with_auth(self, setup_user):
        new_pswd = {'password': RegData.create_user()["password"]}
        auth_token = {'Authorization': setup_user}
        response = requests.patch(f"{Urls.URL}{Handlers.UPDATE_USER}", headers=auth_token, data=new_pswd)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка изменения данных неавторизованного пользователя")
    @pytest.mark.parametrize('new_data, data', [['new_name', 'name'], ['new_pswd', 'password'], ['new_email', 'email']])
    def test_update_user_datas_without_auth(self, setup_user, new_data, data):
        new_data = {data: RegData.create_user()[data]}
        response = requests.patch(f"{Urls.URL}{Handlers.UPDATE_USER}", data=new_data)
        assert response.status_code == 401 and ResponseText.UPDATE_WITHOUT_AUTH in response.text
