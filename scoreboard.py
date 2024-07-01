from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 14, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 230)
        self.hideturtle()
        self.upd_board()

    def upd_board(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT )

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT )
    def inc_score(self):
        self.score += 1
        self.clear()
        self.upd_board()
