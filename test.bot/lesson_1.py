# pip install pyTelegramBotAPI
import telebot
import webbrowser
bot = telebot.TeleBot('8138349623:AAGCv4KZFc5tASUjzIWa9ULzRL7htVdaLRE')




@bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, '<b>Hello</b> --- <em><u>information</u></em>', parse_mode='html')

def main(message):
    bot.send_message(message.chat.id, f'Привіт {message.chat.first_name} як пройшов твій сьогоднішній день?')


@bot.message_handler()
def site(message):
    if message.text.lower() == "site":
            webbrowser.open('https://www.edu.goit.global/uk/courses')



    
bot.polling(non_stop=True)