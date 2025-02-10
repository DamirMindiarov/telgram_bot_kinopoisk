from loader import bot
from states import states_01
from keyboards.gen_genres import gen_genres


@bot.message_handler(commands=['deep_find'])
def deep_find(message):

    bot.send_message(message.from_user.id, 'Выбери жанр', reply_markup=gen_genres())
    bot.set_state(message.from_user.id, states_01.DeepFind.genre, message.chat.id)
