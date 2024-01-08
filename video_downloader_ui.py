from pytube_downloader import download_audio
from tkinter import *

def download():
    link = videoInput.get()
    download_audio(link)




root = Tk()
root.minsize(250,250)
root.configure(background="gray")




videoLabel = Label(root, font="Helvetica 42",text="Youtube Audio Downloader\nInsert the video link", bg="gray")
videoLabel.pack()

videoInput = Entry(root, width=100)
videoInput.pack()

downloadButton = Button(root, text="Download Audio", padx=20, pady=20, command=download)
downloadButton.pack()


root.mainloop()
