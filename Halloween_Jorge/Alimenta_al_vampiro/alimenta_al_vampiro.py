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

tricks = 0
trick_velocity = 30

# Establecer colores
red = (255, 0, 0)
darkred = (80, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 20, 147)

# Establecer fuentes
font = pygame.font.Font('faceYourFears.ttf', 32)
font_small = pygame.font.Font('faceYourFears.ttf', 20)  # Fuente más pequeño

# Establecer texto
score_text = font.render("Puntuación: " + str(score), True, red, black)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)  # 10 pixeles hacia abajo y 10 pixeles hacia dentro

title_text = font.render("Alimenta al Vampiro", True, red, darkred)
title_rect = title_text.get_rect()
title_rect.centerx = window_width // 2
title_rect.y = 10  # Así queda alineado con la puntuación, que era 10, 10 (recuerda, el primer 10 es 10
# pixeles hacia abajo

lives_text = font.render("Vidas: " + str(player_lives), True, red, black)
lives_rect = lives_text.get_rect()
lives_rect.topright = (window_width - 10, 10)  # Esto primero coloca las vidas arriba a la derecha, luego le
# digo que lo haga en el ancho de pantalla menos 10, para que no se quede pegada del tod a la derecha y el siguiente
# 0 es para que está 0 pixeles hacia abajo del top

