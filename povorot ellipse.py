import pygame
from pygame.draw import *

pygame.init()


GREEN = (0, 204, 0)
ORANGE = (255, 153, 51)
BLACK = (0, 0, 0)
FPS = 30

screen = pygame.display.set_mode((400, 600))
# Создаю поверхность размерами 120*50
surf = pygame.Surface((120, 50))

#Рисую на этой поверхности
rect(surf, GREEN, (0, 0, 120, 50))
ellipse(surf, ORANGE, (0, 0, 120, 50))
ellipse(surf, BLACK, (0, 0, 120, 50), 1)

#Поворачиваю поверхность и прикрепляю ее к экрану
surf_rot = pygame.transform.rotate(surf, 45)
screen.blit(surf_rot, (300, 350))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()