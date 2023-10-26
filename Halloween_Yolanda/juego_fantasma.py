import pygame, random

#Iniciamos pygame
pygame.init()

#Seteamos el tamaño de la ventana
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("La caza del fantasma")

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

    #Actualizar display y reloj
    pygame.display.update()
    clock.tick(FPS)

#Salir del juego
pygame.quit()


