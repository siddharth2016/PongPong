import pyglet


class Paddle(pyglet.shapes.Rectangle):

    def __init__(self, *args, **kwargs):
        super(Paddle, self).__init__(*args, **kwargs)

    def update(self, win_size, border, dt):
        pass

    def collide_with(self, win_size, other_object, dt):
        pass