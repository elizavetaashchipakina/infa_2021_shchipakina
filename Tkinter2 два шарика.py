from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = [['red'], ['orange'], ['yellow'], ['blue'], ['green'], ['lightgreen'], ['purple'], ['cyan'], ['lightcyan'], ['linen'], ['RosyBrown2'], ['tomato2'], ['OliveDrab2'], ['aquamarine']]
colors[1] = ['black']

def new_ball():
    """Функция, рисующая первый шарик"""
    global x, y, r
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(10, 60)
    canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)
    

    """Функция, рисующая второй шарик"""
    global x1, y1, r1
    x1 = rnd(100, 700)
    y1 = rnd(100, 500)
    r1 = rnd(10, 60)
    canv.create_oval(x1-r1, y1-r1, x1+r1, y1+r1, fill=choice(colors), width=0)
    root.after(1000, new_ball)

b=0
def click(event):
    global b, x, y, r, x1, y1, r1
    if (r**2) >= ((event.x-x)**2 + (event.y-y)**2) and r<=60 and r>40:
        b+=1
    elif ((r**2)/2) >= ((event.x-x)**2 + (event.y-y)**2) and r<=40 and r>20:
        b+=2
    elif (r**2) >= ((event.x-x)**2 + (event.y-y)**2) and r<=20 and r>10:
        b+=3
    elif (r1**2) >= ((event.x-x1)**2 + (event.y-y1)**2) and r1<=60 and r1>40:
        b+=1
    elif ((r1**2)/2) >= ((event.x-x1)**2 + (event.y-y1)**2) and r1<=40 and r1>20:
        b+=2
    elif (r1**2) >= ((event.x-x1)**2 + (event.y-y1)**2) and r1<=20 and r1>10:
        b+=3
    else:
        b=0
    print(b)

new_ball()
    
canv.bind('<Button-1>', click)

root.mainloop()
