## 
## alien_invasion.py
## @ianpasm(kno30826@gmail.com)
## 2018-04-21 19:28:46
## 
 
#!/usr/bin/env python3
# coding=utf-8

import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

run_game()

