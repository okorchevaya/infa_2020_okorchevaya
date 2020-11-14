
import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 40
screen = pygame.display.set_mode((1200, 800))

length=1200
height=800
change = [-4, -3, -2, -1, 1, 2, 3, 4]


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
points = 0

def new_balls(x,y,r, color):
    circle(screen, color, (x, y), r)


clock = pygame.time.Clock()
finished = False
click = False
click1 = False
def running_ball():
    finished=False
    score = 0
    while not finished:
        x = randint(1, 500)
        y = randint(1, 500)
        r = randint(10, 50)
        color = COLORS[randint(0, 5)]
        del_x = change[randint(1, 5)]
        del_y = change[randint(1, 5)]

        x1 = randint(1, 500)
        y1 = randint(1, 500)
        r1 = randint(10, 50)
        color1 = COLORS[randint(0, 5)]
        del_x1 = change[randint(1, 5)]
        del_y1 = change[randint(1, 5)]
        click = False
        click1 = False

        while (finished == False) and (click == False or click1 == False):
            if click == False:
                new_balls(x, y, r, color)
                x +=del_x
                y +=del_y

            if click1 == False:
                new_balls(x1, y1, r1, color1)
                x1 += del_x1
                y1 += del_y1

            clock.tick(FPS)
            #отталкивание от стен
            if y+r >= height or y-r <= 0:
                del_y = del_y * (-1)
            if x+r >= length or x-r <= 0:
                del_x = del_x*(-1)

            if y1+r1 >= height or y1-r1 <= 0:
                del_y1= del_y1 * (-1)
            if x1+r1 >= length or x1-r1 <= 0:
                del_x1 = del_x1*(-1)
            pygame.display.update()
            screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print('Click')
                    if (x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2 <= r ** 2:
                        score += 1
                        x = randint(1, 500)
                        y = randint(1, 500)
                        r = randint(10, 50)
                        color = COLORS[randint(0, 5)]
                        del_x = change[randint(1, 5)]
                        del_y = change[randint(1, 5)]
                    if (x1 - event.pos[0]) ** 2 + (y1 - event.pos[1]) ** 2 <= r1 ** 2:
                        score += 1
                        x1 = randint(1, 500)
                        y1 = randint(1, 500)
                        r1 = randint(10, 50)
                        color1 = COLORS[randint(0, 5)]
                        del_x1 = change[randint(1, 5)]
                        del_y1 = change[randint(1, 5)]



running_ball()
running_ball1()
pygame.quit()