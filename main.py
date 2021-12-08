import os
import time
import sys
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

game_screen = Screen()
game_screen.setup(600, 600)
game_screen.title("Snake")
game_screen.bgcolor("black")
game_screen.tracer(0)
game_screen.listen()

scoreboard = Scoreboard()
snake = Snake()
food = Food()

game_screen.onkey(fun=snake.right, key="Right")
game_screen.onkey(fun=snake.up, key="Up")
game_screen.onkey(fun=snake.left, key="Left")
game_screen.onkey(fun=snake.down, key="Down")

game_on = True

while game_on:
    game_screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.update_high_score()
        if game_screen.textinput(title="Game over", prompt="Press Enter to play again") == "":
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            game_screen.bye()

    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.update_high_score()
            if game_screen.textinput(title="Game over", prompt="Press Enter to play again") == "":
                os.execv(sys.executable, ['python'] + sys.argv)
            else:
                game_screen.bye()

game_screen.exitonclick()
