import pygame
from random import randint, choice
from pygame.locals import RLEACCEL

from elements.projectile import Projectile

alienpng = pygame.image.load('assets/alien_plus.png')
alienpng_scaled = pygame.transform.scale(alienpng, (125, 125))

class AlienPlus(pygame.sprite.Sprite):
    """Clase que representa a los aliens, que se moverán hacia los lados a velocidad constante."""

    def __init__(self, screen_width: int, screen_height: int, alien_projectiles):
        """Inicializa al alienplusplsu."""

        super(AlienPlus, self).__init__()
        self.screen_width: int = screen_width # Usamos esto para recordar el ancho de la pantalla.
        self.screen_height: int = screen_height # Usamos esto para recordar el alto de la pantalla.
        self.surf = alienpng_scaled # Le asignamos una foto al dibujo.
        self.surf.set_colorkey((0, 50, 0), RLEACCEL) # Se asegura de que los colores no cambien.
        self.rect = self.surf.get_rect(center = (randint(0, screen_width), 100)) # Posición inicial.
        #que se mueva para donde quiera el choice hace elegir entre uno u otro (lo ví en un video de youtube y lo encontré GOD)
        self.direction_x = choice([-1, 1])
        #Rate del disparo con y los ticks me costó mucho entenderlo aujduaowdu
        self.shoot_timer = pygame.time.get_ticks()
        self.shoot_rate = 500
        self.alien_projectiles = alien_projectiles

    def update(self):
        """Actualiza la posición del AlienPlus."""

        self.rect.x += self.direction_x *15 # Velocidad.
        #cambia la dirección en el borde
        if self.rect.left < 0 or self.rect.right > self.screen_width:
            self.direction_x *= -1
        
        # Si se sale de la pantalla, se elimina:
        if self.rect.top > self.screen_height:
            self.kill() 
        
        #aquí aplicamos el rate del disparo
        current_time = pygame.time.get_ticks()
        if current_time - self.shoot_timer > self.shoot_rate:
            self.shoot ()
            self.shoot_timer = current_time

    def shoot(self):
        #definismos el shoot, la direccion
        direction = (0, 1)
        projectile = Projectile(self.rect.center, direction, self.screen_width, self.screen_height)
        self.alien_projectiles.add(projectile)
