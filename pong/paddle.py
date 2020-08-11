import pyglet


class Paddle(pyglet.shapes.Rectangle):

    def __init__(self, *args, **kwargs):
        super(Paddle, self).__init__(*args, **kwargs)
