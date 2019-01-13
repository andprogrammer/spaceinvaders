#!/usr/bin/python3
from gameobject import GameObject


class Bullet(GameObject):
    def __init__(self, pos):
        GameObject.__init__(self, "./resources/images/bullet.png")
        self.init_pos(pos)
