from tkinter import *
from tkinter.ttk import *
from time import strftime
from PIL import Image, ImageTk
root = Tk()
root.title('Clock')
root.geometry("309x100")
root.maxsize(309,100)
ico = Image.open('alarm.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text=string)
	lbl.after(1000, time)


# Styling the label widget

lbl = Label(root, font=('cursive', 40, 'italic'),
			background='purple',
			foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()
