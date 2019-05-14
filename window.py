from tkinter import *
import funcs


def window():

    window = Tk()
    window.title('Dizzy Dear')
    img = Image('photo', file = 'dizzydeer.gif')
    window.tk.call('wm', 'iconphoto', window._w, img)


    #window.iconbitmap(r'/home/jck/Documents/python/dizzydeer/DizzyDeer/dizzydeer.ico')


    button_play = Button(window, text = 'PLAY', command = lambda: funcs.play_playlist(funcs.get_songs_from_dir('/home/jck/Documents/python/dizzydeer/DizzyDeer/songs/')))
    button_play.pack()
    


    while True: # placeholder
        mainloop()
