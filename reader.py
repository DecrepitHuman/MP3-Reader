import pygame
import tkinter as tk
import os

player = tk.Tk()
player.title("MP3 Player")
player.geometry("205x340")

#Playlist:
os.chdir("C:/Users/nicho/Documents/Others/Python-Projects/mp3-reader/Songs")
songList = os.listdir()

playlist = tk.Listbox(player, highlightcolor="blue", selectmode=tk.SINGLE)
print(songList)
for item in songList:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()

def Play():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()
    
def ExitPlayer():
    pygame.mixer.music.stop()

Button1 = tk.Button(player, width=8, height=5, text="PLAY", command=Play)
Button1.pack(fill="x")

Button2 = tk.Button(player, width=8, height=5, text="STOP", command=ExitPlayer)
Button2.pack(fill="x")

var = tk.StringVar()
songTitle = tk.Label(player, textvariable=var)
songTitle.pack()
playlist.pack(fill="both", expand="yes")

player.mainloop()