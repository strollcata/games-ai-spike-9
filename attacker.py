from vector2d import Vector2D
from vector2d import Point2D
from graphics import egi, KEY
from math import sin, cos, radians
from projectile import Projectile


WEAPON_TYPES = {
    KEY._1: 'rifle',
    KEY._2: 'rocket',
    KEY._3: 'pistol',
    KEY._4: 'grenade'
}

class Attacker(object):
    def __init__(self, world = None):
        self.world = world
        self.pos = Vector2D(world.cx / 2, 100)
        self.size = 10
        self.target = self.world.target
        self.weapon = 'rifle'

    def shoot_target(self):
        self.world.projectiles.append(Projectile(self.world, self.weapon))
                
    def render(self):
        egi.blue_pen()
        egi.circle(self.pos, self.size)
