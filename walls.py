from turtle import Turtle

class wall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("brown")
        self.hideturtle()
        self.width(20)
        self.penup()
        self.goto(-295, 0)

    def create_wall(self):
        self.pendown()
        self.left(90)
        self.forward(295)
        self.right(90)
        self.forward(235)

        self.penup()
        self.forward(105)

        self.pendown()
        self.forward(240)

        self.right(90)
        self.forward(580)

        self.right(90)
        self.forward(580)

        self.right(90)
        self.forward(300)

