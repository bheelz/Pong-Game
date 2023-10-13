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
            self.ball.speed("slow")
            self.ball.forward(30)
            self.x_coordinate = self.ball.xcor()
            self.y_coordinate = self.ball.ycor()
            if self.x_coordinate > 380:
                self.ball.left(60)
                self.ball.forward(30)
            elif self.x_coordinate < -380:
                self.ball.left(60)
                self.ball.forward(30)
            elif self.y_coordinate > 380:
                self.ball.left(60)
                self.ball.forward(30)
            elif self.y_coordinate < -370:
                self.ball.left(60)
                self.ball.forward(30)