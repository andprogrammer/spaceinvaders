#!/usr/bin/python3
import pygame


class GameObject(object):
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.sprite = self.image.get_rect()

    def init_pos(self, pos):
        self.sprite.x, self.sprite.y = pos
