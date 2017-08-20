
#!/usr/bin/env python     

import math
import time
import tkinter as tk
import tkinter.messagebox as messagebox
import threading

window = tk.Tk()
window.title('TEST')
window.geometry('800x600')

flag = 1
counter=0
track_list=[[0 for col in range(2)] for row in range(500)]

def Track(start,v0,sita):
    global track_list
    for t in range(500):
        x=round(v0*math.cos(sita))
        y=-round(v0*math.sin(sita)-0.3*t)
        track_list[t]=[x,y]
    print(track_list)

def do_job():
    global flag
    global counter
    global track_list
    if flag == 1 :
        print('init')
        start=(200,200)   
        Track(start,10,(math.pi)/12)
        flag=0

    if counter < 50 :
        print(track_list[counter])
        # canvas.coords(image,(track_list[counter]))
        canvas.move(oval,track_list[counter][0],track_list[counter][1])
        counter+=1

def Task():
    print('hello')
    global timer
    do_job()
    timer=threading.Timer(1,Task)
    timer.start()

timer=threading.Timer(1,Task)
timer.start()

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='Img',menu=filemenu)
filemenu.add_command(label='Reset',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)
window.config(menu=menubar)

canvas = tk.Canvas(window,bg='green',height=550,width=800)
img_file = tk.PhotoImage(file = 'images.png')
image = canvas.create_image(0,0,anchor='center',image=img_file)
line = canvas.create_line(50,50,200,200,width= 3)
oval = canvas.create_oval(100,200,110,210,fill='red')
canvas.pack()

def moveit():
    canvas.move(image,5,5)

b = tk.Button(window,text='move',command=do_job)
b.pack()

window.mainloop()
timer.cancel()
