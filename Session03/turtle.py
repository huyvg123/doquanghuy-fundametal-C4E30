from turtle import * 
colors = ['red', 'blue', 'brown', 'yellow', 'gray']
for i in range(3): 
    color(colors[0])
    forward(100)
    left(120)
for i in range(4): 
    color(colors[1])
    forward(100)
    left(90)
for i in range(5): 
    color(colors[2])
    forward(100)
    left(360/5)
for i in range(6): 
    color(colors[3])
    forward(100)
    left(360/6)
for i in range(7): 
    color(colors[4])
    forward(100)
    left(360/7)
mainloop()

from turtle import *
colors = ['red','blue','brown','yellow','grey']
for v in colors:
    begin_fill()
    color(v)
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
    end_fill()
mainloop()