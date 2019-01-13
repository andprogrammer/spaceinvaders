#!/usr/bin/python3

import pygame


class Life(object):
    def __init__(self, pos):
        self.image = pygame.image.load("./resources/images/spaceship_mini.png")
        self.sprite = self.image.get_rect()
        self.sprite.x, self.sprite.y = pos
