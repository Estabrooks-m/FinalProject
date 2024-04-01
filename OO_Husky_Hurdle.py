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
        
        self.x = 700
        

    #use to update constant movement (falling + moving forward)
    def update(self):
        self.HuskyCoord.centery += self.yspeed

class Pillar():
    def __init__(self, win):
        self.length = random.randint(0, 600)
        self.pillars = []
        self.pillar_speed = 1
        self.win = win

       
    def generation(self):
        x = 1400
        length = random.randint(0, 501)
        self.rect =  py.Rect(x, 0, 90, length)
        self.rect1 =  py.Rect(x, length + 250, 90, 800 - length + 250)
        return [self.rect, self.rect1]


    def move(self, pillarList):
        for i in pillarList:
            for j in i:
                j.x -= self.pillar_speed
                print("called move")

       

    def draw(self, pillarList):
        for i in pillarList:
            for j in i:
                py.draw.rect( self.win, [0, 255, 0], j)

                print("called draw")
        py.display.update()
        

class Movement(Pillar, Husky):
    #initializes an instance from the Husky Class
    def __init__(self, HuskyInst, PillarInstance, win, clock):
        #creates the screen with specific dimensions
        self.win = win
        self.going = True
        self.HuskyInst = HuskyInst
        self.PillarInst = PillarInstance
        self.clock = clock
        self.x = 8000
        self.pillars = []
        self.score = 2

        
    #constant method for the stuff that is constantly running
    def constant(self):
        print("Checking game loop runs")

        while self.going:


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

            if py.time.get_ticks() > self.x:
                self.pillars.append(self.PillarInst.generation())
                self.x += 8000
                
     
            if len(self.pillars) > 4:
                self.pillars.pop(0)
                self.score += 1
        
            self.PillarInst.draw(self.pillars)
            self.PillarInst.move(self.pillars)
            
            self.HuskyInst.update()
                
                
            self.win.blit(self.HuskyInst.background, (0, 0))
            #moves the husky using the new x and y coordinates
            self.win.blit(self.HuskyInst.husky, self.HuskyInst.HuskyCoord)
            
            #updates the display
            py.display.update()

            #makes it so the program doesnt run at more than 60 fps (limits it so it doesnt run too fast or too slow)
            self.clock.tick(60)
    

class Collision(Husky, Pillar):
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
    win = py.display.set_mode((1400, 1000)) 
    clock = py.time.Clock()
    HuskyInstance = Husky()
    PillarInstance = Pillar(win)
    MovementInstance = Movement(HuskyInstance, PillarInstance, win, clock)
    MovementInstance.constant()
    

main()