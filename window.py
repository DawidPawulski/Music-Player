from tkinter import *

class DeezyDeer():
    window = Tk()
app = DeezyDeer(master = window)
app.mainloop()


p = ttk.Progressbar(parent, orient=HORIZONTAL, length=200, mode='determinate') # progress bar -> uncklickable
s = ttk.Scale(parent, orient=HORIZONTAL, length=200, from_=1.0, to=100.0) # scale for volume