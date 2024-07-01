from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()

    # wall
    if snake.head.xcor()>235 or snake.head.xcor()<-235 or snake.head.ycor()>235 or snake.head.ycor()<-235:
        is_on = False
        scoreboard.game_over()

    # tail
    for segm in snake.segments[1:]:
        if snake.head.distance(segm) < 10:
            is_on = False
            scoreboard.game_over()

screen.exitonclick()
