import pygame
# Create TextBox sprite for Pygame
#
#   Input: pos -> topleft coordinate of box encapsulating text in (x ,y) tuple form.  
#          dimension -> dimension of box encapsulating text in (w, h) tuple form.
#          text -> string that will be displayed
#          font -> pygame.font.Font object that will be rendered
#          RGBfont -> color of text
#          RGBbg -> color of box encapsulating text
#          transparent -> boolean value of whether you want the encapsulating box to be transparent or not
class TextBox(pygame.sprite.Sprite):
    def __init__(self, pos, dimension, text, font, RGBfont, RGBbg, transparent):
        super().__init__()
        self.bg_width = dimension[0]
        self.bg_height = dimension[1]

        self.text_surface = font.render(text, True, RGBfont)
        self.text_w = self.text_surface.get_width()
        self.text_h = self.text_surface.get_height()

        self.image = pygame.Surface((self.bg_width, self.bg_height)).convert_alpha()
        self.image.fill(RGBbg + ((not transparent) * 255,))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.image.blit(self.text_surface, [self.bg_width/2 - self.text_w/2, self.bg_height/2 - self.text_h/2])
    
    def update(self, pos):
        self.rect.topleft = pos

        

        