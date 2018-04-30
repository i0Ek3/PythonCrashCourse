## 
## alien_invasion.py
## @ianpasm(kno30826@gmail.com)
## 2018-04-21 19:28:46
## 
 
#!/usr/bin/env python3
# coding=utf-8

import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    pygame.init()
    ai_settings = Settings()
    #screen = pygame.display.set_mode((1200, 800)) #create window, screen use to show element of the game
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #create window, screen use to show element of the game
    pygame.display.set_caption("Alien Invasion")

    #setting backgroud color
    bg_color = (230, 230, 230)

    # create an airship
    ship = Ship(screen)

    while True: #loop to update code on the screen
        for event in pygame.event.get(): #visit event
            if event.type == pygame.QUIT:
                sys.exit() #exit the game

        screen.fill(ai_settings.bg_color) #every time to loop to update screen, color defined by RGB range in 0~255.
        ship.blitme()
        
        pygame.display.flip() #make the screen visible which pictured on nearly

run_game()

