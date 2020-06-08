import tkinter as tk
from tkinter.filedialog import asksaveasfile as asf, askopenfile as aof
from tkinter import messagebox

FILE_NAME = tk.NONE

def new_file():
    global FILE_NAME
    FILE_NAME = "Newfile"
    text.delete('1.0', tk.END)

def save_file():
    data = text.get('1.0', tk.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()

def save_as():
    out = asf(mode='w', defaultextension='txt')
    data = text.get('1.0', tk.END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror(title="Error", message="Saving file error")

def open_file():
    global FILE_NAME
    inp = aof(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', tk.END)
    text.insert('1.0', data)

def info():
    messagebox.showinfo("Information", "Simple text editor\\nby CoderLog")


root = tk.Tk()
root.title("Text editor")
root.minsize(width=600, height=300)
root.maxsize(width=600, height=300)

text = tk.Text(root, width=300, height=300, wrap="word")
scrollb = tk.Scrollbar(root, orient=tk.VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)
text.pack()

menuBar = tk.Menu(root)
fileMenu = tk.Menu(menuBar)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Save as", command=save_as)

menuBar.add_cascade(label= "File", menu=fileMenu)
menuBar.add_cascade(label= "Info")
menuBar.add_cascade(label= "Exit", command=root.quit)
root.config(menu=menuBar)


root.mainloop()