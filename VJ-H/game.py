"""Este módulo contiene el loop del juego."""

import pygame
from pygame.locals import QUIT, RLEACCEL

from elements.player import Player
from elements.meteor import Meteor
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
"""https://docs.google.com/presentation/d/19HiltlZxWHHvsCcHTysb3Hx---TpeK4n/edit#slide=id.p1"""

def game_loop() -> None:
    """Loop principal del juego."""

    pygame.init() # Se inicia el "motor" de pygame.

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Se crea la pantalla.
    background_image = pygame.image.load("assets/pixelBackground.jpg").convert() # Fondo pantalla.

    # Aquí creo la imagen del corazón:
    heart_png = pygame.image.load('assets/heart.png') # Aquí se guarda la foto.
    heart_png_scaled = pygame.transform.scale(heart_png, (60, 60)) # La escalamos.
    sprite_heart = pygame.sprite.Sprite() # Creamos un sprite.
    sprite_heart.surf = heart_png_scaled # Le asignamos una foto al dibujo.
    sprite_heart.rect = sprite_heart.surf.get_rect(center = (60, 60)) # Lo situo en la esquina.

    # Aquí creo la imagen de la estrella:
    star_png = pygame.image.load('assets/star.png') # Aquí se guarda la foto.
    star_png_scaled = pygame.transform.scale(star_png, (120, 60)) # La escalamos.
    sprite_star = pygame.sprite.Sprite() # Creamos un sprite.
    sprite_star.surf = star_png_scaled # Le asignamos una foto al dibujo.
    sprite_star.rect = sprite_star.surf.get_rect(center = (260, 60)) # Lo situo en la esquina.

    clock = pygame.time.Clock() # Se crea el reloj del juego (como FPS).

    ADDENEMY = pygame.USEREVENT + 1 # Se crea un evento que después podré llamar.
    pygame.time.set_timer(ADDENEMY, 1000) # Se lama el evento cada un segundo.

    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT) # Se crea el jugador.

    enemies = pygame.sprite.Group() # Guardo los sprites de enemigos aquí.
    all_sprites = pygame.sprite.Group() # Guardo todos los sprites aquí.
    all_sprites.add(player) # Añado al jugador.

    running = True
    lost = False

    while running:

        """==================== REDIBUJAR TODAS LAS COSAS ===================="""
        screen.blit(background_image, [0, 0]) # Actualizo el fondo (o sino las imágenes se pegan).
        
        # La línea anterior se puso sobre las sprites, ahora las dibujo de nuevo:
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        # También se redibujan los proyectiles:
        for projectile in player.projectiles:
            screen.blit(projectile.surf, projectile.rect)
        
        # Redibujo el corazón:
        screen.blit(sprite_heart.surf, sprite_heart.rect)
        
        # Redibujo el número de vidas:
        font = pygame.font.Font(None, 50)
        text = font.render(f"{player.lives} / 3", True, (0, 0, 0))
        screen.blit(text, (120, 50))

        # Redibujo la estrella:
        screen.blit(sprite_star.surf, sprite_star.rect)

        # Redibujo el puntaje
        font = pygame.font.Font(None, 50)
        text = font.render(f"{player.score}", True, (0, 0, 0))
        screen.blit(text, (320, 50))
        
        """==================== MANEJO DE EVENTOS ===================="""
        pressed_keys = pygame.key.get_pressed() # Da como una lista de qué teclas están presionadas.
        player.update(pressed_keys) # El jugador se mueve según lo digan las teclas presionadas.
        enemies.update() # Los enemigos se mueven (aleatoriamente).
        
        # Si choco con algo, pierdo una vida.
        collided_enemy = pygame.sprite.spritecollideany(player, enemies)
        if collided_enemy:
            player.lives -= 1
            collided_enemy.kill()
            if player.lives == 0:
                running = False
                lost = True
        
        # iteramos sobre cada evento en la cola:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
            # Si se ejecutó el evento de añadir un meteorit:
            elif event.type == ADDENEMY:
                new_enemy = Meteor(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy) # Añadimos al meteorito al grupo de los meteoritos.
                all_sprites.add(new_enemy) # Añadimos al meteorito al grupo de todos los sprites.
                # Como es un meteorito por segundo, le damos puntaje al jugador:
                player.score += 1
            
            # Si apreté el mouse, disparo.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot(pygame.mouse.get_pos())
        
        # Esto borra si colisionan los proyectiles con los enemigos:
        pygame.sprite.groupcollide(player.projectiles, enemies, True, True)
        
        clock.tick(40)
        
        pygame.display.flip()