"""Este módulo contiene el loop del juego."""

import pygame, sys, random
from pygame import Rect, draw, mouse
import time
from pygame.locals import QUIT, RLEACCEL

from elements.player import Player
from elements.meteor import Meteor
from parametros import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE, GREEN, RED

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
    background_image = pygame.image.load("assets/fondo_resized.jpeg").convert() # Fondo pantalla.

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

    #Cargamos los efectos de sonido.
    laser_sound = pygame.mixer.Sound("assets/sonidos/sonido laser.ogg")
    meteoro_sound = pygame.mixer.Sound("assets/sonidos/sonido golpe.mp3")

    pygame.mixer.music.load("assets/sonidos/musica_fondo_1.mp3")
    pygame.mixer.music.play(-1)

    #Fuentes pantalla de inicio.
    font_titulo = pygame.font.SysFont("arial", 75)
    font_inicio = pygame.font.SysFont("arial", 30)

    #Creamos los botones de inicio.
    x = (SCREEN_WIDTH // 2) - (150 // 2)
    y = (SCREEN_HEIGHT // 2) - (50 // 2)
    exit_button_inicio = Rect(x, y + 70, 150, 50) #Creamos un rectangulo para el boton salir.
    play_button = Rect(x, y + 130, 150, 50) #Creamos un rectangulo para el boton play.
    
    def pantalla_inicio():
        screen.fill(WHITE)
        text = font_titulo.render("¡GAME START!", True, BLACK) #Creamos el texto que aparecerá en la pantalla de termino. 
        posicion_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
        posicion_y = ((SCREEN_HEIGHT // 2) - (text.get_height() // 2)) - 70
        screen.blit(text, [posicion_x, posicion_y]) #Lo mostramos en pantalla.

        draw.rect(screen, BLACK, exit_button_inicio, 0)
        draw.rect(screen, BLACK, play_button, 0)
        text = font_inicio.render("EXIT", True, WHITE)
        text_two = font_inicio.render("PLAY", True, WHITE)
        screen.blit(text, (x + (exit_button_inicio.width - text.get_width()) // 2, \
                        y + (exit_button_inicio.height - text.get_height()) // 2 + 70))
        screen.blit(text_two, (x + (play_button.width - text_two.get_width()) // 2, \
                    y + (play_button.height - text_two.get_height()) // 2 + 130))
        pygame.display.update()
    
    #Creamos los botones de pausa.
    x = (SCREEN_WIDTH // 2) - (150 // 2)
    y = (SCREEN_HEIGHT // 2) - (50 // 2)
    exit_button_pausa = Rect(x, y + 70, 200, 50) #Creamos un rectangulo para el boton salir.
    continue_button = Rect(x, y + 130, 200, 50) #Creamos un rectangulo para el boton play.
    font = pygame.font.SysFont("arial", 20)


    def pause_game():
        screen.fill(WHITE)
        text = font_titulo.render("¡GAME PAUSED!", True, BLACK) #Creamos el texto que aparecerá en la pantalla de termino. 
        posicion_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
        posicion_y = ((SCREEN_HEIGHT // 2) - (text.get_height() // 2)) - 70
        screen.blit(text, [posicion_x, posicion_y]) #Lo mostramos en pantalla.

        draw.rect(screen, BLACK, exit_button_pausa, 0)
        draw.rect(screen, BLACK, continue_button, 0)
        text = font.render("EXIT", True, WHITE)
        text_two = font.render("CONTINUE", True, WHITE)
        screen.blit(text, (x + (exit_button_pausa.width - text.get_width()) // 2, \
                        y + (exit_button_pausa.height - text.get_height()) // 2 + 70))
        screen.blit(text_two, (x + (continue_button.width - text_two.get_width()) // 2, \
                    y + (continue_button.height - text_two.get_height()) // 2 + 130))
        pygame.display.update()   


    running = True
    lost = False
    game_over = False #Variable para controlar el termino del juego.
    running_screen = True #Variable para controlar la pantalla de inicio.
    paused = False

    while running:

        if running_screen:
            pantalla_inicio()

        elif paused:
            pause_game()
        
        else:

            if game_over:
                font_button = pygame.font.SysFont("arial", 20)
                x = (SCREEN_WIDTH // 2) - (150 // 2)
                y = (SCREEN_HEIGHT // 2) - (50 // 2)
                exit_button = Rect(x, y + 70, 150, 50) #Creamos un rectangulo para el boton salir.
                play_again = Rect(x, y + 130, 150, 50) #Creamos un rectangulo para el boton play again.
                screen.fill(WHITE)
                #Pintamos los botones.     
                draw.rect(screen, BLACK, exit_button, 0)
                draw.rect(screen, BLACK, play_again, 0)
                text = font_button.render("EXIT", True, WHITE)
                text_two = font_button.render("PLAY AGAIN", True, WHITE)
                screen.blit(text, (x + (exit_button.width - text.get_width()) // 2, \
                                        y + (exit_button.height - text.get_height()) // 2 + 70))
                screen.blit(text_two, (x + (play_again.width - text_two.get_width()) // 2, \
                                        y + (play_again.height - text_two.get_height()) // 2 + 130))
                font = pygame.font.SysFont("arial", 50)
                text = font.render("¡GAME OVER!", True, BLACK) #Creamos el texto que aparecerá en la pantalla de termino. 
                text_two = font.render("PUNTAJE: " + str(player.score), True, BLACK)
                posicion_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
                posicion_y = ((SCREEN_HEIGHT // 2) - (text.get_height() // 2)) - 70
                screen.blit(text, [posicion_x, posicion_y]) #Lo mostramos en pantalla.
                screen.blit(text_two, [posicion_x, posicion_y + 80])
                pygame.display.flip()

            else:

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
                    meteoro_sound.play()
                    collided_enemy.kill()
                    if player.lives == 0:
                        game_over = True #Cambiamos el estado del juego.
                        lost = True
            
            # iteramos sobre cada evento en la cola:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
            # Si se ejecutó el evento de añadir un meteorito:
            elif event.type == ADDENEMY and not game_over:
                new_enemy = Meteor(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy) # Añadimos al meteorito al grupo de los meteoritos.
                all_sprites.add(new_enemy) # Añadimos al meteorito al grupo de todos los sprites.
                # Como es un meteorito por segundo, le damos puntaje al jugador:
                player.score += 1
            
            #Control de eventos pantalla de inicio.
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and running_screen == True:
                if exit_button_inicio.collidepoint(pygame.mouse.get_pos()):
                    running_screen = False
                    running = False
                elif play_button.collidepoint(pygame.mouse.get_pos()):
                    running_screen = False
                    running = True

            #Control de eventos pantalla de pausa.
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and paused == True:
                if exit_button_pausa.collidepoint(pygame.mouse.get_pos()):
                    paused = False
                    running = False
                elif continue_button.collidepoint(pygame.mouse.get_pos()):
                    paused = False
                    running = True
                
            #Si apreto boton salir.
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and lost == True:
                if exit_button.collidepoint(pygame.mouse.get_pos()):
                    running = False
                elif play_again.collidepoint(pygame.mouse.get_pos()):
                    player.score = 0
                    player.lives = 3
                    running = True
                    game_over = False

            # Si apreté el mouse, disparo.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot(pygame.mouse.get_pos())
                laser_sound.play()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = True
            
        # Esto borra si colisionan los proyectiles con los enemigos:
        pygame.sprite.groupcollide(player.projectiles, enemies, True, True)
            
        clock.tick(40)
            
        pygame.display.flip()