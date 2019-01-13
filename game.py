#!/usr/bin/python3

import sys
import pygame
from random import randint
from ship import Ship
from bullet import Bullet
from invader import Invader
from life import Life
from utils import WHITE_COLOR

pygame.init()


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.screen_size = self.screen_width, self.screen_height

        # Background Game
        self.background_image = pygame.image.load("resources/images/gamebackground.jpg")
        self.background_rect = self.background_image.get_rect()

        # Sound Game
        self.laser_sound = pygame.mixer.Sound('resources/sounds/laser_shot.wav')
        self.laser_sound.set_volume(0.2)

        # Labels
        self.font = pygame.font.SysFont(None, 40)
        self.game_over_label = self.font.render("Game Over", 1, WHITE_COLOR)
        self.victory_label = self.font.render("Victory", 1, WHITE_COLOR)

        # Life Bar
        self.lifes = []
        self.number_of_lifes = 3

        # Invaders
        self.invaders = []
        self.number_of_invaders = 12

        # Ship and bullets
        self.ship = Ship(self.screen_size)
        self.init_position_bullet = (self.ship.sprite.x + self.ship.sprite.width / 2, self.ship.sprite.y)
        self.bullet = Bullet(self.init_position_bullet)

        self.game_over = False
        self.victory = False
        self.escape_selected = False

        # Objects initialisation
        self.rand_invader = ()
        self.enemy_bullet = ()

        # Invaders
        self.has_already_chosen = False
        # Go down every second
        self.nasty_move_time = 1000
        # Invader shoot duration
        self.nasty_shoot_time = 1000

        self.invaders_moving = False
        self.invader_exploding = False

        # Time Variables
        self.clock = pygame.time.Clock()

        # Timer for invaders vertical moving
        self.timecount_m = 0

        # Time for invader bullet vertical moving
        self.timecount = 0

        # Init Invaders
        self.invader_init_position_x = 20
        for invader in range(self.number_of_invaders):
            self.invaders.append(Invader((self.invader_init_position_x, 70)))
            self.invader_init_position_x += 50

        # Init life bar
        self.life_init_position_x = 20

        for invader in range(self.number_of_lifes):
            self.lifes.append(Life((self.life_init_position_x, 0)))
            self.life_init_position_x += 40

    def run(self):
        game_loop = True
        while game_loop:
            self.clock.tick(50)
            self.screen.fill([0, 0, 0])
            self.screen.blit(self.background_image, self.background_rect)

            # Close the game when the red cross is clicked
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Keyboard Events
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.ship.sprite.x -= 10
                if not self.ship.shooting:
                    self.bullet.sprite.x -= 10
            elif keys[pygame.K_RIGHT]:
                self.ship.sprite.x += 10
                if not self.ship.shooting:
                    self.bullet.sprite.x += 10
            elif keys[pygame.K_SPACE]:
                self.ship.shoot = True
            elif keys[pygame.K_ESCAPE]:
                # Go back to the game menu
                game_loop = False
                self.escape_selected = True
                pygame.mixer.music.rewind()

            if self.ship.shoot:
                self.laser_sound.play()

                if self.bullet.sprite.y > 0 and not self.invader_exploding:
                    self.ship.shooting = True
                    self.bullet.sprite = self.bullet.sprite.move([0, -6])
                else:
                    self.laser_sound.fadeout(1000)
                    self.bullet.sprite.x, self.bullet.sprite.y = (self.ship.sprite.x + self.ship.sprite.width / 2, self.ship.sprite.y)
                    self.ship.shoot = False
                    self.ship.shooting = False
                    self.invader_exploding = False

            item_to_remove = None

            # Invader Colision + Vertical Movement

            # Allow slowly vertical movement
            if self.timecount_m > self.nasty_move_time:
                self.invaders_moving = True
            else:
                self.invaders_moving = False
                self.timecount_m += self.clock.get_time()

            if len(self.invaders) > 0:
                for i, invader in enumerate(self.invaders):
                    if invader.sprite.collidepoint(self.bullet.sprite.x, self.bullet.sprite.y):
                        item_to_remove = i
                        self.invader_exploding = True
                    else:
                        if self.invaders_moving and not self.game_over:
                            invader.sprite.y += 15
                            self.timecount_m = 0

                        self.screen.blit(invader.image, invader.sprite)

                    if invader.sprite.y > 370:
                        self.game_over = True

            # Remove dead invaders:
            if item_to_remove is not None:
                del self.invaders[item_to_remove]

            if not self.has_already_chosen:

                # Select random invader among survivor invaders

                if len(self.invaders) > 0 and not self.game_over:
                    if len(self.invaders) is not 1:
                        self.rand_invader = self.invaders[randint(1, len(self.invaders) - 1)]
                    else:
                        self.rand_invader = self.invaders[0]

                    self.has_already_chosen = True
                    posx = self.rand_invader.sprite.x
                    width = self.rand_invader.sprite.width
                    height = self.rand_invader.sprite.height
                    posy = self.rand_invader.sprite.y
                    self.enemy_bullet = Bullet((posx + width / 2, posy + height))
                else:
                    self.victory = True

            self.timecount += self.clock.get_time()

            # Handle the bullet shot by the random invader

            if self.timecount > self.nasty_shoot_time and self.has_already_chosen:
                self.timecount = 0
                self.has_already_chosen = False
            elif self.timecount < self.nasty_shoot_time and self.has_already_chosen:
                if self.enemy_bullet.sprite.y < self.screen_height:
                    self.enemy_bullet.sprite = self.enemy_bullet.sprite.move([0, 6])
                    self.screen.blit(self.enemy_bullet.image, self.enemy_bullet.sprite)

            # Shuttle Displaying and Colision
            if self.ship.sprite.collidepoint(self.enemy_bullet.sprite.x, self.enemy_bullet.sprite.y) and not self.ship.exploding:
                self.timecount = self.nasty_shoot_time
                self.has_already_chosen = False
                self.ship.exploding = True
            else:
                self.screen.blit(self.bullet.image, self.bullet.sprite)
                self.screen.blit(self.ship.image, self.ship.sprite)

            self.handle_life()
            self.handle_labels()

            pygame.display.flip()

            if self.game_over or self.victory:
                pygame.time.delay(2000)
                game_loop = False

    def handle_labels(self):
        if self.victory:
            victory_label_position = (self.screen_width / 2 - self.victory_label.get_rect().width / 2,
                                      self.screen_height / 2 - self.victory_label.get_rect().height / 2)
            self.screen.blit(self.victory_label, victory_label_position)
        if self.game_over:
            game_over_label_position = (self.screen_width / 2 - self.game_over_label.get_rect().width / 2,
                                        self.screen_height / 2 - self.game_over_label.get_rect().height / 2)
            self.screen.blit(self.game_over_label, game_over_label_position)

    def handle_life(self):
        if self.ship.exploding:
            self.ship.exploding = False
            if len(self.lifes) > 0:
                self.lifes.pop()
            if len(self.lifes) == 0:
                self.game_over = True
                self.ship.exploding = False

        for life in self.lifes:
            self.screen.blit(life.image, life.sprite)
