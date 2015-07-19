#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot  # https://github.com/eternnoir/pyTelegramBotAPI
import random
from DTCScrapper import DTCScrapper

TOKEN = '117836291:AAEFICSt5P4aaSHnfWm7BEMGCiiyRBIlJGI'

bot = telebot.TeleBot(TOKEN)

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

def send_message(messages):
    """
    Send the messages to the chat
    """
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = ""
            text = quote()
            bot.send_message(chatid,text)

bot.set_update_listener(send_message)
bot.polling()

while True: # Don't let the main Thread end.
    pass
