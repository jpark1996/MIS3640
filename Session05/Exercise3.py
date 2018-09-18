import turtle
import math

# First picture
john = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
# polyline(john, 3, 100,30)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


def circle(t,r):
    arc(t,r,360)
    circle(john, 100)
    john.up()
    john.goto(0,100)
    john.down()
    john.lt(60)
    arc(john, 100 , 60)
    john.lt(120)
    arc(john, 100 , 60)

    john.lt(60)
    arc(john, 100 , 60)
    john.lt(120)
    arc(john, 100 , 60)

    john.lt(240)
    arc(john, 100 , 60)
    john.lt(120)
    arc(john, 100 , 60)

    john.rt(60)
    arc(john, 100 , 60)
    john.lt(120)
    arc(john, 100 , 60)

    john.rt(360)
    arc(john, 100 , 60)
    john.lt(120)
    arc(john, 100 , 60)

    john.rt(540)
    arc(john, 100 , 60)
    john.lt(120)
    arc(john, 100 , 60)

turtle.mainloop()

#  second picture 

john = turtle.Turtle()

john.circle(100)
john.up()
john.goto(0, 100) 
john.down()
john.circle(50, 180)
john.up()
john.goto(0, 100)  
john.down()
john.circle(50, 180)
john.up()
john.goto(0, 35)  
john.down()
john.circle(20)
john.up()
john.goto(0, 125)  
john.down()
john.circle(20)

turtle.mainloop()

