from screen import Display
from ball import Ball
from paddle import User, Computer

#Screen
screen = Display()
screen.lines()
screen.display_scores()

#User
user = User()
user.up()
user.down()

#Computer
computer = Computer()

#Ball
ball = Ball()

screen.exit()