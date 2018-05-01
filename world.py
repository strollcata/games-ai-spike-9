'''A 2d world that supports agents with steering behaviour

Created for COS30002 AI for Games by Clinton Woodward cwoodward@swin.edu.au

'''

from vector2d import Vector2D
from matrix33 import Matrix33
from graphics import egi
from target import PractiseTarget


class World(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.target = None
        self.attacker = None
        self.projectiles = []
        self.paused = True
        self.show_info = True
        self.target_size = 10
        self.growing = True
        self.left = True

    def update(self, delta):
        for projectile in self.projectiles:
            projectile.update(delta)
        self.target.update(delta)
                            
    def render(self):
        for projectile in self.projectiles:
            projectile.render()

        if self.target:
            egi.red_pen()
            egi.cross(self.target.pos, self.target.size)

        if self.attacker:
            self.attacker.render()

    def wrap_around(self, pos):
        ''' Treat world as a toroidal space. Updates parameter object pos '''
        max_x, max_y = self.cx, self.cy
        if pos.x > max_x:
            pos.x = pos.x - max_x
        elif pos.x < 0:
            pos.x = max_x - pos.x
        if pos.y > max_y:
            pos.y = pos.y - max_y
        elif pos.y < 0:
            pos.y = max_y - pos.y

    def transform_point(self, point, pos, forward, side):
        ''' Transform the given single point, using the provided position and
            direction (forward and side unit vectors) to object world space. '''
        # make a copy of original point (so we don't trash it)
        wld_pt = point.copy()
        # create a transformation matrix to perform the operations
        mat = Matrix33()
        # rotate
        mat.rotate_by_vectors_update(forward, side)
        # and translate
        mat.translate_update(pos.x, pos.y)
        # now transform all the points (vertices)
        mat.transform_vector2d(wld_pt)
        # done
        return wld_pt

    def transform_points(self, points, pos, forward, side, scale):
        ''' Transform the given list of points, using the provided position,
            direction and scale, to object world space. '''
        # make a copy of original points (so we don't trash them)
        wld_pts = [pt.copy() for pt in points]
        # create a transformation matrix to perform the operations
        mat = Matrix33()
        # scale,
        mat.scale_update(scale.x, scale.y)
        # rotate
        mat.rotate_by_vectors_update(forward, side)
        # and translate
        mat.translate_update(pos.x, pos.y)
        # now transform all the points (vertices)
        mat.transform_vector2d_list(wld_pts)
        # done
        return wld_pts
