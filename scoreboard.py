from turtle import Turtle

class Scoreboard(Turtle):
    """A class representing the scoreboard in the game."""
    
    def __init__(self) -> None:
        """Initialize the Scoreboard object.

        Creates a scoreboard object and sets the initial score to 0.
        """
        super().__init__(visible=False)
        self.color('white')
        self.score: int = 0
        self.goto(x=0, y=270)
        self.show_score()

    def show_score(self) -> None:
        """Display the current score on the screen."""
        self.clear()
        self.write(f"Your score: {self.score}", align='center', font=('Arial', 16, 'normal'))
        self.score += 1

    def game_over(self) -> None:
        """Display 'Game Over' message on the screen."""
        self.goto(0, 0)
        self.write(f"Game over", align='center', font=('Arial', 24, 'normal'))
