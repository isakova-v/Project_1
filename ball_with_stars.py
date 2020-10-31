import pygame
from pygame.draw import *
from random import randint
import math
import os

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))
time = 15  # time of one game

# colors of balls
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

Name = input("Name ")


def new_ball():  # New ball as a target
    '''рисует новый шарик '''
    global x, y, r, delta_x, delta_y, color
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    delta_x = randint(-10, 10)
    delta_y = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    return [x, y, r, delta_x, delta_y, color]


def new_square():  # New square as a target
    '''рисует новый квадрат (новая мишень со специфичным типом движения)'''
    x = randint(100, 1200)
    y = randint(100, 900)
    a = randint(60, 100)
    color = COLORS[randint(0, 5)]
    rect(screen, color, (x, y, a, a))
    delta_x = randint(-10, 10)
    delta_y = randint(-50, 50)
    dvx = 0
    dvy = randint(1, 10)
    return [x, y, a, color, delta_x, delta_y, dvx, dvy]


def click(event):  # Coords of mouth
    (x, y) = event.pos
    return [x, y]


balls_pos = []  # list for balls' parameters
square_pos = []  # list for squares' parameters
score = 0


def hit_ball(f_click, balls_pos):  # if hit was inside of the ball, score grows
    global score
    for i in range(len(balls_pos)):
        if math.sqrt((f_click[0] - balls_pos[i][0]) ** 2 + (f_click[1] - balls_pos[i][1]) ** 2) <= balls_pos[i][2]:
            del balls_pos[i]
            balls_pos.append(new_ball())
            score += 1


def hit_squares(f_click, square_pos):  # if hit was inside of the square, score grows
    global score
    for i in range(len(square_pos)):
        if 0 < (f_click[0] - square_pos[i][0]) < square_pos[i][0]:
            if 0 < (f_click[1] - square_pos[i][1]) < square_pos[i][0]:
                del square_pos[i]
                square_pos.append(new_square())
                score += 3


def score_of_the_user(score):  # create surface with letters "SCORE "
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('SCORE ' + str(score), 1, (180, 0, 0))
    screen.blit(text1, (10, 50))


# Add parameters of targets
for i in range(10):
    balls_pos.append(new_ball())
for i in range(3):
    square_pos.append(new_square())


def go_balls(balls_pos):  # Moving of the balls
    for i in range(len(balls_pos)):
        balls_pos[i][0] += balls_pos[i][3]  # changing x-coord
        balls_pos[i][1] += balls_pos[i][4]  # changing y-coord

        # vertical wall impact condition
        if balls_pos[i][0] + balls_pos[i][2] >= 1200:
            balls_pos[i][0] -= balls_pos[i][3]
            balls_pos[i][3] = - balls_pos[i][3]

        if balls_pos[i][0] - balls_pos[i][2] <= 0:
            balls_pos[i][0] -= balls_pos[i][3]
            balls_pos[i][3] = - balls_pos[i][3]

        # horizontal wall impact condition
        if balls_pos[i][1] + balls_pos[i][2] >= 900:
            balls_pos[i][1] -= balls_pos[i][4]
            balls_pos[i][4] = - balls_pos[i][4]

        if balls_pos[i][1] - balls_pos[i][2] <= 0:
            balls_pos[i][1] -= balls_pos[i][4]
            balls_pos[i][4] = - balls_pos[i][4]

        circle(screen, balls_pos[i][5], (balls_pos[i][0], balls_pos[i][1]), balls_pos[i][2])


def go_squares(square_pos):  # Moving of the squares
    for i in range(len(square_pos)):
        square_pos[i][0] += square_pos[i][4]  # changing x-coord
        square_pos[i][1] += square_pos[i][5]  # changing y-coord
        square_pos[i][4] += square_pos[i][6]  # changing delta_x
        square_pos[i][5] += square_pos[i][7]  # changing delta_y

        # vertical wall impact condition
        if square_pos[i][0] + square_pos[i][2] >= 1200:
            square_pos[i][0] -= square_pos[i][4]
            square_pos[i][4] = - square_pos[i][4]

        if square_pos[i][0] <= 0:
            square_pos[i][0] -= square_pos[i][4]
            square_pos[i][4] = - square_pos[i][4]

        # horizontal wall impact condition
        if square_pos[i][1] + square_pos[i][2] >= 900:
            square_pos[i][1] -= square_pos[i][5]
            square_pos[i][5] = - square_pos[i][5]
            square_pos[i][5] -= round(square_pos[i][5] * 0.2 - 0.01)

        if square_pos[i][1] <= 0:
            square_pos[i][1] -= square_pos[i][5]
            square_pos[i][5] = - square_pos[i][5]
            square_pos[i][5] += round(square_pos[i][5] * 0.2 - 0.01)

        rect(screen, square_pos[i][3], (square_pos[i][0], square_pos[i][1], square_pos[i][2], square_pos[i][2]))


pygame.display.update()
clock = pygame.time.Clock()
finished = 0

while finished < time * FPS:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            hit_ball(click(event), balls_pos)
            hit_squares(click(event), square_pos)
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')

    score_of_the_user(score)
    go_balls(balls_pos)
    go_squares(square_pos)
    pygame.display.update()
    screen.fill(BLACK)
    finished += 1

print('here', os.getcwd()) #directory of the file
f = open("top.txt", 'a')  #open file to write top of the gamers

f.write(Name + " " + str(score) + '\n')
f.close()

f = open('top.txt', 'r')
data = []
while True:
    result = f.readline()
    if result == "":
        break
    data.append(result)
for i in range(len(data)):
    result = data[i]
    result = result.split()
    data[i] = result

print(data)
f.close()


def table_top(i):
    return int(i[1])


print(data)
data.sort(key=table_top, reverse=True)  # descending grading
for i in range(len(data)):
    print("Gamer " + str(data[i][0]) + " has score " + str(data[i][1]))
f.close()

file = open('top.txt', 'w')  # saving the players' top in the table
for i in range(len(data)):
    file.write(str(data[i][0]) + " " + str(data[i][1]) + "\n")

pygame.quit()
