from turtle import Screen, Turtle

LINE_COORDINATES = [20.00, 60.00, 100.00, 140.00, 180.00, 220.00, 260.00, 300.00, 340.00, 380.00, 420.00]

class Display:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width = 800, height = 600)
        self.screen.bgcolor("black")
      
    def create_turtle(self):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.color("gray")
        self.turtle.shape("square")
        self.turtle.shapesize(1, 0.1)
        self.turtle.speed("fastest")
    
    def lines(self):
        for coordinates in LINE_COORDINATES:
            self.create_turtle()
            self.turtle.sety(coordinates)
        for coordinates in LINE_COORDINATES:
            self.create_turtle()
            self.turtle.sety(-(coordinates))

    def display_scores(self):
            self.score_turtle = Turtle()
            self.score_turtle.speed(0)
            self.score_turtle.color("white")
            self.score_turtle.penup()
            self.score_turtle.hideturtle()
            self.score_turtle.goto(100, 330)  # Position the score display
            self.score_turtle.write(f"0", align="center", font=("Freshman", 40, "normal"))
            self.score_turtle.goto(-100, 330)  # Position the computer's score display
            self.score_turtle.write(f"0", align="center", font=("Freshman", 40, "normal"))

    def exit(self):
        self.screen.exitonclick()

