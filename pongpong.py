import pyglet
from pong import rectangle, ball, paddle, load

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

        self.win_size = (WIDTH, HEIGHT)
        self.paddle_pos = (WIDTH/2-PWIDTH/2, 0)
        self.main_batch = pyglet.graphics.Batch()
        self.walls = load.load_rectangles(self.win_size, BORDER, batch=self.main_batch)
        self.balls = load.load_balls(self.win_size, RADIUS, num_balls=1, paddle_pos=self.paddle_pos, batch=self.main_batch)
        self.paddles = load.load_paddles(self.paddle_pos, PWIDTH, PHEIGHT, batch=self.main_batch)

    def on_draw(self):
        self.clear()
        self.main_batch.draw()


game_window = PongPongWindow(width=WIDTH, height=HEIGHT, caption='PongPong')
game_objects = game_window.balls + game_window.paddles


def update(dt):
    global game_objects, game_window

    for obj in game_objects:
        obj.update(game_window.win_size, BORDER, dt)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()