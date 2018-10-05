from tkinter import *
import pygame
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox

window = Tk();
window.geometry('300x300')
window.title('Python Music Player')
pygame.init()

def browse_file():
	global filename
	filename = filedialog.askopenfilename()

def help_me():
	tkinter.messagebox.showinfo("Help", "Isn't it great")

menubar = Menu(window)
window.config(menu=menubar)

submenu = Menu(menubar, tearoff = 0)

menubar.add_cascade(label = "File", menu = submenu)
submenu.add_command(label = "Open", command = browse_file)
submenu.add_command(label = "Exit", command = window.destroy)

submenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "About us", menu = submenu)
submenu.add_command(label = "Help", command = help_me)


textLabel = Label(window,text="This is a play button")
textLabel.pack()

photo_start = PhotoImage(file='play.png')
photo_stop = PhotoImage(file = 'stop.png')
photo_pause = PhotoImage(file = 'pause.png')
#photolabel = Label(window,image=photo)
#photolabel.pack()
#def start_song():
#	print ("hey im being clicked")


def play_music():
	try:
		paused
	except:
		try:
			mixer.music.load(filename)
			mixer.music.play()
			statusbar['text'] = "Keep enjoying the Music"
		except:
			tkinter.messagebox.showerror("File Error","File not found!")
	else:
		mixer.music.unpause()

def stop_music():
	mixer.music.stop()
	statusbar['text'] = "Music is stopped"

def set_volume(value):
	volume = float(value)/100
	mixer.music.set_volume(volume)

def pause_music():
	global paused
	paused = True
	mixer.music.pause()
	statusbar['text'] = "Music is paused"
def rewind_music():
	play_music()
	statusbar['text'] = "Music is rewinded"


frame = Frame(window)
frame.pack(padx=10,pady=10)

statusbar = Label(window, text="Keep enjoying the music", relief=SUNKEN, anchor=W)#relief =flat or raised
statusbar.pack(side=LEFT, fill= X)

playButton = Button(frame, image=photo_start, command = play_music )
stopButton = Button(frame, image = photo_stop, command = stop_music)
pauseButton = Button(frame, image= photo_pause, command = pause_music)

playButton.grid(row=0, column=0, padx=10)
stopButton.grid(row=0, column=1, padx=10)
pauseButton.grid(row=0, column=2, padx=10)

bottomframe = Frame(window)
bottomframe.pack()

rewind_photo = PhotoImage(file="rewind.png")
rewind_button = Button(bottomframe, image = rewind_photo, command = rewind_music)
rewind_button.grid(row=0,column=0,padx=10)

scale = Scale(bottomframe, from_= 0, to= 100, orient = HORIZONTAL, command = set_volume)
scale.set(70)
scale.grid(row=0,column=1, pady=15)


window.mainloop()
