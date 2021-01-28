# ./PongPong/pong/paddle.py

import pyglet
from pyglet.window import key
from typing import Tuple


class Paddle(pyglet.shapes.Rectangle):

    def __init__(self, *args, **kwargs):
        super(Paddle, self).__init__(*args, **kwargs)

        self.acc_left, self.acc_right = 0.0, 0.0
        self.rightx = 0
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
