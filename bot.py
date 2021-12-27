import telebot
import config
import cipher_metod

bot = telebot.TeleBot(config.TOKEN)
'''
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Привет! '
        'Я могу зашифровать или расшировать твое сообщение, используя шифр Цезаря.\n' +
        'Чтобы использовать шифр Цезаря, нажми /encrypt. Затем введи текст, который ты хочешь зашифровать или расшифровать и число сдвига \n' +
        'Чтобы получить помощь, нажмите /help\n'
        '\n')
'''

"""
@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url='telegram.me/nalgievmh')
    )
    bot.send_message(
        message.chat.id,
        'При возникновении вопросов, обращайтесь к @nalgievmh.\n',
        reply_markup=keyboard
    )
"""
#@bot.message_handler(commands=['encrypt'])

'''
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('help', callback_data='get-help')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('encrypt', callback_data='get-encrypt')
    )

    bot.send_message(
        message.chat.id,
        'Click on the currency of choice:',
        reply_markup=keyboard
    )


    @bot.callback_query_handler(func=lambda call: True)
    def iq_callback(query):
        data = query.data
        if data == 'get-help':
            help_command(message)
        else:
            main(message)

def get_ex_callback(query):
    bot.answer_callback_query(query.id)
    main(message='text')
'''

"""
def main(message):
    msg = bot.send_message(message.chat.id, 'Введите текст')
    bot.register_next_step_handler(msg, fio_step)

def fio_step(message):
    user_info = {}
    user_info['plain'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите сдвиг')
    bot.register_next_step_handler(msg, age_step, user_info)

def age_step(message, user_info):
    user_info['shift1'] = message.text
    msg = bot.send_message(message.chat.id, f'{cipher_metod.caesar(str(user_info["plain"]), int(user_info["shift1"]))}')
"""



@bot.message_handler(commands=['start'])
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('encrypt', callback_data='get-encrypt')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('help', callback_data='get-help')
    )

    bot.send_message(
        message.chat.id,
        'Привет! '
        'Я могу зашифровать или расшировать твое сообщение, используя шифр Цезаря.\n' +
        'Чтобы использовать шифр Цезаря, нажми /encrypt. '
        'Затем введи текст, который ты хочешь зашифровать или расшифровать и число сдвига \n' +
        'Чтобы получить помощь, нажмите /help\n'
        '\n',
        reply_markup=keyboard
    )

    @bot.callback_query_handler(func=lambda call: True)
    def iq_callback(query):
        data = query.data
        if data == 'get-help':
            help_command(message)
        else:
            main(message)


@bot.message_handler(commands=['encrypt'])
def main(message):
    msg = bot.send_message(message.chat.id, 'Введите текст, который вы хотите зашифровать (латиницей и без пробелов)')
    bot.register_next_step_handler(msg, fio_step)


def fio_step(message):
    user_info = {}
    user_info['plain'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите сдвиг (с положительным или отрицательным значением')
    bot.register_next_step_handler(msg, age_step, user_info)


def age_step(message, user_info):
    user_info['shift1'] = message.text
    bot.send_message(message.chat.id, f'Твой зашифрованный текст:\n{cipher_metod.caesar(str(user_info["plain"]), int(user_info["shift1"]))}\n\nНовый шифр: /encrypt')


@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url='telegram.me/nalgievmh')
    )
    bot.send_message(
        message.chat.id,
        'При возникновении вопросов, обращайтесь к @nalgievmh.\n',
        reply_markup=keyboard)


bot.polling(none_stop=True)
