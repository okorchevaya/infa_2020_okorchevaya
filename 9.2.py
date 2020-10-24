import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 700))
rect(screen, (0, 255, 255), (0, 0, 900, 400))
rect(screen, (245, 245, 245), (0, 400, 900, 300))
line(screen, (0,0,0), (0,400),(900,400),2)
surface_fish = pygame.Surface((900,700), pygame.SRCALPHA)
surface_bear = pygame.Surface((900,700), pygame.SRCALPHA)
#sun
surface1 = screen.convert_alpha()
surface1.fill([0,0,0,0])
pygame.draw.circle(surface1, (245, 245, 220, 200), (300, 150), 150,25)
pygame.draw.line(surface1,(245, 245, 220,200),(150,145),(450,150),20)
pygame.draw.line(surface1,(245, 245, 220, 200),(300,0),(290,300),20)
pygame.draw.circle(surface1, (245, 245, 220, 250), (300, 150),20)
screen.blit(surface1, (0,0))
#bear1
ellipse(screen,(245,245,245), (87, 267,100,60))
ellipse(screen,(0,0,0), (87,267,100,60),1)
ellipse(screen,(245,245,245), (0, 300,150,270))
ellipse(screen,(0,0,0), (0, 300,150,270),1)
circle(screen,(0,0,0),(130,286),3)
circle(screen,(0,0,0),(185,290),3)
arc(screen, (0,0,0),(-90,290,300,20),math.pi*5/3, math.pi*11/6)
arc(screen,(0,0,0),(150,300,900,300),math.pi*2/3,math.pi,5) #stick
arc(screen,(0,0,0),(95,270,20,20),math.pi/6, math.pi*3/2) #ear
ellipse(screen,(245,245,245), (95, 270,20,20))
line(screen,(0,0,0),(103,288),(113,274),1)

ellipse(screen,(245,245,245), (130, 385,65,30))
ellipse(screen,(0,0,0), (130, 385,65,30),1)
ellipse(screen,(245,245,245), (90, 500,100,80))
ellipse(screen,(0,0,0), (90, 500,100,80),1)
ellipse(screen,(245,245,245), (155, 555,80,30))
ellipse(screen,(0,0,0), (155, 555,80,30),1)
#ice1
ellipse(screen,(80,80,80), (285, 480,170,60))
ellipse(screen,(0,0,0), (285, 480,170,60),1)
ellipse(screen,(0,80,60), (300, 500,140,40))
ellipse(screen,(0,0,0), (300, 500,140,40),1)
line(screen,(0,0,0),(375,320),(375,510),1)
#bear2
ellipse(surface_bear,(245,245,245), (87, 267,100,60))
ellipse(surface_bear,(0,0,0), (87,267,100,60),1)
ellipse(surface_bear,(245,245,245), (0, 300,150,270))
ellipse(surface_bear,(0,0,0), (0, 300,150,270),1)
circle(surface_bear,(0,0,0),(130,286),3)
circle(surface_bear,(0,0,0),(185,290),3)
arc(surface_bear, (0,0,0),(-90,290,300,20),math.pi*5/3, math.pi*11/6)
arc(surface_bear,(0,0,0),(150,300,900,300),math.pi*2/3,math.pi,5) #stick
arc(surface_bear,(0,0,0),(95,270,20,20),math.pi/6, math.pi*3/2) #ear
ellipse(surface_bear,(245,245,245), (95, 270,20,20))
line(surface_bear,(0,0,0),(103,288),(113,274),1)

ellipse(surface_bear,(245,245,245), (130, 385,65,30))
ellipse(surface_bear,(0,0,0), (130, 385,65,30),1)
ellipse(surface_bear,(245,245,245), (90, 500,100,80))
ellipse(surface_bear,(0,0,0), (90, 500,100,80),1)
ellipse(surface_bear,(245,245,245), (155, 555,80,30))
ellipse(surface_bear,(0,0,0), (155, 555,80,30),1)

surface_bear1 = pygame.transform.flip(surface_bear, True, False)
screen.blit(surface_bear1, (0, 0))
#ice2
ellipse(surface_bear,(80,80,80), (285, 480,170,60))
ellipse(surface_bear,(0,0,0), (285, 480,170,60),1)
ellipse(surface_bear,(0,80,60), (300, 500,140,40))
ellipse(surface_bear,(0,0,0), (300, 500,140,40),1)
line(surface_bear,(0,0,0),(375,320),(375,510),1)
surface_bear1 = pygame.transform.flip(surface_bear, True, False)
screen.blit(surface_bear1, (0, 0))



def fish(x,y,size,xbool, ybool):

    polygon(surface_fish, (173,216,230, 255),[(x,y),(x-10*size,y-15*size),(x-10*size,y+15*size)])
    polygon(surface_fish, (0,0,0,255),[(x,y),(x-10*size,y-15*size),(x-10*size,y+15*size)],1*size)
    ellipse(surface_fish, (173,216,230,255),(x,y-10*size,70*size,20*size))
    ellipse(surface_fish, (0,0,0,255),(x,y-10*size,70*size,20*size), 1*size)
    circle(surface_fish, (30,144,255,255),(x+50*size,y),5*size)
    circle(surface_fish, (0,0,0,255),(x+51*size,y+1*size),2*size)
    polygon(surface_fish,(255,255,255,255), [(x+50*size,y-1*size),(x+51*size,y-2*size),(x+49*size,y-3*size),(x+48*size,y-4*size)])
    polygon(surface_fish,(240,128,128,255),[(x+46*size,y-10*size),(x+43*size,y-20*size),(x+17*size,y-18*size),(x+30*size,y-10*size)])
    polygon(surface_fish,(240,128,128,255),[(x+50*size,y+8*size),(x+56*size,y+15*size),(x+50*size,y+20*size),(x+46*size,y+8*size)])
    polygon(surface_fish,(240,128,128,255),[(x+15*size,y+8*size),(x+5*size,y+20*size),(x+25*size,y+17*size),(x+22*size,y+6*size)])
    surface_fish1 = pygame.transform.flip(surface_fish, xbool, ybool)
    screen.blit(surface_fish1, (0, 0))
    pygame.display.update()

fish(350,610,1, False, False)
fish(650,610,1, False, False)
fish(310,600,2, True, False)
fish(230,540,1, True, False)

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()