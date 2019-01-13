#!/usr/bin/python3

import sys
import pygame

from utils import WHITE_COLOR, DATA_DIRECTORY


class Settings:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.size = self.screen_width, self.screen_height
        self.escape_selected = False

        self.background_image = pygame.image.load(DATA_DIRECTORY + 'menusettingsbackground.jpg')
        self.background_image_rect = self.background_image.get_rect()

        self.font = pygame.font.SysFont(None, 40)
        self.esc_label = self.font.render("Esc - back", 1, WHITE_COLOR)
        self.space_label = self.font.render("Space - shoot", 1, WHITE_COLOR)
        self.left_arrow_label = self.font.render("Left arrow - move left", 1, WHITE_COLOR)
        self.right_arrow_label = self.font.render("Right arrow - move right", 1, WHITE_COLOR)

    def run(self):
        settings_loop = True
        while settings_loop:
            self.screen.blit(self.background_image, self.background_image_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                settings_loop = False
                self.escape_selected = True

            self.handle_labels()

            pygame.display.flip()

    def handle_labels(self):
        esc_label_position = (self.screen_width / 2 - self.esc_label.get_rect().width / 2,
                              self.screen_height / 2 - self.esc_label.get_rect().height / 2)
        self.screen.blit(self.esc_label, esc_label_position)
        shift = 30
        space_label_position = (self.screen_width / 2 - self.space_label.get_rect().width / 2,
                                self.screen_height / 2 - self.space_label.get_rect().height / 2 + shift)
        self.screen.blit(self.space_label, space_label_position)
        shift += 30
        left_arrow_label_position = (self.screen_width / 2 - self.left_arrow_label.get_rect().width / 2,
                                     self.screen_height / 2 - self.left_arrow_label.get_rect().height / 2 + shift)
        self.screen.blit(self.left_arrow_label, left_arrow_label_position)
        shift += 30
        right_arrow_label_position = (self.screen_width / 2 - self.right_arrow_label.get_rect().width / 2,
                                      self.screen_height / 2 - self.right_arrow_label.get_rect().height / 2 + shift)
        self.screen.blit(self.right_arrow_label, right_arrow_label_position)
