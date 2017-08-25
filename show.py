#show moudle
import tkinter as tk
import tkinter.messagebox as messagebox
import math

TRACK_NUM = 60
flag = 0
counter=0
track_list=[[0 for col in range(2)] for row in range(TRACK_NUM)]
Angle = 30 
Strength = 15

def Track(start,v0,sita):
    global track_list
    sum_x=start[0]
    sum_y=start[1]
    a=(start[0],start[1])
    for t in range(TRACK_NUM):
        x=round(v0*math.cos(sita))
        y=-round(v0*math.sin(sita)-0.6*t)
        track_list[t]=[x,y]
        sum_x += x
        sum_y += y
        a+=(sum_x,sum_y)
    print("a====>",a)
    return a

def do_job():
    global flag
    global counter
    global track_list
    print("in do job",Angle,flag)
    if flag == 1 :
        start=(100,200)   
        print("in do job ---line ",Angle,flag)
        line=Track(start,Strength,Angle*(math.pi)/180)
        canvas.create_line(line)
        # flag=0

    if flag ==2 and counter < TRACK_NUM :
        # print(track_list[counter])
        canvas.move(oval,track_list[counter][0],track_list[counter][1])
        counter+=1

def leftKey(event):
    canvas.move(image,-5,0)
    print ("Left key pressed")

def rightKey(event):
    canvas.move(image,5,0)
    print ("Right key pressed")

def upKey(event):
    global Angle
    print("up key")
    Angle += 1
def downKey(event):
    global Angle
    print("down key")
    Angle -= 1
def spaceKey(event):
    global flag
    flag += 1
    # event like this:<KeyPress event state=Mod1 keysym=space keycode=32 char=' ' x=-21 y=-33>
    print(event)

def moveit():
    canvas.move(image,5,5)
    print("in move")

window = tk.Tk()
window.title('TEST')
window.geometry('800x600')
frame = tk.Frame(window)
window.bind('<Left>', leftKey)
window.bind('<Right>', rightKey)
window.bind('<Up>', upKey)
window.bind('<Down>', downKey)
window.bind('<space>', spaceKey)
frame.pack()

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

