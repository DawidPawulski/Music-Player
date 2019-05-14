from tkinter import *
from tkinter import filedialog
import funcs

def pick_dir():
    directory = filedialog.askdirectory()
    return directory
def window():

    window = Tk()
    window.title('Dizzy Dear')
    img = Image('photo', file = 'dizzydeer.gif')
    window.tk.call('wm', 'iconphoto', window._w, img)


    #window.iconbitmap(r'/home/jck/Documents/python/dizzydeer/DizzyDeer/dizzydeer.ico')


    # filedialog.askdirectory()
    
    #window.file =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
    directory = pick_dir()


    button_play = Button(window, text = 'PLAY', command = lambda: funcs.play_playlist(funcs.get_songs_from_dir(directory)))
    button_play.pack()
    button_stop = Button(window, text = 'STOP', command = lambda: funcs.stop_song())
    button_stop.pack()
    button_pick = Button(window, text = 'Pick Directory', command = lambda: pick_dir())
    button_pick.pack()







    while True: # placeholder
        mainloop()
