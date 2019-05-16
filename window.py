from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import funcs
import pygame


def pick_dir():
    directory = filedialog.askdirectory()
    return directory

def window():
	window = Tk()
	window.title('Dizzy Dear')
	window.geometry('450x200')
	img = Image('photo', file = 'dizzydeer.gif')
	window.tk.call('wm', 'iconphoto', window._w, img)
	song_index = 0
	topFrame=Frame(window)
	topFrame.pack()

	directory = pick_dir()

	bottomFrame = Frame(window)
	bottomFrame.pack(side = BOTTOM)

	pb = ttk.Progressbar(window, orient="horizontal", length=400, mode="determinate")
	pb.pack()
	
	button_previous_song = Button(topFrame, text = '|<<',activebackground = "purple", command = lambda: funcs.previous_song(funcs.get_songs_from_dir(directory)))
	button_previous_song.pack(side=LEFT)
	button_play = Button(topFrame, text = '| >',activebackground = "purple", command=lambda: funcs.play_playlist(funcs.get_songs_from_dir(directory), song_index))
	button_play.pack(side=LEFT)
	button_stop = Button(topFrame, text = '| |',activebackground = "purple", command = lambda: funcs.pause_song())
	button_stop.pack(side=LEFT)
	button_next_song = Button(topFrame, text = '>>|',activebackground = "purple", command = lambda: funcs.next_song(funcs.get_songs_from_dir(directory)))
	button_next_song.pack(side=LEFT)
	button_pick = Button(window, text = 'PD',activebackground = "purple", command = lambda: pick_dir())
	button_pick.pack(side=RIGHT,fill = Y)
	T = Text(window, height=10, width=30)
	T.pack()
	# T.insert(END, "Just a text Widget\nin two lines\n")
	T.insert(END, funcs.display_playlist(funcs.get_songs_from_dir(directory)))
	#button_pick = Button(window, text = 'PD',activebackground = "purple", command = lambda: pick_dir())
	#button_pick.pack(side=RIGHT,fill = Y)
	slider_volume = Scale(window, from_=0, to=100, orient=HORIZONTAL)
	slider_volume.pack(side=RIGHT)
	pb.start()
	

	while True: # placeholder
		mainloop()
