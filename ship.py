#!/usr/bin/python3

import pygame

from utils import DATA_DIRECTORY


class Ship(object):
    def __init__(self, screen_size):
        self.image = pygame.image.load(DATA_DIRECTORY + "ship.png")
        self.sprite = self.image.get_rect()
        if 2 == len(screen_size):
            pos = (screen_size[0] / 2 - self.sprite.width / 2, screen_size[1] - self.sprite.height)
            self.sprite.x, self.sprite.y = pos
        else:
            self.sprite.x, self.sprite.y = (0, 0)
        self.exploding = False
        self.shoot = False
        self.shooting = False
