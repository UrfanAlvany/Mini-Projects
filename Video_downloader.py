from tkinter import *
from pytube import YouTube

#The part for the creating window and designing.
window = Tk()
window.geometry("600x800")
window.config(bg="gray")
window.title("YouTube Video Downloader")

window.iconphoto(False,PhotoImage(file = 'images/logo.png'))

Label(window, text="Video Downloader" , font = ("Arial 30 bold"), bg="lightgreen").pack(padx = 5, pady = 50)

video_link = StringVar()

Label(window, text = "Enter the Link :" ,font = ("Arial",25,"bold")).place(x = 170, y = 110)

Entry_link = Entry(window, width = 50, font = 35, textvariable = video_link).place(x = 35, y = 200)

#The part for downloading the video.
def video_download():
    video_url = YouTube(str(video_link.get()))
    videos = video_url.streams.first()
    videos.download()
    #Comment for the process
    Label(window, text = "Download Completed ! \n Thank For Using Our Service :0", font = ("Arial",20,"bold"),bg = "lightcyan", fg ="black").place(x = 100, y = 300)

Button(window, text = "Download", font = ("Arial",25,"bold"),bg = "lightblue", command = video_download).place(x = 180, y = 300)

window.mainloop()