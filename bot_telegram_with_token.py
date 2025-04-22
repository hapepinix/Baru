
import telebot

# Token bot dari BotFather
API_TOKEN = '7556876226:AAHOib-ctsLU1TzwuqlZW4x5X8rqpkTLSis'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Halo, saya bot Telegram sederhana!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Bot sedang berjalan...")
bot.infinity_polling()
