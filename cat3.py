import pygame
from pygame.draw import *

pygame.init()

#colors
DARK_GREEN = (51, 51, 0)
LIGHT_GREEN = (102, 153, 0)
GREEN = (0, 204, 0)
LIGHT_BLUE = (204, 255, 255)
BLUE = (102, 204, 255)
ORANGE = (255, 153, 51)
PINK = (255, 187, 153)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (194, 194, 163)

FPS = 30
screen = pygame.display.set_mode((400, 600))

# draw the floor and wall
rect(screen, DARK_GREEN, (0, 0, 400, 250))
rect(screen, LIGHT_GREEN, (0, 250, 400, 350))

# draw window
rect(screen, LIGHT_BLUE, (230, 10, 160, 200))
rect(screen, BLUE, (240, 20, 65, 50))
rect(screen, BLUE, (315, 20, 65, 50))
rect(screen, BLUE, (240, 80, 65, 120))
rect(screen, BLUE, (315, 80, 65, 120))

# draw the main part of cat using ellipse
#body
ellipse(screen, ORANGE, (50, 300, 280, 140))
ellipse(screen, BLACK, (50, 300, 280, 140), 1)
#tail

#front paw
ellipse(screen, ORANGE, (35, 345, 38, 90))
ellipse(screen, BLACK, (35, 345, 38, 90), 1)
#head
ellipse(screen, ORANGE, (25, 305, 110, 105))
ellipse(screen, BLACK, (25, 305, 110, 105), 1)
#back paw
ellipse(screen, ORANGE, (250, 350, 80, 80))
ellipse(screen, BLACK, (250, 350, 80, 80), 1)
#back paw2
ellipse(screen, ORANGE, (305, 400, 30, 80))
ellipse(screen, BLACK, (305, 400, 30, 80), 1)
#front paw2
ellipse(screen, ORANGE, (80, 405, 70, 40))
ellipse(screen, BLACK, (80, 405, 70, 40), 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()