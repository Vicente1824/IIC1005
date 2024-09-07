# Funcionamiento del código
## Datos útiles
- PYGame funciona en un loop, va a haber un reloj que se asegurará de ejecutar este loop ```x``` veces cada segundo.
- En cada loop se ejecutará todo lo que está dentro de un while.
- PYGame funciona principalmente en base a **eventos** para interactuar con el usuario. Todos los eventos se registrarán al principio de cada loop para ser manejados por el código.
- Si el usuario está apretando teclas al inicio de un loop, luego el loop registrará eso dentro de sus eventos. De ahí podrá hacer lo que decida, o incluso pasarle esos eventos a otras clases que verán qué hacer con eso.
- Para añadir cosas a pantallas se usarán ***sprites***. Un sprite es como un dibujo en algún punto de la pantalla. Los *sprites* tienen un *rect*, que es un rectángulo invisible que rodea todo el dibujo. El *sprite* tiene métodos que permiten moverlo, eliminarlo, etc.

## Flujo del código
1. En ```main.py``` se ejecuta el ```game_loop()```, que está dentro de ```game.py```.
2. En ```game.py``` inicio el motor de PYGame usando ```pygame.init()````.
3. En ```game.py``` creo la pantalla y le doy un fondo.
4. En ```game.py``` creo un evento personalizado, que se llama ADDENEMY. Este evento se ejecutará cada un segundo. Ojo que este evento no hace nada, ningún evento hace nada, solo se ejecutará cada un segundo y más adelante en el código se recibirá ese evento **y el código** tendrá que ver que hacer.
5. En ```game.py``` creo 2 grupos: uno que tendrá todos los *sprites* de los enemigos y otro que tendrá todos los *sprites* de todo.
6. En ```game.py``` se da inicio al loop.
7. En ```game.py``` cada vez que inicio un loop actualizo toda la pantalla con ```.blit()``` y poniéndole el fondo.
8. En ```game.py``` tengo que volver a dibujar todas las entidades en sus respectivas posiciones usando

## Archivos listos:
- ```meteor.py```: Tiene la clase ```Meteor``` que es un meteorito que se mueve a velocidad de 2 por iteración y aparece arriba.

# Features que podemos hacer
## De un punto
### PowerUps
### Habilidades especiales del jugador
### Nueva mecánica
### Menú de inicio y pausa
### Música y sonido
### ✅ Sistema de puntuación (Vicho)
Se recibe un punto por segundo que ha vivido.
### ✅ Vidas del jugador (Vicho)
El jugador parte con 3 vidas, las pierde al chocar contra meteoritos.
### Pantalla de muerte
### Nuevos enemigos
### Logros (Vicho)
### Personalización del jugador
### Entorno interactivo

## De dos puntos
### Progresión de niveles
### Boss fight (Vicho)
### Modo de juego cooperativo (Vicho)