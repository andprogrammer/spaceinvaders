#!/usr/bin/python3

import pygame
from game import Game
from menu import Menu
from settings import Settings
from utils import *

pygame.init()


def application():
    screen = pygame.display.set_mode((640, 480), 0, 32)

    pygame.display.set_caption(MENU_CAPTION)
    menu_items = (START_GAME_LABEL, GAME_SETTINGS_LABEL, QUIT_GAME_LABEL)

    menu = Menu(screen, menu_items)
    settings = Settings(screen)
    game = None

    menu_selected = True
    main_loop = True
    while main_loop:
        screen.fill(BLACK_COLOR)
        if menu_selected or game.escape_selected:
            menu.run()
            if game is not None:
                game.escape_selected = False
            settings.escape_selected = False

        if menu.start_selected:
            pygame.display.set_caption(GAME_CAPTION)
            game = Game(screen)
            game.run()
            menu.start_selected = False
            menu.quit_select = False

        if menu.settings_selected:
            settings.run()
            menu.settings_selected = False

        if menu.quit_select is True:
            main_loop = False

        pygame.display.flip()


if __name__ == "__main__":
    application()
