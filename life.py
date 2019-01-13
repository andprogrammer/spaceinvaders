#!/usr/bin/python3
from gameobject import GameObject


class Life(GameObject):
    def __init__(self, pos):
        GameObject.__init__(self, "./resources/images/spaceship_mini.png")
        self.init_pos(pos)
