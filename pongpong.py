import pyglet
from pong import rectangle, ball, paddle, load

#Variables, Considering a vertical oriented window for game
WIDTH = 600
HEIGHT = 600
BORDER = 10
RADIUS = 12
PWIDTH = 120 #Paddle Width
PHEIGHT = 15 #Paddle Height


class PongPongWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(PongPongWindow, self).__init__(*args, **kwargs)

        self.win_size = (WIDTH, HEIGHT)
        self.paddle_pos = (WIDTH/2-PWIDTH/2, 0)
        self.main_batch = pyglet.graphics.Batch()
        self.walls = load.load_rectangles(self.win_size, BORDER, batch=self.main_batch)
        self.balls = load.load_balls(self.win_size, RADIUS, batch=self.main_batch)
        self.paddles = load.load_paddles(self.paddle_pos, PWIDTH, PHEIGHT, batch=self.main_batch)

    def on_draw(self):
        self.clear()
        self.main_batch.draw()


game_window = PongPongWindow(width=WIDTH, height=HEIGHT, caption='PongPong')
game_objects = game_window.balls + game_window.paddles


def update(dt):
    global game_objects, game_window

    for obj1 in game_objects:
        for obj2 in game_objects:
            if obj1 is obj2:
                continue
            obj1.update(game_window.win_size, BORDER, obj2)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()