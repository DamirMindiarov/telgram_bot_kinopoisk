import requests
from typing import Any

from config_data.config import URL_FOR_FIND_FILMS, API_KEY


def find_films(film_name: str, count=1) -> Any:
    """
    Функция отправляет запрос, возвращает результат запроса.

    :param film_name: Название фильма
    :param count: Количество найденных фильмов
    """
    headers = {'accept': 'application/json', 'X-API-KEY': API_KEY}
    params = {'page': 1, 'limit': count, 'query': film_name}

    try:
        response = requests.get(URL_FOR_FIND_FILMS, params=params, headers=headers, timeout=15)
    except requests.ConnectTimeout:
        return 'Ошибка тайм-аута'

    if response.status_code != 200:
        return 'Что-то не так с API'

    return response
