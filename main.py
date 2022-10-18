import time
from turtle import Screen

from bullet import BulletManager
from ships import Ships
from scoreboard import Scoreboard



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.addshape('ship.gif')
screen.addshape("alien.gif")
screen.addshape("bullet.gif")
screen.addshape("enemy_bullet.gif")

main_ship = Ships((0, -230))
bullet_manager = BulletManager()
scoreboard = Scoreboard()
main_ship.create_army()

screen.listen()
screen.onkey(main_ship.go_left, "a")
screen.onkey(main_ship.go_right, "d")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    bullet_manager.move()
    bullet_manager.create_bullet(main_ship.position())

    for enemy in main_ship.enemies:
        enemy.move()
        bullet_manager.create_enemy_bullet(enemy.position())
        for bullet in bullet_manager.bullets:
            if bullet.distance(enemy) < 30:
                bullet.goto(900, 900)
                enemy.goto(800, 800)
                scoreboard.point()

    if scoreboard.score == 44:
        main_ship.enemies.clear()
        scoreboard.game_over()
        time.sleep(1)
        main_ship.create_army()
        scoreboard.score = 0

    for bullet in bullet_manager.alien_shots:
        if bullet.distance(main_ship) < 30:
            scoreboard.game_over()
            scoreboard.score = 0
            for enemy in main_ship.enemies:
                enemy.reset()
                enemy.goto(800, 800)
            main_ship.enemies.clear()
            main_ship.create_army()


screen.exitonclick()
