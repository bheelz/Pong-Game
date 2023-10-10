from screen import Display
from paddle import User, Computer

screen = Display()
screen.lines()

user = User()
user.up()
user.down()

computer = Computer()

screen.exit()