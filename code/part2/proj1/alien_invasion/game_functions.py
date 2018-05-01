## 
## game_functions.py
## @ianpasm(kno30826@gmail.com)
## 2018-05-01 19:17:49
## 
 
#!/usr/bin/env python3

import sys
import pygame

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False 
    if event.key == pygame.K_LEFT:
        ship.moving_left = False 


def check_events(ship):
    """response click and mouse events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()


