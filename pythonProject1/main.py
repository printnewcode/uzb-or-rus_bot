import os

import telebot
from telebot import types
from texts import *
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))


@bot.message_handler(commands=['start'])
def start(message):
    first_mess = "Выберите язык\n\nTilni tanlang"
    markup = types.InlineKeyboardMarkup()
    btn_uzb = types.InlineKeyboardButton(text="o'zbek🇺🇿", callback_data='btn_uzb')
    btn_rus = types.InlineKeyboardButton(text='Русски🇷🇺', callback_data='btn_rus')
    markup.add(btn_uzb).add(btn_rus)
    bot.send_message(message.chat.id, first_mess, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_r(call):
    ru_buttons = types.InlineKeyboardMarkup()
    btn_rus_r1 = types.InlineKeyboardButton(text="1 Раздел: Миграционный и регистрационный учет",
                                            callback_data='btn_rus_r1')
    btn_rus_r2 = types.InlineKeyboardButton(text="2 Раздел: Трудовой патент", callback_data='btn_rus_r2')
    btn_rus_r3 = types.InlineKeyboardButton(text="3 Раздел: Разрешение на работу в РФ", callback_data='btn_rus_r3')
    btn_rus_r4 = types.InlineKeyboardButton(text="4 Раздел: Разрешение на временное пребывание",
                                            callback_data='btn_rus_r4')
    btn_rus_r5 = types.InlineKeyboardButton(text="5 Раздел: Экзамены по русскому языку", callback_data='btn_rus_r5')
    btn_rus_r6 = types.InlineKeyboardButton(text="6 Раздел: Мечети", callback_data='btn_rus_r6')
    ru_buttons.add(btn_rus_r1).add(btn_rus_r2).add(btn_rus_r3).add(btn_rus_r4).add(btn_rus_r5).add(btn_rus_r6)
    uzb_buttons = types.InlineKeyboardMarkup()
    btn_uzb_r1 = types.InlineKeyboardButton(text="1 Раздел: Migratsiya va ro'yxatga olish",
                                            callback_data='btn_uzb_r1')
    btn_uzb_r2 = types.InlineKeyboardButton(text="2 Раздел: Патенти меҳнатӣ", callback_data='btn_uzb_r2')
    btn_uzb_r3 = types.InlineKeyboardButton(text="3 Раздел: Иҷозати кор дар ФЕДЕРАТСИЯИ РУСИЯ",
                                            callback_data='btn_uzb_r3')
    btn_uzb_r4 = types.InlineKeyboardButton(text="4 Раздел: Иҷозатномаи истиқомати муваққатӣ",
                                            callback_data='btn_uzb_r4')
    btn_uzb_r5 = types.InlineKeyboardButton(text="5 Раздел: Маълумот барои тамос", callback_data='btn_uzb_r5')
    btn_uzb_r6 = types.InlineKeyboardButton(text="6 Раздел: Masjidlar", callback_data='btn_uzb_r6')
    uzb_buttons.add(btn_uzb_r1).add(btn_uzb_r2).add(btn_uzb_r3).add(btn_uzb_r4).add(btn_uzb_r5).add(btn_uzb_r6)
    if call.data == "btn_rus":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, RUS_START, reply_markup=ru_buttons)
    elif call.data == "btn_uzb":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, UZB_START, reply_markup=uzb_buttons)
    elif call.data == "btn_rus_delete_2":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.delete_message(call.message.chat.id, call.message.id-1)
        bot.send_message(call.message.chat.id, RUS_START, reply_markup=ru_buttons)
    elif call.data == "btn_uzb_delete_2":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.delete_message(call.message.chat.id, call.message.id-1)
        bot.send_message(call.message.chat.id, RUS_START, reply_markup=uzb_buttons)
    markup_uzb = types.InlineKeyboardMarkup()
    btn_uzb_back = types.InlineKeyboardButton(text="Boshqa bo'limni tanlang", callback_data='btn_uzb')
    markup_uzb.add(btn_uzb_back)
    markup_uzb_2 = types.InlineKeyboardMarkup()
    btn_uzb_back_2 = types.InlineKeyboardButton(text="Boshqa bo'limni tanlang", callback_data='btn_uzb_delete_2')
    markup_uzb_2.add(btn_uzb_back_2)
    markup_rus = types.InlineKeyboardMarkup()
    btn_rus_back = types.InlineKeyboardButton(text="Выбрать другой раздел", callback_data='btn_rus')
    markup_rus.add(btn_rus_back)
    markup_rus_2 = types.InlineKeyboardMarkup()
    back_rus_2 = types.InlineKeyboardButton(text="Выбрать другой раздел", callback_data='btn_rus_delete_2')
    markup_rus_2.add(back_rus_2)

    if call.data == "btn_rus_r1":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, RUS_R1, reply_markup=markup_rus)
    if call.data == "btn_rus_r2":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, RUS_R2_1)
        bot.send_message(call.message.chat.id, RUS_R2_2, reply_markup=markup_rus_2)
    if call.data == "btn_rus_r3":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, RUS_R3, reply_markup=markup_rus)
    if call.data == "btn_rus_r4":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, RUS_R4_1)
        bot.send_message(call.message.chat.id, RUS_R4_2, reply_markup=markup_rus_2)
    if call.data == "btn_rus_r5":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, RUS_R5, reply_markup=markup_rus)
    if call.data == "btn_rus_r6":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, RUS_R6, reply_markup=markup_rus)
    if call.data == "btn_uzb_r1":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, UZB_R1, reply_markup=markup_uzb)
    if call.data == "btn_uzb_r2":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, UZB_R2_1)
        bot.send_message(call.message.chat.id, UZB_R2_2, reply_markup=markup_uzb_2)
    if call.data == "btn_uzb_r3":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, UZB_R3, reply_markup=markup_uzb)
    if call.data == "btn_uzb_r4":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, UZB_R4_1)
        bot.send_message(call.message.chat.id, UZB_R4_2, reply_markup=markup_uzb_2)
    if call.data == "btn_uzb_r5":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, UZB_R5, reply_markup=markup_uzb)
    if call.data == "btn_uzb_r6":
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, UZB_R6, reply_markup=markup_uzb)

try:
    bot.remove_webhook()
except Exception as e:
    print(f"Ошибка при удалении вебхука: {e}")

bot.polling(none_stop=True)
