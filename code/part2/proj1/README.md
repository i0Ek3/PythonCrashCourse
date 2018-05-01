# Alien Invasion

## 1 Equipment Airship

### 1.1 The Plan of Project
    
    - On the bottom, you can control an airship to move and enter space to shoot.
    - Start of the game, there are many aliens moves on the screen.You task is shoot them.
    - When you killed them all then there will show you a new flock of aliens, however faster. 
    - As long as one alien crash your airship or come to the bottom, that means you will lost an airship in your game life.
    - If you lost three airships, you out!


### 1.2 Install Pygame
```Shell
$ # You'd better use python3 to develop
$ brew install hg sdl sdl_image sdl_ttf sdl_mixer portmidi  #install dependencies
$ pip3 install --user hg+http://bitbucket.org/pygame/pygame #install pygame
```


### 1.3 Start Project of the Game

You should create a windows for pygame, check code in alien_invasion.py.Then setting your backgroud color in it. The next you should create a class Settings to save all settings in this project.<br>


### 1.4 Add Airship Image

Add picture to game use free site like http://pixabay.com/. Pygame load .bmp defaultly, you'd better choose a picture which has transparency background color. More visit /images. <br>
![12-2](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj1/pic/12-2.png)<br>


### 1.5 Reconsitution: game_functions Model

We will create a new model named game_functions which will save lots of fuctions for running game and avoid alien_invasion.py much longer.

We split some codes into check_events() and update_screen() in game_functions.py.


### 1.6 Dirve Airship

Now we should make gamer to control the airship to move. Use direction key to response actions. We also use event KEYDOWN and KEYUP to write code.

To avoid the airship move out of the screen we should optimized codes now, so we will revised update() in class ship.

Then we should reconsitute check_events().


### 1.7 Review

### 1.8 Shoot

### 1.9 Summary



## 2 Aliens



## 3 Score




