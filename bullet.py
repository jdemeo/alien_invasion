# Creating the Bullet Class
import pygame
from pygame.sprite import Sprite
# When you use sprites, you can group related elements in yhour game and act on all the grouped elements at once.

class Bullet(Sprite):
    """A Class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__() # inherit properly from Sprite
        self.screen = screen

        # Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height) # build bullets rect from scratch
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top # makes bullets appear at top center of ship

        # Store the bullet's position as a decimal value. (the y-coordinate)
        self.y = float(self.rect.y)

        # Store color and speed settings
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
