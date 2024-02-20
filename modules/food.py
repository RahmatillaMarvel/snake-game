from turtle import Turtle
from random import randint

class Food(Turtle):
    """A class representing food for the snake game."""
    
    def __init__(self) -> None:
        """Initialize the Food object.

        Creates a food object with a circular shape at a random position on the screen.
        """
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('blue')
        self.speed(0)
        self.refresh()

    def refresh(self) -> None:
        """Move the food to a random position on the screen.

        Randomly selects x and y coordinates within the game boundary and moves the food to that position.
        """
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
