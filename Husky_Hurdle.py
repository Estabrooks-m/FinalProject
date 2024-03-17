# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 19:37:40 2024

@author: Estabrooks
"""
def main():
    #imports the pygame module as py
    import pygame as py
    import random

    py.init() 
    #creates the screen with specific dimensions
    win = py.display.set_mode((1400, 1000)) 
    # set caption
    py.display.set_caption("Husky Hurdle")

    #creates the "speed" that it falls
    falling = 0.15
    #creates the "speed" that it jumps
    jumping = 5
    #creates the "speed" in the ydirection
    yspeed = 1
    
    going = True
    
    #loads the background image
    background = py.image.load("background.png")
    #edits the size of the background image
    background = py.transform.scale(background, (1400, 1000)) 
    #loads the husky image
    husky = py.image.load("husky.png")
    #edits the size of the husky image
    husky = py.transform.scale(husky, (150, 150)) 
    #get_rect returns the coordinates of the husky (1000 is the height )
    HuskyCoord = husky.get_rect(center=(100, 1000 // 2))
    #creates a variable for the fps
    clock = py.time.Clock()
    length = random.randint(0, 600)
    x = 700

    print(clock)

    while going:
    
        #adds the background
        win.blit(background, (0, 0))
    
        #creates the pillars
        #if HuskyCoord.centerx % 750 == 0:
        
        
        rect = py.draw.rect(win, [0, 255, 0], py.Rect(x, 0, 90, length))
        rect2 = py.draw.rect(win, [0, 255, 0], py.Rect(x, length + 250, 90, (800 - length + 250)))


       # Husky(husky, background)
       # obj = Husky(husky, background)


        #print(HuskyCoord)
        for event in py.event.get():
            if event.type == py.QUIT:
                going = False
            elif event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                  yspeed = -jumping
                #a fun little cheat feature
                if event.key == py.K_RIGHT:
                    HuskyCoord.centerx += 150
        
        #makes the husky fall (add because the coordinates get more positive as you go down)
        yspeed += falling
        #adjusts the y coordinate after accounting for if the user clicked space and falling
        HuskyCoord.centery += yspeed
        #adjusts the x coordinate (constant)
        if HuskyCoord.centerx < 700:
            HuskyCoord.centerx += 1
        if HuskyCoord.centerx == 700:
            x -= 3
        print(HuskyCoord)
        print(rect.left)

        """
        if x % 400:
            y = 700
            length = random.randint(0, 600)
            py.draw.rect(win, [0, 255, 0], py.Rect(y, 0, 90, length))
            py.draw.rect(win, [0, 255, 0], py.Rect(y, length + 250, 90, (800 - length + 250)))
            None
        """
        #moves the husky using the new x and y coordinates
        win.blit(husky, HuskyCoord)
      #  win.blit(rect, (rect.left))
      #  win.blit(rect2, (rect.left))
        

         #displays/updates
        py.display.update()
        #makes it so the program doesnt run at more than 60 fps (limits it so it doesnt run too fast or too slow)
        clock.tick(60)


    #closes the pygame window	 
    py.quit() gits
    

main()
