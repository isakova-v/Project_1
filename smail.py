import pygame
from pygame.draw import *

pygame.init()

#colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 30
screen = pygame.display.set_mode((400, 400))

# color of space - white
rect(screen, WHITE, (0, 0, 400, 400))

# draw main circle
circle(screen, YELLOW, (200, 200), 100)
circle(screen, BLACK, (200, 200), 100, 1)

# draw eyes
circle(screen, RED, (150, 160), 20)
circle(screen, RED, (250, 160), 15)
circle(screen, BLACK, (150, 160), 20, 1)
circle(screen, BLACK, (250, 160), 15, 1)
circle(screen, BLACK, (150, 160), 10)
circle(screen, BLACK, (250, 160), 10)

# draw mouth
rect(screen, BLACK, (150, 250, 100, 10))

# draw eyebrows
polygon(screen, BLACK, [[100, 107], [105, 102], [180, 147], [175, 152]])
polygon(screen, BLACK, [[220, 150], [225, 155], [305, 115], [300, 110]])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()