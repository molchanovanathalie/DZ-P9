import telebot

from telebot import types

bot = telebot.TeleBot('6120515342:AAHQvhPENdmBtP5mEV49XXiK3PTXQsC2Ky0')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-проводник в мире ароматов!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Как посмотреть отзывы?')
        btn2 = types.KeyboardButton('Как со мной связаться')
        btn3 = types.KeyboardButton('Описание ароматов')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) 


    elif message.text == 'Как посмотреть отзывы?':
        bot.send_message(message.from_user.id, 'Перейдите по ссылке на сайт Авито. Все отзывы представлены там ' + '[ссылке](https://www.avito.ru/user/c638cc63c118c7f10ad7af4ec5ba5b78/profile?src=sharing)', parse_mode='Markdown')

    elif message.text == 'Как со мной связаться':
        bot.send_message(message.from_user.id, 'Контакты вы можете найти на сайте Авито ' + '[ссылке](https://www.avito.ru/user/c638cc63c118c7f10ad7af4ec5ba5b78/profile?src=sharing)', parse_mode='Markdown')

    elif message.text == 'Описание ароматов':
        bot.send_message(message.from_user.id, 'Подробно про пирамиду ароматов можно прочитать по ' + '[ссылке](https://www.fragrantica.ru//)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0)