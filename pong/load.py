from . import util, ball, paddle, rectangle
import random


def load_balls(win_size, radius, batch=None):
    balls = []
    ball_x = win_size[0]/2
    ball_y = win_size[1]/2
    new_ball = ball.BallObject(x=ball_x, y=ball_y, radius=radius, batch=batch)
    new_ball.velocity_x, new_ball.velocity_y = -2, -2
    balls.append(new_ball)
    return balls


def load_paddles(paddle_pos, width, height, batch=None):
    paddles = []
    new_paddle = paddle.Paddle(x=paddle_pos[0], y=paddle_pos[1], width=width, height=height, batch=batch)
    paddles.append(new_paddle)
    return paddles


def load_rectangles(win_size, border, batch=None):
    rectangles = []
    top = rectangle.RectangleObject(x=0, y=win_size[1]-border, width=win_size[0], height=border, batch=batch)
    left = rectangle.RectangleObject(x=0, y=0, width=border, height=win_size[1], batch=batch)
    right = rectangle.RectangleObject(x=win_size[0] - border, y=0, width=border, height=win_size[1], batch=batch)
    rectangles.extend([left, top, right])
    return rectangles