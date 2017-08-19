
#!/usr/bin/env python     

import tkinter as tk
import tkinter.messagebox as messagebox

windows = tk.Tk()
windows.title('TEST')
windows.geometry('350x450')

e = tk.Entry(windows,show='*')
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert',var)

def insert_end():
    var = e.get()
    t.insert('end',var)

button1 = tk.Button(windows,text = 'insert point',bg='green',width = 15,
                    height = 2,command=insert_point)
button1.pack()

button2 = tk.Button(windows,text = 'insert end',bg='yellow',width = 15,
                    height = 2,command=insert_end)
button2.pack()

t=tk.Text(windows,height=8)
t.pack()

windows.mainloop()

