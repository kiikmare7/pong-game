from turtle import Turtle
from paddle import Paddle,Paddle2
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.shape("circle")
        self.x_m=10
        self.y_m=10
        self.hit()

    def bounce(self):
        x = self.xcor() + self.x_m
        y = self.ycor() + self.y_m
        self.goto(x, y)


    def collition(self):
        self.y_m *= -1

    def hit(self):
        self.x_m *= -1





