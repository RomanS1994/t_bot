# pip install pyTelegramBotAPI
import telebot

bot = telebot.TeleBot('8138349623:AAGCv4KZFc5tASUjzIWa9ULzRL7htVdaLRE')

@bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, '<b>Hello</b> --- <em><u>information</u></em>', parse_mode='html')

def main(message):
    bot.send_message(message.chat.id, f'Привіт {message.chat.first_name} як пройшов твій сьогоднішній день?')




    
bot.polling(non_stop=True)