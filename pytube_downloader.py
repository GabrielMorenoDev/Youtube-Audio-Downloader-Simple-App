from pytube import YouTube

def download_audio(link):

    youtube = YouTube(link)

    stream= youtube.streams.filter(only_audio=True)

    stream[0].download("D:\\Programas\\PyTube\\")