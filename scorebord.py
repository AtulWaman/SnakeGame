from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.clear()
        self.penup()
        self.goto(-50, 280)
        self.pendown()
        self.write(f"score is {self.points}",move=False,align ="left",font = ("Arial",15,"normal"))
        # self.forward(150)

    def increment(self):
        self.clear()
        self.points+=1
        self.write(f"score is {self.points}", move=False, align="left", font=("Arial", 15, "normal"))

    def gameover(self):
        self.goto(-50,0)
        self.write("GAME OVER", move=False, align="left", font=("Arial", 15, "normal"))
