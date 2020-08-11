import pyglet


class BallObject(pyglet.shapes.Circle):

    def __init__(self, *args, **kwargs):
        super(BallObject, self).__init__(*args, **kwargs)
        self.color = (255, 180, 0)