from turtle import Turtle


class BulletManager:

    def __init__(self):
        self.bullets = []

    def create_bullet(self, position):
        new_bullet = Turtle("circle")
        new_bullet.color("white")
        new_bullet.penup()
        new_bullet.left(90)
        new_bullet.goto(position)
        print(position)
        self.bullets.append(new_bullet)

    def move(self):
        for bullet in self.bullets:
            bullet.forward(15)
