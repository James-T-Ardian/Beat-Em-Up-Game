import pygame
import sys
from Player import *
from World import *
from TextBox import *


pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background = pygame.image.load('sprites/background_cropped_extended.png').convert_alpha()

clock = pygame.time.Clock()
pygame.display.set_caption('Infinitum')

world = World(screen)
    

def game():
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        screen.blit(background,(0,0))
        result = world.run()
        if result > 0:
            game_running = False
            end_screen(result)

        pygame.display.update()
        clock.tick(60)
    
def end_screen(result):
    end_screen_running = True
    while end_screen_running:
        screen.blit(background,(0,0))
        mouse_pos = pygame.mouse.get_pos()

        white_rgb = (255,255,255)
        black_rgb = (0,0,0)

        winner_font = pygame.font.Font('font\merchant-copy\Merchant Copy.ttf', 100)
        winner_text_w = 300
        winner_text_h = 100
        winner_text = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - winner_text_w / 2,SCREEN_HEIGHT / 3), (winner_text_w, winner_text_h), f"P{result} Wins", winner_font, white_rgb, black_rgb, True))
        winner_text.draw(screen)

        play_again_font = pygame.font.Font('font\merchant-copy\Merchant Copy.ttf', 50)
        play_again_button_w = 200
        play_again_button_h = 70
        play_again_button = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - play_again_button_w / 2,SCREEN_HEIGHT / 2), (play_again_button_w, play_again_button_h), "Play Again", play_again_font, white_rgb, black_rgb, True))
        play_again_button.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and play_again_button.sprite.rect.collidepoint(mouse_pos):
                end_screen_running = False
                world.setup_world()
                game()
        

        pygame.display.update()
        clock.tick(60)

            
game()

    
    
