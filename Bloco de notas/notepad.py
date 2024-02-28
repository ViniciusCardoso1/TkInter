import tkinter

def NewFile():
    text_area.delete(1.0, "end")

def Save():
    container = text_area.get(1.0, "end")
    file = open("notepad.txt", "w")
    file.write(container)
    file.close()
def Open():
    file=open("notepad.txt", "r")
    container = file.read()
    text_area.insert(1.0, container)
    
def updateFont():
    size = spinSize.get()
    font = spinFontSize.get()
    text_area.config(font="{} {}".format(font, size))

    
window = tkinter.Tk()
window.title("Notepad")
window.minsize(width=1280, height=720)
window.geometry("1280x720")

frame = tkinter.Frame(window, height=30)
frame.pack(fill="x")

fontText = tkinter.Label(frame, text=" Font: ")
fontText.pack(side="left")

spinFontSize = tkinter.Spinbox(frame, values=("Arial", "Verdana"))
spinFontSize.pack(side="left")

fontSize = tkinter.Label(frame, text= "Font size: ")
fontSize.pack(side="left")

spinSize = tkinter.Spinbox(frame, from_=0, to=60)
spinSize.pack(side="left")

buttonUpdate = tkinter.Button(frame, text=" UP ", command=updateFont)
buttonUpdate.pack(side="left")

frame2 = tkinter.Frame(window, height=30)
frame2.pack(fill="x")

infoText = tkinter.Label(frame2, text="Este é um teste para outro frame!" )
infoText.pack(side="left")

text_area = tkinter.Text(window, font="Arial 20", width=1980, height=720)
text_area.pack()

main_menu = tkinter.Menu(window)

file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label="New", command=NewFile)
file_menu.add_command(label="Save", command=Save)
file_menu.add_command(label="Open", command=Open)
file_menu.add_command(label="Exit", command=window.quit)

main_menu.add_cascade(label="File", menu=file_menu)
window.config(menu=main_menu)

window.mainloop()
