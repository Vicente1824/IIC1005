import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL)
import math

from elements.projectile import Projectile


JorgePNG = pygame.image.load('assets/spaceship.png') # Aquí se guarda la foto.
JorgePNG_scaled = pygame.transform.scale(JorgePNG, (80, 80)) # La escalamos.

class Player(pygame.sprite.Sprite):
    """Clase que representa al jugador."""

    # Sprite es un dibujo. Al heredar, crearemos un dibujo que se mueve y le daremos métodos.
    def __init__(self, screen_width: int, screen_height: int):
        super(Player, self).__init__() # Heredamos la clase (PA).
        self.screen_width: int = screen_width # Usamos esto para recordar el ancho de la pantalla.
        self.screen_height: int = screen_height # Usamos esto para recordar el alto de la pantalla.
        self.surf = JorgePNG_scaled # Le asignamos una foto al dibujo.
        self.surf.set_colorkey((0, 0, 0), RLEACCEL) 
        self.rect = self.surf.get_rect(center = (screen_width / 2, screen_height - 100)) # Crea el "área" de colisión del jugador.
        self.lives = 3
        self.projectiles = pygame.sprite.Group()

    def update(self, pressed_keys):
        """Actualiza la posición del jugador."""

        # Mueve al jugador dependiendo de las teclas presionadas.
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-4, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(4, 0)
        
        # Si el rect (rectángulo del jugador) se sale de la pantalla, lo regresamos.
        if self.rect.left < 0: # Lado izquierdo del rectángulo fuera.
            self.rect.left = 0
        if self.rect.right > self.screen_width: # Lado derecho del rectángulo fuera.
            self.rect.right = self.screen_width
        if self.rect.top < 0: # Lado superior del rectángulo fuera.
            self.rect.top = 0
        if self.rect.bottom > self.screen_height: # Lado inferior del rectángulo fuera.
            self.rect.bottom = self.screen_height
        self.projectiles.update()

    
    def shoot(self, mouse_pos):
        direction = (mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery)
        length = math.hypot(*direction)
        direction = (direction[0] / length, direction[1] / length)
        projectile = Projectile(self.rect.center, direction, self.screen_width, self.screen_height)
        self.projectiles.add(projectile)