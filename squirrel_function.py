import os
import pygame
pygame.init()
import random
import squirrel_config as config

    
class Button: 
    def __init__(self, text, x, y, width, height, enabled): 
        self.text = text 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.enabled = enabled 
        self.rect = pygame.Rect(x, y, width, height)
    def draw(self, screen, font, border_color=(255, 255, 255), border_width=4): # Outer border rectangle 
        border_rect = pygame.Rect( self.x - border_width, self.y - border_width, self.width + 2 * border_width, self.height + 2 * border_width ) 
        pygame.draw.rect(screen, border_color, border_rect) 
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height) 
        pygame.draw.rect(screen, config.BOX_COLOR, button_rect)
        button_text = font.render(self.text, True, config.TEXT_COLOR) 
        text_rect = button_text.get_rect(center=button_rect.center) 
        screen.blit(button_text, text_rect)
    def is_clicked(self, mouse_pos,): 
        if not getattr(self, "enabled", True):
            return False 
        return self.rect.collidepoint(mouse_pos)


class Enemy:
    def __init__(self, random):
        self.size = 40
        self.x = config.ROOM_WIDTH
        self.y = random.randint(0, config.ROOM_HEIGHT - self.size)
        self.speed = random.uniform(2, 6)
        self.color = (config.PLAY_SCREEN)

    def update(self):
        self.x -= self.speed

        if self.x < -self.size:
            self.reset()

    def reset(self):
    
        self.x = config.ROOM_WIDTH
        self.y = random.randint(0, config.ROOM_HEIGHT - self.size)
        self.speed = random.uniform(2, 6)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

def game_over_screen(screen):
    game_over_image = pygame.image.load(config.GAME_OVER).convert_alpha()
    game_over_rect = game_over_image.get_rect(center=(config.WIDTH//2, config.HEIGHT//2))
    screen.blit(game_over_image, game_over_rect)
    pygame.display.flip()

def you_win_screen(screen):
    you_win_image = pygame.image.load(config.YOU_WIN).convert_alpha()
    you_win_rect = you_win_image.get_rect(center=(config.WIDTH//2, config.HEIGHT//2))
    screen.blit(you_win_image, you_win_rect)
    pygame.display.flip()

def apple_load_image(screen):
    apple_image = pygame.image.load(config.APPLE_IMAGE_PATH).convert_alpha()
    apple_image = pygame.transform.scale(apple_image, config.APPLE_SIZE)


def draw_text(screen, text, x, y, font, color=config.BOX_COLOR): 
    rendered_text = font.render(text, True, color) 
    screen.blit(rendered_text, (x, y))

_player_image = None
_warned_once = False

def load_player_image():
    """Call once at startup after pygame.init()."""
    global _player_image, _warned_once
    _player_image = None  # default

    path = getattr(config, "PLAYER_IMAGE_PATH", None)
    size = getattr(config, "PLAYER_IMAGE_SIZE", None)

    if path and os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        if size:
            img = pygame.transform.smoothscale(img, size)
        _player_image = img
    else:
        if not _warned_once:
            print("No player image found or PLAYER_IMAGE_PATH not set; using circle.")
            _warned_once = True

def draw_player(screen, x, y):
    """Draw sprite centered at (x, y); fall back to circle if no image."""
    if _player_image:
        rect = _player_image.get_rect(center=(int(x), int(y)))
        screen.blit(_player_image, rect.topleft)
   
    else:
        pygame.draw.circle(screen, config.PLAYER_COLOR, (int(x), int(y)), config.PLAYER_RADIUS)
        pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), config.PLAYER_RADIUS, 2)


