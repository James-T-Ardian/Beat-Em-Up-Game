import pygame

# Get hitbox by creating a rectangle bounding only parts of the image that is not transparent 
def getMaskRect(surf, top, left):
        surf_mask = pygame.mask.from_surface(surf)
        rect_list = surf_mask.get_bounding_rects()
        surf_mask_rect = rect_list[0].unionall(rect_list)
        surf_mask_rect.move_ip(top, left)
        return surf_mask_rect