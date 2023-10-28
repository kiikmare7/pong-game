from turtle import Turtle


class SCORE(Turtle):
    def __init__(self,positionx,positiony):
        super().__init__()
        self.score = -1
        self.color("white")
        self.penup()
        self.goto(positionx, positiony)
        self.write(f"score {self.score}",align="center",font=("Arial",20,"normal"))
        self.hideturtle()
        self.score_increment()

    def score_increment(self):
        self.score += 1
        self.clear()
        self.write(f"score {self.score}", align="center", font=("Arial", 20, "normal"))

