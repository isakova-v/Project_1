import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

#colors of balls
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''рисует новый шарик '''
    global x, y, r, delta_x, delta_y, color
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    delta_x = randint(-10, 10)
    delta_y = randint(-10, 10)
    color = COLORS[randint(0, 5)]


pygame.display.update()
clock = pygame.time.Clock()
finished = False


Score = []
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            def click():
                if (((event.pos[0] - x)**2) + (event.pos[1] - y)**2) <= (r**2):
                    print('OKEY')
                    Score.append(1)
                    print(len(Score))
                else:
                    print('TRY AGAIN')
            click()

    new_ball()

    while (x-r)>0 and (x+r)<1200 and (y-r)>0 and (y+r)<900:

        pygame.display.update()
        screen.fill(BLACK)
        x += delta_x
        y += delta_y
        circle(screen, color, (x, y), r)


pygame.quit()