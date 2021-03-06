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
# create screen
screen = pygame.display.set_mode((400, 600))

# draw the floor and wall
rect(screen, DARK_GREEN, (0, 0, 400, 250))
rect(screen, LIGHT_GREEN, (0, 250, 400, 350))

def window (Xw):
    rect(screen, LIGHT_BLUE, (230 - Xw, 10, 160, 200))
    rect(screen, BLUE, (240 - Xw, 20, 65, 50))
    rect(screen, BLUE, (315 - Xw, 20, 65, 50))
    rect(screen, BLUE, (240 - Xw, 80, 65, 120))
    rect(screen, BLUE, (315 - Xw, 80, 65, 120))


 # draw the main part of cat using ellipse

screen1 = pygame.Surface((400, 600))
screen2 = pygame. Surface((400, 600))
surf = pygame.Surface((120, 50))
surf2 = pygame.Surface((10, 5))

rect(screen1, LIGHT_GREEN, (0, 250, 400, 350))
# tail
rect(surf, LIGHT_GREEN, (0, 0, 120, 50))
ellipse(surf, ORANGE, (0, 0, 120, 50))
ellipse(surf, BLACK, (0, 0, 120, 50), 1)
surf_rot = pygame.transform.rotate(surf, 135)
screen1.blit(surf_rot, (300, 350))



def sad_cat (X, Y, size, mirrow, color):
    if color == 1:
        ORANGE = (76, 76, 52)
        GREEN = (128, 159, 255)
    if color == 0:
        GREEN = (0, 204, 0)
        ORANGE = (255, 153, 51)
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


    x0 = (400/size)//1
    y0 = (600/size)//1
    Cat = pygame.transform.scale(screen1, (x0, y0))
    Cat = pygame.transform.flip(Cat, mirrow, 1)
    screen.blit(Cat, (X, Y))


def roll_of_thread(X1, Y1, size):
    circle(screen2, GREY, (250, 500), 50)
    circle(screen2, BLACK, (250, 500), 50, 1)
    arc(screen2, GREY, (150, 450, 100, 100), 4, 0)
    arc(screen2, GREY, (70, 500, 100, 100), 0.3, 3.14)
    arc(screen2, BLACK, (200, 450, 100, 50), 3.5, -0.5)
    arc(screen2, BLACK, (210, 460, 100, 50), 3.5, -0.5)
    arc(screen2, BLACK, (200, 480, 100, 40), 3.5, -0.5)
    arc(screen2, BLACK, (200, 450, 100, 50), 4, 0)
    sc2 = pygame.transform.scale(screen2, (x2, y3))
    screen.blit(sc2)

sad_cat(0, 0, 1, 1, 0)
sad_cat(10, 10, 2, 0, 1)
sad_cat(0, -50, 4, 1, 1)
sad_cat(100, -50, 3, 1, 0)
sad_cat(0, 0, 4, 1, 1)
sad_cat(10, -50, 4, 1, 0)
roll_of_thread(0, 0, 1)
roll_of_thread(10, 20, 2)
roll_of_thread(-30, 50, 3)


window(0)
window(200)



pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()