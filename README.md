Our project is "Husky Hurdle" which is a take on flappy bird. 
The user is playing against themselves, the goal is to avoid obsitcals 
and score as high as possible.

Rules and Play:
To play the game the user will use the space bar to make the husky move up and down to avoid the obsticals.
The code will generate random sized pillars as the user moves through the game.
If the user hits the pillars at any time the game is over and the score is equal to how many pillars the player passed.

Tracking:
The game uses a pixel based tracking system, so if the pixals of the players icon overlap/touch the pixles of the genrated 
rectangle the game countes that as a "collison" and ends the game. 

Downloading Pygame:
Our code uses the pygame library which is not included in the python 3 instalation.
In order to download pygame follow these steps:
1. Open the command prompt window 
2. Type into the bar "pip install pygame"
3. Check if pygame has installed correclty by restarting the command window and typing "import pygame"



Citations:  <br />
Pygame installation instructions: https://www.geeksforgeeks.org/how-to-install-pygame-in-windows/