from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()

    def update_level(self):
        self.current_level += 1

    def display_level(self):
        self.goto(-230, 260)
        self.clear()
        self.write(f"Level: {self.current_level}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Courier", 50, "normal"))
        self.goto(0, -20)
        self.write(f"Level: {self.current_level}", align="center", font=FONT)


