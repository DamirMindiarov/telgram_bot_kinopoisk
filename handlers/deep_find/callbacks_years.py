from loader import bot
from states import states_01
from keyboards.gen_rating import gen_rating


@bot.callback_query_handler(state=states_01.DeepFind.years, func=lambda callback_query: 'years ' in callback_query.data)
def years(callback_query):
    period = callback_query.data.split()[1]

    with bot.retrieve_data(callback_query.from_user.id, callback_query.message.chat.id) as data:
        data['years'] = period

    bot.set_state(callback_query.from_user.id, states_01.DeepFind.rating, callback_query.message.chat.id)

    bot.edit_message_text(
        'Выбери рейтинг по "Кинопоиску"',
        callback_query.message.chat.id,
        callback_query.message.message_id,
        reply_markup=gen_rating())
