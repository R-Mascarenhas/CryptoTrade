# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:00:57 2021

@author: Rafae
"""

import telebot
import my_infos

token = my_infos.token
myId = my_infos.myId

bot = telebot.TeleBot(token)

user = bot.get_me()



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "oi")
    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
    
def sendMessage(ChatID = myId, Message = ""):
    bot.send_message(ChatID, Message)