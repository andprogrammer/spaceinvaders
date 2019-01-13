#!/usr/bin/python3

import pygame

from utils import DATA_DIRECTORY


class Bullet(object):
    def __init__(self, pos):
        self.image = pygame.image.load(DATA_DIRECTORY + "bullet.png")
        self.sprite = self.image.get_rect()
        self.sprite.x, self.sprite.y = pos
