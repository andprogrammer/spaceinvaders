#!/usr/bin/python3

import sys
import pygame

from utils import *

pygame.init()


class Menu:
    def __init__(self, screen, menu_items, font=None, font_size=80, font_color=YELLOW_COLOR):
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.background_image = pygame.image.load(DATA_DIRECTORY + 'menubackground.jpg')
        self.background_image_rect = self.background_image.get_rect()

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(font, font_size)

        self.start_selected = False
        self.settings_selected = False
        self.quit_select = False

        self.index_selected = 0
        self.current_item = ()
        self.menu_items = []

        for index, item in enumerate(menu_items):
            label = self.font.render(item, 1, font_color)

            width = label.get_rect().width
            height = label.get_rect().height

            labels_position_x = (self.screen_width / 2) - (width / 2)

            total_height = len(menu_items) * height

            position_y = (self.screen_height / 2) - (total_height / 2) + (index * height)
            self.menu_items.append([item, label, (width, height), (labels_position_x, position_y)])

    def run(self):
        menu_loop = True
        while menu_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_loop = False
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        for index, item in enumerate(self.menu_items):
                            if self.current_item[0] == item[0]:
                                if self.index_selected > 0:
                                    self.index_selected -= 1
                    if event.key == pygame.K_DOWN:
                        for index, item in enumerate(self.menu_items):
                            if self.current_item[0] == item[0]:
                                if self.index_selected < (len(self.menu_items) - 1):
                                    self.index_selected += 1
                    if event.key == pygame.K_RETURN:
                        if len(self.current_item) > 0:
                            if self.current_item[0] == START_GAME_LABEL:
                                self.start_selected = True
                            elif self.current_item[0] == GAME_SETTINGS_LABEL:
                                self.settings_selected = True
                            elif self.current_item[0] == QUIT_GAME_LABEL:
                                self.quit_select = True

                            pygame.mixer.music.fadeout(1000)
                            menu_loop = False

            self.current_item = self.menu_items[self.index_selected]

            if not self.start_selected or not self.settings_selected:
                self.screen.blit(self.background_image, self.background_image_rect)

                for name, label, (width, height), (posx, posy) in self.menu_items:
                    self.screen.blit(label, (posx, posy))

                name, label, (width, height), (posx, posy) = self.current_item

                pygame.draw.rect(self.screen, WHITE_COLOR, [posx, posy, width, height], 2)

            pygame.display.flip()
