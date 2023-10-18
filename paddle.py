from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)





# from turtle import Turtle, Screen

# class User:

#     def __init__(self):
#         self.turtle = Turtle()
#         self.turtle.penup()
#         self.turtle.color("white")
#         self.turtle.shape("square")
#         self.turtle.speed("fastest")
#         self.turtle.shapesize(stretch_wid=5, stretch_len=1)
#         self.turtle.setx(-390)
#         self.screen = Screen()
        
#         # Register keypress events and start listening
#         self.screen.onkeypress(self.up, "Up")
#         self.screen.onkeypress(self.down, "Down")
#         self.screen.listen()

#     def up(self):
#         y = self.turtle.ycor()  # Get current y-coordinate
#         y += 40  # Increase y-coordinate
#         self.turtle.sety(y)  # Set new y-coordinate

#     def down(self):
#         y = self.turtle.ycor()  # Get current y-coordinate
#         y -= 40  # Decrease y-coordinate
#         self.turtle.sety(y)  # Set new y-coordinate

# class Computer:

#     def __init__(self):
#         self.turtle = Turtle()
#         self.turtle.penup()
#         self.turtle.color("white")
#         self.turtle.shape("square")
#         self.turtle.speed("fastest")
#         self.turtle.shapesize(stretch_wid=5, stretch_len=1)
#         self.turtle.setx(380)
#         self.screen = Screen()
        