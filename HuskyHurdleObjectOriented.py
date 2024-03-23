import pygame as py
import random




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


    def pillars(self):
        #use to create the pillars (using the random function)
        None

    def flap(self):
        while True:
            #use to create the movement when the user presses certain keys
            None

    def update(self):
        self.HuskyCoord.centery += self.yspeed
        #use to have the constant movement (falling + moving forward)
        None
class Movement(Husky):
    
    def __init__(self, HuskyInstance):
        self.going = True
        self.HuskyInst = HuskyInstance
        

    def constant(self):
        print("Checking game loop runs")
        while self.going:
            #HuskyInst = Husky()
            #Collision(HuskyInst)
        

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

            self.HuskyInst.update()
            self.HuskyInst.win.blit(self.HuskyInst.background, (0, 0))
            #moves the husky using the new x and y coordinates
            self.HuskyInst.win.blit(self.HuskyInst.husky, self.HuskyInst.HuskyCoord)
            py.display.update()

            #displays/updates

            #makes it so the program doesnt run at more than 60 fps (limits it so it doesnt run too fast or too slow)
            self.HuskyInst.clock.tick(60)
    
"""    def clicked(self):
        #print(HuskyCoord)
        for event in py.event.get():
            if event.type == py.QUIT:
                self.going = False
            elif event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                  self.HuskyInst.yspeed = -self.HuskyInst.jumping
                #a fun little cheat feature
                if event.key == py.K_RIGHT:
                    self.HuskyInst.HuskyCoord.centerx += 150"""

class Collision(Husky):
    def __init__(self):
        #adds the background
        
        None

    def collisionTest(self):
        #checks for collision
        None

    def ifCollision(self):
        #returns a game over screen
        None

def main():

    HuskyInstance = Husky()
    MovementInstance = Movement(HuskyInstance)
    MovementInstance.constant()
  #  MovementInstance.clicked()



main()
