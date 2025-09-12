import telebot

TOKEN = "fake-token-telegram-bot"

bot = telebot.TeleBot(TOKEN)

@bot.messsage_handler(commands=["start"])
def send_welc(message):
    bot.reply_to(message, "Welcome! This is a test bot")

@bot.message_handler(func=lambda message:True)
def echo(message):
    bot.reply_to(message, f"You said: {message.text}")