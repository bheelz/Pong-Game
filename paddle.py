from turtle import Turtle, Screen

class Paddle:

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.color("white")
        self.turtle.shape("square")
        self.turtle.speed("fastest")
        self.turtle.shapesize(stretch_wid=5, stretch_len=1)
        self.turtle.setx(-400)
        self.screen = Screen()
        
        # Register keypress events and start listening
        self.screen.onkeypress(self.up, "Up")
        self.screen.onkeypress(self.down, "Down")
        self.screen.listen()

    def up(self):
        y = self.turtle.ycor()  # Get current y-coordinate
        y += 40  # Increase y-coordinate
        self.turtle.sety(y)  # Set new y-coordinate

    def down(self):
        y = self.turtle.ycor()  # Get current y-coordinate
        y -= 40  # Decrease y-coordinate
        self.turtle.sety(y)  # Set new y-coordinate
