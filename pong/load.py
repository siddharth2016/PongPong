from . import util, ball, paddle, rectangle
import random

BUFFER = 10

def load_balls(win_size, radius, num_balls, paddle_pos, batch=None):
    balls = []
    for i in range(num_balls):
        ball_x, ball_y = paddle_pos
        while util.distance((ball_x, ball_y), paddle_pos) < 200:
            ball_x = random.randint(0, win_size[0]-radius-BUFFER)
            ball_y = random.randint(0, win_size[1]-radius-BUFFER)
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
