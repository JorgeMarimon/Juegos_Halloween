import pygame

# Inicializamos pygame
pygame.init()

# Establecemos la pantalla de juego
pantalla_ancho = 1000
pantalla_alto = 400
pantalla_juego = pygame.display.set_mode((pantalla_ancho, pantalla_alto))
pygame.display.set_caption("Alimenta al Vampiro")

# Establecer FPS y reloj

# Bucle principal del juego
activo = True
while activo:
    # Verificamos si el jugador quiere quitar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            activo = False

# Cerramos el juego
pygame.quit()
