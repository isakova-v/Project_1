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

# create surfaces and screen
screen = pygame.display.set_mode((400, 600))


# draw the floor and wall
rect(screen, DARK_GREEN, (0, 0, 400, 250))
rect(screen, LIGHT_GREEN, (0, 250, 400, 350))

def window(x):
    rect(screen, LIGHT_BLUE, (230-x, 10, 160, 200))
    rect(screen, BLUE, (240-x, 20, 65, 50))
    rect(screen, BLUE, (315-x, 20, 65, 50))
    rect(screen, BLUE, (240-x, 80, 65, 120))
    rect(screen, BLUE, (315-x, 80, 65, 120))

def sad_cat(size_x, size_y, start_x, start_y, color, mirrow):
    if color == 1:
        ORANGE = (255, 153, 51)
        GREEN = (0, 204, 0)
    if color == 0:
        ORANGE = (128, 128, 128)
        GREEN = (102, 255, 255)

    screen1 = pygame.Surface((400, 600))
    surf = pygame.Surface((120, 50))
    surf2 = pygame.Surface((10, 5))

    screen1.set_colorkey((1, 1, 1))
    rect(screen1, (1, 1, 1), (0, 0, 400, 600))

    # draw the main part of cat using ellipse
    # tail
    rect(surf, LIGHT_GREEN, (0, 0, 120, 50))
    ellipse(surf, ORANGE, (0, 0, 120, 50))
    ellipse(surf, BLACK, (0, 0, 120, 50), 1)
    surf_rot = pygame.transform.rotate(surf, 135)
    screen1.blit(surf_rot, (300, 350))

    # body
    ellipse(screen1, ORANGE, (50, 300, 280, 140))
    ellipse(screen1, BLACK, (50, 300, 280, 140), 1)

    # front paw
    ellipse(screen1, ORANGE, (35, 345, 38, 90))
    ellipse(screen1, BLACK, (35, 345, 38, 90), 1)

    # head
    ellipse(screen1, ORANGE, (25, 305, 110, 105))
    ellipse(screen1, BLACK, (25, 305, 110, 105), 1)

    # eyes
    circle(screen1, GREEN, (60, 355), 15)
    circle(screen1, GREEN, (100, 355), 15)
    circle(screen1, BLACK, (60, 355), 15, 1)
    circle(screen1, BLACK, (100, 355), 15, 1)
    ellipse(screen1, BLACK, (60, 340, 5, 30))
    ellipse(screen1, BLACK, (100, 340, 5, 30))
    rect(surf2, GREEN, (0, 0, 10, 5))
    ellipse(surf2, WHITE, (0, 0, 10, 5))
    surf2_rot = pygame.transform.rotate(surf2, 135)
    screen1.blit(surf2_rot, (50, 345))
    screen1.blit(surf2_rot, (90, 345))

    # ears
    polygon(screen1, ORANGE, [(30, 340), (35, 300), (60, 315)])
    polygon(screen1, BLACK, [(30, 340), (35, 300), (60, 315)], 1)
    polygon(screen1, ORANGE, [(130, 340), (125, 300), (100, 315)])
    polygon(screen1, BLACK, [(130, 340), (125, 300), (100, 315)], 1)

    polygon(screen1, PINK, [(32, 336), (37, 304), (56, 315)])
    polygon(screen1, BLACK, [(32, 336), (37, 304), (56, 315)], 1)
    polygon(screen1, PINK, [(128, 336), (123, 304), (104, 315)])
    polygon(screen1, BLACK, [(128, 336), (123, 304), (104, 315)], 1)

    # nose
    polygon(screen1, PINK, [(77, 375), (83, 375), (80, 380)])
    polygon(screen1, BLACK, [(77, 375), (83, 375), (80, 380)], 1)
    line(screen1, BLACK, (80, 380), (80, 390))
    ellipse(screen1, BLACK, (70, 388, 10, 10))
    ellipse(screen1, ORANGE, (70, 386, 10, 10))
    ellipse(screen1, BLACK, (80, 388, 10, 10))
    ellipse(screen1, ORANGE, (80, 386, 10, 10))
    arc(screen1, BLACK, (20, 375, 45, 10), 0, 2.5, 1)
    arc(screen1, BLACK, (95, 375, 45, 10), 0.64, 3.14, 1)
    arc(screen1, BLACK, (20, 378, 45, 10), 0, 2.5, 1)
    arc(screen1, BLACK, (95, 378, 45, 10), 0.64, 3.14, 1)
    arc(screen1, BLACK, (20, 381, 45, 10), 0, 2.5, 1)
    arc(screen1, BLACK, (95, 381, 45, 10), 0.64, 3.14, 1)

    # back paw
    ellipse(screen1, ORANGE, (250, 350, 80, 80))
    ellipse(screen1, BLACK, (250, 350, 80, 80), 1)

    # back paw2
    ellipse(screen1, ORANGE, (305, 400, 30, 80))
    ellipse(screen1, BLACK, (305, 400, 30, 80), 1)

    # front paw2
    ellipse(screen1, ORANGE, (80, 405, 70, 40))
    ellipse(screen1, BLACK, (80, 405, 70, 40), 1)
    if mirrow == 1:
        screen1 = pygame.transform.flip(screen1, True, False)
    screen1 = pygame.transform.scale(screen1, (size_x, size_y))
    screen.blit(screen1, (start_x, start_y))

def ball(size_x, size_y, start_x, start_y, mirrow):
    screen2 = pygame.Surface((400, 600))
    screen2.set_colorkey((1, 1, 1))
    rect(screen2, (1, 1, 1), (0, 0, 400, 600))
    # roll of thread
    circle(screen2, GREY, (250, 500), 50)
    circle(screen2, BLACK, (250, 500), 50, 1)
    arc(screen2, GREY, (150, 450, 100, 100), 4, 0)
    arc(screen2, GREY, (70, 500, 100, 100), 0.3, 3.14)
    arc(screen2, BLACK, (200, 450, 100, 50), 3.5, -0.5)
    arc(screen2, BLACK, (210, 460, 100, 50), 3.5, -0.5)
    arc(screen2, BLACK, (200, 480, 100, 40), 3.5, -0.5)
    arc(screen2, BLACK, (200, 450, 100, 50), 4, 0)

    if mirrow == 1:
        screen2 = pygame.transform.flip(screen2, True, False)
    screen2 = pygame.transform.scale(screen2, (size_x, size_y))
    screen.blit(screen2, (start_x, start_y))


window(0)
window(170)
window(340)

sad_cat(200, 300, 200, 150, 1, 0)
sad_cat(200, 300, 0, 250, 0, 1)
sad_cat(100, 150, 20, 200, 1, 1)
sad_cat(100, 150, 300, 330, 1, 1)
sad_cat(100, 150, 220, 400, 1, 0)
sad_cat(100, 150, 20, 450, 0, 1)
sad_cat(100, 150, 300, 450, 0, 0)

ball(160, 240, 50, 100, 0)
ball(160, 240, 220, 180, 1)
ball(160, 240, 20, 300, 0)
ball(160, 240, 180, 350, 0)
ball(250, 370, 150, 130, 1)
ball(250, 370, 260, 180, 1)
ball(400, 600, -50, 50, 0)


pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()