from turtle import Turtle


class ScoreboardTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score :{self.score}", align="center", font=("Ariel", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over current score is :{self.score}", align="center", font=("Ariel", 24, "normal"))

    def update_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()
