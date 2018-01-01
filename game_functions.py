import sys
import pygame
from bullet import Bullet

# Game Functions

# KEYSTROKE EVENTS
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT: # check if right arrow key is pressed
        ship.moving_right = True
    elif event.key == pygame.K_LEFT: # check if left arrow key is pressed
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT: # check if right arrow key is pressed
        ship.moving_right = False
    elif event.key == pygame.K_LEFT: # check if left arrow key is pressed
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypressed and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: # detects a keydown event
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP: # detects a keyup event
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""

    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites(): # bullets.sprites() method returns a list of all sprites in the group bullets
        bullet.draw_bullet() # method from Bullet class
    # Redraw ship onscreen after filling the background
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions
    bullets.update() # calls bullet.update() for each bullet we place in the group bullets

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy(): # you shouldn't remove items from a list or group within a for loop
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
