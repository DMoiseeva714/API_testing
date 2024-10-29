import pytest
import requests

# Определение URL-адресов для запросов
LOGIN_URL = "https://uauirt-admin.bars.group/api/Security/Login"
DATA_URL = "https://uauirt-admin.bars.group/api/PhysicalPerson/List"

# Данные для логина
login_payload = {
    "Login": "d.moiseeva",
    "Password": "123"
}

# Данные для запроса получения информации
data_payload = {
    "Parameters": [],
    "Limit": 15,
    "Sorts": [{"PropertyName": "VersionId", "Ascendant": True}],
    "Includes": [],
    "QueryPeriod": {
        "DateFrom": "2024-09-17T00:00:00.000Z",
        "DateTo": "2024-09-17T00:00:00.000Z"
    }
}


def test_login_and_fetch_data():
    # Отправка запроса на логин
    response_login = requests.post(LOGIN_URL, json=login_payload)
    assert response_login.status_code == 200, "Failed to log in"

    # Извлечение токена из ответа, если он необходим для следующего запроса
    token = response_login.json().get('token')

    # Добавление токена в заголовки, если это необходимо
    headers = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'

    # Отправка запроса на получение данных
    response_data = requests.post(DATA_URL, json=data_payload, headers=headers)
    assert response_data.status_code == 200, "Failed to fetch data"

    # Проверка полученных данных
    data = response_data.json()
    assert data is not None, "No data received"
    print(data)
