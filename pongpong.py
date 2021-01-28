# ./PongPong/pongpong.py

import pyglet
from pong import rectangle, ball, paddle, load

# Variables, Considering a vertical oriented window for game
WIDTH = 600   # Game Window Width
HEIGHT = 600  # Game Window Height
BORDER = 10   # Walls Thickness/Border Thickness
RADIUS = 12   # Ball Radius
PWIDTH = 120  # Paddle Width
PHEIGHT = 15  # Paddle Height
ballspeed = (-2, -2)    # Initially ball will be falling with speed (x, y)
paddleacc = (-5, 5)   # Paddle Acceleration on both sides - left: negative acc, right: positive acc, for x-axis