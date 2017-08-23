
#!/usr/bin/env python     
TRACK_NUM = 60     #save the num of postion in track_list

import math
import time
import tkinter as tk
import tkinter.messagebox as messagebox
import threading

window = tk.Tk()
window.title('TEST')
window.geometry('800x600')

def leftKey(event):
    canvas.move(image,-5,0)
    print ("Left key pressed")

def rightKey(event):
    canvas.move(image,5,0)
    print ("Right key pressed")

frame = tk.Frame(window)
window.bind('<Left>', leftKey)
window.bind('<Right>', rightKey)
frame.pack()

flag = 1
counter=0
track_list=[[0 for col in range(2)] for row in range(TRACK_NUM)]

def Track(start,v0,sita):
    global track_list
    sum_x=start[0]
    sum_y=start[1]
    for t in range(TRACK_NUM):
        x=round(v0*math.cos(sita))
        y=-round(v0*math.sin(sita)-0.6*t)
        track_list[t]=[x,y]
        canvas.create_line(sum_x,sum_y,sum_x+x,sum_y+y)
        sum_x += x
        sum_y += y
        print(sum_x,sum_y)
  
def do_job():
    global flag
    global counter
    global track_list
    if flag == 1 :
        start=(100,200)   
        Track(start,15,(math.pi)/12)
        flag=0

    if counter < TRACK_NUM :
        print(track_list[counter])
        canvas.move(oval,track_list[counter][0],track_list[counter][1])
        counter+=1

def Task():
    global timer
    do_job()
    timer=threading.Timer(0.1,Task)
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

canvas = tk.Canvas(window,bg='green',height=600,width=800)
img_file = tk.PhotoImage(file = 'images.png')
image = canvas.create_image(110,450,anchor='center',image=img_file)
oval = canvas.create_oval(100,200,110,210,fill='red')
canvas.pack()

def moveit():
    canvas.move(image,5,5)

# b = tk.Button(window,text='move',command=do_job)
# b.pack()

window.mainloop()
timer.cancel()
