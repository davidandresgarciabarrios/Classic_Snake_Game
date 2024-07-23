from turtle import Screen
from snake import Snake
from food import Food
from score import Board
import time

# Define global variables:
snake = None
food = None
board = None
game_is_on = None


def reset_game():
    global snake, food, board, game_is_on
    screen.clear()
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    board = Board()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(reset_game, "Return")  # Bind the Enter key to reset the game

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Collision with food:
        if snake.head.distance(food) < 15:
            food.random_food()
            snake.longer()
            board.increase_score()

        # Collision with walls:
        if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
            game_is_on = False
            board.game_over()

        # Collision with tail:
        for segment in snake.snake_segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                board.game_over()


# Initial game setup:
screen = Screen()
screen.setup(600, 600)
reset_game()  # Start the first game

screen.exitonclick()
