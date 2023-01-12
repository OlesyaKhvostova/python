from pytube import YouTube
import os

def rename_file_to_mp3(output_filename):
    base, ext = os.path.splitext(output_filename)
    new_file = base + '.mp3'
    os.rename(output_filename, new_file)
    print(new_file)

def Download(link, output_path,video):
    youtubeObject = YouTube(link)
    if video:
        youtubeObject = youtubeObject.streams.get_highest_resolution()
    else:
        youtubeObject = youtubeObject.streams.filter(only_audio=True).first()

    output_filename = None
    try:
        output_filename = youtubeObject.download(output_path)
    except:
        print("Произошла ошибка")

    print(output_filename)
    if not video:

        rename_file_to_mp3(output_filename)

def run():
    output_path = input("Введите путь для сохранения:\n")
    video = bool(input("Введите 1 - для Видео 0 - только звук\n"))
    link = input("Введите ссылку на ютуб URL: \n")
    Download(link, output_path, video)

if __name__ == '__main__':
    run()