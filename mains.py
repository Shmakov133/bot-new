import telebot
from telebot import types
import requests

bot = telebot.TeleBot('1499809620:AAEQoTZWRjg-8SABQdNqnFrjZtw2CHdtpSg')

keyboard = types.InlineKeyboardMarkup()

key_news_polit = types.InlineKeyboardButton(text='Новости мира', callback_data='polit')
keyboard.add(key_news_polit)
key_news_it = types.InlineKeyboardButton(text='IT', callback_data='IT')
keyboard.add(key_news_it)
key_news_covid = types.InlineKeyboardButton(text='COVID', callback_data='COVID')
keyboard.add(key_news_covid)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'IT':
        bot.send_message(call.message.chat.id, "https://web.telegram.org/#/im?p=c1383348298_2578742398315582261")
    elif call.data == 'COVID':
        COVID = requests.get('https://coronavirus-monitor.ru/')
        bot.send_message(call.message.chat.id, "Сдохли все")
    else:
        bot.send_message(call.message.chat.id, "Бот сам за себя не оплатит, кидай карту и CVC")

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "Чмо":
        bot.send_message(message.from_user.id, "Сам такой")

    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я КвантоОтец (Древнегреческий бот).")
        bot.send_message(message.from_user.id, "Что тебе надобно старче?", reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "На ваш адрес заказано 30 пеперони, если хотите отменить заказ напишите: /help")


bot.polling(none_stop=True, interval=0)
