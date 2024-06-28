from turtle import Turtle
import random

chance = [1,1,1,1,1,2,2]
col = []
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        self.goto(x,y)
        self.color(self.change_color())
    def change_color(self):
        random_colors = ["red", "green", "yellow", "orange", "purple", "pink", "brown", "gray", "black"]
        return random.choice(random_colors)