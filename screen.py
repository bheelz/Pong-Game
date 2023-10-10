from turtle import Screen, Turtle

LINE_COORDINATES = [20.00, 60.00, 100.00, 140.00, 180.00, 220.00, 260.00, 300.00, 340.00, 380.00, 420.00]

class Display:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.size = (1, 0,1)

    def create_turtle(self):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.color("white")
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

    def exit(self):
        self.screen.exitonclick()

