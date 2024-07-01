from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.25, stretch_wid=0.25)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(a=-230, b=230)
        y = random.randint(a=-230, b=230)
        self.goto(x, y)
