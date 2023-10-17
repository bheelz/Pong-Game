from turtle import Turtle

class Ball:
    
    def __init__(self):
        self.ball = Turtle()
        self.ball.penup()
        self.ball.color("white")
        self.ball.shape("circle")
        self.ball.speed(0)
        self.ball.goto(0, 0)
        self.x_move = 5
        self.y_move = 5
    
    def move_ball(self):
        self.ball.setx(self.ball.xcor() + self.x_move)
        self.ball.sety(self.ball.ycor() + self.y_move)
        self.check_collision()

    def check_collision(self):
        if self.ball.ycor() > 290 or self.ball.ycor() < -280:
            self.y_move *= -1
        if self.ball.xcor() > 390 or self.ball.xcor() < -390:
            self.x_move *= -1
