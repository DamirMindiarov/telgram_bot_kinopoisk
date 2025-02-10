import requests
from config_data.config import URL_FOR_DEEP_FIND, API_KEY
from typing import Any


def find_films_for_deep(genre: str, years: str, rating: str) -> Any:
    """
    Функция отправляет запрос, возвращает результат.

    :param genre: Жанр
    :param years: Период
    :param rating: Оценка на кинопоиске
    """
    headers = {'accept': 'application/json', 'X-API-KEY': API_KEY}
    params = {'page': 1, 'limit': 250, 'year': years, 'rating': rating, 'genres.name': genre}

    try:
        response = requests.get(URL_FOR_DEEP_FIND, params=params, headers=headers, timeout=15)
    except requests.ConnectTimeout:
        return 'Ошибка тайм-аута'

    if response.status_code != 200:
        return 'Что-то не так с API'

    return response
