from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position, img="ship.gif"):
        super().__init__()
        self.shape(img)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def go_right(self):
        if self.xcor() >= 360:
            return
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def go_left(self):
        if self.xcor() <= -360:
            return
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

