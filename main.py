from tkinter import *
import funcs
#def a():
    #a = 0
#    a = funcs.play_playlist(funcs.get_songs_from_dir('/home/jck/Documents/python/dizzydeer/DizzyDeer/songs/'))
    #return a
window = Tk()
window.title('Dizzy Dear')
#window.iconbitmap(r'/home/jck/Documents/python/dizzydeer/DizzyDeer/dizzydeer.ico')
button_play = Button(window, text = 'PLAY', command = lambda: funcs.play_playlist(funcs.get_songs_from_dir('/home/jck/Documents/python/dizzydeer/DizzyDeer/songs/')))
button_play.pack()


if __name__ == '__main__':
    mainloop()
