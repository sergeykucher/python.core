import pygame
import random

# визначаємо константу затримки кадрів
# та інші константи
FPS = 60

WIDTH_DISPLAY=800
HEIGHT_DISPLAY=600

WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 0, 255)  
ORANGE_COLOR = (255, 150, 100)

RADIUS=50

DELTA_STEP_X=random.randint(5,10)
DELTA_STEP_Y=random.randint(5,10)

COORD_X=random.randint(2*RADIUS,WIDTH_DISPLAY-2*RADIUS)
COORD_Y=random.randint(2*RADIUS,HEIGHT_DISPLAY-2*RADIUS)

# ініціалізація та створення об'єктів
pygame.init()
gameDisplay=pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))


# gameDisplay=pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("The funny ball")


run = True
clock = pygame.time.Clock()
left_and_right = False
top_and_bottom = False

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run=False

    COORD_X += DELTA_STEP_X
    COORD_Y += DELTA_STEP_Y

    if COORD_X + RADIUS > WIDTH_DISPLAY:
        left_and_right = True
    if COORD_X - 2*RADIUS > WIDTH_DISPLAY:
        COORD_X -= WIDTH_DISPLAY
        left_and_right = False
        
    if COORD_Y + RADIUS > HEIGHT_DISPLAY:
        top_and_bottom = True
    if COORD_Y - 2*RADIUS > HEIGHT_DISPLAY:
        COORD_Y -= HEIGHT_DISPLAY
        top_and_bottom = False

    gameDisplay.fill((0,0,0))

    if left_and_right and top_and_bottom:
        pygame.draw.circle(gameDisplay, BLUE_COLOR, (COORD_X-WIDTH_DISPLAY, COORD_Y-HEIGHT_DISPLAY), RADIUS)
    elif left_and_right:
        pygame.draw.circle(gameDisplay, BLUE_COLOR, (COORD_X-WIDTH_DISPLAY, COORD_Y), RADIUS)
    elif top_and_bottom:
        pygame.draw.circle(gameDisplay, BLUE_COLOR, (COORD_X, COORD_Y-HEIGHT_DISPLAY), RADIUS)

        
    pygame.draw.circle(gameDisplay, BLUE_COLOR, (COORD_X, COORD_Y), RADIUS)
    # pygame.draw.rect(gameDisplay, (255,0,0), [COORD_X, COORD_Y, WIDTH_RECTANGLE, HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)