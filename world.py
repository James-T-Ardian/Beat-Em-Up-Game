import pygame
from Player import *
from TextBox import TextBox

GROUND_Y = 450
PLAYER_ONE_CONTROL = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_n, pygame.K_v]
PLAYER_TWO_CONTROL = [pygame.K_COMMA, pygame.K_PERIOD, pygame.K_SLASH, pygame.K_RIGHT, pygame.K_LEFT]

# Class is specific to the game world we are creating and in this case the game is infinitum. 
# Requires only the pygame.display screen as input though you need to also import character sprites 
# that will be in the game. Class will primarily be used to determine what characters are in the game
# as well as their interactions. 
#   Input: screen -> pygame screen where the game will take place in 
class World:
    def __init__(self, screen):
        self.screen = screen
        self.setup_world()

    def setup_world(self):
        white_rgb = (255,255,255)
        black_rgb = (0,0,0)

        font_one = pygame.font.Font('font\merchant-copy\Merchant Copy.ttf', 20)
        self.identifier_one = pygame.sprite.GroupSingle(TextBox((206, GROUND_Y - 20), (50, 25), 'P1', font_one, white_rgb, black_rgb, True))
        self.player_one = pygame.sprite.GroupSingle(Player((200, GROUND_Y), PLAYER_ONE_CONTROL))

        font_two = pygame.font.Font('font\merchant-copy\Merchant Copy.ttf', 20)
        self.identifier_two = pygame.sprite.GroupSingle(TextBox((606, GROUND_Y - 20), (50, 25), 'P2', font_two, white_rgb, black_rgb, True))
        self.player_two = pygame.sprite.GroupSingle(Player((600, GROUND_Y), PLAYER_TWO_CONTROL, False))
        
    def run(self):
        self.player_one.update()
        self.identifier_one.update((self.player_one.sprite.rect.x + 6, self.player_one.sprite.rect.y - 20))
        self.player_two.update()
        self.identifier_two.update((self.player_two.sprite.rect.x + 6, self.player_two.sprite.rect.y - 20))

        if self.player_one.sprite.weapon_hitbox.colliderect(self.player_two.sprite.player_hitbox):
            return 1

        if self.player_two.sprite.weapon_hitbox.colliderect(self.player_one.sprite.player_hitbox):
            return 2

        # Draws rectangle and hitbox of player. For testing hitbox timings
        # pygame.draw.rect(self.screen, 'White', self.player.sprite.rect, 3)
        # pygame.draw.rect(self.screen, 'red', self.player.sprite.player_hitbox, 3)
        # pygame.draw.rect(self.screen, 'pink', self.player_one.sprite.weapon_hitbox, 3)
        # pygame.draw.rect(self.screen, 'pink', self.player_two.sprite.weapon_hitbox, 3)
        
        self.player_one.draw(self.screen)
        self.identifier_one.draw(self.screen)
        self.player_two.draw(self.screen)
        self.identifier_two.draw(self.screen)
        return 0
        

