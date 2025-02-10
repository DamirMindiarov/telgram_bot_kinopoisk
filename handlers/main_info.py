from database.models import Movie
from keyboards.gen_keyboard import gen_keyboard
from loader import bot
from config_data.config import URL_FOR_FILM
from database.get_user_info import get_list_id


@bot.callback_query_handler(func=lambda callback_query: 'main_info ' in callback_query.data)
def main_info(callback_query):
    cur_id_film, id_message = callback_query.data.split()[1:]
    film = Movie.get(Movie.movie_id == cur_id_film)
    user_id = callback_query.from_user.id

    id_films = get_list_id(user_id, id_message)

    movie_short_description = film.movie_short_description if film.movie_short_description else ''
    caption = '{name}{alt_name} {year}\n{genre}\n{country}\n{short_desc}\n{link}'.format(
        name=film.movie_name,
        alt_name=f'({film.movie_alt_name})' if film.movie_alt_name else "",
        year=film.movie_year,
        genre=film.genre,
        country=film.countries,
        short_desc=movie_short_description,
        link=f'{URL_FOR_FILM}/{film.movie_id}/'
    )

    bot.edit_message_caption(
        caption=caption,
        chat_id=callback_query.message.chat.id,
        message_id=int(id_message) + 1,
        reply_markup=gen_keyboard(id_message, id_films, cur_id_film, description=True)
    )
