from pytube import YouTube
import os

MAX_FILE_SIZE = 52428800
def check_size(filesize, youtubeObject):
    media_object = None
    if youtubeObject.streams.get_highest_resolution().filesize < MAX_FILE_SIZE:
        media_object = youtubeObject.streams.get_highest_resolution()
    elif youtubeObject.streams.get_lowest_resolution().filesize < MAX_FILE_SIZE:
        media_object = outubeObject.streams.get_lowest_resolution()

    return media_object

def rename_file_to_mp3(output_filename):
    base, ext = os.path.splitext(output_filename)
    new_file = base + '.mp3'
    if os.path.exists(new_file):
        os.remove(new_file)

    os.rename(output_filename, new_file)
    print(new_file)
    return new_file

def Download(link, output_path,video):
    youtubeObject = YouTube(link)
    filesize = youtubeObject.streams.get_highest_resolution().filesize


    print(f'Size = {filesize}')
    if video:
        youtubeObject = check_size(filesize, youtubeObject)
    else:
        youtubeObject = youtubeObject.streams.get_audio_only()

    output_filename = None
    try:
        if youtubeObject:
            output_filename = youtubeObject.download(output_path)
        else:
            return output_filename
    except:
        print("Произошла ошибка")

    print(output_filename)
    if not video:
        output_filename = rename_file_to_mp3(output_filename)

    return output_filename

def run():
    output_path = input("Введите путь для сохранения:\n")
    video = int(input("Введите 1 - для Видео 0 - только звук\n"))
    print(video)
    link = input("Введите ссылку на ютуб URL: \n")
    Download(link, output_path, video)

if __name__ == '__main__':
    run()