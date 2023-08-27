import tkinter
import customtkinter as ct
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_lowest_resolution()
        video.download()
    except:
        finishedLabel.configure(text="Link Invalid", bg_color="red",font=("Arial", 25) )
        return
    
    finishedLabel.configure(text="Download Complete", bg_color="green", font=("Arial", 25))

#System Settings

ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")

app = ct.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# UI elements

title = ct.CTkLabel(app, text="Insert Youtube URL", font=("Arial", 25))
title.pack(padx=10, pady=10)

url = tkinter.StringVar()
link = ct.CTkEntry(app, width=350, height= 40, textvariable=url)
link.pack()

finishedLabel = ct.CTkLabel(app, text="")
finishedLabel.pack(padx=10, pady=10)

download = ct.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=15, pady=15)


#Run app
app.mainloop()