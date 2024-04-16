Our project is "Husky Hurdle" which is a take on flappy bird. 
The user is playing against themselves, the goal is to avoid obstacles 
and score as high as possible.

Rules and Play:
To play the game the user will use the space bar to make the husky move up and down to avoid the obstacles.
The code will generate random-sized pillars as the user moves through the game.
If the user hits the pillars at any time the game is over and the score is equal to how many pillars the player passed.

Tracking:
The game uses a pixel-based tracking system, so if the pixels of the player's icon overlap/touch the pixels of the generated 
rectangle the game counts that as a "collision" and ends the game. 

Downloading Pygame:
Our code uses the pygame library which is not included in the python 3 installation.
In order to download pygame follow these steps:
1. Open the command prompt window 
2. Type into the bar "pip install pygame"
3. Check if pygame has installed correctly by restarting the command window and typing "import pygame"


Note:

When the game begins, you have to wait for the husky to reach the middle of the screen for the pillar generation to start.

Make sure your cursor isn’t clicked on the code or the program might not register that you've clicked a letter because you’ll just be typing directly into the code.

Click P to pause (while playing)

Click R to restart (from the pause screen or lose screen)

Click Q to quit (at any time)

Citations:  <br />
Pygame installation instructions: https://www.geeksforgeeks.org/how-to-install-pygame-in-windows/
