import pygame
from pygame.draw import *
import numpy as np

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
# create surfaces and screen
screen = pygame.display.set_mode((400, 600))
surf = pygame.Surface((120, 50))
surf2 = pygame.Surface((10, 5))
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
#tail
rect(surf, LIGHT_GREEN, (0, 0, 120, 50))
ellipse(surf, ORANGE, (0, 0, 120, 50))
ellipse(surf, BLACK, (0, 0, 120, 50), 1)
surf_rot = pygame.transform.rotate(surf, 135)
screen.blit(surf_rot, (300, 350))

#body
ellipse(screen, ORANGE, (50, 300, 280, 140))
ellipse(screen, BLACK, (50, 300, 280, 140), 1)

#front paw
ellipse(screen, ORANGE, (35, 345, 38, 90))
ellipse(screen, BLACK, (35, 345, 38, 90), 1)

#head
ellipse(screen, ORANGE, (25, 305, 110, 105))
ellipse(screen, BLACK, (25, 305, 110, 105), 1)

#eyes
circle(screen, GREEN, (60, 355), 15)
circle(screen, GREEN, (100, 355), 15)
circle(screen, BLACK, (60, 355), 15, 1)
circle(screen, BLACK, (100, 355), 15, 1)
ellipse(screen, BLACK, (60, 340, 5, 30))
ellipse(screen, BLACK, (100, 340, 5, 30))
rect(surf2, GREEN, (0, 0, 10, 5))
ellipse(surf2, WHITE, (0, 0, 10, 5))
surf2_rot = pygame.transform.rotate(surf2, 135)
screen.blit(surf2_rot, (50, 345))
screen.blit(surf2_rot, (90, 345))

#ears
polygon(screen, ORANGE, [(30, 340), (35, 300), (60, 315)])
polygon(screen, BLACK, [(30, 340), (35, 300), (60, 315)], 1)
polygon(screen, ORANGE, [(130, 340), (125, 300), (100, 315)])
polygon(screen, BLACK, [(130, 340), (125, 300), (100, 315)], 1)

polygon(screen, PINK, [(32, 336), (37, 304), (56, 315)])
polygon(screen, BLACK, [(32, 336), (37, 304), (56, 315)], 1)
polygon(screen, PINK, [(128, 336), (123, 304), (104, 315)])
polygon(screen, BLACK, [(128, 336), (123, 304), (104, 315)], 1)

#nose
polygon(screen, PINK, [(77, 375), (83, 375), (80, 380)])
polygon(screen, BLACK, [(77, 375), (83, 375), (80, 380)], 1)
line(screen, BLACK, (80, 380), (80, 390))
acr(screen, BLACK, (75, 380, 5, 5), 3*np.pi/2, 2*np.pi)

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