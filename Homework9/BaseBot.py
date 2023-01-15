import telebot
import os
import DownloderBot
api_token = ''
bot = telebot.TeleBot(api_token)
bot.disable_web_page_preview = True

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "/loadvideo - скачать видео\n/loadmusic - скачать музыку")

@bot.message_handler(commands=['loadvideo'])
def loadvideo_message(message):
    bot.send_message(message.chat.id, 'Введите ссылку на видео')
    bot.register_next_step_handler(message, enter_video_link)

def enter_video_link(message):
    main_path = create_base_folder()
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

def enter_music_link(message):
    main_path = create_base_folder()
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
    main_path = str(os.path.abspath(os.path.join(os.path.curdir,'\Bot')))
    print(main_path)
    if not os.path.exists(main_path):
        os.mkdir(main_path)

    return main_path

def delete_media_file(output_file):
    if os.path.exists(output_file):
        os.remove(output_file)

bot.polling(none_stop=True)