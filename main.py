# Author : Noah Payne
# Written : 05/02/2022

import turtle as t
import colorsys

t.bgcolor('black')

t.speed('fastest')

t.pensize(2)

t.setpos(50, 0)

hue = 0.0

t.hideturtle()


for i in range(400):
    color = colorsys.hsv_to_rgb(hue, 1, 1)

    t.pencolor(color)

    hue += 0.005

    t.fd(i)

    t.bk(i)

    t.lt(1)

    t.right(120)

    t.forward(100)

    t.right(120)

    t.right(120*2+0.1)

    t.tracer(30)

t.exitonclick()
