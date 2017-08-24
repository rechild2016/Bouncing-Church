import math
import time
import threading
import show

def Task():
    global timer
    show.do_job()
    timer=threading.Timer(0.1,Task)
    timer.start()

timer=threading.Timer(1,Task)
timer.start()

# show.init()
show.window.mainloop()
timer.cancel()
print("The End!")
