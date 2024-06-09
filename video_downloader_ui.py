from pytube_downloader import download_audio, get_name
from tkinter import *

def download():
    link = videoInput.get()
    download_audio(link)
    add_to_history(get_name(link))

def add_to_history(video_name):
    try:
        with open("download_history.txt", "a") as history:
            history.write("\n"+video_name)
        history.close()
        historyListBox.insert(0, video_name)
    except FileNotFoundError:
        with open('log.txt', 'w') as history:
            history.write(video_name)



root = Tk()
root.minsize(250,250)
root.configure(background="gray")




videoLabel = Label(root, font="Helvetica 42",text="Youtube Audio Downloader\nInsert the video link", bg="gray")
videoLabel.pack()

videoInput = Entry(root, width=100)
videoInput.pack()

downloadButton = Button(root, text="Download Audio", padx=20, pady=20, command=download)
downloadButton.pack()

historyListBox = Listbox(root, font="Helvetica 20", height=5, width=30  , bg="gray")


with open("download_history.txt", "r") as history:
    history_list = reversed(history.readlines())
        
    position = 1
    for line in history_list:
            
        if position != 5:
            historyListBox.insert(position, line)
            position += 1
            continue
        break
            

    history.close()

    

historyListBox.pack()

root.mainloop()
