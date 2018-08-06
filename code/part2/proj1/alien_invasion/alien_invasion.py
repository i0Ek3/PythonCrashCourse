## 
## alien_invasion.py
## @ianpasm(kno30826@gmail.com)
## 2018-04-21 19:28:46
## 
 
#!/usr/bin/env python3
# coding=utf-8

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf 
from pygame.sprite import Group 


def run_game():
    pygame.init()
    ai_settings = Settings()
    #screen = pygame.display.set_mode((1200, 800)) #create window, screen use to show element of the game
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #create window, screen use to show element of the game
    pygame.display.set_caption("Alien Invasion")

    #setting backgroud color
    bg_color = (230, 230, 230)

    # create an airship
    ship = Ship(ai_settings, screen)
    
    #create a group to save bullets
    bullets = Group()

    while True: #loop to update code on the screen
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets) 
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()

