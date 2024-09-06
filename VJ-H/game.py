"""Este módulo contiene el loop del juego."""

import pygame
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.jorge import Player
from elements.meteorito import Enemy
from parametros import SCREEN_WIDTH, SCREEN_HEIGHT

from time import sleep

"""
Mini resumen:
game_loop será un loop que está constantemente corriendo. El clock hace que hayan x iteraciones
del gameloop cada segundo. En cada iteración pueden pasar muchas cosas. Por ejemplo, si el teclado
está siendo apretado, el jugador se moverá, y quizás durante esa misma iteración, aparezca un
enemigo. Todo eso ocurre dentro de una iteración, por lo que cuando termine la iteración se
actualizará la pantalla para mostrar ambos cambios exactamente al mismo tiempo.
"""

def game_loop() -> None:
    """Loop principal del juego."""

    pygame.init() # Se inicia el "motor" de pygame.

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Se crea la pantalla.
    background_image = pygame.image.load("assets/pixelBackground.jpg").convert() # Fondo pantalla.

    clock = pygame.time.Clock() # Se crea el reloj del juego (como FPS).

    ''' 2.- generador de enemigos'''
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT) # Se crea el jugador.

    enemies = pygame.sprite.Group() # Guardo los sprites de enemigos aquí.
    all_sprites = pygame.sprite.Group() # Guardo todos los sprites aquí.
    all_sprites.add(player) # Añado al jugador.

    running = True

    while running:
        screen.blit(background_image, [0, 0]) # Actualizo el fondo (o sino las imágenes se pegan).
        
        # La línea anterior borró las sprites, ahora las dibujo de nuevo:
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        # También se redibujan los proyectiles:
        for projectile in player.projectiles:
            screen.blit(projectile.surf, projectile.rect)
        
        pressed_keys = pygame.key.get_pressed() # Da como una lista de qué teclas están presionadas.
        player.update(pressed_keys) # El jugador se mueve según lo digan las teclas presionadas.
        enemies.update() # Los enemigos se mueven (aleatoriamente).
        
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            screen = pygame.display.set_mode((400, 640))
            background_image = pygame.image.load("assets/finalImage.jpeg").convert()
            font = pygame.font.Font(None, 50)
            text = font.render("PERDISTE.", True, (0, 255, 0))
            screen.blit(background_image, [0, 0])
            screen.blit(text, [200, 320])
            pygame.display.flip()
            sleep(5)
            running = False
        

        pygame.display.flip()
        
        # iteramos sobre cada evento en la cola
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy) # Añadimos al enemigo al grupo de los enemigos.
                all_sprites.add(new_enemy) # Añadimos al enemigo al grupo de todos los sprites.
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot(pygame.mouse.get_pos())

        pygame.sprite.groupcollide(player.projectiles, enemies, True, True)
        clock.tick(40)
        