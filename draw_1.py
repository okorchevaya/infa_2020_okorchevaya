import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((360, 520))
screen.fill((185, 211, 238))


polygon(screen, (96, 123, 139), [(0,330), (360, 330), (360,520), (0,520)])
#lrft house
polygon(screen, (159, 182, 205), [(10,10), (80, 10),(80,340), (10,340)])
polygon(screen, (150, 205, 205), [(90,30), (170, 30), (170,350), (90,350)])
polygon(screen, (198, 226, 255), [(60,80), (150, 80), (150,390), (60,390)])
#right houses
polygon(screen, (202, 225, 255), [(270,10), (350,10), (350, 340), (270, 340)])
polygon(screen, (122, 197, 205), [(240,90), (320, 90), (320, 400), (240, 400)])
#clouds
pygame.draw.ellipse(screen, (96, 123, 139), (80, 130, 400, 80))
pygame.draw.ellipse(screen, (96, 123, 139), (40, 30, 210, 70))
pygame.draw.ellipse(screen, (141, 182, 205), (20, 410, 110, 25))
pygame.draw.ellipse(screen, (141, 182, 205), (25, 445, 110, 25))
pygame.draw.ellipse(screen, (141, 182, 205), (-60, 380, 110, 25))


circle(screen, (202, 225, 255), (230, 840), 400)
#car
#tryba
pygame.draw.ellipse(screen, (28, 28, 28), (130, 465, 20, 7))
#metall red
polygon(screen, (139, 26, 26), [(140,455), (290, 455),(290,485), (140,485)])
polygon(screen, (139, 26, 26), [(170,430), (245, 430),(245,455), (170,455)])
#windows
polygon(screen, (248, 248, 255), [(175,435), (200, 435), (200,450), (175,450)])
polygon(screen, (248, 248, 255), [(215,435), (240, 435), (240,450), (215,450)])
#wheels
pygame.draw.ellipse(screen, (28, 28, 28), (150, 475, 35, 20))
pygame.draw.ellipse(screen, (28, 28, 28), (245, 475, 35, 20))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
