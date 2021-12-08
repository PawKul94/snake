from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.setpos(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score} / HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_high_score()
        self.update_score()

    @staticmethod
    def get_high_score():
        with open("snake_high_score.txt", mode="r") as file:
            return int(file.read())

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_score()
            with open("snake_high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
