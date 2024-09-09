import pygame
from random import randint
from pygame.locals import RLEACCEL

from elements.projectile import Projectile

alienpng = pygame.image.load('assets/alien.png')
alienpng_scaled = pygame.transform.scale(alienpng, (100, 100))

class Alien(pygame.sprite.Sprite):
    """Clase que representa a los aliens, que se moverán hacia los lados a velocidad constante."""

    def __init__(self, screen_width: int, screen_height: int, alien_projectiles):
        """Inicializa al alien."""

        super(Alien, self).__init__()
        self.screen_width: int = screen_width # Usamos esto para recordar el ancho de la pantalla.
        self.screen_height: int = screen_height # Usamos esto para recordar el alto de la pantalla.
        self.surf = alienpng_scaled # Le asignamos una foto al dibujo.
        self.surf.set_colorkey((0, 50, 0), RLEACCEL) # Se asegura de que los colores no cambien.
        self.rect = self.surf.get_rect(center = (randint(0, screen_width), 100)) # Posición inicial.

        #Rate del disparo con y los ticks me costó mucho entenderlo aujduaowdu
        self.shoot_timer = pygame.time.get_ticks()
        self.shoot_rate = 1000
        self.alien_projectiles = alien_projectiles

    def update(self):
        """Actualiza la posición del alien."""

        self.rect.move_ip(0, 0)
        
        # Si se sale de la pantalla, se elimina:
        if self.rect.top > self.screen_height:
            self.kill() 
        
        #aquí aplicamos el rate del disparo y su reload ganggang
        current_time = pygame.time.get_ticks()
        if current_time - self.shoot_timer > self.shoot_rate:
            self.shoot ()
            self.shoot_timer = current_time

    def shoot(self):
        #definismos el shoot, la direccion y sus variantes :DDDDDDDD
        direction = (0, 1)
        projectile = Projectile(self.rect.center, direction, self.screen_width, self.screen_height)
        self.alien_projectiles.add(projectile)


