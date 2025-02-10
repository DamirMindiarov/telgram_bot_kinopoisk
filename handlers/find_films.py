from loader import bot
from states import states_01


@bot.message_handler(commands=['find_film'])
def find_film(message):
    bot.send_message(message.from_user.id, 'Введи название фильма')
    bot.set_state(message.from_user.id, states_01.MyStates.name, message.chat.id)
