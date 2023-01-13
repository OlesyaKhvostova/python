import telebot
import os
import DownloderBot
api_token = ''
bot = telebot.TeleBot(api_token)
commands_list = ['/start','/downloadvideo','/downloadmp3','/enterpath']

def load_path_from_file():
    main_path = ''
    with open('downloder_bot_settings.txt', 'r') as f:
        main_path = f.readline()

    return main_path

def write_path_from_file(main_path):
    with open('downloder_bot_settings.txt', 'w') as f:
        f.write(main_path)

#@bot.message_handler(content_types=['text'])
#def start(message):
    #if message.text != '/start':
        #bot.send_message(message.chat.id, text=f"Напишите команду '/start'")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "/path - задать путь\n/loadvideo - скачать видео\n/loadmusic - скачать музыку")

@bot.message_handler(commands=['path'])
def path_message(message):
    main_path = message.text
    directory = os.listdir(os.curdir)
    print(directory)
    print(f'Main path = {main_path}')
    write_path_from_file(main_path)

@bot.message_handler(commands=['loadvideo'])
def loadvideo_message(message):
    main_path = load_path_from_file()
    os.mkdir(main_path)
    DownloderBot.Download(message.text, main_path, 1)
    bot.send_message(message.chat.id,'Видео скачено')

@bot.message_handler(commands=['loadmusic'])
def loadmusic_message(message):
        main_path = load_path_from_file()
        os.mkdir(main_path)
        DownloderBot.Download(message.text, main_path, 0)
        bot.send_message(message.chat.id, 'Музика скачена')

bot.polling(none_stop=True)