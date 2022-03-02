from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCORE_POSITION = (-280, 260)
FINISH_LINE_POSITION = (-150, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POSITION)
        self.update_scoreboard()
        self.draw_finish_line()

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.draw_finish_line()

    def game_over(self):
        self.color("black")
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.write("GAME OVER", align="center", font=FONT)

    def draw_finish_line(self):
        self.color("black")
        self.penup()
        self.goto(FINISH_LINE_POSITION)
        self.pendown()
        self.hideturtle()
        self.speed("fastest")
        self.forward(400)
