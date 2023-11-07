import telebot
import os
from dotenv import load_dotenv
import model

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
bot.set_webhook()

@bot.message_handler(commands=['start'])
def start(message):
    """
    Bot will introduce itself upon /start command, and prompt user for his request
    """
    try:
        # Start bot introduction    
        start_message = "Hello, HealthServe volunteers! I'm an automated chatbot designed to enhance your understanding of medical coverage for migrant workers and the challenges they face in accessing these services in Singapore. My responses are available in English, Chinese, Bengali and Tamil to cater to the various demographics of migrant workers. Kindly allow me a moment to organize my responses to your questions, as I am not a human operator. Do note that "
        bot.send_message(message.chat.id, start_message)

    except Exception as e:
        bot.send_message(
            message.chat.id, 'Sorry, I do not have the information to answer your question. Do rephrase your question again or try again later!')


@bot.message_handler(content_types=['text'])
def send_text(message):
    response = model.getResponse(message.text)
    bot.send_message(message.chat.id, response)

def main():
    """Runs the Telegram Bot"""
    print('Loading configuration...') # Perhaps an idea on what you may want to change (optional)
    print('Successfully loaded! Starting bot...')
    bot.infinity_polling()


if __name__ == '__main__':
    main()