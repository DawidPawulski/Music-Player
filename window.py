from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import funcs

def pick_dir():
    directory = filedialog.askdirectory()
    return directory

def window():

	window = Tk()
	window.title('Dizzy Dear')
	window.geometry('450x100')
	img = Image('photo', file = 'dizzydeer.gif')
	window.tk.call('wm', 'iconphoto', window._w, img)

	topFrame=Frame(window)
	topFrame.pack()


    #window.iconbitmap(r'/home/jck/Documents/python/dizzydeer/DizzyDeer/dizzydeer.ico')

    #label_smth = Label(window, text = "  ")    

    # filedialog.askdirectory()
    
    #window.file =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
	directory = pick_dir()


	bottomFrame = Frame(window)
	bottomFrame.pack(side = BOTTOM)




	pb = ttk.Progressbar(window, orient="horizontal", length=400, mode="determinate")
	pb.pack()
	



	button_previous_song = Button(topFrame, text = '|<<',activebackground = "purple")  #, command = lambda: pick_dir())
	button_previous_song.pack(side=LEFT)
	button_play = Button(topFrame, text = '| >',activebackground = "purple", command = lambda: funcs.play_playlist(funcs.get_songs_from_dir(directory)))
	button_play.pack(side=LEFT)
	button_stop = Button(topFrame, text = '| |',activebackground = "purple", command = lambda: funcs.stop_song())
	button_stop.pack(side=LEFT)
	button_next_song = Button(topFrame, text = '>>|',activebackground = "purple")  #, command = lambda: pick_dir())
	button_next_song.pack(side=LEFT)
	button_pick = Button(window, text = 'PD',activebackground = "purple", command = lambda: pick_dir())
	button_pick.pack(side=RIGHT,fill = Y)
	pb.start()
	






	while True: # placeholder
		mainloop()
