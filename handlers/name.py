from loader import bot
from states.states_01 import MyStates
from telebot.util import quick_markup


@bot.message_handler(state=MyStates.name)
def name(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text

    keyboard = quick_markup(
        {str(i): {'callback_data': f'count {str(i)} {message.message_id + 1}'} for i in range(1, 9)},
        row_width=8
    )

    bot.send_message(
        message.from_user.id,
        f'Выбери/введи кол-во результатов поиска по названию {message.text}',
        reply_markup=keyboard)

    bot.set_state(message.from_user.id, MyStates.count, message.chat.id)
