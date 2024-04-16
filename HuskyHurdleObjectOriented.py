import pygame as py
import random
import sys


#Huskey class is for creating the necessary objects needed to run the game
class Husky:
    #define the image and the background with coordinates and speed
    def __init__(self, win):
        py.init() 
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

        #outputs the background on the screen with the size of the screensize
        self.background = py.transform.smoothscale(self.background, self.win.get_size())
       

        
        #the following two lines edits and loads the husky image
        self.husky = py.image.load("husky.png")
        self.husky = py.transform.scale(self.husky, (150, 125)) 
        #sets the height to the second element in the string that self.win.get_size() contains
        height = self.win.get_size()[1]
        #get_rect returns the coordinates of the husky (1000 is the height)
        self.HuskyCoord = self.husky.get_rect(center=(100, height  // 2))
        
#for pillar generation and movement
class Pillar():
    #initializes necessary variables
    def __init__(self, win):
        self.pillars = []
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
    def move(self, pillarList, time):
        self.pillar_speed = time/5000
     
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
        self.pausedTime = 0
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
            
            #draws the background image
            self.win.blit(self.HuskyInst.background, (0, 0))

            for event in py.event.get():
                #checks if a key has been clicked
                if event.type == py.KEYDOWN:
                    #if the key is q the program quits
                    if event.key == py.K_q:
                        py.display.quit()
                        sys.exit()
                    #controls when the husky humps
                    if event.key == py.K_SPACE:
                        self.HuskyInst.yspeed = -self.HuskyInst.jumping
                    if event.key == py.K_p:
                      #maintains the while loop when the user pauses
                      waiting = True
                      self.font = py.font.Font(None, 50)

                      while waiting:
                        #creates a variable for the time the user pauses the game
                        startingTime = py.time.get_ticks()
                        #creates text for the user to know whats happening
                        pausedText = self.font.render('PAUSED', True, (0, 0, 160))
                        pausedScreen = self.font.render('(CLICK R to replay, Q to quit, P to unpause)', True, (0, 0, 160))
                        self.win.blit(pausedScreen, dest=(400,420))
                        self.win.blit(pausedText, dest=(640,390))
                        #updates the screen after the text has been blit
                        py.display.update()
                        typed = py.event.wait() 
                       
                        #if p is pressed, game unpauses
                        if typed.type == py.KEYDOWN:
                            if typed.key == py.K_p:
                                waiting = False
                            #if q is pressed, game quits
                            elif typed.key == py.K_q:
                                py.display.quit()
                                sys.exit()
                            #if r is pressed, game goes to collision screen
                            elif typed.key == py.K_r:
                                    waiting = False
                                    self.CollisionInst.ifCollision() == True
                                    #if they want to play again, call reset method
                                    self.reset()
                            #gets the time the user unpauses
                            endingTime = py.time.get_ticks()
                            #creates a variable with the amount of time paused (used for pillar generation)
                            self.pausedTime += endingTime - startingTime




            #generates the pillars using time 
            #self.time accounts for if the user has played a game before (restarts the clock in a way)
            #self.pausedTime holds the amount of time the user was paused during that round
            #self.pillarTime increases the value needed to be met for a pillar to generate (allows time to pass)
            if py.time.get_ticks() - self.time - self.pausedTime > self.pillarTime:
                self.pillars.append(self.PillarInst.generation())
                self.pillarTime += 4000
                    
            #ensures the list of pillars doesn't get too long
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


            #checks if there is a collision
            if self.CollisionInst.collisionTest(self.HuskyInst.HuskyCoord, self.pillars):
                #if collision, returns lose screen + asks user if they want to play again
                if self.CollisionInst.ifCollision():
                    #if they want to play again, call reset method
                    self.reset()

            #resets the husky if it falls off the screen
            if self.HuskyInst.HuskyCoord.y > 10000:
                if self.CollisionInst.ifCollision():
                    self.reset()

            #draws the husky image
            self.win.blit(self.HuskyInst.husky, self.HuskyInst.HuskyCoord)
            #following two lines calls the draw and move methods from the pillar class
            self.PillarInst.draw(self.pillars)
            self.PillarInst.move(self.pillars, self.pillarTime )
            #updates the display
            py.display.update()
            #makes it so the program doesnt run at more than 60 fps (limits it so it doesnt run too fast or too slow)
            self.clock.tick(60)

class Collision():
    def __init__(self, win):
        #loads the lose screen image
        self.loseScreen = py.image.load("LoseScreen.png")
        self.win = win
        #edits the size of the lose screen image
        self.loseScreen = py.transform.smoothscale(self.loseScreen, self.win.get_size())
        
        self.PlayerScore = 0
        self.font = py.font.Font(None, 50)
        self.passedPillars = []



    #checks for collision
    def collisionTest(self, HuskyCoord, PillarList):
        
        for i in PillarList:
            #updates the score if the pillar hasn't passed yet and the pillar is less than the x coordinates of the husky
            if i not in self.passedPillars:
                if HuskyCoord.x > i[0].x:
                    self.PlayerScore += 1
                    self.passedPillars.append(i)

 
            #blits the users score + details for how to pause and quit
            score = self.font.render(f'Score: {self.PlayerScore}', True, (0, 0, 160))
            self.win.blit(score, dest=(50, 50))
            pause = self.font.render(f"Press P to pause", True, (0, 0, 160))
            self.win.blit(pause, dest=(50, 80))
            quit = self.font.render(f"Press Q to quit", True, (0, 0, 160))
            self.win.blit(quit, dest=(50, 110))
            #checks for collision
            for j in i:
                if j.colliderect(HuskyCoord):
                    return True
        
    #method for when there is a collision 
    def ifCollision(self):
        #calls the lose screen method
        self.LoseScreen()
        text = self.font.render(' Collision! Would you like to play again?', True, (0, 112, 200))
        moretext = self.font.render('(CLICK R to play, Q to quit)', True, (0, 112, 200))
        #using an fstring to display the score
        score = self.font.render(f'Score: {self.PlayerScore}', True, (0, 112, 200))
        self.win.blit(text, dest=(400,360))
        self.win.blit(moretext, dest=(500,420))
        self.win.blit(score, dest=(610,480))
        py.display.update()

        #the while loop ensure that its only quit or space being picked (it wont respond to the other keys)
        while True:
        #waits for an event from the user (like clicking a key)
         for event in py.event.get():
            if event.type == py.KEYDOWN:
                if event.key == py.K_q:
                    py.quit()
                    sys.exit()
                if event.key == py.K_r:
                   self.PlayerScore = 0
                   return True
                
    #creates and returns a lose screen
    def LoseScreen(self):
         self.win.blit(self.loseScreen, (0, 0))


#use for calling necessary methods + creating instances
def main():
    #creates the screen
    win = py.display.set_mode(flags=py.FULLSCREEN)
    #creates a variable for the clock
    clock = py.time.Clock()
    #creates an instance of the husky class, passing it win
    HuskyInstance = Husky(win)
    #same as previous line but for the pillar class
    PillarInstance = Pillar(win)
    #creates an instance of the movement instance, passing it the other instances, win, and clock
    MovementInstance = Movement(HuskyInstance, PillarInstance, win, clock)
    #calls the constant method from the Movement class
    MovementInstance.constant()
    

main()