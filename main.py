import time
from turtle import Screen

from bullet import BulletManager
from paddle import Paddle
from scoreboard import Scoreboard



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.addshape('ship.gif')
screen.addshape("alien.gif")
screen.addshape("bullet.gif")

main_paddle = Paddle((0, -230))
bullet_manager = BulletManager()
scoreboard = Scoreboard()
colors = ["yellow", "green", "blue", "red"]
paddles = []
x_cor_paddles = -230
y_cor_paddles = 30
for y_cor in range(4):
    for _ in range(11):
        ### ADD IMG TO ENEMY ###
        paddle = Paddle((x_cor_paddles, y_cor_paddles), "alien.gif")
        paddle.shapesize(stretch_wid=1, stretch_len=3)
        paddle.color(colors[y_cor])
        x_cor_paddles += 45
        paddles.append(paddle)
    x_cor_paddles = -230
    y_cor_paddles += 60


screen.listen()
screen.onkey(main_paddle.go_left, "a")
screen.onkey(main_paddle.go_right, "d")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    bullet_manager.move()
    bullet_manager.create_bullet(main_paddle.position())
    for paddle in paddles:
        paddle.move()
        for bullet in bullet_manager.bullets:
            if bullet.distance(paddle) < 30:
                bullet.goto(900, 900)
                paddle.goto(800, 800)
                scoreboard.point()

screen.exitonclick()

