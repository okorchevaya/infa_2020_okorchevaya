import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
#body4
circle(screen, (0, 0, 0), (200, 200), 83)
circle(screen, (255, 215, 0), (200, 200), 80)
#eyes
circle(screen, (178, 34, 34), (180, 180), 20)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
