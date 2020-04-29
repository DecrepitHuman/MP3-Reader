import pygame
import tkinter as tk
import os

#Creating & Editing window:
player = tk.Tk()
player.title("MP3 Player")
player.geometry("300x700")

#Playlist:
#Playlist has been sourced from another creator, it is NOT my code. All credit goes to creator
os.chdir("Songs")
songList = os.listdir()

#Volume Control
#Volume control has been sourced from another creator, it is NOT my code. All credit goes to creator
VolumeLevel = tk.Scale(player, from_=0.0,to_=1.0,
                        orient=tk.HORIZONTAL, resolution=0.1)
VolumeLevel.pack()

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
    pygame.mixer.music.set_volume(VolumeLevel.get())

def ExitPlayer():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()

def Resume():
    pygame.mixer.music.unpause()
    pygame.mixer.music.set_volume(VolumeLevel.get())

def OpenMixer():
    #Creating & Editing window:
    OpenMixer = tk.Tk()
    OpenMixer.title("MP3: Mixer settings")
    OpenMixer.geometry("300x300")

    def createPlaylist():
        PlayListLoader = tk.Tk()
        PlayListLoader.title("Enter Playlist Name")
        PlayListLoader.geometry("300x300")

        def createNow():
            os.mkdir(str(e1.get()))

        e1 = tk.Entry(PlayListLoader)
        e1.pack(fill="x")

        tk.Button(PlayListLoader, text="Submit", command=createNow).pack()

        PlayListLoader.mainloop()
        ###END OF PLAYLIST###

    editPlaylist =  tk.Button(OpenMixer, text="Create Playlist", command=createPlaylist)
    editPlaylist.pack(fill="x")

    OpenMixer.mainloop()

def Website():
    try:
        songNameWebsite = str(playlist.get(tk.ACTIVE))
        newSongNameWebsite = songNameWebsite.replace(" ", "+")
        os.system("start https://www.youtube.com/results?search_query=" + newSongNameWebsite)
    except IOError:
        print("IOError reached")
    else:
        os.system("cls")
        print("Error, song reached char limit. Please shorten name.",
              "If this error was mistaken, please ignore.")

#Buttons:
Button1 = tk.Button(player, width=8, height=5, text="PLAY", command=Play)
Button1.pack(fill="x")

Button2 = tk.Button(player, width=8, height=5, text="STOP", command=ExitPlayer)
Button2.pack(fill="x")

Button3 = tk.Button(player, width=8, height=5, text="PAUSE", command=Pause)
Button3.pack(fill="x")

Button4 = tk.Button(player, width=8, height=5, text="RESUME", command=Resume)
Button4.pack(fill="x")

Button5 = tk.Button(player, width=8, height=5, text="GOOGLE", command=Website)
Button5.pack(fill="x")

Button6 = tk.Button(player, width=14, height=8, text="OTHER SETTINGS", command=OpenMixer)
Button6.pack()

#More Playlist code:
var = tk.StringVar()
songTitle = tk.Label(player, textvariable=var)
songTitle.pack(fill="both")
playlist.pack(fill="both", expand="yes")

#Starting application
player.mainloop()
