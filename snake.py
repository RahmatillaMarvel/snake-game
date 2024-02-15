from turtle import Turtle

class Snake:
    """A class representing the snake in the game."""
    
    def __init__(self) -> None:
        """Initialize the Snake object.

        Creates a snake with initial body parts and assigns the head of the snake.
        """
        self.snake_parts: list[Turtle] = []
        self.create_snake()
        self.head: Turtle = self.snake_parts[0]


    def create_snake(self) -> None:
        """Create the initial segments of the snake.

        Creates the initial segments of the snake at predefined positions.
        """
        for position in [(0, 0), (-20, 0), (-40, 0)]:
            self.add_body_part(position)

    def add_body_part(self, position: tuple[int, int]) -> None:
        """Add a new body part to the snake.

        Args:
            position (Tuple[int, int]): The position to add the new body part.
        """
        body_part: Turtle = Turtle(shape="square")
        body_part.color("white")
        body_part.penup()
        body_part.goto(position)
        self.snake_parts.append(body_part)

    def extend_tail(self) -> None:
        """Extend the snake's tail by adding a new body part."""
        self.add_body_part(self.snake_parts[-1].position())

    def move(self) -> None:
        """Move the snake forward."""
        for i in range(len(self.snake_parts) - 1, 0, -1):
            x: float = self.snake_parts[i - 1].xcor()
            y: float = self.snake_parts[i - 1].ycor()
            self.snake_parts[i].goto(x, y)
        self.head.forward(20)

    def up(self) -> None:
        """Change the snake's direction to up."""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self) -> None:
        """Change the snake's direction to down."""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self) -> None:
        """Change the snake's direction to left."""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self) -> None:
        """Change the snake's direction to right."""
        if self.head.heading() != 180:
            self.head.setheading(0)
