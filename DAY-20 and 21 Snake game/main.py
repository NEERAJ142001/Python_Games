# importing turtle
from turtle import Screen

from ScoreboardTurtle import ScoreboardTurtle

# import time library to make a delay
import time

from foodturtle import FoodTurtle
# import snake from Snake class
from snaketurtle import SnakeTurtle

# making a screen and it's attributes
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("yellow")

# animations off
screen.tracer(0)

# calling a Snake class,food class and Scoreboard class
snake = SnakeTurtle()
food = FoodTurtle()
score = ScoreboardTurtle()

# creating listener
screen.listen()

# onkey function
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:

    # it used when tracer is off
    screen.update()
    # 0.1 sec take to move
    time.sleep(0.1)
    # to move the snake
    snake.move()

    # detect collision with food 1 * 10 size of food, so we put 15 as a maximum distance from the food
    if snake.head.distance(food) < 15:
        # if snake reach near the food then we have to refresh the food means setting at random position
        food.refresh()
        # when snake eat the food then we to update the score
        score.update_score()
        # increase the size
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 290 or \
            snake.head.xcor() < -290 or \
            snake.head.ycor() > 260 or \
            snake.head.ycor() < -290:
        # game over and display the score
        score.game_over()
        break

    # detect collision with tail
    for x in snake.snake_maker:
        if x == snake.head:
            pass
        elif snake.head.distance(x) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
