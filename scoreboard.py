from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.level = 1
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"LEVEL: {self.level}", align = "left", font = FONT)


    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER !!!", align = "center",font = FONT )


    def increase_level_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
        # print(self.score)