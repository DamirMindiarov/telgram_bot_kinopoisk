from loader import bot
from states import states_01
from keyboards.gen_years import gen_years


@bot.callback_query_handler(state=states_01.DeepFind.genre,
                            func=lambda callback_query: f'genre ' in callback_query.data)
def callback_genre(callback_query):
    genre = callback_query.data.split()[1]

    with bot.retrieve_data(callback_query.from_user.id, callback_query.message.chat.id) as data:
        data['genre'] = genre

    bot.edit_message_text(
        'выбери период',
        callback_query.message.chat.id,
        callback_query.message.message_id,
        reply_markup=gen_years())

    bot.set_state(callback_query.from_user.id, states_01.DeepFind.years, callback_query.message.chat.id)
