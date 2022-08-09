import tkinter as tk
import random
import threading
import time
def dow():
    window = tk.Tk()
    window.title('you are a fool!!!')
    window.geometry("300x75" + "+" + str(random.randrange(0, window.winfo_screenwidth())) + "+" + str(random.randrange(0,window.winfo_screenheight())))
    tk.Label(window,
             text='you are a fool!!!',
             bg='Blue',
             font=('幼圆', 17),
             width=20, height=2
             ).pack()
    window.mainloop()
threads = []
for i in range(100000000):
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()

