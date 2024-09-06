""""Este es el módulo a ejecutar del juego."""

import pygame

from game import game_loop
from parametros import SCREEN_WIDTH, SCREEN_HEIGHT

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("assets/pixelBackground.jpg").convert()
    game_loop(SCREEN_WIDTH, SCREEN_HEIGHT)