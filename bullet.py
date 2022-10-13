from turtle import Turtle


class BulletManager:

    def __init__(self):
        self.bullets = []
        self.count = 0

    def create_bullet(self, position):
        if self.count % 2 == 0:
            new_bullet = Turtle("square")
            new_bullet.color("red")
            new_bullet.penup()
            new_bullet.left(90)
            new_bullet.goto(position[0], position[1]+60)
            self.bullets.append(new_bullet)
        self.count += 1

    def move(self):
        for bullet in self.bullets:
            bullet.forward(25)

