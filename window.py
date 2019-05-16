import tkinter
from tkinter import filedialog
from tkinter import ttk
import funcs


def pick_dir():
    directory = filedialog.askdirectory()
    return directory


def window():
    window = tkinter.Tk()
    window.title('Dizzy Dear')
    window.geometry('450x200')
    img = tkinter.Image('photo', file='dizzydeer.gif')
    window.tk.call('wm', 'iconphoto', window._w, img)
    song_index = 0
    topFrame = tkinter.Frame(window)
    topFrame.pack()

    directory = pick_dir()

    bottomFrame = tkinter.Frame(window)
    bottomFrame.pack(side=tkinter.BOTTOM)

    pb = ttk.Progressbar(window, orient="horizontal", length=400, mode="determinate")
    pb.pack()

    button_previous_song = tkinter.Button(topFrame, text='|<<', activebackground="purple",
                                          command=lambda: funcs.previous_song(funcs.get_songs_from_dir(directory)))
    button_previous_song.pack(side=tkinter.LEFT)
    button_play = tkinter.Button(topFrame, text='| >', activebackground="purple",
                                 command=lambda: funcs.play_playlist(funcs.get_songs_from_dir(directory), song_index))
    button_play.pack(side=tkinter.LEFT)
    button_stop = tkinter.Button(topFrame, text='| |', activebackground="purple",
                                 command=lambda: funcs.pause_song())
    button_stop.pack(side=tkinter.LEFT)
    button_next_song = tkinter.Button(topFrame, text='>>|', activebackground="purple",
                                      command=lambda: funcs.next_song(funcs.get_songs_from_dir(directory)))
    button_next_song.pack(side=tkinter.LEFT)
    button_pick = tkinter.Button(window, text='PD', activebackground="purple",
                                 command=lambda: pick_dir())
    button_pick.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    T = tkinter.Text(window, height=10, width=30)
    T.pack()
    T.insert(tkinter.END, funcs.display_playlist(funcs.get_songs_from_dir(directory)))
    slider_volume = tkinter.Scale(window, from_=0, to=100, orient=tkinter.HORIZONTAL)
    slider_volume.pack(side=tkinter.RIGHT)
    pb.start()

    while True:  # placeholder
        tkinter.mainloop()
