# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 12:49:27 2024

@author: Estabrooks
"""
import pygame as py
import random

#Huskey class is for creating the necessary objects needed to run the game
class Husky:
    #define the image and the background with coordinates and speed
    def __init__(self):
        print("Checking for initializing")
        py.init() 
        #creates the screen with specific dimensions
        self.win = py.display.set_mode((1400, 1000)) 
        # set caption
        py.display.set_caption("Husky Hurdle")
        #creates the "speed" that it falls
        self.falling = 0.15
        #creates the "speed" that it jumps
        self.jumping = 5
        #creates the "speed" in the ydirection
        self.yspeed = 1

    
        #loads the background image
        self.background = py.image.load("background.png")
        #edits the size of the background image
        self.background = py.transform.scale(self.background, (1400, 1000)) 
        #loads the husky image
        self.husky = py.image.load("husky.png")
        #edits the size of the husky image
        self.husky = py.transform.scale(self.husky, (150, 150)) 
        #get_rect returns the coordinates of the husky (1000 is the height )
        self.HuskyCoord = self.husky.get_rect(center=(100, 1000 // 2))
        #creates a variable for the fps
        self.clock = py.time.Clock()
        self.length = random.randint(0, 600)
        self.x = 700


    #use to create the pillars (using the random function)
    def pillars(self):
            self.rect = py.draw.rect(self.win, [0, 255, 0], py.Rect(self.x, 0, 90, self.length))
            self.rect2 = py.draw.rect(self.win, [0, 255, 0], py.Rect(self.x, self.length + 250, 90, (800 - self.length + 250)))
            py.display.update()
        

    #use to update constant movement (falling + moving forward)
    def update(self):
        self.HuskyCoord.centery += self.yspeed



class Movement(Husky):
    #initializes an instance from the Husky Class
    def __init__(self, HuskyInstance):
        self.going = True
        self.HuskyInst = HuskyInstance
        

    #constant method for the stuff that is constantly running
    def constant(self):
        print("Checking game loop runs")

        while self.going:
            #HuskyInst = Husky()
            #Collision(HuskyInst)
            """if self.HuskyInst.x % 400 ==0:
                 self.HuskyInst.pillars()"""

            #  win.blit(rect, (rect.left))
            #  win.blit(rect2, (rect.left))
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.going = False
                elif event.type == py.KEYDOWN:
                    if event.key == py.K_SPACE:
                        self.HuskyInst.yspeed = -self.HuskyInst.jumping
                    #a fun little cheat feature
                    if event.key == py.K_RIGHT:
                        self.HuskyInst.HuskyCoord.centerx += 150

            #makes the husky fall (add because the coordinates get more positive as you go down)
            self.HuskyInst.yspeed += self.HuskyInst.falling
            #adjusts the y coordinate after accounting for if the user clicked space and falling
            self.HuskyInst.HuskyCoord.centery += self.HuskyInst.yspeed
            #adjusts the x coordinate (constant)
            if self.HuskyInst.HuskyCoord.centerx < 700:
                self.HuskyInst.HuskyCoord.centerx += 1
            if self.HuskyInst.HuskyCoord.centerx == 700:
                self.HuskyInst.x -= 3       


            self.HuskyInst.update()
    
            self.HuskyInst.pillars()
            #self.HuskyInst.pillars()
            self.HuskyInst.win.blit(self.HuskyInst.background, (0, 0))
            #moves the husky using the new x and y coordinates
            self.HuskyInst.win.blit(self.HuskyInst.husky, self.HuskyInst.HuskyCoord)
            py.display.update()

            #displays/updates

            #makes it so the program doesnt run at more than 60 fps (limits it so it doesnt run too fast or too slow)
            self.HuskyInst.clock.tick(60)
    


class Collision(Husky):
    def __init__(self):
        #gets necessary variables
        pass

    def collisionTest(self):
        #checks for collision
        pass

    def ifCollision(self):
        #calls the lose screen and maybe asks the player if they want to play again
        #this means we'll need to check for keys clicked
        pass

    def WinScreen(self):
        #creates and returns a win screen
        pass

    def LoseScreen(self):
        #creates and returns a lose screen
        pass

#use for calling necessary methods + creating instances
def main():

    HuskyInstance = Husky()
    MovementInstance = Movement(HuskyInstance)
    MovementInstance.constant()




main()