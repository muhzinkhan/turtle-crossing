from turtle import Turtle


class ScreenBorder(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-300, 300)
        self.pendown()
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)
        self.goto(-300, 300)
