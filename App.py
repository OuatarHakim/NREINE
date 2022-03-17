from tkinter import *

from Chessboard import Chessboard

window  = Tk()
window.title("N QUEEN")
window.geometry("660x400")
window.minsize(200, 150)
#window.iconbitmap("./reine.ico")
window.config(background='#41B77F')

frame = Frame(window ,bg ='#41B77F')
width = 300
height = 300

lable_title = Label(frame,text= "Problème N reines ",font=("Courrier",20),bg='#41B77F' , fg='white')
lable_title.pack()
canvas = Canvas(window, width= width, height = height ,bg='#41B77F')
canvas.pack()

frame.pack(expand = YES)
spin=Spinbox(window, values=(4,5,6,7,8,9,10,11), width=4)
spin.config( font="sans 12", justify="center")
spin.pack()
b=Button(window,text="calculer",command=Chessboard(int(spin.get())))
b.pack()
ll=Label(window,text="nombre de solutions")
ll.pack()
window.mainloop()

