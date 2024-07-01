from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for pos in POSITION:
            self.add_seg(pos)

    def add_seg(self, pos):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(pos)
        self.segments.append(snake)

    def extend(self):
        self.add_seg(self.segments[-1].position())
    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 2].ycor()
            self.segments[seg].goto(x, y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.setheading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heaing() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
