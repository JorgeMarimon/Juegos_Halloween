import pygame, random

#Iniciamos pygame
pygame.init()

#Seteamos el tamaño de la ventana
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("La caza del fantasma gay")

#**Imagenes:
#Necesito un png de cazador de fantasmas con la cara de Iker Jimenez
#Varios fantasmas de colores (copiar tal cual)
#**Sonidos: (uso Leshy SFMaker)
#Sonido cuando caza el fantasma correcto
#Sonido cuando muere
#Sonido siguiente_nivel
#Sonido cuando aumenta la velocidad del juego

#Setear FPS y reloj, 60 FPS por segundo 
FPS = 60
clock = pygame.time.Clock()

#Definir clases
class Juego():
    """Clase para controlar partida"""
    def __init__(self):
        """Inicializar el objeto juego"""
        pass

    def actualiza(self):
        """Actualizar el objeto juego"""
        pass

    def panel_central(self):
        """Panel central o interfaz donde los jugadores pueden acceder a diversas partes del juego, como niveles, opciones, estadísticas, etc."""
        pass

    def colisionar(self):
        """Colisiones entre el jugador y fantasmas"""
        pass

    def nueva_ronda(self):
        """Llenar de fantasmas la pantalla"""
        pass

    def elegir_objetivo(self):
        """El jugador elige el color del fantasma y se convierte en el nuevo objetivo"""
        pass

    def pausar_juego(self):
        """Se pausa el juego"""
        pass

    def reset_juego(self):
        """Resetear el juego"""
        pass

#Un sprite es una instancia del objeto
#representa un elemento gráfico que puede ser dibujado en la pantalla y 
# puede tener propiedades como posición, velocidad, colisión, 
# reaccionar a eventos, etc.


class Jugador(pygame.sprite.Sprite):
    
    """La clase jugador que el usuario controla"""
    def __init__(self):
        """Inicializar el jugador"""
        super().__init__()
        self.image = pygame.image.load("nicoFace.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.warps = 2
        self.velocity = 8

        self.catch_sound = pygame.mixer.Sound("catch.wav")
        self.die = pygame.mixer.Sound("die.wav")
        self.warp = pygame.mixer.Sound("warp.wav")
    
    def update(self):
        """Actualiza jugador"""
        keys = pygame.key.get_pressed()

        #Mover al jugador
        if keys(pygame.K_LEFT) and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys(pygame.K_RIGHT) and self.rect.right > 0:
            self.rect.x += self.velocity
        if keys(pygame.K_UP) and self.rect.top > 0:
            self.rect.y -= self.velocity
        if keys(pygame.K_DOWN) and self.rect.bottom > 0:
            self.rect.y += self.velocity

    def warp(self):
        """Posiciona al jugador a la zona segura"""
        if self.warp > 0:
            self.warps -= 1
            self.warp_sound.play()
            self.rect.bottom = WINDOW_HEIGHT

    def reset_posicion(self):
        """Resetea posicion del jugador"""
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

class Fantasma(pygame.sprite.Sprite):
    """Clase para crear objeto fantasma"""

    def __init__(self):
        """Inicializar el fantasma"""
        pass

    def actualizar(self):
        """Actualizar el fantasma"""
        pass
    
#Crear un grupo de jugador y un objeto jugador
grupo_jugador = pygame.sprite.Group()
mi_jugador = Jugador()
grupo_jugador.add(mi_jugador)

#Crear un grupo de fantasma y un objeto fantasma
grupo_fantasma = pygame.sprite.Group()

#Crear un objeto juego
mi_juego = Juego()


#Bucle principal jugar/salir del juego
#Variable running para controlar la ejecución del bucle
running = True
while running:
    #Comprueba si el usuario quiere salir del juego
    #Se esta recorriendo una lista de eventos generados por pygame.
    for event in pygame.event.get():
        #Detecta el evento cerrar ventana/salir del juego
        if event.type == pygame.QUIT:
            running = False

    #Llenar la pantalla
    display_surface.fill((0, 0, 0))

    #Actualizar con los grupos
    grupo_jugador.update()
    grupo_jugador.draw(display_surface)

    grupo_jugador.update()
    grupo_jugador.draw(display_surface)

    #No le añado display_surface porque la clase juego ya incorpora 
    # un método para Draw
    mi_juego.update()
    mi_juego.draw()

    #Tick clock actualizacion
    pygame.display.update()
    clock.tick(FPS)

#Salir del juego
pygame.quit()


