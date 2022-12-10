from turtle import *
from suv import *
from car import *
from truck import *
import sys

class Environment():
    def __init__(self) -> None:
        self.WIDTH = 800
        self.HEIGHT = 500
        self.offset = 0
    
    def initialiseTurtle(self):
        title("First 2D vehicle with python")
        speed(0)
        pensize(2)
        hideturtle()

    def the_sun(self):
        # the sun
        penup()
        setpos(-250, 200)
        dot((60), "red")
        pendown()
        penup()
        ht()
        
    def the_background(self):
        background = Turtle(visible=False)
        background.penup()
        background.setx(-self.WIDTH/2)
        background.pendown()

        background.color('green')
        background.begin_fill()

        for _ in range(2):
            background.forward(self.WIDTH)
            background.right(90)
            background.forward(self.HEIGHT/2)
            background.right(90)

        background.end_fill()
        
    def drawFlower(self):
        # Set initial position
        penup()
        setpos(-400 + self.offset, -150)
        speed(30)
        hideturtle()
        left(90)
        fd(20)
        pendown()
        right(90)
        # flower base
        fillcolor("red")
        begin_fill()
        circle(1, 180)
        circle(2, 110)
        left(50)
        circle(6, 45)
        circle(2, 170)
        right(24)
        fd(3)
        left(10)
        circle(3, 110)
        fd(2)
        left(40)
        circle(9, 70)
        circle(3, 150)
        right(30)
        fd(1.5)
        circle(8, 90)
        left(15)
        fd(4.5)
        right(165)
        fd(2)
        left(155)
        circle(15, 80)
        left(50)
        circle(15, 90)
        end_fill()

        # Petal 1
        left(150)
        circle(-9, 70)
        left(20)
        circle(7.5, 105)
        setheading(60)
        circle(8, 98)
        circle(-9, 40)

        # Petal 2
        left(180)
        circle(9, 40)
        circle(-8, 98)
        setheading(-83)

        # Leaves 1
        fd(3)
        left(90)
        fd(2.5)
        left(45)
        fillcolor("green")
        begin_fill()
        circle(-8, 90)
        right(90)
        circle(-8, 90)
        end_fill()
        right(135)
        fd(6)
        left(180)
        fd(8.5)
        left(90)
        fd(8)

        # Leaves 2
        right(90)
        right(45)
        fillcolor("green")
        begin_fill()
        circle(8, 90)
        left(90)
        circle(8, 90)
        end_fill()
        left(135)
        fd(6)
        left(180)
        fd(6)
        right(90)
        circle(20, 60)
        penup()

        

    def drawFlowers(self):

        for i in range(0, 15):
            self.offset += 50
            self.drawFlower()
            penup()
        penup()
        ht()
