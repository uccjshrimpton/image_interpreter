from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

filename = None


def New():
    filename = "Untitled"
    Notepad.delete(0.0, END)


def Save():
    t = Notepad.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()


def SaveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = Notepad.get(0.0, END)
    f.write(t.rstrip())
    f.close()


def Open():
    f = askopenfile(parent=mainWindow, title='Select a File')
    filename = f.name
    t = f.read()
    Notepad.delete(0.0, END)
    Notepad.insert(0.0, t)
    f.close()


def Undo():
    print("Undo.")


def Redo():
    print("Redo.")


def Cut():
    print("Cut.")


def Copy():
    print("Copy.")


def Paste():
    print("Paste.")


def Delete():
    print("Delete.")


def ViewHelp():
    print("View Help.")


def AboutNotepad():
    print("About Notepad.")


mainWindow = Tk()

mainWindow.title("Notepad")

Notepad = Text(mainWindow)
Notepad.pack()

myMenu = Menu(mainWindow)
mainWindow.config(menu=myMenu)

FileMenu = Menu(myMenu)
myMenu.add_cascade(label="File", menu=FileMenu)
FileMenu.add_command(label="New", command=New)
FileMenu.add_command(label="Open...", command=Open)
FileMenu.add_command(label="Save", command=Save)
FileMenu.add_command(label="Save As...", command=SaveAs)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=mainWindow.quit)

EditMenu = Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=EditMenu)
EditMenu.add_command(label="Undo", command=Undo)
EditMenu.add_command(label="Redo", command=Redo)
EditMenu.add_separator()
EditMenu.add_command(label="Cut", command=Cut)
EditMenu.add_command(label="Copy", command=Copy)
EditMenu.add_command(label="Paste", command=Paste)
EditMenu.add_command(label="Delete", command=Delete)

HelpMenu = Menu(myMenu)
myMenu.add_cascade(label="Help", menu=HelpMenu)
HelpMenu.add_command(label="View Help", command=ViewHelp)
HelpMenu.add_separator()
HelpMenu.add_command(label="About Notepad", command=AboutNotepad)

mainWindow.mainloop()