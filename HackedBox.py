from tkinter import *

root = Tk()

photo = PhotoImage(file="hacked.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()