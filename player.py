import pygame
from pygame_image_analyzer import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('sprites/player/idle/tile000.png').convert_alpha()

        # rect to determine character location and hitbox to determine character collision 
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = getMaskRect(self.image ,*self.image.get_rect(topleft = pos).topleft)

        # Movement variables
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 0
    
    # Responds to user's key inputs 
    def _get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.speed = 8
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.speed = 8
            self.direction.x = -1
        else: 
            self.speed = 0
            self.direction.x = 0
    
    def update(self):
        self._get_input()
        self.rect.x += self.direction.x * self.speed
        self.hitbox.x += self.direction.x * self.speed

