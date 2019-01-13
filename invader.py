#!/usr/bin/python3
from gameobject import GameObject


class Invader(GameObject):
    def __init__(self, pos):
        GameObject.__init__(self, "./resources/images/invader.png")
        self.init_pos(pos)
