import telebot
import config
import cipher_metod

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Привет! '
        'Я могу зашифровать или расшировать твое сообщение, используя шифр Цезаря.\n' +
        'Чтобы использовать шифр Цезаря, нажми /exchange. Затем введи текст, который ты хочешь зашифровать или расшифровать и число сдвига \n' +
        'Чтобы получить помощь, нажмите /help\n'
        '\n')


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

@bot.message_handler(commands=['encrypt'])

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
    bot.register_next_step_handler(msg, keyboard)


def keyboard(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton('encrypt', callback_data='encrypt'))
    bot.send_message(
        message.chat.id,
        'Зашифровать сообщение\n',
        reply_markup=keyboard)



bot.polling(none_stop=True)
