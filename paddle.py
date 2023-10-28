from turtle import Turtle
# from ball import Ball
postion_paddle=[(350,0),(350,20),(350,40)]
postion_paddle2=[(-350,0),(-350,20),(-350,40)]


class Paddle:
    def __init__(self):
        self.new = []
        self.new_turtle()
        self.head=self.new[1]

    def new_turtle(self):
        for position in postion_paddle:
            news = Turtle()
            news.penup()
            news.goto(position)
            news.shape("square")
            news.color("red")
            news.speed("fastest")
            # news.hideturtle()
            self.new.append(news)
    # def hit(self)


    # def move(self):
    #     for p in range (len(postion_paddle)-1,0,-1):
    #         x = self.new[p-1].xcor()
    #         y = self.new[p-1].ycor()
    #         self.new[p].goto(x,y)
    #     self.new[0].forward(20)

    def up(self):
        for p in range (len(postion_paddle)-1,0,-1):
            x = self.new[p-1].xcor()
            y = self.new[p-1].ycor()
            self.new[p].goto(x,y)
        self.new[0].setheading(90)
        self.new[0].forward(20)

    def down(self):
        for p in range(len(postion_paddle)-1,0,-1):
            x = self.new[p-1].xcor()
            y = self.new[p-1].ycor()
            self.new[p].goto(x,y)

        self.new[0].setheading(270)
        self.new[0].forward(20)


class Paddle2:
    def __init__(self):
        self.new = []
        self.new_turtle()
        self.head=self.new[1]

    def new_turtle(self):
        for position in postion_paddle2:
            news = Turtle()
            news.penup()
            news.goto(position)
            news.shape("square")
            news.color("white")
            news.speed("fastest")
            # news.hideturtle()
            self.new.append(news)

    def up(self):
        for p in range(len(postion_paddle) - 1, 0, -1):
            x = self.new[p - 1].xcor()
            y = self.new[p - 1].ycor()
            self.new[p].goto(x, y)
        self.new[0].setheading(90)
        self.new[0].forward(20)

    def down(self):
        for p in range(len(postion_paddle) - 1, 0, -1):
            x = self.new[p - 1].xcor()
            y = self.new[p - 1].ycor()
            self.new[p].goto(x, y)
        self.new[0].setheading(270)
        self.new[0].forward(20)