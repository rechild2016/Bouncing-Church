
#!/usr/bin/env python     

import tkinter as tk
import tkinter.messagebox as messagebox

window = tk.Tk()
window.title('TEST')
window.geometry('500x500')

def do_job():
    canvas.coords(image,(0,0))    


menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='Img',menu=filemenu)
filemenu.add_command(label='Reset',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)
window.config(menu=menubar)

canvas = tk.Canvas(window,bg='green',height=450,width=500)
img_file = tk.PhotoImage(file = 'images.png')
image = canvas.create_image(0,0,anchor='nw',image=img_file)
line = canvas.create_line(50,50,200,200,width= 3)
oval = canvas.create_oval(200,200,300,300,fill='red')
canvas.pack()

def moveit():
    canvas.move(image,5,5)

b = tk.Button(window,text='move',command=moveit)
b.pack()


window.mainloop()

