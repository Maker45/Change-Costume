# import pygame
import pygame

# initializes the pygame modules 
pygame.init()

# sets the variable WHITE to the following RGB values
WHITE = (255, 255, 255)

# sets the width and height of the screen
WIDTH = 800
HEIGHT = 500

# Create a Clock object to keep track of the fps
FPSCLOCK = pygame.time.Clock()

# Create a constant for our fps
FPS = 60

# Global Variables
XPos = 400
YPos = 250

# Change values (speed)
XChange = 0
YChange = 0

# Boolean for costume change
IsMoving = False

# create the screen object
DisplaySurface = pygame.display.set_mode((WIDTH, HEIGHT))
# sets the caption
pygame.display.set_caption('Change Costume')

# load image
Image = pygame.image.load('penguin.png')
Image1 = pygame.image.load('penguin1.png')
Image2 = pygame.image.load('penguin2.png')
BG = pygame.image.load('tundra.png')

# store costumes as a list
Costumes = (Image1, Image2, Image)

# Start a Counter
Counter = 0

# Create a bit holder
Bit = 1

# game loop( allows to check user actions )
while (True):
    # fills surface with white
    DisplaySurface.fill(WHITE)
    DisplaySurface.blit( BG, (0,0))

    image = Costumes[2]

    if IsMoving == True:
        if Counter % 3 == 0:
            Bit ^= 1 # A simple way to toggle between 0 and 1
            image = Costumes[Bit]
        else:
            image = Costumes[Bit]
    else:
        image = Costumes[2]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # quits pygame modules
            pygame.quit()
            # exits the screen
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #some code
                XChange = 1
                IsMoving = True
            if event.key == pygame.K_LEFT:
                #some code
                XChange = -1
                IsMoving = True
            if event.key == pygame.K_UP:
                #some code
                YChange = -1
                IsMoving = True
            if event.key == pygame.K_DOWN:
                #some code
                YChange = 1
                IsMoving = True
        else:
            XChange = 0
            YChange = 0
            IsMoving = False
    
    XPos += XChange
    YPos += YChange

    DisplaySurface.blit( image, (XPos,YPos))

    # Incorporate Frames per Second to control the speed of costume changes
    FPSCLOCK.tick(FPS)

    # Increment Counter
    Counter += 1
    
    # Displays everything or updates display
    pygame.display.update()
