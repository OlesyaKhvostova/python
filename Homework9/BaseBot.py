import telebot
import os
import DownloderBot
api_token = ''
bot = telebot.TeleBot(api_token)
bot.disable_web_page_preview = True
commands_list = ['/start','/downloadvideo','/downloadmp3','/enterpath']

#def load_path_from_file():
 #   main_path = ''
 #   with open('downloder_bot_settings.txt', 'r') as f:
  #      main_path = f.readline()

 #   return main_path

#def write_path_from_file(main_path):
 #   with open('downloder_bot_settings.txt', 'w') as f:
 #       f.write(main_path)

#@bot.message_handler(content_types=['text'])
#def start(message):
    #bot.send_message(message.chat.id, text=f"Напишите команду '/start'")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "/loadvideo - скачать видео\n/loadmusic - скачать музыку")

#@bot.message_handler(commands=['path'])
#def path_message(message):
 #   main_path = message.text
 #   directory = os.listdir(os.curdir)
  #  print(directory)
   # print(f'Main path = {main_path}')
   # write_path_from_file(main_path)

@bot.message_handler(commands=['loadvideo'])
def loadvideo_message(message):
    #main_path = 'Bot\Video'#load_path_from_file()
    #print(main_path)
    #if not os.path.exists(main_path):
    #    os.mkdir(main_path)
    bot.send_message(message.chat.id, 'Введите ссылку на видео')
    bot.register_next_step_handler(message, enter_video_link)
    #output_filename = DownloderBot.Download(message.text, main_path, 1)
    #print(message.text)
    #bot.send_video(message.chat.id, video=open(output_filename, 'rb'), supports_streaming=True)
    #bot.send_message(message.chat.id,'Видео скачено')

def enter_video_link(message):
    create_base_folder()
    bot.send_message(message.chat.id, 'Скачеваем видео')
    output_filename = DownloderBot.Download(message.text, main_path, 1)
    print(message.text)
    if output_filename:
        bot.send_video(message.chat.id, video=open(output_filename, 'rb'), supports_streaming=True)
        bot.send_message(message.chat.id, 'Видео скачено')
        delete_media_file(output_filename)
    else:
        bot.send_message(message.chat.id, 'Ошибка: слишком большое видео')

@bot.message_handler(commands=['loadmusic'])
def loadmusic_message(message):
    bot.send_message(message.chat.id, 'Введите ссылку на музыку')
    bot.register_next_step_handler(message, enter_music_link)
        #main_path = 'Bot'#load_path_from_file()
        #print(main_path)
        #if not os.path.exists(main_path):
        #    os.mkdir(main_path)
        #print(message.text)
        #bot.send_message(message.chat.id, 'Скачеваем музыку')
        #output_filename = DownloderBot.Download(message.text, main_path, 0)
        #bot.send_audio(message.chat.id, output_filename)
        #bot.send_message(message.chat.id, 'Музика скачена')

def enter_music_link(message):
    create_base_folder()
    bot.send_message(message.chat.id, 'Скачеваем музыку')
    output_filename = DownloderBot.Download(message.text, main_path, 0)
    print(message.text)
    if output_filename:
        bot.send_audio(message.chat.id, audio=open(output_filename, 'rb'))
        bot.send_message(message.chat.id, 'Музыка скачена')
        delete_media_file(output_filename)
    else:
        bot.send_message(message.chat.id, 'Ошибка: слишком большое аудио')

def create_base_folder():
    main_path = '\Bot'
    print(main_path)
    if not os.path.exists(main_path):
        os.mkdir(main_path)

def delete_media_file(output_file):
    if os.path.exists(output_file):
        os.remove(output_file)

bot.polling(none_stop=True)