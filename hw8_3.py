#class work 8_1 no_trace
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Fly')
clock = pygame.time.Clock()
pygame.display.update()
background_position = [0, 0]
player_image = pygame.image.load("plane.png").convert()
player_image.set_colorkey(BLACK)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True            
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    screen.fill((0,0,0))#new_line

    screen.blit(player_image, [x, y])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

#class work 8_2 the_circle_folows_a_pointer
import pygame
 
FPS = 60
DISPLAY_WIDTH = 700
DISPLAY_HEIGH = 300
  
WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 70, 225)

RADIUS = 50

pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH))

pygame.display.set_caption("My second game")

clock = pygame.time.Clock()
 
while True:
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]  
    screen.fill(WHITE_COLOR)
    pygame.draw.circle(screen, BLUE_COLOR, (x, y), RADIUS)
    pygame.display.update()
    clock.tick(FPS)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

#class work 8_3 the_circle_moving_around
import pygame

FPS = 60
DISPLAY_WIDTH = 700
DISPLAY_HEIGH = 300
  
WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 70, 225)
 
RADIUS = 50
COORD_X = DISPLAY_WIDTH-RADIUS
COORD_Y = DISPLAY_HEIGH // 2

pygame.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH))
pygame.display.set_caption("My second game")
clock = pygame.time.Clock()
 
while True:

    screen.fill(WHITE_COLOR)
    for el in range(0,DISPLAY_WIDTH+RADIUS*2,1):
        pygame.draw.circle(screen, BLUE_COLOR, (COORD_X+el, COORD_Y), RADIUS)
        pygame.display.update()
        pygame.time.delay(20)
        screen.fill((255, 255, 255)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
         
    clock.tick(FPS)