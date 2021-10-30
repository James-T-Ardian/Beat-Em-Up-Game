import pygame
import sys
from player import *
from world import *

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background = pygame.image.load('sprites/background_cropped_extended.png').convert_alpha()

clock = pygame.time.Clock()
pygame.display.set_caption('Infinitum')

world = World(screen)

game_run = True
while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.blit(background,(0,0))
    world.run()

    pygame.display.update()
    clock.tick(60)
    
    
