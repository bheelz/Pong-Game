from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()




# from turtle import Turtle

# class Ball:
    
#     def __init__(self):
#         self.ball = Turtle()
#         self.ball.penup()
#         self.ball.color("white")
#         self.ball.shape("circle")
#         self.ball.speed(0)
#         self.ball.goto(0, 0)
#         self.x_move = 5
#         self.y_move = 5
    
#     def move_ball(self):
#         self.ball.setx(self.ball.xcor() + self.x_move)
#         self.ball.sety(self.ball.ycor() + self.y_move)
#         self.wall_collision()

#     def wall_collision(self):
#         if self.ball.ycor() > 290 or self.ball.ycor() < -280:
#             self.y_move *= -1
#         if self.ball.xcor() > 390 or self.ball.xcor() < -390:
#             self.x_move *= -1

#     def paddle_collision(self):
#         self.x_move *= -1

#     def distance(self, x):
#         self.ball.distance(x)