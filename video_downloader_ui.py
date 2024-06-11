from pytube_downloader import download_audio, get_name, download_video, download_audio_and_video
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb 

def download():
    link = videoInput.get()
    match option_var.get():
        case "Audio":
            download_audio(link)
        case "Video":
            download_video(link)
        case "Both":
            download_audio_and_video(link)
        case _:
            raise("Error in code")
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



#root = Tk()
#root.minsize(250,250)
#root.configure(background="gray")
root = tb.Window(themename="darkly")



videoLabel = Label(root, font="Helvetica 42",text="Youtube Audio Downloader\nInsert the video link", bg="gray")
videoLabel.pack()

videoInput = Entry(root, width=100)
videoInput.pack()

downloadButton = tb.Button(root, text="Download Audio", padding=(10,10),command=download)
downloadButton.pack()

downloadOptionsButton = tb.Menubutton(text="Choose download options")
optionsMenu = tb.Menu(downloadOptionsButton)
option_var = StringVar(value="Audio")
optionsMenu.add_radiobutton(label="Audio only",value="Audio",variable=option_var)
optionsMenu.add_radiobutton(label="Video Only",value="Video",variable=option_var)
optionsMenu.add_radiobutton(label="Both",value="Both",variable=option_var)
downloadOptionsButton['menu'] = optionsMenu

downloadOptionsButton.pack()
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
