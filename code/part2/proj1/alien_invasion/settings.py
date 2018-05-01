## 
## settings.py
## @ianpasm(kno30826@gmail.com)
## 2018-04-29 20:34:12
## 
 
#!/usr/bin/env python3

class Settings():
    """The class to save all settings in this project"""
    
    def __init__(self):
        """initial"""

        #setting screen
        self.screen_width = 1200
        self.screen_height =  800
        self.bg_color = (230, 230, 230)

        #the settings of airship
        self.ship_speed_factor = 1.5


