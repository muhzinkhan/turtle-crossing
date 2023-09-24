import time
import tkinter
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from screen_border import ScreenBorder
from scoreboard import Scoreboard


screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
img = tkinter.Image("photo", file="assets/turtle.png")
turtle._Screen._root.iconphoto(True, img)

screen_border = ScreenBorder()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(screen.bye, "Escape")

car_manager = CarManager()
car_manager.create()
score.display_level()

game_is_on = True

# 1 iteration = 1 frame
while game_is_on:
    time.sleep(0.01)
    screen.update()
    car_manager.move()
    for car in car_manager.car_set:
        if car.xcor() < -320:
            car_manager.reset_car(car)

    # collision
    for car in car_manager.car_set:
        if player.distance(car) < 23:
            game_is_on = False
            if player.xcor() == car.xcor():
                game_is_on = True

    if player.ycor() > 280:
        score.update_level()
        score.display_level()
        player.reset_player()
        car_manager.increases_speed()

score.game_over()

screen.exitonclick()
