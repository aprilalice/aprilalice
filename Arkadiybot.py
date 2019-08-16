# -*- coding: utf8 -*-
import telebot        
from telebot import types



arr = []
a = ['Закрыть вопрос', 'Открыть вопрос']
b = ['Status: open', 'Status: closed']
bot = telebot.TeleBot('yourtoken');
i = 0
admin = 123
        
@bot.message_handler(content_types=['text'])
def echo(message):
    if '#Новый вопрос' in message.text:
        global admin
        admin = message.from_user.id
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        button1 = telebot.types.InlineKeyboardButton(text=a[i], callback_data ='change') 
        button2 = telebot.types.InlineKeyboardButton(text=b[i], callback_data = 'app')
        markup.add(button1, button2)         
        bot.send_message(message.chat.id, text = 'Новый вопрос', reply_markup= markup)        
                                                                                                

    
    
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'change':
        global admin
        if call.from_user.id == admin:
            global i
            if i == 0:
                i = 1
            else:
                i = 0
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            button1 = telebot.types.InlineKeyboardButton(text=a[i], callback_data ='change') 
            button2 = telebot.types.InlineKeyboardButton(text=b[i], callback_data = 'app')
            markup.add(button1, button2)             
            msg = bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
      

bot.polling(none_stop=True, interval=0)
