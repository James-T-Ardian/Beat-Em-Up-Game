import pygame
import sys
from Player import *
from World import *
from TextBox import *


pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550
WHITE_RGB = (255,255,255)
BLACK_RGB = (0,0,0)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background = pygame.image.load('sprites/background_cropped_extended.png').convert_alpha()

clock = pygame.time.Clock()
pygame.display.set_caption('Infinitum')

gameIcon = pygame.image.load('sprites/tree-of-life_icon.png')
pygame.display.set_icon(gameIcon)

world = World(screen)
    
def main_menu():
    menu_running = True
    while menu_running:
        screen.blit(background,(0,0))
        mouse_pos = pygame.mouse.get_pos()

        title_font = pygame.font.Font('font\merchant-copy\Merchant Copy.ttf', 100)
        title_text_w = 400
        title_text_h = 100
        title_text = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - title_text_w / 2,SCREEN_HEIGHT / 3), (title_text_w, title_text_h), "Infinitum", title_font, WHITE_RGB, BLACK_RGB, True))
        title_text.draw(screen)

        menu_buttons_font = pygame.font.Font('font\merchant-copy\Merchant Copy.ttf', 50)
        menu_buttons_button_w = 200
        menu_buttons_button_h = 70

        start_button = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - menu_buttons_button_w / 2,SCREEN_HEIGHT / 3 + 100), (menu_buttons_button_w, menu_buttons_button_h), "Start", menu_buttons_font, WHITE_RGB, BLACK_RGB, True))
        start_button.draw(screen)

        controls_button = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - menu_buttons_button_w / 2,SCREEN_HEIGHT / 3 + 150), (menu_buttons_button_w, menu_buttons_button_h), "Controls", menu_buttons_font, WHITE_RGB, BLACK_RGB, True))
        controls_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and start_button.sprite.rect.collidepoint(mouse_pos):
                menu_running = False
                world.setup_world()
                game()
            elif event.type == pygame.MOUSEBUTTONDOWN and controls_button.sprite.rect.collidepoint(mouse_pos):
                menu_running = False
                controls_menu()

        pygame.display.update()
        clock.tick(60)

def controls_menu():
    controls_running = True

    while controls_running:
        screen.blit(background,(0,0))
        mouse_pos = pygame.mouse.get_pos()

        controls_text_font = pygame.font.Font('font\merchant-copy\Merchant Copy.ttf', 50)
        controls_text_w = 600
        controls_text_h = 70

        p1_p2_text = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - 467,SCREEN_HEIGHT / 4 - 50), (controls_text_w, controls_text_h), "P1      P2", controls_text_font, WHITE_RGB, BLACK_RGB, True))
        p1_p2_text.draw(screen)

        jump_text = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - 350,SCREEN_HEIGHT / 4), (controls_text_w, controls_text_h), "A   |   ,    --   Jump", controls_text_font, WHITE_RGB, BLACK_RGB, True))
        jump_text.draw(screen)

        attack_text = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - 332,SCREEN_HEIGHT / 4 + 50), (controls_text_w, controls_text_h), "S   |   .    --   Attack", controls_text_font, WHITE_RGB, BLACK_RGB, True))
        attack_text.draw(screen)

        dash_text = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - 350,SCREEN_HEIGHT / 4 + 100), (controls_text_w, controls_text_h), "D   |   /    --   Dash", controls_text_font, WHITE_RGB, BLACK_RGB, True))
        dash_text.draw(screen)

        move_right_text = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - 295,SCREEN_HEIGHT / 4 + 150), (controls_text_w, controls_text_h), "N   |   ->   --   Move Right", controls_text_font, WHITE_RGB, BLACK_RGB, True))
        move_right_text.draw(screen)

        move_left_text = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - 305,SCREEN_HEIGHT / 4 + 200), (controls_text_w, controls_text_h), "V   |   <-   --   Move Left", controls_text_font, WHITE_RGB, BLACK_RGB, True))
        move_left_text.draw(screen)

        back_button_font = pygame.font.Font('font\merchant-copy\Merchant Copy.ttf', 50)
        back_button_button_w = 300
        back_button_button_h = 70
        back_button = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - back_button_button_w / 2,SCREEN_HEIGHT / 3 + 250), (back_button_button_w, back_button_button_h), "Back to menu", back_button_font, WHITE_RGB, BLACK_RGB, True))
        back_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and back_button.sprite.rect.collidepoint(mouse_pos):
                controls_running = False
                main_menu()
            

        pygame.display.update()
        clock.tick(60)

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

        winner_font = pygame.font.Font('font\merchant-copy\Merchant Copy.ttf', 100)
        winner_text_w = 300
        winner_text_h = 100
        winner_text = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - winner_text_w / 2,SCREEN_HEIGHT / 3), (winner_text_w, winner_text_h), f"P{result} Wins", winner_font, WHITE_RGB, BLACK_RGB, True))
        winner_text.draw(screen)

        play_again_font = pygame.font.Font('font\merchant-copy\Merchant Copy.ttf', 50)
        play_again_button_w = 200
        play_again_button_h = 70
        play_again_button = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - play_again_button_w / 2,SCREEN_HEIGHT / 3 + 100), (play_again_button_w, play_again_button_h), "Play Again", play_again_font, WHITE_RGB, BLACK_RGB, True))
        play_again_button.draw(screen)

        back_button_font = pygame.font.Font('font\merchant-copy\Merchant Copy.ttf', 50)
        back_button_button_w = 300
        back_button_button_h = 70
        back_button = pygame.sprite.GroupSingle(TextBox((SCREEN_WIDTH / 2 - back_button_button_w / 2,SCREEN_HEIGHT / 3 + 150), (back_button_button_w, back_button_button_h), "Back to menu", back_button_font, WHITE_RGB, BLACK_RGB, True))
        back_button.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and play_again_button.sprite.rect.collidepoint(mouse_pos):
                end_screen_running = False
                world.setup_world()
                game()
            elif event.type == pygame.MOUSEBUTTONDOWN and back_button.sprite.rect.collidepoint(mouse_pos):
                end_screen_running = False
                main_menu()
        

        pygame.display.update()
        clock.tick(60)

            
main_menu()

    
    
