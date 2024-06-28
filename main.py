from turtle import Screen
import time
from pygame import mixer
from walls import wall

mixer.init()
import scorebord
from snake import Snake
from food import Food
from scorebord import Score

screen=Screen()
screen.bgcolor('light blue')
screen.setup(width=600,height=600)
screen.tracer(0)

wall = wall()
wall.create_wall()

snake = Snake()
food = Food()
score = Score()
game_is_on = True
mixer.music.load("Fluffing-a-Duck(chosic.com).mp3")
mixer.music.play()
while game_is_on:


    screen.update()
    screen.listen()
    # food.refresh()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    time.sleep(0.1)
    snake.move()
    #detect food
    if snake.head.distance(food) < 15:  #distance is pixls
        food.refresh()
        snake.extend()
        score.increment()     #increasing score object

    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        game_is_on = False
        mixer.music.stop()
        score.gameover()

    #detect collision with tail

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            mixer.music.stop()
            score.gameover()

screen.exitonclick()