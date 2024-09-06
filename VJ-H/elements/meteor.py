""" Este módulo contiene la clase meteor, que representará meteoritos."""

import pygame
from random import randint
from pygame.locals import RLEACCEL

BUGpng = pygame.image.load('assets/meteor.png')
BUGpng_scaled = pygame.transform.scale(BUGpng, (64, 64))

class Meteor(pygame.sprite.Sprite):
    """Clase que representa a los meteoritos, que se moverán hacia abajo a velocidad constante."""

    def __init__(self, screen_width: int, screen_height: int):
        """Inicializa al meteorito."""

        super(Meteor, self).__init__()
        self.screen_width: int = screen_width # Usamos esto para recordar el ancho de la pantalla.
        self.screen_height: int = screen_height # Usamos esto para recordar el alto de la pantalla.
        self.surf = BUGpng_scaled # Le asignamos una foto al dibujo.
        self.surf.set_colorkey((0, 0, 0), RLEACCEL) # Se asegura de que los colores no cambien.
        self.rect = self.surf.get_rect(center = (randint(0, screen_width), -100)) # Posición inicial.

    def update(self):
        """Actualiza la posición del meteorito."""

        self.rect.move_ip(0, 2)
        
        # Si se sale de la pantalla, se elimina:
        if self.rect.top > self.screen_height:
            self.kill() 