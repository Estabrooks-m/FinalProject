import pygame as py
import random
import sys


#Huskey class is for creating the necessary objects needed to run the game
class Husky:
    #define the image and the background with coordinates and speed
    def __init__(self, win):
        print("Checking for initializing")
        py.init() 
        #set caption
        py.display.set_caption("Husky Hurdle")
        #creates the "speed" that it falls
        self.falling = 0.15
        #creates the "speed" that it jumps
        self.jumping = 4.5
        #creates the "speed" in the ydirection
        self.yspeed = 1

        self.win = win
    
        #loads the background image
        self.background = py.image.load("background.png")
        #edits the size of the background image

        #outputs the background on the screen with the size of the screensize
        self.background = py.transform.smoothscale(self.background, self.win.get_size())

        #loads the husky image
        self.husky = py.image.load("husky.png")
        #edits the size of the husky image
        self.husky = py.transform.scale(self.husky, (150, 125)) 
        #sets the height to the second element in the string that self.win.get_size() contains
        height = self.win.get_size()[1]
        #get_rect returns the coordinates of the husky (1000 is the height)
        self.HuskyCoord = self.husky.get_rect(center=(100, height  // 2))
        

class Pillar():
    def __init__(self, win):
        #initializes an empty list for the pillars
        self.pillars = []
        #sets the pilar speed to 3
        self.pillar_speed = 3
        #initializes win
        self.win = win

    def generation(self):
        #sets the xcoordinate that the pillar will be generated at to the width of the screen
        x = self.win.get_size()[0]
        #generates a random number from 0 to 600
        length = random.randint(0, 501)
        #the two lines below create a pair of rectangles with the same x coordinate
        self.rect =  py.Rect(x, 0, 90, length)
        self.rect1 =  py.Rect(x, length + 300, 90, 800 - length + 300)
        #returns the rectangles as a list
        return [self.rect, self.rect1]

    #loops through the list of pillars and moves them
    def move(self, pillarList):
        for i in pillarList:
            for j in i:
                j.x -= self.pillar_speed

    #draws the pilllars by looping through the list
    #Note: it has to be a nested for loop because we wanted to keep the pillars together as a list in the pillar clist
    def draw(self, pillarList):
        for i in pillarList:
            for j in i:
                py.draw.rect( self.win, [0, 112, 200], j)


class Movement():
    #initializes an instance from the Husky Class
    def __init__(self, HuskyInst, PillarInstance, win, clock):
        #creates the screen with specific dimensions
        self.win = win
        self.going = True
        self.HuskyInst = HuskyInst
        self.PillarInst = PillarInstance
        self.clock = clock
        self.pillarTime = 12000
        self.pillars = []
        self.score = 0
        #important for the reset method
        self.time = 0
        self.CollisionInst = Collision(self.win)
        self.screenSize = self.win.get_size()

    def reset(self):
            self.HuskyInst.HuskyCoord.center = (100, self.screenSize[1] // 2)
            self.pillars = []
            self.score = 0
            self.pillarTime = 10000
            self.time = py.time.get_ticks()
            self.going = True

    #constant method for the stuff that is constantly running
    def constant(self):
        while self.going:
            

            for event in py.event.get():
                
                if event.type == py.KEYDOWN:
                    if event.type == py.K_q:
                        py.display.quit()
                        #py.quit()
                        sys.exit()
                    if event.key == py.K_SPACE:
                        self.HuskyInst.yspeed = -self.HuskyInst.jumping

                        #working on a way to pause and then end the game (This would mean getting rid of the if q is clicked statement)
                        """   if event.type == py.K_p:
                        py.event.wait()
                        if event.key == py.K_p:
                            continue
                        if py.event.wait() == py.K_q:
                            self.CollisionInst.ifCollision() == True
                            #if they want to play again, call reset method
                            self.reset()"""



            if py.time.get_ticks() - self.time > self.pillarTime:
                self.pillars.append(self.PillarInst.generation())
                
                if self.pillarTime < 20000:
                    #speeds up the generation of the pillars
                    self.pillarTime += 4000
                    self.HuskyInst.yspeed += 0.2
                elif self.pillarTime < 40000 and self.pillarTime > 20000:
                    #speeds up the generation of the pillars
                    self.pillarTime += 3500
                elif self.pillarTime < 50000 and self.pillarTime > 40000:
                    #speeds up the generation of the pillars
                    self.pillarTime += 3000
                else:
                    #speeds up the generation of the pillars
                    self.pillarTime += 2500
                    #speeds up the falling speed
                    
                
            if len(self.pillars) > 4:
                self.pillars.pop(0)
         
        
            #makes the husky fall (add because the coordinates get more positive as you go down)
            self.HuskyInst.yspeed += self.HuskyInst.falling
            #adjusts the y coordinate after accounting for if the user clicked space and falling
            self.HuskyInst.HuskyCoord.centery += self.HuskyInst.yspeed
            #adjusts the x coordinate (constant)
            if self.HuskyInst.HuskyCoord.centerx < 700:
                self.HuskyInst.HuskyCoord.centerx += 1
            if self.HuskyInst.HuskyCoord.centerx == 700:
                self.HuskyInst.HuskyCoord.centerx += 0    
                

             #moves the husky using the new x and y coordinates
            self.HuskyInst.HuskyCoord.centery += self.HuskyInst.yspeed



            #draws the background image
            self.win.blit(self.HuskyInst.background, (0, 0))

            #checks if there is a collision
            if self.CollisionInst.collisionTest(self.HuskyInst.HuskyCoord, self.pillars):
                #if collision, returns lose screen + asks user if they want to play again
                if self.CollisionInst.ifCollision():
                    #if they want to play again, call reset method
                    self.reset()

            #resets the husky if it falls off the screen
            """if self.HuskyInst.HuskyCoord.y == 1500:
                if self.CollisionInst.ifCollision():
                    self.reset()"""

            #draws the husky image
            self.win.blit(self.HuskyInst.husky, self.HuskyInst.HuskyCoord)
            #calls the draw method from the pillar class
            self.PillarInst.draw(self.pillars)
            #calls the move method from the pillar class
            self.PillarInst.move(self.pillars)
            #updates the display
            py.display.update()
            #makes it so the program doesnt run at more than 60 fps (limits it so it doesnt run too fast or too slow)
            self.clock.tick(60)

class Collision():
    def __init__(self, win):
        #gets necessary variables
        #loads the lose screen image
        self.loseScreen = py.image.load("LoseScreen.png")
        #edits the size of the lose screen image
        #self.loseScreen = py.transform.scale(self.loseScreen, (1400, 1000)) 
        self.win = win
        self.loseScreen = py.transform.smoothscale(self.loseScreen, self.win.get_size())
        
        self.PlayerScore = 0
        self.font = py.font.Font(None, 75)

    #checks for collision
    def collisionTest(self, HuskyCoord, PillarList):
        for i in PillarList:
            #if the x value of the pillar is 584 add to the score
            if i[0].x == 583:
                self.PlayerScore += 1
            elif i[0].x == 584:
                self.PlayerScore += 1
            elif i[0].x == 585:
                self.PlayerScore += 1 

            score = self.font.render(f'Score: {self.PlayerScore}', True, (0, 112, 200))
            self.win.blit(score, dest=(50, 150))
            for j in i:
                if j.colliderect(HuskyCoord):
                    return True
        
    #method for when there is a collision 
    def ifCollision(self):
        self.LoseScreen()
        text = self.font.render(' Collision! Would you like to play again?', True, (0, 112, 200))
        moretext = self.font.render('(CLICK R to play, Q to quit)', True, (0, 112, 200))
        #using an fstring to display the score
        score = self.font.render(f'Score: {self.PlayerScore}', True, (0, 112, 200))
        self.win.blit(text, dest=(230,360))
        self.win.blit(moretext, dest=(540,420))
        self.win.blit(score, dest=(545,480))
        py.display.update()

        #the while loop ensure that its only quit or space being picked (it wont respond to the other keys)
        while True:
            #waits for an event from the user (like clicking a key)
         for event in py.event.get():
            if event.type == py.K_q:
                py.quit()
            elif event.type == py.KEYDOWN:
                if event.key == py.K_r:
                   self.PlayerScore = 0
                   return True
                
    #creates and returns a lose screen
    def LoseScreen(self):
         self.win.blit(self.loseScreen, (0, 0))


#use for calling necessary methods + creating instances
def main():

    win = py.display.set_mode(flags=py.FULLSCREEN)
    
    


    clock = py.time.Clock()
    HuskyInstance = Husky(win)
    PillarInstance = Pillar(win)
    MovementInstance = Movement(HuskyInstance, PillarInstance, win, clock)
    MovementInstance.constant()
    

main()