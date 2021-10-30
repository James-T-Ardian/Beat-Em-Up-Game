import pygame
from player import *

GROUND_Y = 450
PLAYER_ONE_CONTROL = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_n, pygame.K_v]
PLAYER_TWO_CONTROL = [pygame.K_COMMA, pygame.K_PERIOD, pygame.K_SLASH, pygame.K_RIGHT, pygame.K_LEFT]

# Class is specific to the game world we are creating and in this case the game is infinitum. 
# Requires only the pygame.display screen as input though you need to also import character sprites 
# that will be in the game. Class will primarily be used to determine what characters are in the game
# as well as their interactions. 
class World:
    def __init__(self, screen):
        self.screen = screen
        self._start_world()

    def _start_world(self):
        self.player_one = pygame.sprite.GroupSingle(Player((200, GROUND_Y), PLAYER_ONE_CONTROL))
        self.player_two = pygame.sprite.GroupSingle(Player((600, GROUND_Y), PLAYER_TWO_CONTROL))

    def run(self):
        self.player_one.update()
        self.player_two.update()

        if self.player_one.sprite.weapon_hitbox.colliderect(self.player_two.sprite.player_hitbox):
            print("banana")

        if self.player_two.sprite.weapon_hitbox.colliderect(self.player_one.sprite.player_hitbox):
            print("apple")

        # Draws rectangle and hitbox of player. Delete later
        # pygame.draw.rect(self.screen, 'White', self.player.sprite.rect, 3)
        # pygame.draw.rect(self.screen, 'red', self.player.sprite.player_hitbox, 3)
        pygame.draw.rect(self.screen, 'pink', self.player_one.sprite.weapon_hitbox, 3)
        pygame.draw.rect(self.screen, 'pink', self.player_two.sprite.weapon_hitbox, 3)
        
        self.player_one.draw(self.screen)
        self.player_two.draw(self.screen)
        

