import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к. отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv('API_KEY')

BASE_URL = 'https://api.kinopoisk.dev'
URL_FOR_FIND_FILMS = 'https://api.kinopoisk.dev/v1.4/movie/search'
URL_FOR_DEEP_FIND = 'https://api.kinopoisk.dev/v1.4/movie'
URL_FOR_FILM = 'https://www.kinopoisk.ru/film'