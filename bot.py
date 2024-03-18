import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

TOKEN = "7099919089:AAGV2FWnCzOFQlqGvJkQ-bceNJ7odDIMiGY"

bot = telebot.TeleBot(TOKEN)

SUGGEST = ["Начнём!?", "Я пошёл..."]


# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    name = message.from_user.first_name
    markup = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    for suggest in SUGGEST:
        button = KeyboardButton(suggest)
        markup.add(button)

    bot.send_message(message.chat.id, reply_markup=markup, text=f"Привет Пикс-{name}, Пиксабот приветствует тебя!")


@bot.message_handler(func=lambda message: message.text != SUGGEST[1])
def echo_message(message):
    print(f"Пользователь {message.chat.first_name}-{message.chat.username} пишет '{message.text}'")
    markup = ReplyKeyboardRemove()
    bot.send_message(message.chat.id, text=f"Уа!", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == SUGGEST[1])
def echo_message(message):
    print(f"Пользователь {message.chat.first_name}-{message.chat.username} пишет '{message.text}'")
    markup = ReplyKeyboardRemove()
    bot.send_message(message.chat.id, text=f"Ну и ладно...", reply_markup=markup)


bot.infinity_polling()
