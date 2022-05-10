import sys
import pygame
from pygame.locals import *
import math

pygame.init()
    
    

width, height = 840, 840
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
car = pygame.image.load("rc-arlos-af-240s13-nissan-240sx-s13-bn-sports-clea.png")
car = pygame.transform.scale(car, (120, 67.5))
bg = pygame.image.load("images.png")


x = 0
y = 0
velx = 0
vely = 0
blue_rotation = 180



while True:
    
    mouse = pygame.mouse.get_pos()
    print(mouse)
    blue_x = 420
    blue_y = 420

    screen.fill((255,255,255))
    screen.blit(bg, (bg.get_rect()[0] - x ,bg.get_rect()[1] - y))
    screen.blit(car, (420 - 60, 420 - 33.75))
    pygame.draw.polygon(screen, (0,0,255), [(blue_x + 16 * math.sin(math.radians(blue_rotation)), blue_y - 16 * math.cos(math.radians(blue_rotation))),(blue_x + 16 * math.sin(math.radians(blue_rotation + 140)), blue_y - 16 * math.cos(math.radians(blue_rotation + 140))),(blue_x + 8 * math.sin(math.radians(blue_rotation + 180)), blue_y - 8 * math.cos(math.radians(blue_rotation + 180))),(blue_x + 16 * math.sin(math.radians(blue_rotation + 220)), blue_y - 16 * math.cos(math.radians(blue_rotation + 220)))])
    
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]: 
        blue_rotation -= 2
    if keys[K_RIGHT]: 
        blue_rotation += 2
    if keys[K_UP]: 
        velx += .1 * math.sin(math.radians(blue_rotation))
        vely -= .1 * math.cos(math.radians(blue_rotation))
    
    if velx > 5:
        velx = 5
    if vely > 5:
        vely = 5

    if velx > 0:
        velx -= .03
    elif velx < 0:
        velx += .03
    if vely > 0:
        vely -= .03
    elif vely < 0:
        vely += .03
    
    x += velx
    y += vely
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.KEYDOWN:


    clock.tick(120)
    pygame.display.flip()