from tkinter import *

def quit():
    if rtn != True:
        popup.quit()
        return
    print(entry)
    popup.quit()
    return entry

class pop():
    def __init__(self):
        self.desc = 'erstellt ein pop up window'
    
    def show(self, title, color, text, inp=False):
        global rtn
        rtn = inp
        global popup
        popup = Tk()
        popup.title(title)
        popup.geometry('350x100')
        
        my_lable = Label(popup , foreground=color, text=text)
        my_lable.pack()

        if inp:
            global entry
            entry = Entry(popup)
            entry.pack()

        Button(popup, text='Close', command=quit).pack(side=BOTTOM)
        
        popup.mainloop()
