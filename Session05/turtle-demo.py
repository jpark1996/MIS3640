import turtle

jack = turtle.Turtle() ## drew square 

for i in range(4):
    jack.fd(100) 
    jack.lt(90) 


turtle.mainloop()

# Simple repetition 
for i in range(4)
    print('hello!') # repeat hello! for four times 

import turtle

def square(t): 
    for i in range(4):
        t.fd(100)
        t.lt(90)

#  Generalization 
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(jack, 7, 70)

# interface design
import math

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

# Refactoring
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

jack = turtle.Turtle()

#circle 
def circle(t, r):
    arc(t, r, 360)

# square(jack)
circle(jack, )

turtle.mainloop()

