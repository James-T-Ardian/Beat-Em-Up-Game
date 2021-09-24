import pygame
from pygame_image_analyzer import *

GROUND_Y = 450

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('sprites/player/idle/tile000.png').convert_alpha()

        # Rect to determine character, player hitbox and weapon hitbox
        self.rect = self.image.get_rect(topleft = pos)
        self.player_hitbox = getMaskRect(self.image ,*self.image.get_rect(topleft = pos).topleft)
        self.weapon_hitbox = pygame.Rect.copy(self.player_hitbox).move(25, 0)

        # Movement variables
        self.direction = pygame.math.Vector2(0,0)
        self.move_speed = 3
        self.apply_gravity = False
        self.jump_speed = 50
        self.gravity = 2

        # Cooldowns
        self.last_dash = pygame.time.get_ticks()
        self.dash_cooldown = 600
    
    # Responds to user's key inputs 
    def _get_input(self):
        keys = pygame.key.get_pressed()
        now = pygame.time.get_ticks()

        # Move right or left
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else: 
            self.direction.x = 0
        
        # Jump
        if keys[pygame.K_z] and not self.apply_gravity:
            self.direction.y = -1
        
        # Dash
        if keys[pygame.K_c] and now - self.last_dash >= self.dash_cooldown:
            self.last_dash = now
            self.move_speed = 50
        elif now - self.last_dash <= self.dash_cooldown / 5:                    # Make Dash Smoother
            self.move_speed = 7
        else:
            self.move_speed = 3
        
        # Attack
        if keys[pygame.K_x]:
            pass

    def _gravity(self):
        if self.direction.y == -1:
            self.apply_gravity = True

        if self.apply_gravity:
            self.direction.y = 1

        if self.rect.y == GROUND_Y:
            self.direction.y = 0
            self.apply_gravity = False
    
    def _update_image_and_hitboxes_location(self):
        self.rect.x += self.direction.x * self.move_speed
        self.rect.y += self.direction.y * self.jump_speed * (not self.apply_gravity) + self.direction.y * self.gravity * self.apply_gravity
        self.player_hitbox.x += self.direction.x * self.move_speed
        self.player_hitbox.y += self.direction.y * self.jump_speed * (not self.apply_gravity) + self.direction.y * self.gravity * self.apply_gravity
        self.weapon_hitbox.x += self.direction.x * self.move_speed
        self.weapon_hitbox.y += self.direction.y * self.jump_speed * (not self.apply_gravity) + self.direction.y * self.gravity * self.apply_gravity

    def update(self):
        self._get_input()
        self._update_image_and_hitboxes_location()
        self._gravity()


