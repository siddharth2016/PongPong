import pyglet
from pong import rectangle, ball, paddle

#Variables
WIDTH = 600
HEIGHT = 600
BORDER = 10
RADIUS = 12
PWIDTH = 120
PHEIGHT = 15

class PongPongWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(PongPongWindow, self).__init__(*args, **kwargs)

        self.main_batch = pyglet.graphics.Batch()
        self.top_rect = rectangle.RectangleObject(x=0, y=HEIGHT-BORDER, width=WIDTH, height=BORDER, batch=self.main_batch)
        self.left_rect = rectangle.RectangleObject(x=0, y=0, width=BORDER, height=HEIGHT, batch=self.main_batch)
        self.right_rect = rectangle.RectangleObject(x=WIDTH-BORDER, y=0, width=BORDER, height=HEIGHT, batch=self.main_batch)
        self.ball = ball.BallObject(x=WIDTH/2, y=HEIGHT/2, radius=RADIUS, batch=self.main_batch)
        self.paddle = paddle.Paddle(x=WIDTH/2-PWIDTH/2, y=0, width=PWIDTH, height=PHEIGHT, batch=self.main_batch)

    def on_draw(self):
        self.clear()
        self.main_batch.draw()


if __name__ == '__main__':
    game_window = PongPongWindow(width=WIDTH, height=HEIGHT, caption='PongPong')
    pyglet.app.run()