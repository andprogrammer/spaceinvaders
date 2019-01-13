#!/usr/bin/python3
from gameobject import GameObject


class Spaceship(GameObject):
    def __init__(self, screen_size):
        GameObject.__init__(self, "./resources/images/spaceship.png")
        pos = (screen_size[0] / 2 - self.sprite.width / 2, screen_size[1] - self.sprite.height)
        self.init_pos(pos)
        self.exploding = False
        self.shoot = False
        self.shooting = False
