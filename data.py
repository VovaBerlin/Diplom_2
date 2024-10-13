import allure
import requests


class Urls:
    URL = 'https://stellarburgers.nomoreparties.site'


class Handlers:
    CREATE_USER = '/api/auth/register'
    CREATE_ORDER = '/api/orders'
    UPDATE_USER = '/api/auth/user'
    LOGIN = '/api/auth/login'
    GET_ORDERS = '/api/orders'
    DELETE_USER = '/api/auth/user'
    headers = {"Content-Type": "application/json"}


class ResponseText:
    USER_ALREADY_EXISTS = 'User already exists'
    REG_WITHOUT_DATA = 'Email, password and name are required fields'
    INCORRECT_LOGIN = 'email or password are incorrect'
    UPDATE_WITHOUT_AUTH = 'You should be authorised'
    WITHOUT_INGREDIENTS = 'Ingredient ids must be provided'
    ERROR = 'Internal Server Error'
    AUTH_ERROR = 'You should be authorised'


class Ingredient:
    correct_ingredients = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70"]}

    incorrect_ingredients = {
        "ingredients": ["01c0c5a71d1f82001bdaaa6f", "11c0c5a71d1f82001bdaaa70"]}

