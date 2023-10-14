from turtle import Turtle
import random

class Ball:
    
    def __init__(self):
        self.ball = Turtle()
        self.ball.penup()
        self.ball.color("white")
        self.ball.shape("circle")
        self.ball.speed("fastest")
        self.move_ball()

    def move_ball(self):
        self.ball.left(30)
    
    def move_ball(self):
        self.ball.left(30)
        while True:
            self.ball.speed(0)
            self.ball.forward(30)
            self.x_coordinate = self.ball.xcor()
            self.y_coordinate = self.ball.ycor()
            if self.x_coordinate > 390 or self.x_coordinate < -390:
                # Change horizontal direction on hitting the edges
                self.ball.setheading(180 - self.ball.heading())
            if self.y_coordinate > 290 or self.y_coordinate < -280:
                # Change vertical direction on hitting the edges
                self.ball.setheading(-self.ball.heading())
