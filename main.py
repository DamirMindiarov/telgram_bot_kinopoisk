from loader import bot
from telebot import custom_filters
from telebot.types import BotCommand
import handlers

if __name__ == '__main__':
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.set_my_commands([
        BotCommand('find_film', 'Поиск по названию.'),
        BotCommand('start', 'Стартовое сообщение'),
        BotCommand('deep_find', 'Поиск по названию, жанру, году, рейтингу'),
        BotCommand('help', 'Справочная информация по командам'),
        BotCommand('history', 'Показать историю запросов')
    ])
    bot.infinity_polling()
