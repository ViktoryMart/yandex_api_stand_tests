import configuration
import requests
import data
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)
# Функция для получения данных из таблицы пользователей
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
# Определение функции для отправки POST-запроса на поиск наборов по продуктам
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,  # Тело запроса содержит ID продуктов в формате JSON
                         headers=data.headers)  # Использование заголовков из файла data.py
