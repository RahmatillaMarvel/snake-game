# Import necessary modules
from turtle import Screen
from modules.snake import Snake
from modules.food import Food
from modules.scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off screen updates

# Create snake, food, and scoreboard objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for keyboard input to control the snake
screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right, 'Right')

screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left,'a')
screen.onkey(snake.right, 'd')

# Main game loop
game_over = False
while not game_over:
    screen.update()  # Update the screen
    time.sleep(.1)  # Pause for a short time

    snake.move()  # Move the snake

    # Check if the snake has eaten the food
    if snake.head.distance(food) < 15:
        food.refresh()  # Refresh the food position
        snake.extend_tail()  # Extend the snake's tail
        scoreboard.show_score()  # Update the scoreboard
        scoreboard.increase_score()  # Increase the score

    # Check if the snake has collided with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()  # Reset the game if the snake collides with the wall
        snake.reset()  # Reset the snake
    # Check if the snake has collided with itself
    for body_part in snake.snake_parts[1:]:
        if snake.head.distance(body_part) < 10:
            scoreboard.reset()  # Reset the game if the snake collides with itself
