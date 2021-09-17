import pygame
from player import *

GROUND_Y = 450

class World:
    def __init__(self, screen):
        self.screen = screen
        self._start_world()
        pass

    def _start_world(self):
        self.player = pygame.sprite.GroupSingle(Player((200, GROUND_Y)))

    def run(self):
        self.player.update()
        
        # Draws rectangle and hitbox of player. Delete later
        pygame.draw.rect(self.screen, 'White', self.player.sprite.rect, 3)
        pygame.draw.rect(self.screen, 'red', self.player.sprite.hitbox, 3)
        
        self.player.draw(self.screen)
        

