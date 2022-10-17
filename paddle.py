from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position, img="ship.gif"):
        super().__init__()
        self.shape(img)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.frequency = 0

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

    def move(self):
        if self.frequency % 2:
            if self.frequency < 100:
                self.goto(self.xcor() + 1, self.ycor() - 0.5)
                self.frequency += 1
            elif self.frequency < 200:
                self.goto(self.xcor() - 1, self.ycor() - 0.5)
                self.frequency += 1
            else:
                self.frequency = 0
        else:
            self.frequency +=1


