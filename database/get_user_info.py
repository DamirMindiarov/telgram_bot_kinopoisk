from database.models import HistoryUserMessage, UserHistory
from typing import List


def get_list_id(user_id: int, message_id: int) -> List[str]:
    """
    Функция возвращает список id фильмов в сообщении.
    """
    id_films = HistoryUserMessage.get(
        HistoryUserMessage.user_id == user_id,
        HistoryUserMessage.message_id == message_id
    )

    return id_films.list_id_movies.split()


def get_user_history(user_id: int) -> list[str]:
    """
    Функция получает из БД всю историю запросов пользователя, возвращает в виде списка
    """
    user_history = UserHistory.select().where(
        UserHistory.user_id == user_id
    )

    list_of_history = []
    for elem in user_history:
        list_of_history.append(f'- {elem.command} - "{elem.body}"\n\t - {elem.date}\n')

    return list_of_history
