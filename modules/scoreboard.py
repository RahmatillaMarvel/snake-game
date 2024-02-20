from turtle import Turtle
import os

class Scoreboard(Turtle):
    """A class representing the scoreboard in the game."""
    
    def __init__(self) -> None:
        """Initialize the Scoreboard object.

        Creates a scoreboard object and sets the initial score to 0.
        """
        super().__init__(visible=False)
        self.color('white')
        self.score: int = 0
        if not os.path.exists('high_score.txt'):
            with open('high_score.txt', 'w') as file:
                file.write('0')
        
        with open('high_score.txt', 'r') as file:
            self.high_score = int(file.read())
        self.goto(x=0, y=270)
        self.show_score()
        



    def show_score(self) -> None:
        """Display the current score on the screen."""
        self.clear()
        self.write(f"Your score: {self.score} High score: {self.high_score}", align='center', font=('Arial', 16, 'normal'))

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as file:
                file.write(str(self.high_score))

        self.score = 0
        self.show_score()

    def increase_score(self):
        self.score += 1
        self.show_score()
