import pygame
from pygame_image_analyzer import *

GROUND_Y = 450

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('sprites/player/idle/tile000.png').convert_alpha()

        # Rect to determine character location and hitbox to determine character collision 
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = getMaskRect(self.image ,*self.image.get_rect(topleft = pos).topleft)

        # Movement variables
        self.direction = pygame.math.Vector2(0,0)
        self.move_speed = 4
        self.apply_gravity = False
        self.jump_speed = 32
        self.gravity = 2
    
    # Responds to user's key inputs 
    def _get_input(self):
        keys = pygame.key.get_pressed()

        # Move right or left
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else: 
            self.direction.x = 0
        
        # Jump
        if keys[pygame.K_UP] and not self.apply_gravity:
            self.direction.y = -1
            
    def _gravity(self):
        if self.direction.y == -1:
            self.apply_gravity = True

        if self.apply_gravity:
            self.direction.y = 1

        if self.rect.y == GROUND_Y:
            self.direction.y = 0
            self.apply_gravity = False

    def _update_player_and_hitbox_location(self):
        self.rect.x += self.direction.x * self.move_speed
        self.rect.y += self.direction.y * self.jump_speed * (not self.apply_gravity) + self.direction.y * self.gravity * self.apply_gravity
        self.hitbox.x += self.direction.x * self.move_speed
        self.hitbox.y += self.direction.y * self.jump_speed * (not self.apply_gravity) + self.direction.y * self.gravity * self.apply_gravity

    def update(self):
        self._get_input()
        self._update_player_and_hitbox_location()
        self._gravity()


