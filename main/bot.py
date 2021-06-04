import logging

import telebot
from django.conf import settings
from telebot import types
from telebot.apihelper import ApiException


try:
    bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)
except:
    bot = telebot.TeleBot('not worked telegram token')


def send_telegram_notification(message, chat_id):
    try:
        bot.send_message(chat_id=chat_id, text=message)
    except:
        logging.error("Can't send to the telegam")


@bot.message_handler(commands=['url'])
def send_telegram_notification_url(message, group_id, link):
    markup = types.InlineKeyboardMarkup()
    button_to_site = types.InlineKeyboardButton(text='перейти', url=link)
    markup.add(button_to_site)
    try:
        bot.send_message(group_id, message, reply_markup=markup)
    except ApiException:
        send_telegram_notification(message, group_id, )
    except Exception:
        logging.error("Can't send to the telegam")
