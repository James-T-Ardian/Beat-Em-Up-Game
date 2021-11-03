import pygame
from os import walk

LEFT = -1
RIGHT = 1
UP = -1
DOWN = 1
IN_PLACE = 0

# Player character in pygame.
#
#   Input: pos -> character topleft coordinate on screen in (x ,y) tuple form. Y POSITION MUST ALWAYS BE GROUND.  
#          control -> array that specifies character controls using pygame key inputs (ex. pygame.K_b for b) where position
#                     in array determines which action it corresponds to. In [jump, attack, dash, right, left] form. 
#          face_right -> bolean value that determines whether character faces right at the start
#
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, control, face_right = True):
        super().__init__()

        # Imports character frames for animation
        self._import_character_assets()

        # Animation variables 
        self.frame_index = 0
        self.animation_speed = 0.2
        self.image = self.animations['idle'][self.frame_index]
        
        # Rect to determine character, player hitbox and weapon hitbox
        self.rect = self.image.get_rect(topleft = pos)
        self.player_hitbox = _getMaskRect(self.image ,*self.image.get_rect(topleft = pos).topleft).move(-2,0)
        self.weapon_hitbox = pygame.Rect.copy(self.player_hitbox)
        self.starting_pos = pos

        # Movement variables
        self.move_speed = 3
        self.apply_gravity = False
        self.jump_speed = 60
        self.gravity = 3

        # Three direction variables: for normal movement, for animation + attack, for dash. All needed to make attack + dash combos not wonky.
        self.direction = pygame.math.Vector2(0,0)
        self.facing_right = face_right
        self.dash_right = True

        # Cooldowns
        self.last_dash = pygame.time.get_ticks() - 1000
        self.dash_cooldown = 700
        self.last_attack = pygame.time.get_ticks() - 1000
        self.attack_cooldown = 1000
        self.last_jump = pygame.time.get_ticks() - 1000
        self.jump_cooldown = 500

        # Player states = 'attack', 'dash', 'idle', 'jump', 'run'
        self.state = 'idle'

        # Player keyboard controls
        self.jump_key, self.attack_key, self.dash_key, self.right_key, self.left_key = control
    
    def _import_character_assets(self):
        character_path = 'sprites/player/'
        self.animations = {'attack':[], 'dash':[], 'idle':[], 'jump':[], 'run':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = _import_folder(full_path)

    def _get_input(self):
        keys = pygame.key.get_pressed()
        now = pygame.time.get_ticks()

        # Move right or left. Cant change dash direction too early in dash. Cant change attack + animation direction mid attack. 
        if keys[self.right_key]:
            self.state = 'run'
            if now - self.last_attack > self.attack_cooldown / 2.5:
                self.facing_right = True
            if now - self.last_dash > self.dash_cooldown / 2.5:
                self.dash_right = True
                self.direction.x = RIGHT
        elif keys[self.left_key]: 
            self.state = 'run'
            if now - self.last_attack > self.attack_cooldown / 2.5:
                self.facing_right = False
            if now - self.last_dash > self.dash_cooldown / 2.5:    
                self.dash_right = False
                self.direction.x = LEFT
        else: 
            self.state = 'idle'
            self.direction.x = IN_PLACE
            self.dash_right = self.facing_right

        # Jump
        if keys[self.jump_key] and not self.apply_gravity and now - self.last_jump >= self.jump_cooldown:
            self.last_jump = now
            self.state = 'jump'
            self.direction.y = UP
        # Not input but just for fall animation since this line needs to be before code for dash :/
        if self.apply_gravity:
            self.state = 'jump'
        
        # Dash
        if keys[self.dash_key] and now - self.last_dash >= self.dash_cooldown and now - self.last_attack > self.attack_cooldown / 2.8:
            self.state = 'dash'
            self.last_dash = now
            self.move_speed = 50
            self.direction.y = IN_PLACE
            self.direction.x = 1 if self.dash_right else -1
        # Make dash smoother
        elif now - self.last_dash <= self.dash_cooldown / 2.5:                    
            self.state = 'dash'
            self.move_speed = 7
            self.direction.y = IN_PLACE
            self.direction.x = 1 if self.dash_right else -1
        else:
            self.move_speed = 3
        
        # Attack
        if keys[self.attack_key] and now - self.last_attack >= self.attack_cooldown:
            self.last_attack = now
            self.state = 'attack'
            self.move_speed = 0
            self.direction.y = IN_PLACE
        # Make attack smoother and generate weapon hitbox only after some delay 
        elif now - self.last_attack <= self.attack_cooldown / 2.5: 
            self.state = 'attack'
            if now - self.last_attack > self.attack_cooldown / 5:
                self.weapon_hitbox.update(self.player_hitbox.x + (25 if self.facing_right else -25),self.player_hitbox.y,self.player_hitbox.width, self.player_hitbox.height)
            self.move_speed = 0
            self.direction.y = IN_PLACE
        else:
            self.weapon_hitbox.update(0,0,self.player_hitbox.width, self.player_hitbox.height)
 
    def _gravity(self):
        # When player not at ground, gravity is applied :O
        if self.direction.y == UP:
            self.apply_gravity = True
        if self.apply_gravity:
            self.direction.y = DOWN
        if self.rect.y == self.starting_pos[1]:
            self.direction.y = IN_PLACE
            self.apply_gravity = False
    
    def _update_image_and_hitboxes_location(self):
        # To make sure player does not go out of bounds of screen
        if -20 > self.rect.x and self.direction.x == LEFT or self.rect.x > pygame.display.get_window_size()[0] - 40 and self.direction.x == RIGHT:
            self.direction.x = IN_PLACE

        self.rect.x += self.direction.x * self.move_speed
        self.rect.y += self.direction.y * self.gravity if self.apply_gravity else self.direction.y * self.jump_speed 
        self.player_hitbox.x += self.direction.x * self.move_speed
        self.player_hitbox.y += self.direction.y * self.gravity if self.apply_gravity else self.direction.y * self.jump_speed 

    
    def _animate(self):
        animation = self.animations[self.state]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        if self.facing_right:
            self.image = animation[int(self.frame_index)]
        else:
            self.image = pygame.transform.flip(animation[int(self.frame_index)], True, False)
            
    def update(self):
        self._get_input()
        self._update_image_and_hitboxes_location()
        self._animate()
        self._gravity()

# Get files from folder
def _import_folder(path):
	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list

# Get hitbox by creating a rectangle bounding only parts of the image that is not transparent 
def _getMaskRect(surf, top, left):
        surf_mask = pygame.mask.from_surface(surf)
        rect_list = surf_mask.get_bounding_rects()
        surf_mask_rect = rect_list[0].unionall(rect_list)
        surf_mask_rect.move_ip(top, left)
        return surf_mask_rect



