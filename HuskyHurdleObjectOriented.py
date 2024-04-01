import pygame as py
import random



#Huskey class is for creating the necessary objects needed to run the game
class Husky:
    #define the image and the background with coordinates and speed
    def __init__(self):
        print("Checking for initializing")
        py.init() 
        #set caption
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
        self.pillar_speed = 3
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


       

    def draw(self, pillarList):
        for i in pillarList:
            for j in i:
                py.draw.rect( self.win, [0, 255, 0], j)

   

        


class Movement():
    #initializes an instance from the Husky Class
    def __init__(self, HuskyInst, PillarInstance, win, clock):
        #creates the screen with specific dimensions
        self.win = win
        self.going = True
        self.HuskyInst = HuskyInst
        self.PillarInst = PillarInstance
        self.clock = clock
        self.x = 5000
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


            if py.time.get_ticks() > self.x:
                self.pillars.append(self.PillarInst.generation())
                
                if self.x < 20000:
                    self.x += 5000
                elif self.x < 40000 and self.x > 20000:
                    self.x += 4000
                elif self.x < 50000 and self.x > 40000:
                    self.x += 3000
                else:
                    self.x += 2500
                
     
            if len(self.pillars) > 4:
                self.pillars.pop(0)
                self.score += 1
        

            

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
                
                
            self.win.blit(self.HuskyInst.background, (0, 0))
            #moves the husky using the new x and y coordinates


            self.win.blit(self.HuskyInst.husky, self.HuskyInst.HuskyCoord)
            
            self.PillarInst.draw(self.pillars)
            self.PillarInst.move(self.pillars)
            #updates the display
            py.display.update()

            #makes it so the program doesnt run at more than 60 fps (limits it so it doesnt run too fast or too slow)

            if Collision(self.HuskyInst.HuskyCoord, self.pillars, self.win).collisionTest():
                Collision(self.HuskyInst.HuskyCoord, self.pillars, self.win).ifCollision()
                print("checking")
                self.HuskyInst.HuskyCoord.center = (100, 1000 // 2)
                self.pillars = []
                self.score = 0
                self.x = 5000


            self.clock.tick(60)

    


class Collision():
    def __init__(self, HuskyCoord, PillarList, win):
        #gets necessary variables
        self.HuskyCoord = HuskyCoord
        self.PillarList = PillarList
        self.win = win
        

    def collisionTest(self):
        for i in self.PillarList:
            for j in i:
                #if self.HuskyCoord.x == j.x and self.HuskyCoord == j.y:
                if self.HuskyCoord.colliderect(j):
                    return True

        #if husky x position == pillar x position and husky y position == pillar y position:
            #losescreen (need score)
        #checks for collision
        

        """    def ifCollision(self):
                font = py.font.Font('freesansbold.ttf', 32)
                text = font.render(' Collision! Would you like to play again? ', True, (0, 255, 0))
                self.win.blit(text, dest=(500,500))
        """

                        
    def ifCollision(self):
        font = py.font.Font(None, 100)
        text = font.render(' Collision! Would you like to play again? ', True, (0, 255, 0))
        self.win.blit(text, dest=(20,500))
        py.display.update()
        event = py.event.wait()
        if event.type == py.QUIT:
                self.going = False
        elif event.type == py.KEYDOWN:
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