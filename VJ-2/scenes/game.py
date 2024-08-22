'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''

import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.jorge import Player

from elements.bug import Enemy


def gameLoop():
    ''' iniciamos los modulos de pygame'''

    pygame.init()

    ''' Creamos y editamos la ventana de pygame (escena) '''
    ''' 1.-definir el tamaño de la ventana'''
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700

    ''' 2.- crear el objeto pantalla'''
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("assets/pixelBackground.jpg").convert()

    ''' Preparamos el gameloop '''
    ''' 1.- creamos el reloj del juego'''

    clock = pygame.time.Clock()
    ''' 2.- generador de enemigos'''

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    ''' 3.- creamos la instancia de jugador'''
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    ''' hora de hacer el gameloop '''
    # variable booleana para manejar el loop
    running = True

    # loop principal del juego

    while running:

        screen.blit(background_image, [0, 0])
        
        for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
        
        for projectile in player.projectiles:
            screen.blit(projectile.surf, projectile.rect)
        
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            screenblit
            running = False
        

        pygame.display.flip()
        
        # iteramos sobre cada evento en la cola
        for event in pygame.event.get():
            # se presiono una tecla?
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
        