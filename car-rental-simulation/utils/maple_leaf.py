import turtle
import random
import math

a = 0
b = 2 * math.pi

def random_number_gen():
    rand = random.random()
    return a + (rand * (b - a))

def MapleLeaf(x=0, y=0, scale=random_number_gen()):
    def my_goto(x_offset, y_offset):
        turtle.goto(x + scale*x_offset, y + scale*y_offset)
    if x == None:
        x = 0
    if y == None:
        y = 0
    turtle.penup()
    my_goto(1, -3)
    turtle.pendown()
    my_goto(5, -4)
    my_goto(4, -3)
    my_goto(9, 1)
    my_goto(7, 2)
    my_goto(8, 5)
    my_goto(5, 4)
    my_goto(5, 5)
    my_goto(3, 4)
    my_goto(4, 9)
    my_goto(2, 7)
    my_goto(0, 10)
    my_goto(-2, 7)
    my_goto(-4, 8)
    my_goto(-3, 3)
    my_goto(-5, 6)
    my_goto(-5, 4)
    my_goto(-8, 5)
    my_goto(-7, 2)
    my_goto(-9, 1)
    my_goto(-4, -3)
    my_goto(-5, -4)
    my_goto(0, -3)
    my_goto(2, -7)
    my_goto(2, -6)
    my_goto(1, -3)
    turtle.hideturtle()


turtle.pencolor("black")
turtle.fillcolor("red")
turtle.begin_fill()
MapleLeaf(120, 120)
turtle.end_fill()
turtle.done()
