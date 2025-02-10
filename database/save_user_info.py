from database.models import Movie, HistoryUserMessage, UserHistory
from typing import Dict, Any, List


def add_movie(json_loads: Dict[Any, Any]) -> None:
    """
    Функция добавляет фильмы в БД, если их еще там нет.
    :param json_loads: Данные полученные после requests.get в json формате
    """
    for movie in json_loads['docs']:

        film_genres = ''
        film_countries = ''

        for i in [elem['name'] for elem in movie['genres']]:
            film_genres += i + ' '

        for i in [elem['name'] for elem in movie['countries']]:
            film_countries += i + ' '

        if not Movie.select().where(Movie.movie_id == movie['id']):
            Movie(movie_id=movie['id'],
                  movie_name=movie['name'],
                  movie_alt_name=movie['alternativeName'],
                  movie_year=movie['year'],
                  movie_short_description=movie['shortDescription'],
                  movie_description=movie['description'],
                  poster=movie['poster']['previewUrl'],
                  genre=film_genres,
                  countries=film_countries
                  ).save()
        else:
            continue


def add_movie_for_deep_find(json_loads: Dict[Any, Any]) -> List[str]:
    """
    Функция добавляет фильмы в БД, если их еще там нет.
    :param json_loads: Данные полученные после requests.get в json формате
    """
    id_films = [str(elem['id']) for elem in json_loads['docs']]

    for movie in json_loads['docs']:
        film_genres = ''
        film_countries = ''

        try:
            for elem in [elem['name'] for elem in movie['genres']]:
                film_genres += elem + ' '
        except KeyError:
            film_genres = 'Не указано'

        try:
            for elem in movie['countries']:
                film_countries += elem['name'] + ' '
        except KeyError:
            film_countries = 'Не указано'

        if not Movie.select().where(Movie.movie_id == movie['id']):
            try:
                movie_id = movie['id']
                movie_name = movie['name']
                movie_alt_name = movie['alternativeName']
                movie_year = movie['year']
                movie_short_description = movie['shortDescription']
                movie_description = movie['description']
                poster = movie['poster']['previewUrl']
                genre = film_genres
                countries = film_countries
            except KeyError:
                id_films.remove(str(movie['id']))
                continue

            Movie(movie_id=movie_id,
                  movie_name=movie_name,
                  movie_alt_name=movie_alt_name,
                  movie_year=movie_year,
                  movie_short_description=movie_short_description,
                  movie_description=movie_description,
                  poster=poster,
                  genre=genre,
                  countries=countries
                  ).save()

        else:
            continue

    return id_films


def add_history_message(user_id: int, message_id: int, list_id_movies: str) -> None:
    """
    Функция добавляет в БД id сообщения и список id фильмов
    """
    HistoryUserMessage(
        user_id=user_id,
        message_id=message_id,
        list_id_movies=list_id_movies
    ).save()


def add_user_history(user_id: int, command: str, body: str, date: str) -> None:
    """
    Функция добавляет в БД информацию о запросе пользователя в таблицу UserHistory
    """
    UserHistory(
        user_id=user_id,
        command=command,
        body=body,
        date=date
    ).save()
