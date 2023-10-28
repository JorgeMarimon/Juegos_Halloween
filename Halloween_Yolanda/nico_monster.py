import pygame, random

#Initialize pygame
pygame.init()

#Set display window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Nico Monster")

#Set FPS and Clock
#60 segundos
FPS = 60
clock = pygame.time.Clock()

#Clases
class Game():
    """Clase para control del juego"""
    def __init__(self, player, monster_group):
        """Inicializar variables del juego"""
        #Set valores juego: puntualición se inicia en cero y ronda en 0
        self.score = 0
        self.round_number = 0

        self.round_time = 0
        self.frame_count = 0

        self.player = player
        self.monster_group = monster_group

        #Set musica
        self.next_level_sound = pygame.mixer.Sound("next_level.wav")

        #Set letra
        self.font = pygame.font.Font("leadcoat.ttf", 30)

        #Set imagenes
        blue_image = pygame.image.load("blue_monster.png")
        green_image = pygame.image.load("green_monster.png")
        purple_image = pygame.image.load("purple_monster.png")
        yellow_image = pygame.image.load("yellow_monster.png")

        #Lista para mostrar una imagen de monstruo segun el atributo monster_type int 0 -> blue, 1 -> green, 2 -> purple, 3 -> yellow
        self.target_monster_images = [blue_image, green_image, purple_image, yellow_image]

        self.target_monster_type = random.randint(0,3)

        #Se asigna la imagen del monstruo correspondiente al tipo seleccionado aleatoriamente.
        # La imagen se obtiene de la lista target_monster_images
        # usando el valor almacenado en self.target_monster_type.
        # La imagen seleccionada se almacena en la variable self.target_monster_image.
        self.target_monster_image = self.target_monster_images[self.target_monster_type]

        #Con el get_rect() renderizamos la imagen aleatoria anterior self.target_monster_image
        # y se almacena en la variable self.target_monster_rect
        self.target_monster_rect = self.target_monster_image.get_rect()

        #Posiciona la imagen en el centro del eje horizontal
        self.target_monster_rect.centerx = WINDOW_WIDTH//2
        #A 30px del top de la ventana
        self.target_monster_rect.top = 30

    def update(self):
        """Actualiza el objeto juego"""
        #Código para medir el tiempo en segundos en un juego
        #Resetea en 0 de nuevo
        self.frame_count += 1
        if self.frame_count == FPS:
            self.round_time += 1
            self.frame_count = 0

        #Check de colisiones de objetos
        self.check_collisions()

    def draw(self):
        """Interfaz del juego"""
        #Set colores
        WHITE = (255, 255, 255)
        BLUE = (20, 176, 235)
        GREEN = (87, 201, 47)
        PURPLE = (226, 73, 243)
        YELLOW = (243, 157, 20)

        #Añado colores de monstruos a la lista (matches target_monster_images)
        colors = [BLUE, GREEN, PURPLE, YELLOW]

        #Set textos
        catch_text = self.font.render("Objetivo", True, WHITE)
        catch_rect = catch_text.get_rect()
        catch_rect.centerx = WINDOW_WIDTH//2
        catch_rect.top = 5

        score_text = self.font.render("Puntos: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (5, 5)

        lives_text = self.font.render("Vidas: " + str(self.player.lives), True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topleft = (5, 35)

        round_text = self.font.render("Ronda: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (5, 65)

        time_text = self.font.render("Tiempo Ronda: " + str(self.round_time), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 10, 5)

        #Usamos el objeto player creado en la clase Game
        warp_text = self.font.render("Velocidad: " + str(self.player.warps), True, WHITE)
        warp_rect = warp_text.get_rect()
        warp_rect.topright = (WINDOW_WIDTH - 10, 35)

        #Blit la interfaz, renderizar lo anterior en la pantalla
        display_surface.blit(catch_text, catch_rect)
        display_surface.blit(score_text, score_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(lives_text, lives_rect)
        display_surface.blit(time_text, time_rect)
        display_surface.blit(warp_text, warp_rect)
        display_surface.blit(self.target_monster_image, self.target_monster_rect)

        #Dibujamos el rectangulo que rodea el monstruo, el color de la línea será el color del monstruo
        pygame.draw.rect(display_surface, colors[self.target_monster_type], (WINDOW_WIDTH//2 - 32, 30, 64, 64), 2)
        #Dibujamos el rectangulo de la zona de juego, el color de la línea será el color del monstruo tambien
        pygame.draw.rect(display_surface, colors[self.target_monster_type], (0, 100, WINDOW_WIDTH, WINDOW_HEIGHT-200), 4)

    def check_collisions(self):
        """Check colisiones entre jugador y monstruo de color especifico"""
        #Check monster.type si coincide con el color target
        collided_monster = pygame.sprite.spritecollideany(self.player, self.monster_group)

        #Si colisiona con un monstruo
        if collided_monster:

            #Ha colisionado con el monstruo correcto (target)
            if collided_monster.type == self.target_monster_type:
                self.score += 100*self.round_number

                #Elimina el monstruo de la pantalla
                collided_monster.remove(self.monster_group)

                #Si hay más monstruos en la pantalla
                #Selecciona nuevo target
                if (self.monster_group):
                    self.player.catch_sound.play()
                    self.choose_new_target()
                else:
                    #Empieza ronda nueva y se resetea el juego
                    self.player.reset()
                    self.start_new_round()

            #Si captura el monstruo incorrecto
            else:
                self.player.die_sound.play()
                self.player.lives -= 1
                #Check game over
                if self.player.lives <= 0:
                    self.pause_game("Puntuación final: " + str(self.score), "Pulsa 'Enter' para jugar de nuevo")
                    self.reset_game()
                self.player.reset()


    def start_new_round(self):
        """Llenar pantalla con monstruos"""
        #Puntuación extra si termina la ronda más rápido
        self.score += int(10000*self.round_number/(1 + self.round_time))

        #Resetea valores ronda
        self.round_time = 0
        self.frame_count = 0
        self.round_number += 1
        self.player.warps += 1

        #Limpiamos monstruos de la pantalla al hacer el reset de nueva ronda
        for monster in self.monster_group:
            self.monster_group.remove(monster)

        #Añadimos los cuatro monstruos al grupo con pòsicion random
        #Si vamos a la clase Monstruo le tenemos que pasar:
        #self, x, y, image (esto es una lista), monstrer_type (coincide con la posicion de la lista de imagenes)
        for i in range(self.round_number):
            self.monster_group.add(Monster(random.randint(0, WINDOW_WIDTH - 64), random.randint(100, WINDOW_HEIGHT-164), self.target_monster_images[0], 0))
            self.monster_group.add(Monster(random.randint(0, WINDOW_WIDTH - 64), random.randint(100, WINDOW_HEIGHT-164), self.target_monster_images[1], 1))
            self.monster_group.add(Monster(random.randint(0, WINDOW_WIDTH - 64), random.randint(100, WINDOW_HEIGHT-164), self.target_monster_images[2], 2))
            self.monster_group.add(Monster(random.randint(0, WINDOW_WIDTH - 64), random.randint(100, WINDOW_HEIGHT-164), self.target_monster_images[3], 3))

        #Elige un nuevo objetivo de monstruo
        self.choose_new_target()

        #Sonido que indica nuevo nivel
        self.next_level_sound.play()

    def choose_new_target(self):
        """Choose a new target monster for the player"""
        target_monster = random.choice(self.monster_group.sprites())
        self.target_monster_type = target_monster.type
        self.target_monster_image = target_monster.image

    def pause_game(self, main_text, sub_text):
        """Pause the game"""
        global running

        #Set color
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        #Create the main pause text
        main_text = self.font.render(main_text, True, WHITE)
        main_rect = main_text.get_rect()
        main_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

        #Create the sub pause text
        sub_text = self.font.render(sub_text, True, WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

        #Display the pause text
        display_surface.fill(BLACK)
        display_surface.blit(main_text, main_rect)
        display_surface.blit(sub_text, sub_rect)
        pygame.display.update()

        #Pause the game
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False


    def reset_game(self):
        """Reset the game"""
        self.score = 0
        self.round_number = 0

        self.player.lives = 5
        self.player.warps = 2
        self.player.reset()

        self.start_new_round()


class Player(pygame.sprite.Sprite):
    """A player class that the user can control"""
    def __init__(self):
        """Initialize the player"""
        super().__init__()
        self.image = pygame.image.load("nico.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.warps = 2
        self.velocity = 8

        self.catch_sound = pygame.mixer.Sound("catch.wav")
        self.die_sound = pygame.mixer.Sound("die.wav")
        self.warp_sound = pygame.mixer.Sound("warp.wav")


    def update(self):
        """Update the player"""
        keys = pygame.key.get_pressed()

        #Move the player within the bounds of the screen
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT - 100:
            self.rect.y += self.velocity


    def warp(self):
        """Warp the player to the bottom 'safe zone'"""
        if self.warps > 0:
            self.warps -= 1
            self.warp_sound.play()
            self.rect.bottom = WINDOW_HEIGHT


    def reset(self):
        """Resets the players position"""
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT


class Monster(pygame.sprite.Sprite):
    """Clase para crear una imagen de monstruo"""
    #Le paso las cordenadas, el parametro imagen y type
    def __init__(self, x, y, image, monster_type):
        """Inicializo el monstruo"""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        #Monster type (int 0 -> blue, 1 -> green, 2 -> purple, 3 -> yellow)
        self.type = monster_type

        #Set random para el movimiento
        #-1 se mueve hacia la izquierda y 1 se mueve a la derecha
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.velocity = random.randint(1, 5)

    def update(self):
        """Actualizar la posición del objeto en función de las variables dx, dy, y velocity"""
        self.rect.x += self.dx*self.velocity
        self.rect.y += self.dy*self.velocity

        #Rebote del monstruo en los límites de la pantalla horizontal
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            #Invierte la dirección del movimiento en el eje x del monstruo *-1
            self.dx = -1*self.dx
        # Rebote del monstruo en los límites de la pantalla vertical
        if self.rect.top <= 100 or self.rect.bottom >= WINDOW_HEIGHT - 100:
            # Invierte la dirección del movimiento en el eje y del monstruo *-1
            self.dy = -1*self.dy


#Crear el objeto grupo de jugador y mi objeto jugador
my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)

#Crear el objeto de monstruos
my_monster_group = pygame.sprite.Group()

#Instancio objeto juego con mi jugador y el grupo de monstruos
#Llamno a las funciones de la clase Game
my_game = Game(my_player, my_monster_group)
my_game.pause_game("Nico Monster", "Press 'Enter' to begin")
my_game.start_new_round()

#Bucle juego principal
running = True
while running:
    #Check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Player wants to warp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.warp()

    #Fill the display
    display_surface.fill((0, 0, 0))

    #Update and draw sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_monster_group.update()
    my_monster_group.draw(display_surface)

    #Update and draw the Game
    my_game.update()
    my_game.draw()

    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()