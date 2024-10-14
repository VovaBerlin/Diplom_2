import pytest
import requests
import allure

from data import Urls, Handlers, Ingredient, ResponseText


class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией.")
    def test_create_order_with_auth(self, setup_user):
        auth_token = {'Authorization': setup_user[0]}
        response = requests.post(f'{Urls.URL}{Handlers.CREATE_ORDER}', headers=auth_token,
                                 data=Ingredient.correct_ingredients)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Создание заказа без авторизацией.")
    def test_create_order_without_auth(self):
        response = requests.post(f'{Urls.URL}{Handlers.CREATE_ORDER}', data=Ingredient.correct_ingredients)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка создания заказа без ингредиентов.")
    def test_create_order_without_ingredients(self):
        response = requests.post(f'{Urls.URL}{Handlers.CREATE_ORDER}')
        assert response.status_code == 400 and ResponseText.WITHOUT_INGREDIENTS in response.text

    @allure.title("Проверка создания заказа с некорректным хэшем ингредиента.")
    def test_create_order_with_incorrect_hash_ingredient(self):
        response = requests.post(f'{Urls.URL}{Handlers.CREATE_ORDER}', data=Ingredient.incorrect_ingredients)
        assert response.status_code == 500 and ResponseText.ERROR in response.text
