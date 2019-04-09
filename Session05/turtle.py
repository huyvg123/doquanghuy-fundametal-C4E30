print("1: ")
def say_hello(): 
    for i in range(3): 
        print("Hello world")
say_hello()
print()
print("2: ")
def add_two_number(): 
    a = int(input('nhap so thu nhat: '))
    b = int(input('Nhap so thu hai: '))
    print('Tong cua hai so la: ', a+b)
add_two_number()
print()
print('3: ')
def draw_square(l,v):
    color(v)
    for i in range(4):
        forward(l)
        left(90)
from turtle import *     
draw_square(100,'blue')
mainloop()
print('4: ')
def draw_square(l,v):
    color(v)
    for i in range(4):
        forward(l)
        left(90)
from turtle import *
for i in range(30):
    draw_square(i * 5, 'blue')
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()
print()
print('5: ')
from turtle import *
def draw_star(x,y,length): 
    penup()
    setposition(x,y)
    pendown()
    color("black")
    for i in range(5): 
        forward(length) 
        left(360/5)
draw_star(10,15,200)
mainloop()
print()
print('6: ')
from turtle import *
shape('turtle')
def draw_star(x,y,length):
    penup()
    setposition(x,y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
mainloop()


    

