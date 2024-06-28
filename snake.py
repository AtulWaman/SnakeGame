from turtle import Screen,Turtle
INIT_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for pos in INIT_POS:
            self.addseg(pos)

    def addseg(self,position):
        snake = Turtle('circle')
        snake.penup()
        snake.goto(position)
        if len(self.segments) == 0:
            snake.color('green')
        else:
            snake.color('lime green')
        self.segments.append(snake)

    def extend(self):
        self.addseg(self.segments[-1].position())
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)