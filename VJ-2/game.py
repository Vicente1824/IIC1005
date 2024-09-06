"""Este módulo contiene el loop del juego."""

import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.jorge import Player

from elements.bug import Enemy

from time import sleep

"""
Mini resumen:
game_loop será un loop que está constantemente corriendo. El clock hace que hayan x iteraciones
del gameloop cada segundo. En cada iteración pueden pasar muchas cosas. Por ejemplo, si el teclado
está siendo apretado, el jugador se moverá, y quizás durante esa misma iteración, aparezca un
enemigo. Todo eso ocurre dentro de una iteración, por lo que cuando termine la iteración se
actualizará la pantalla para mostrar ambos cambios exactamente al mismo tiempo.
"""

def game_loop(screen_width: int, screen_height: int) -> None:
    """Loop principal del juego."""

    clock = pygame.time.Clock() # Crea el reloj del juego (como FPS).
    
    ''' 2.- generador de enemigos'''
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    player = Player(screen_width, screen_height) # Se crea el jugador.

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group() # Guardo todos los sprites aquí.
    all_sprites.add(player)

    running = True

    while running:

        screen.blit(background_image, [0, 0])
        
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        for projectile in player.projectiles:
            screen.blit(projectile.surf, projectile.rect)
        
        pressed_keys = pygame.key.get_pressed() # Esto da como una lista qué dice qué teclas están presionadas en este fotograma
        player.update(pressed_keys) 
        enemies.update()
        
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
            # Si se presiona cualquier tecla:
            if event.type == KEYDOWN:
                # era la tecla de escape? -> entonces terminamos
                if event.key == K_ESCAPE:
                    running = False

            # fue un click al cierre de la ventana? -> entonces terminamos
            elif event.type == QUIT:
                running = False
            
            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot(pygame.mouse.get_pos())

        pygame.sprite.groupcollide(player.projectiles, enemies, True, True)
        clock.tick(40)
        