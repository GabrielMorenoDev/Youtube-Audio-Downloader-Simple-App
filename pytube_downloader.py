from pytube import YouTube
import os

path = os.getcwd()

def download_audio(link):

    youtube = YouTube(link)

    audio = youtube.streams.get_audio_only()
    
    downloaded_audio = audio.download(path)

    base, ext = os.path.splitext(downloaded_audio)
    new_file = base + '.mp3'
    os.rename(downloaded_audio, new_file)
    

def download_video(link):

    youtube = YouTube(link)

    video = youtube.streams.filter(res='1080p').first()
    video.download(path)

def download_audio_and_video(link):

    youtube = YouTube(link)

    

    audio = youtube.streams.get_audio_only()
    
    downloaded_audio = audio.download(path)

    base, ext = os.path.splitext(downloaded_audio)
    new_file = base + '.mp3'
    os.rename(downloaded_audio, new_file)

    video = youtube.streams.filter(res='1080p').first()
    video.download(path)

def get_name(link):
    youtube = YouTube(link)

    return youtube.title
