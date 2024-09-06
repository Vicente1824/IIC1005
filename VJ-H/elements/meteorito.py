"""
Módulo que contiene la clase meteorito.
"""

import pygame
from random import randint
from pygame.locals import RLEACCEL

BUGpng = pygame.image.load('assets/meteor.png')
BUGpng_scaled = pygame.transform.scale(BUGpng, (64, 64))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width: int, screen_height: int):
        super(Enemy, self).__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.surf = BUGpng_scaled
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # la posicion inicial es generada aleatoriamente.
        self.rect = self.surf.get_rect(center = (randint(0, screen_width), -100))

    def update(self):
        self.rect.move_ip(0, 2)
        if self.rect.top > self.screen_height:
            self.kill() # Si se sale de la pantalla, se elimina.