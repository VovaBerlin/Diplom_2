import allure
import requests

from data import Urls, Handlers, Ingredient, ResponseText


class TestGetOrder:
    @allure.title('Получение заказов авторизованного пользователя.')
    def test_get_order_user_with_auth(self, setup_user):
        auth_token = {'Authorization': setup_user}
        requests.post(f'{Urls.URL}{Handlers.CREATE_ORDER}', headers=auth_token,
                      data=Ingredient.correct_ingredients)
        response_get = requests.get(f'{Urls.URL}{Handlers.GET_ORDERS}', headers=auth_token)
        assert response_get.status_code == 200 and response_get.json()['success'] == True

    @allure.title('Получение заказов без авторизации.')
    def test_get_order_user_without_auth(self):
        requests.post(f'{Urls.URL}{Handlers.CREATE_ORDER}', data=Ingredient.correct_ingredients)
        response_get = requests.get(f'{Urls.URL}{Handlers.GET_ORDERS}')
        assert response_get.status_code == 401 and ResponseText.AUTH_ERROR in response_get.text
