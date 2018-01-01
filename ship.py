import pygame

# Creating the Ship Class
class Ship():

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp') # returns a surface representing the ship
        self.rect = self.image.get_rect() # access surface's rect attribute (rect = rectangles); allows to treat elements
        # as rectangles which are simple to deal with; one can access the top, bottom, left, and right edges, and center
        self.screen_rect = screen.get_rect() # stores screen's rect

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx # places the x-coordinate of the ship's center to match the center of screen
        self.rect.bottom = self.screen_rect.bottom # places the y-coordinate of the ship's bottom to match the bottom of scren

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) # draws image to screen at position specific by self.rect
