import pygame, random

# Inicializamos pygame
pygame.init()

# Establecemos la pantalla de juego
window_width = 1000
window_height = 400
display_surface = pygame.display.set_mode((window_width, window_height))  # Establecemos el tamaño de la pantalla
pygame.display.set_caption("Alimenta al Vampiro")  # El título de la ventana

# Establecer FPS y reloj
FPS = 60
clock = pygame.time.Clock()
delay = 1.5

# Establecer valores del juego (estableces las variables constantes que usaremos para controlar el juego)
player_starting_lives = 5
player_velocity = 10
blood_starting_velocity = 10
blood_aceleration = .5
buffer_distance = 100

score = 0
player_lives = player_starting_lives
blood_velocity = blood_starting_velocity

# Establecer colores
red = (255, 0, 0)
darkred = (80, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# Establecer fuentes
font = pygame.font.Font('faceYourFears.ttf', 32)

# Establecer texto
score_text = font.render("Puntuación: " + str(score), True, red, darkred)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)  # 10 pixeles hacia abajo y 10 pixeles hacia dentro

title_text = font.render("Alimenta al Vampiro", True, red, white)
title_rect = title_text.get_rect()
title_rect.centerx = window_width // 2
title_rect.y = 10  # Así queda alineado con la puntuación, que era 10, 10 (recuerda, el primer 10 es 10
# pixeles hacia abajo

lives_text = font.render("Vidas: " + str(player_lives), True, red, darkred)
lives_rect = lives_text.get_rect()
lives_rect.topright = (window_width - 10, 10)  # Esto primero coloca las vidas arriba a la derecha, luego le
# digo que lo haga en el ancho de pantalla menos 10, para que no se quede pegada del tod a la derecha y el siguiente
# 0 es para que está 0 pixeles hacia abajo del top

