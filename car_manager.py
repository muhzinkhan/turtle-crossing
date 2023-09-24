from turtle import Turtle
import random

CAR_LIMITS = 18
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_POSITION = (random.randint(-300, 300), random.randint(-250, 300))
RESET_POSITION = (300, random.randint(-250, 300))
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 2


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_set = []
        self.moving_distance = STARTING_MOVE_DISTANCE

    def create(self):
        for i in range(1, CAR_LIMITS):
            i = Turtle()
            i.color(COLORS[random.randint(0, 5)])
            i.shape("square")
            i.shapesize(stretch_len=2)
            i.penup()
            i.setheading(180)
            i.goto(random.randint(-300, 300), random.randint(-250, 240))
            self.car_set.append(i)

    def move(self):
        for car in self.car_set:
            car.forward(self.moving_distance)

    def reset_car(self, car_in_consideration):
        car_in_consideration.goto(320, random.randint(-240, 240))

    def increases_speed(self):
        self.moving_distance += MOVE_INCREMENT
