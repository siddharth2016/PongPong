import pyglet


class BallObject(pyglet.shapes.Circle):

    def __init__(self, *args, **kwargs):
        super(BallObject, self).__init__(*args, **kwargs)
        self.color = (255, 180, 0)
        self.velocity_x, self.velocity_y = 0.0, 0.0

    def update(self, win_size, border):
        newx = self.x + self.velocity_x
        newy = self.y + self.velocity_y

        if newx < border + self.radius or newx > win_size[0] - border - self.radius:
            self.velocity_x = -self.velocity_x
        elif newy > win_size[1] - border - self.radius:
            self.velocity_y = -self.velocity_y
        else:
            self.x = newx
            self.y = newy
