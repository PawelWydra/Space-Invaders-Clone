from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-40, 250)
        if self.score == 44:
            self.goto(180, 0)
            self.write(f"Well done!", align="right", font=("Courier", 40, "bold"))
        else:
            self.write(f"Enemy Left {44 - self.score}", align="right", font=("Courier", 32, "italic"))

    def point(self):
        self.score += 1
        self.update_scoreboard()