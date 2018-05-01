from vector2d import Vector2D
from vector2d import Point2D
from graphics import egi, KEY
from math import sin, cos, radians


class PractiseTarget(object):
    def __init__(self, world = None):
        self.world = world
        self.pos = Vector2D(world.cx / 2, 400)
        self.vel = Vector2D()
        self.size = 10
        self.destination = Vector2D(400, 400)
        self.speed = 50
        self.growing = True

    def calculate(self, delta):
        ''' move towards target position '''
        target_pos = self.destination
        desired_vel = (target_pos - self.pos).normalise() * 500
        return (desired_vel)

    def update(self, delta):
        self.vel = self.calculate(delta)
        self.vel.truncate(self.speed)
        self.pos += self.vel * delta
        if self.pos.x >= 400:
            self.destination = Vector2D(100, 400)
        elif self.pos.x <= 100:
            self.destination = Vector2D(400, 400)

    def on_hit(self):
        if self.size == 16:
            self.growing = False
        elif self.size == 4:
            self.growing = True
        if self.growing:
            self.size += 2
        else:
            self.size -= 2
