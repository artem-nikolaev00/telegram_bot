import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import random

TOKEN = ""

bot = telebot.TeleBot(TOKEN)

SUGGEST = ["Рандом на две группы"]
STUBS = ["Аллу 0-0", "Кек", "Уа!", "Бим-бим бам-бам", "Чо нада, розовый?!"]


# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    name = message.from_user.first_name
    markup = ReplyKeyboardMarkup(row_width=len(SUGGEST), one_time_keyboard=True)
    for suggest in SUGGEST:
        button = KeyboardButton(suggest)
        markup.add(button)

    bot.send_message(message.chat.id, reply_markup=markup, text=f"Привет Пикс-{name}, Пиксабот приветствует тебя!")


@bot.message_handler(func=lambda message: message.text == SUGGEST[0])
def echo_message(message):
    print(f"Пользователь {message.chat.first_name}-{message.chat.username} пишет '{message.text}'")
    markup = ReplyKeyboardRemove()
    bot.send_message(message.chat.id, text=f"Введите имена, в следующем формате: 'Имена: имя1, имя2, ...'", reply_markup=markup)


@bot.message_handler(func=lambda message: message if ('Имена' in message.text) else None)
def echo_sort(message):
    print(f"Пользователь {message.chat.first_name}-{message.chat.username} пишет '{message.text}'")
    length = len(message.text)
    first_names = message.text[7:length]
    list_of_first_names = list(first_names.split(", "))
    random.shuffle(list_of_first_names)

    half = len(list_of_first_names) // 2
    first_half = list_of_first_names[:half]
    first_team = ''
    second_half = list_of_first_names[half:]
    second_team = ''
    for i in range(len(first_half)):
        first_team += first_half[i]
        first_team += ", "
    for i in range(len(second_half)):
        second_team += second_half[i]
        second_team += ", "

    bot.send_message(message.chat.id, text=f"Первая команда: {first_team}\nВторая команда: {second_team}")


@bot.message_handler(func=lambda message: message)
def echo_unknown_message(message):
    print(f"Пользователь {message.chat.first_name}-{message.chat.username} пишет '{message.text}'")
    markup = ReplyKeyboardRemove()
    answer = random.choice(STUBS)
    bot.send_message(message.chat.id, text=f"{answer}", reply_markup=markup)


bot.infinity_polling()