game_over_text = font.render("HAS MUERTO", True, red, black)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (window_width // 2, window_height // 2)

continue_text = font.render("Pulsa cualquier tecla para CONTINUAR JUGANDO", True, red, black)
continue_rect = continue_text.get_rect()
continue_rect.center = (window_width // 2, window_height // 2 + 32)

surprise_text = font.render("ENHORABUENA! Tu vampiro ya se ha saciado", True, red, black)
surprise_text2 = font.render("y ahora te mira seductoramente", True, red, black)
surprise_text_rect = surprise_text.get_rect()
surprise_text_rect.center = (window_width // 2 - 170, window_height // 2)
surprise_text2_rect = surprise_text.get_rect()
surprise_text2_rect.center = (window_width // 2 - 170, window_height // 2 + 50)

trick_text = font.render("Te has comido demasiados ***** alados!", True, pink, black)
trick_text2 = font.render("No hay que abusar. Tu pierdes", True, pink, black)
trick_text_rect = trick_text.get_rect()
trick_text_rect.center = (window_width // 2 - 100, window_height // 2)
trick_text2_rect = trick_text2.get_rect()
trick_text2_rect.center = (window_width // 2 - 100, window_height // 2 + 50)

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

error_trick_sound = pygame.mixer.Sound("error_pene_sound.wav")

trick_game_over_sound = pygame.mixer.Sound("trick_game_over_sound.wav")

intro_sound = pygame.mixer.Sound("intro_sonido.wav")

# Establecer imágenes
player_image = pygame.image.load("vampiro.png")
player_rect = player_image.get_rect()
player_rect.left = 10
player_rect.centery = window_height // 2

player_image_opening = pygame.image.load("vampiro_grande.png")
player_rect_opening = player_image_opening.get_rect()

blood_image = pygame.image.load("sangre.png")
blood_image_rect = blood_image.get_rect()
blood_image_rect.x = window_width + buffer_distance
blood_image_rect.y = random.randint(64, window_height - 32)  # Lo desplazamos 64 pixeles desde el top hacia abajo,
# así nunca llegará más arriba, puesto que ahí tenemos la cabecera con los textos y luego le decimos que coja el alto
# de la pantalla y que le reste 32, así si aleatoriamente la pusiese abajo del tod coincidiendo con la parte superior
# de la imagen, no desaparecería, porque hay un límite de cuanto de abajo puede ponerla. 32 exactamente por que es
# el tamaño de la imagen.

blood_image_opening = pygame.image.load("sangre_grande.png")
blood_image_rect_opening = blood_image_opening.get_rect()

game_over_image = pygame.image.load("game_over.png")
game_over_image_rect = game_over_image.get_rect()
game_over_image_rect.center = (window_width // 2, window_height // 2)

nico_seductor_image = pygame.image.load("nico.png")
nico_seductor_image_rect = nico_seductor_image.get_rect()
nico_seductor_image_rect.center = (window_width // 2 + 250, window_height // 2)

nico_lose_image = pygame.image.load("nico_lose.png")
nico_lose_image_rect = nico_lose_image.get_rect()
nico_lose_image_rect.center = (window_width // 2 + 400, window_height // 2)

trick_image = pygame.image.load("pene_alado.png")
trick_image_rect = trick_image.get_rect()
trick_image_rect.x = window_width + buffer_distance
trick_image_rect.y = random.randint(64, window_height - 32)

trick_image_opening = pygame.image.load("pene_alado_grande.png")
trick_image_rect_opening = trick_image_opening.get_rect()

game_over_trick = pygame.image.load("fondo_trick.png")
game_over_trick_rect = game_over_trick.get_rect()
game_over_trick_rect.center = (window_width // 2, window_height // 2)

nico_empachado_image = pygame.image.load("nico_empachado.PNG")
nico_empachado_image_rect = nico_empachado_image.get_rect()
nico_empachado_image_rect.center = (window_width // 2 + 400, window_height // 2 + 100)


# Función para mostrar la pantalla de inicio
def pantalla_inicio():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Fondo dinámico (reemplaza 'nombre_del_archivo_de_fondo.gif' con el nombre de tu archivo de fondo)
        opening_screen = pygame.image.load('fondo_pantalla_inicio.png')
        opening_screen = pygame.transform.scale(opening_screen, (window_width, window_height))
        display_surface.blit(opening_screen, (0, 0))

        # Título en la parte superior
        opening_title_text = font.render("Alimenta al Vampiro", True, red)
        opening_title_rect = opening_title_text.get_rect()
        opening_title_rect.centerx = window_width // 2
        opening_title_rect.y = 10
        display_surface.blit(opening_title_text, opening_title_rect)

        # Información sobre el juego
        info_text1 = font_small.render("Intenta coger tantas gotas de sangre como sea posible!", True, red, black)
        info_text2 = font_small.render("Ojo a los ***** alados!! Si te lo comes, perderás una vida.", True, red,
                                       black)
        info_text3 = font_small.render("Tienes 5 vidas. Cuidalas bien!", True, red, black)
        info_text4 = font_small.render("A medida que avances, todo irá más rápido.", True, red, black)
        info_text5 = font_small.render("Para jugar, solo necesitas los botones de arriba y abajo", True,
                                       red, black)

        display_surface.blit(info_text1, (10, window_height // 2 - 120))
        display_surface.blit(info_text2, (10, window_height // 2 - 80))
        display_surface.blit(info_text3, (10, window_height // 2 - 40))
        display_surface.blit(info_text4, (10, window_height // 2))
        display_surface.blit(info_text5, (10, window_height // 2 + 40))

        info_text6 = font_small.render("Este eres tu --", True, red, white)
        info_text7 = font_small.render("Come esto! --", True, red, white)
        info_text8 = font_small.render("No te comas esto! --", True, red, white)

        display_surface.blit(info_text6, (window_width * 14 / 20, window_height // 2 - 120))
        display_surface.blit(info_text7, (window_width * 14 / 20, window_height // 2 - 40))
        display_surface.blit(info_text8, (window_width * 14 / 20, window_height // 2 + 40))

        # Imágenes de elementos del juego
        display_surface.blit(player_image_opening, (window_width - 90, window_height // 2 - 170))
        display_surface.blit(blood_image_opening, (window_width - 90, window_height // 2 - 60))
        display_surface.blit(trick_image_opening, (window_width - 90, window_height // 2 + 20))

        # Botón "Jugar"
        pygame.draw.rect(display_surface, red, (window_width // 2 - 100, window_height - 60, 200, 50))
        button_text = font.render("Jugar", True, white)
        display_surface.blit(button_text, (window_width // 2 - 40, window_height - 50))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if window_width // 2 - 100 + 200 > mouse[0] > window_width // 2 - 100 and window_height - 60 + 50 > mouse[
            1] > window_height - 60:
            if click[0] == 1:
                intro = False  # Comienza el juego cuando se hace clic en el botón

        intro_sound.play()

        pygame.display.update()
        clock.tick(15)


# Pantalla de inicio
pantalla_inicio()
intro_sound.stop()
# Variables adicionales para controlar los "tricks". Probablidad de que aparezca.
trick_spawn_chance = 0.003

# Bucle principal del juego
pygame.mixer.music.play(-1, 0.0)  # El -1 indica un loop infinito y el 0.0 es que empieza desde el principio
running = True

# Variable para controlar si ya hay un trick en pantalla
trick_on_screen = False

# Variable para controlar si el "trick" debe reaparecer
reappear_trick = False

while running:
    num_random = random.random()

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

    # Generar el "trick" ocasionalmente
    if not trick_on_screen:
        if num_random <= trick_spawn_chance:
            if trick_image_rect.x > 0:
                trick_image_rect.x = window_width + buffer_distance
                trick_image_rect.y = random.randint(64, window_height - 32)
                trick_on_screen = True
    else:
        if trick_image_rect.x < 0:
            trick_on_screen = False
        else:
            trick_image_rect.x -= trick_velocity

    # Mover la sangre
    if blood_image_rect.x < 0:  # Es decir, 0 es el lateral izquierdo, así que si es menor, es que el vampiro no ha
        # atrapado la sangre, por lo que se la ha perdido
        player_lives -= 1
        miss_sound.play()
        blood_image_rect.x = window_width + buffer_distance  # Reposicionmos la sangre en el eje x, como al principio,
        # sacándola de la pantalla un poco, para que no aparezca de la nada ya, sino que venga desde una zona donde
        # no la vemos
        blood_image_rect.y = random.randint(64, window_height - 32)  # Para que, nuevamente, aparezca de manera
        # aleatoria en el eje y
    else:
        # Mover la sangre
        blood_image_rect.x -= blood_velocity

    # Mover el "trick"
    if trick_on_screen:
        if trick_image_rect.x < 0:
            reappear_trick = True
            trick_on_screen = False

    # Verificar las colisiones
    if player_rect.colliderect(blood_image_rect):
        score += 1
        blood_sound.play()
        blood_velocity += blood_aceleration
        blood_image_rect.x = window_width + buffer_distance  # Reposicionmos la sangre en el eje x, como al principio,
        # sacándola de la pantalla un poco, para que no aparezca de la nada ya, sino que venga desde una zona donde
        # no la vemos
        blood_image_rect.y = random.randint(64, window_height - 32)  # Para que, nuevamente, aparezca de manera
        # aleatoria en el eje y
    # Verificar la colisión con el "trick"
    elif trick_on_screen and player_rect.colliderect(trick_image_rect):
        player_lives -= 1
        tricks += 1
        error_trick_sound.play()
        reappear_trick = True
        trick_on_screen = False  # Si colisiona con el "trick", lo quitamos de la pantalla

    # Generamos un nuevo trick si ya no hay ninguno en pantalla
    if reappear_trick:
        trick_image_rect.x = window_width + buffer_distance
        trick_image_rect.y = random.randint(64, window_height - 32)
        reappear_trick = False

    # Actualizamos el banner informativo superior
    score_text = font.render("Puntuación: " + str(score), True, red, black)
    lives_text = font.render("Vidas: " + str(player_lives), True, red, black)

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
    elif tricks == 3:
        display_surface.blit(game_over_trick, game_over_trick_rect)
        display_surface.blit(trick_text, trick_text_rect)
        display_surface.blit(trick_text2, trick_text2_rect)
        display_surface.blit(nico_empachado_image, nico_empachado_image_rect)
        trick_game_over_sound.play()
        pygame.display.update()
        # Parar el juego hasta que el jugador presione una tecla que hará empezar el juego nuevamente
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                # El jugador quiere jugar de nuevo
                if event.type == pygame.KEYDOWN:
                    tricks = 0
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
    if score == 57:
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
    display_surface.blit(blood_image, blood_image_rect)
    display_surface.blit(trick_image, trick_image_rect)

    # Actualizamos la pantalla y marcamos el reloj
    pygame.display.update()
    clock.tick(FPS)  # Así nos aseguramos que el juego vaya a la velocidad que hemos marcado en los FPS arriba

# Cerramos el juego
pygame.quit()
