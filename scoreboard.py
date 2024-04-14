from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def gameover(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=("Arial", 30, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()