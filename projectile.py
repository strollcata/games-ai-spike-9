from vector2d import Vector2D
from vector2d import Point2D
from graphics import egi, KEY
from math import sin, cos, radians
from random import randrange


class Projectile(object):
    def __init__(self, world = None, proj_type = 'rifle'):
        self.world = world
        self.pos = Vector2D(world.cx / 2, 110)
        self.vel = Vector2D()
        self.proj_type = proj_type
        self.cur_targ_pos = Vector2D(world.target.pos.x, world.target.pos.y)
        if self.proj_type == 'rifle':
            self.speed = 500
            deviation_chance = 0
            self.leading = world.target.speed
        elif self.proj_type == 'rocket':
            self.speed = 250
            deviation_chance = 0
            self.leading = world.target.speed * 1.5
        elif self.proj_type == 'pistol':
            self.speed = 500
            deviation_chance = 6
            self.leading = world.target.speed
        elif self.proj_type == 'grenade':
            self.speed = 250
            deviation_chance = 6
            self.leading = world.target.speed * 1.5
        if randrange(10) < deviation_chance:
                deviation = randrange(-110, 130, 40)
                self.target = Vector2D(world.target.pos.x + deviation, 450)
        else:
            if world.target.destination == Vector2D(100, 400):
                if world.target.pos.x > self.pos.x:
                    if self.speed == 250:
                        self.leading *= 3
                    self.target = Vector2D(self.world.target.pos.x - self.leading / 5, world.target.pos.y + 50)
                else:
                    self.target = Vector2D(world.target.pos.x - self.leading, world.target.pos.y + 50)
            else:
                if world.target.pos.x < self.pos.x:
                    if self.speed == 250:
                        self.leading *= 3
                    self.target = Vector2D(world.target.pos.x + self.leading / 5, world.target.pos.y + 50)
                else:
                    self.target = Vector2D(world.target.pos.x + self.leading, world.target.pos.y + 50)
        self.force = Vector2D()

    def calculate(self, delta):
        ''' move towards target position '''
        target_pos = self.target
        desired_vel = (target_pos - self.pos).normalise() * 500
        return (desired_vel)

    def update(self, delta):
        force = self.calculate(delta)
        force.truncate(self.speed)
        self.vel = force
        self.pos += self.vel * delta
        target_pos = self.world.target.pos
        if ((self.pos.x >= target_pos.x - 10) and (self.pos.x <= target_pos.x + 10) and (self.pos.y > target_pos.y)):
            self.world.target.on_hit()
            self.world.projectiles.remove(self)
        elif self.pos.y > self.target.y:
            self.world.projectiles.remove(self)

    def render(self):
        egi.set_pen_color(name = 'YELLOW')
        egi.rect(self.pos.x - 5, self.pos.y - 5, self.pos.x + 5, self.pos.y + 5)
