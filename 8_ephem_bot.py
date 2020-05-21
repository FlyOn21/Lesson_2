"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from datetime import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def constellation_planet(bot,update):
    
    planet_ident = ((update['message']['text'].split())[1])
    planet = planet_ident.capitalize() 
    search_pl = getattr(ephem,str(planet))(datetime.now().strftime('%Y/%m/%d'))
    constellation = ephem.constellation(search_pl)
    update.message.reply_text(constellation)


def world_count(bot,update):
    count_word = []
    message_text = ((update['message']['text'])[12:]).split()
    if len(message_text)==0:
        return update.message.reply_text('Вы ничего не написали...')
    for world_message in message_text:
        if len(world_message)<=1:
            continue
        else:
            count_word.append(world_message)
    update.message.reply_text(len(count_word))

def full_moon(bot,update):
    moon_date = ((update['message']['text'].split())[1])
    moon_full_date = ephem.next_full_moon(moon_date)
    update.message.reply_text(moon_full_date)
    


def main():
    mybot = Updater('1254309533:AAHXtgNikBSAbImTjNAwwrAb2dJA4w-z1KU', request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", constellation_planet))
    dp.add_handler(CommandHandler("worldcount", world_count))
    dp.add_handler(CommandHandler("next_full_moon", full_moon))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
