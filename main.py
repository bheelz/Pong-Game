from screen import Display
from paddle import Paddle

screen = Display()
screen.lines()

paddle = Paddle()
screen.exit()

paddle.up()
paddle.down()