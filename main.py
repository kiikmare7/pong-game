import time
from turtle import Screen,Turtle
from paddle import Paddle,Paddle2
from score import SCORE
from ball import Ball
screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.tracer(0)
screen.title("pond game")

# screen.listen(0)
p = Paddle()
p2 = Paddle2()
b = Ball()
s1=SCORE(-50,280)
s2=SCORE(50,280)
screen.listen()
screen.onkey(p.up,"Up")
screen.onkey(p.down,"Down")
screen.onkey(p2.up,"w")
screen.onkey(p2.down,"s")
s=Turtle()
s.color("white")
s.goto(0,300)
s.goto(0,-300)
s.hideturtle()
game = True
while game:
    screen.update()
    time.sleep(0.1)
    b.bounce()
    # if b.ycor() < 300:
    #     if b.ycor() < 300:
    #         b.bounce()
    #     else:
    #         b.bounce()
    if b.ycor() >= 280 or b.ycor() <= -280 :
        b.collition()
    if p2.head.distance(b) < 40 and b.xcor() < -340:
        print("made contact")
        b.hit()
    elif p.head.distance(b) < 40 and b.xcor() > 340:
        print("made contact")
        b.hit()
    x= b.xcor()
    if x >= 370:
        b.goto(0,0)
        s1.score_increment()
        b.bounce()
    elif x < -370:
        b.goto(0,0)
        b.bounce()
        s2.score_increment()

    # b.collition()
    # game = False


screen.exitonclick()