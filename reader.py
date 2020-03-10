import pygame
import tkinter as tk
import os

#Creating & Editing window:
player = tk.Tk()
player.title("MP3 Player")
player.geometry("205x340")

#Playlist:
os.chdir("Songs")
songList = os.listdir()
playlist = tk.Listbox(player, highlightcolor="blue", selectmode=tk.SINGLE)
print(songList)
for item in songList:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

#Initiating pygame:
pygame.init()
pygame.mixer.init()

#Functions:
def Play():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()
    
def ExitPlayer():
    pygame.mixer.music.stop()
    
def Pause():
    pygame.mixer.music.pause()

def Resume():
    pygame.mixer.music.unpause()

#Buttons:
Button1 = tk.Button(player, width=8, height=5, text="PLAY", command=Play)
Button1.pack(fill="x")

Button2 = tk.Button(player, width=8, height=5, text="STOP", command=ExitPlayer)
Button2.pack(fill="x")

Button3 = tk.Button(player, width=8, height=5, text="PAUSE", command=Pause)
Button3.pack(fill="x")

Button4 = tk.Button(player, width=8, height=5, text="RESUME", command=Resume)
Button4.pack(fill="x")

#More Playlist code:
var = tk.StringVar()
songTitle = tk.Label(player, textvariable=var)
songTitle.pack()
playlist.pack(fill="both", expand="yes")

#Starting window
player.mainloop()