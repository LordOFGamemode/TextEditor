from tkinter import *
from tkinter import filedialog
from funktions import popup
import threading

popupmanager = popup.pop()

opendfile = ''
opendtext = ''

def new_file():
    my_text.delete("1.0", END)
    root.title('Lords|Editor: New File')
    global opendfile
    opendfile = 'save/temp.txt'

def open_file():
    text_file = filedialog.askopenfilename(initialdir="C:/", title="Open File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if(text_file == ''):
        return
    global opendfile
    opendfile = text_file
    name = text_file
    my_text.delete("1.0", END)
    root.title(f'Lords|Editor: {name}')
    text_file = open(text_file, 'r')
    inhalt = text_file.read()
    my_text.insert(END, inhalt)
    text_file.close()

def save_as():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Save File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if text_file:
        global opendfile
        opendfile = text_file
        name = text_file
        root.title(f'Lords|Editor: {name}')

def save():
    print(my_text.get(1.0, "end-1c"))
    file = open(opendfile, 'w')
    file.seek(0)
    file.truncate()
    file.write(my_text.get(1.0, "end-1c"))
    file.close()

def close():
    root.quit()
    file = open('save/lastopend.txt', 'w')
    file.seek(0)
    file.truncate()
    file.write(opendfile)
    file.close()

def update():
    global opendtext
    opendtext = my_text.get(1.0, "end-1c")
    root.after(100, update)

def undo():

    print(opendfile)
    if opendfile == 'save/temp.txt':
        my_thread = threading.Thread(target=popupmanager.show, args=('Error', 'red', 'Undo only works with saved files.'))
        my_thread.start()
        return
    print(f'undid somthing in: {opendfile}')
    my_text.delete("1.0", END)
    opentext = open(opendfile, 'r')
    inhalt = opentext.read()
    my_text.insert(END, inhalt)



root = Tk()
root.title('Lords|Editor')
root.iconbitmap('img/logo1.ico')
root.geometry("1200x620")

main_frame = Frame(root)
main_frame.pack(pady=5)

text_scroll = Scrollbar(main_frame)
text_scroll.pack(side=RIGHT,fill=Y)

last_opend = open('save/lastopend.txt','r')

if last_opend.read() != '':
    my_text = Text(main_frame, width=97, font=("Helvetica", 16), selectbackground="green", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
    my_text.pack()
    file = open('save/lastopend.txt', 'r')
    file = open(file.read(), 'r')
    my_text.insert(END, file.read())
    file.close()
    file = open('save/lastopend.txt', 'r')
    opendfile = file.read()
    file.close()
    print('last file opend')
else:
    my_text = Text(main_frame, width=97, font=("Helvetica", 16), selectbackground="green", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
    my_text.pack()
    print(print(last_opend.read()))

text_scroll.config(command=my_text.yview)

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Save as", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=close)

edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
file_menu.add_separator()
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo")

status_bar = Label(root, text='Ready   ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.resizable(0, 0)
update()

root.mainloop()

file = open('save/lastopend.txt', 'w')
file.seek(0)
file.truncate()
file.write(opendfile)
file.close()
file = open(opendfile, 'w')
file.seek(0)
file.truncate()
file.write(opendtext)
file.close()