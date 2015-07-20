#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot  # https://github.com/eternnoir/pyTelegramBotAPI
import random
from token_file import token_var
from DTCScrapper import DTCScrapper

TOKEN = token_var

bot = telebot.TeleBot(TOKEN)
about_text_bot = "Hey !\nI am a telegram bot built by @n07070. I'm open source on Github : https://github.com/N07070/TelegramDTCBot \nPlease contribute ! :)"
help_text_bot = "You can use theses commands :\n /about - Gets you information about me.\n /help - Gets you this help message.\n /quote - Gets you a random quote from danstonchat.com"

def quote():
    """
    Gets a new quote from the DTC website
    """
    e = DTCScrapper()

    url_of_the_quote = "http://danstonchat.com/"+str(random.randint(1,16000))+".html"
    final_quote = ""
    iter = 0
    for a in e.main(url_of_the_quote):
        if iter % 2 == 0 :
            final_quote += a
        else:
            final_quote += a + "\n"
        iter += 1

    print final_quote
    return final_quote
    del final_quote, a, e

def send_message(messages):
    """
    Send the messages to the chat
    """
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            if m.text == "/quote":
                text = ""
                text = quote()
                bot.send_message(chatid,text)
                del text
            if m.text == '/about':
                bot.send_message(chatid,about_text_bot)
            if m.text == '/help':
                bot.send_message(chatid,help_text_bot)

bot.set_update_listener(send_message)
bot.polling()

while True: # Don't let the main Thread end.
    pass
