import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        score.update_score()


    #Detect collision with wall
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if x_cor > 290 or x_cor < -290 or y_cor > 290 or y_cor < -290:
        score.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()












screen.exitonclick()
