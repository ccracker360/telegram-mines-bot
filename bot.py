import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "7761279374:AAFoMsGoXFL9XV3cb9w1Yk_ft0IeYvsM_2E"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("OPEN", web_app=WebAppInfo(url="https://telegram-mines-webapp1.vercel.app/index.html")))
    bot.send_photo(
        message.chat.id,
        photo="https://i.imgur.com/kH1IxU1.png",
        caption="🎮 O'yinlar markaziga xush kelibsiz!",
        reply_markup=markup
    )

bot.polling()
#test