game_over_text = font.render("HAS MUERTO", True, red, darkred)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (window_width // 2, window_height // 2)

continue_text = font.render("Pulsa cualquier tecla para CONTINUAR JUGANDO", True, red, darkred)
continue_rect = continue_text.get_rect()
continue_rect.center = (window_width // 2, window_height // 2 + 32)

surprise_text = font.render("ENHORABUENA! Tu vampiro ya se ha saciado", True, red, darkred)
surprise_text2 = font.render("y ahora te mira seductoramente", True, red, darkred)
surprise_text_rect = surprise_text.get_rect()
surprise_text_rect.center = (window_width // 2 - 170, window_height // 2)
surprise_text2_rect = surprise_text.get_rect()
surprise_text2_rect.center = (window_width // 2 - 170, window_height // 2 + 50)

# Establecer sonidos y música
blood_sound = pygame.mixer.Sound("sangre_sonido.wav")

miss_sound = pygame.mixer.Sound("error_sonido.wav")
miss_sound.set_volume(1)

pygame.mixer.music.load("background_music.wav")
background_volume = 0.5
pygame.mixer.music.set_volume(background_volume)

game_over_sound = pygame.mixer.Sound("game_over_sonido.wav")
game_over_sound.set_volume(1)

surprise_sound = pygame.mixer.Sound("surprise_sonido.wav")

nico_game_over_sound = pygame.mixer.Sound("nico_derrota_sonido.wav")

nico_victory_sound = pygame.mixer.Sound("nico_hetero.wav")

# Establecer imágenes
player_image = pygame.image.load("vampiro.png")
player_rect = player_image.get_rect()
player_rect.left = 10
player_rect.centery = window_height // 2

blood_image = pygame.image.load("sangre.png")
blood_rect = blood_image.get_rect()
blood_rect.x = window_width + buffer_distance
blood_rect.y = random.randint(64, window_height - 32)  # Lo desplazamos 64 pixeles desde el top hacia abajo,
# así nunca llegará más arriba, puesto que ahí tenemos la cabecera con los textos y luego le decimos que coja el alto
# de la pantalla y que le reste 32, así si aleatoriamente la pusiese abajo del tod coincidiendo con la parte superior
# de la imagen, no desaparecería, porque hay un límite de cuanto de abajo puede ponerla. 32 exactamente por que es
# el tamaño de la imagen.

game_over_image = pygame.image.load("game_over.png")
game_over_image_rect = game_over_image.get_rect()
game_over_image_rect.center = (window_width // 2, window_height // 2)

nico_seductor_image = pygame.image.load("nico.png")
nico_seductor_image_rect = nico_seductor_image.get_rect()
nico_seductor_image_rect.center = (window_width // 2 + 250, window_height // 2)

nico_lose_image = pygame.image.load("nico_lose.png")
nico_lose_image_rect = nico_lose_image.get_rect()
nico_lose_image_rect.center = (window_width // 2 + 400, window_height // 2)

# Bucle principal del juego
pygame.mixer.music.play(-1, 0.0)  # El -1 indica un loop infinito y el 0.0 es que empieza desde el principio
running = True
while running:
    # Verificamos si el jugador quiere quitar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verificar si el jugador quiere moverse
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 64:  # 64 es hasta donde llega la cabecera desde arriba del tod hacia
        # abajo, así impedimos que el jugador se meta en la cabecera
        player_rect.y -= player_velocity  # Al quitarle la velocidad, deja de moverse, así no puede entrar en el banner.
    if keys[pygame.K_DOWN] and player_rect.bottom < window_height:
        player_rect.y += player_velocity

    # Mover la sangre
    if blood_rect.x < 0:  # Es decir, 0 es el lateral izquierdo, así que si es menor, es que el vampiro no ha atrapado
        # la sangre, por lo que se la ha perdido
        player_lives -= 1
        miss_sound.play()
        blood_rect.x = window_width + buffer_distance  # Reposicionmos la sangre en el eje x, como al principio,
        # sacándola de la pantalla un poco, para que no aparezca de la nada ya, sino que venga desde una zona donde
        # no la vemos
        blood_rect.y = random.randint(64, window_height - 32)  # Para que, nuevamente, aparezca de manera
        # aleatoria en el eje y
    else:
        # Mover la sangre
        blood_rect.x -= blood_velocity

    # Verificar las colisiones
    if player_rect.colliderect(blood_rect):
        score += 1
        blood_sound.play()
        blood_velocity += blood_aceleration
        blood_rect.x = window_width + buffer_distance  # Reposicionmos la sangre en el eje x, como al principio,
        # sacándola de la pantalla un poco, para que no aparezca de la nada ya, sino que venga desde una zona donde
        # no la vemos
        blood_rect.y = random.randint(64, window_height - 32)  # Para que, nuevamente, aparezca de manera
        # aleatoria en el eje y

    # Actualizamos el banner informativo superior
    score_text = font.render("Puntuación: " + str(score), True, red, darkred)
    lives_text = font.render("Vidas: " + str(player_lives), True, red, darkred)

    # Verificar el game over
    if player_lives == 0:

        display_surface.blit(game_over_image, game_over_image_rect)
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        display_surface.blit(nico_lose_image, nico_lose_image_rect)
        game_over_sound.play()
        pygame.display.update()
        pygame.time.delay(int(delay * 1000))
        nico_game_over_sound.play()

        # Parar el juego hasta que el jugador presione una tecla que hará empezar el juego nuevamente
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                # El jugador quiere jugar de nuevo
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = player_starting_lives
                    player_rect.y = window_height // 2
                    blood_velocity = blood_starting_velocity
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                # El jugador no quiere jugar más
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    # Insertamos la sorpresa
    if score == 60:
        display_surface.blit(nico_seductor_image, nico_seductor_image_rect)
        display_surface.blit(surprise_text, surprise_text_rect)
        display_surface.blit(surprise_text2, surprise_text2_rect)
        surprise_sound.play()
        pygame.display.update()
        pygame.mixer.music.stop()
        pygame.time.delay(int(delay * 1000))
        nico_victory_sound.play()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                # Paramos el juego, ha llegado al final
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    # Rellenamos la pantalla
    display_surface.fill(black)

    # Añadir el banner a la pantalla
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, white, (0, 64), (window_width, 64), 2)  # El primer 0 es para que empiece
    # arriba a la izquierda, luego 64 para que ocupe 64 pixeles de ancho y llegará hast el ancho de la pantalla
    # teniendo 64 pixeles de ancho también. El 2 es el grosor.

    # Añadir nuestros recursos a la pantalla
    display_surface.blit(player_image, player_rect)
    display_surface.blit(blood_image, blood_rect)

    # Actualizamos la pantalla y marcamos el reloj
    pygame.display.update()
    clock.tick(FPS)  # Así nos aseguramos que el juego vaya a la velocidad que hemos marcado en los FPS arriba

# Cerramos el juego
pygame.quit()
