# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 20:05:09 2021

@author: Prince
"""


from transliterate import to_cyrillic , to_latin

import telebot

TOKEN = "1905260613:AAFBbcsnRyBIwRs3cQvsWuctYFXV0UTKiTE"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu aleykum \nMatn kiriting")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    
    matn = message.text
    if matn.isascii() == True:
        javob = to_cyrillic(matn)
    else:
        javob = to_latin(matn)
            
    
    bot.reply_to(message, javob)

bot.polling()
