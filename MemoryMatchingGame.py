import random
#hello
#test
import pygame

SCREENWIDTH = 800
SCREENHEIGHT = 600
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Final Project")



run = True
while run:
    screen.fill("pink")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

#Finalize sprite sheets
#Begin making grid
#Making levels
#icon locations
#flipping the tiles
#Having the matched icons stay uncovered
#End game scenarios (Win, lose), Repeat Button

Update 11/21
import pygame,random
#initialize pygame ? 
pygame.init()

#Screen Dimensions
# If it takes up your whole screen GOOD 
# if you want to close it click alt tab and ex it out manually
SCREENWIDTH = 500
SCREENHEIGHT = 500
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("I hope you stub your toe extra hard today")
#Grid and Box parameters
boxSize = 50 #Later on when we make functions for each individual level, we can change the box size and spacing to make the grid smaller 
spacing = 20 

#Grid Dimensions
'''Basically the width and height is the amount of boxes and to get the correct spacing you need to add however many spaced times the spacing variable so for 3 spaces in a 4x4 it would be 4 * boxSize + 3 * spacing '''
gridWidth = 3 * boxSize + 2 * spacing
gridHeight = 3 * boxSize + 2 * spacing

#Centering to screen
'''Initial x and y is at top left so to get to the center you take the the SCREEN w & h - the GRID w & h '''
initialX = (SCREENWIDTH - gridWidth) // 2
initialY = (SCREENHEIGHT - gridHeight) // 2

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
colors = random.choice([RED,GREEN])

#Uploading sprite sheet test
spriteSheetFile = pygame.image.load("sprite.png").convert_alpha()

'''Tracks whether or not the square is hidden or revealed'''
grid = []
for row in range(3):
    newRow = []
    for column in range(3):
        newRow.append(False) #False = hidden / True = revealed
                             #can use this to remove boxes if match
    grid.append(newRow) #append each block into the list grid to keep track of them

def getImage(sheet, frame, width, height, scale, color):
    
    image = pygame.Surface((width, height)).convert_alpha() #transparency 
    image.blit(sheet, (0,0), ((frame * width),5, width, height)) #take the picture on the sheet, and show it on the image
                             #^^^chooses specific areas of the sheet to display (0,0 is the top left corner)
    image = pygame.transform.scale(image, (width * scale, height * scale)) #scaling the image (if you want it bigger)
    image.set_colorkey(color) #makes the bg of the image transparent

    return image

frame0 = getImage(spriteSheetFile, 0, boxSize, boxSize, 1.5, BLACK)
 
#Main Loop
run = True
while run:
    
    screen.fill("pink")
    
#Draw 3x3
    for row in range(3): #Changed to 1 for matching test case
        for column in range(3):
            x = initialX + column * (boxSize + spacing) #
            y = initialY + row * (boxSize + spacing) # 

            if grid[row][column]: #if clicked and revealed, change to purple (just a test, we'll add whatever later)
                pygame.draw.rect(screen, RED, (x,y,boxSize, boxSize))  
            else:
                pygame.draw.rect(screen, (255,255,255),(x,y,boxSize, boxSize))

    #show frame image
    screen.blit(frame0, (x,y)) #moves the image to a location 
    
    #pygame.display.flip() #Update the display I guess?
       
    #Event Handling (whatever that means)
    '''Event tracks what the mouse is doing'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos #tracks the mouse location at x,y 
            
            for row in range(3):
                for column in range(3):
                    x = initialX + column * (boxSize + spacing)
                    y = initialY + row * (boxSize + spacing)
                    if x <= mouseX <= x + boxSize and y <= mouseY <= y + boxSize: #checks to make sure that the mouse clicked within the boundary of the square
                        grid[row][column] = not grid[row][column] #flips the square after clicked

    pygame.display.update()

pygame.quit()


Update 11/21 - 6:30
import pygame,random
#initialize pygame ? 
pygame.init()

#Screen Dimensions
# If it takes up your whole screen GOOD 
# if you want to close it click alt tab and ex it out manually
SCREENWIDTH = 500
SCREENHEIGHT = 500
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("I hope you stub your toe extra hard today")
#Grid and Box parameters
boxSize = 50 #Later on when we make functions for each individual level, we can change the box size and spacing to make the grid smaller 
spacing = 20 

#Grid Dimensions
'''Basically the width and height is the amount of boxes and to get the correct spacing you need to add however many spaced times the spacing variable so for 3 spaces in a 4x4 it would be 4 * boxSize + 3 * spacing '''
gridWidth = 3 * boxSize + 2 * spacing
gridHeight = 3 * boxSize + 2 * spacing

#Centering to screen
'''Initial x and y is at top left so to get to the center you take the the SCREEN w & h - the GRID w & h '''
initialX = (SCREENWIDTH - gridWidth) // 2
initialY = (SCREENHEIGHT - gridHeight) // 2

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
colors = random.choice([RED,GREEN])

#Uploading sprite sheet test
spriteSheetFile = pygame.image.load("sprite.png").convert_alpha()

'''Tracks whether or not the square is hidden or revealed'''
def makeGrid():
    
    grid = []
    for row in range(3):
        newRow = []
        for column in range(3):
            newRow.append(False) #False = hidden / True = revealed
                             #can use this to remove boxes if match
        grid.append(newRow) #append each block into the list grid to keep track of them

def getImage(sheet, frame, width, height, scale, color):
    
    image = pygame.Surface((width, height)).convert_alpha() #transparency 
    image.blit(sheet, (0,0), ((frame * width),5, width, height)) #take the picture on the sheet, and show it on the image
                             #^^^chooses specific areas of the sheet to display (0,0 is the top left corner)
    image = pygame.transform.scale(image, (width * scale, height * scale)) #scaling the image (if you want it bigger)
    image.set_colorkey(color) #makes the bg of the image transparent

    return image

frame0 = getImage(spriteSheetFile, 0, boxSize, boxSize, 1.5, BLACK)
 
#Main Loop
def main
run = True
while run:
    
    screen.fill("pink")
    
#Draw 3x3
    for row in range(3): #Changed to 1 for matching test case
        for column in range(3):
            x = initialX + column * (boxSize + spacing) #
            y = initialY + row * (boxSize + spacing) # 

            if grid[row][column]: #if clicked and revealed, change to purple (just a test, we'll add whatever later)
                pygame.draw.rect(screen, RED, (x,y,boxSize, boxSize))  
            else:
                pygame.draw.rect(screen, (255,255,255),(x,y,boxSize, boxSize))

    #show frame image
    screen.blit(frame0, (x,y)) #moves the image to a location 
    
    #pygame.display.flip() #Update the display I guess?
       
    #Event Handling (whatever that means)
    '''Event tracks what the mouse is doing'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos #tracks the mouse location at x,y 
            
            for row in range(3):
                for column in range(3):
                    x = initialX + column * (boxSize + spacing)
                    y = initialY + row * (boxSize + spacing)
                    if x <= mouseX <= x + boxSize and y <= mouseY <= y + boxSize: #checks to make sure that the mouse clicked within the boundary of the square
                        grid[row][column] = not grid[row][column] #flips the square after clicked

    pygame.display.update()

pygame.quit()
#use sprite as a background and match the covering 




THE CODE IS HERE PUT ON YOUR GLASSES!!!!!!!!!!!!!
Update 11/22: got the sprite sheet in the first box
import pygame, random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREENWIDTH = 800
SCREENHEIGHT = 800
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Katelyn's IQ is < 60")

# Grid and box parameters
boxSize = 50  # Size of each square box
spacing = 10  # Spacing between boxes

# Grid dimensions
gridWidth = 3 * boxSize + 2 * spacing
gridHeight = 3 * boxSize + 2 * spacing

# Centering the grid on the screen
initialX = (SCREENWIDTH - gridWidth) // 2
initialY = (SCREENHEIGHT - gridHeight) // 2

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)

#Uploading sprite sheet test
spriteSheetFile = pygame.image.load("sprite.png").convert_alpha()

# Create a list to store grid data
grid = []

board = []
for row in range(3):
    newRow = []
    for column in range(3):
        newRow.append(False) #False = hidden / True = revealed
    board.append(newRow) #append each block into the list grid to keep track of them

# Populate the grid with square positions
for row in range(3):
    row_list = []  # A list for each row
    for column in range(3):
        x = initialX + column * (boxSize + spacing)
        y = initialY + row * (boxSize + spacing)
        rect = pygame.Rect(x, y, boxSize, boxSize)  # Create a rect for the box
        row_list.append(rect)  # Add to the current row list
    grid.append(row_list)  # Add the row to the grid


def getImage(sheet, frame, width, height, scale, color):
    
    image = pygame.Surface((width, height)).convert_alpha() #transparency 
    image.blit(sheet, (0,0), ((frame * width),5, width, height)) #take the picture on the sheet, and show it on the image
                             #^^^chooses specific areas of the sheet to display (0,0 is the top left corner)
    image = pygame.transform.scale(image, (width * scale, height * scale)) #scaling the image (if you want it bigger)
    image.set_colorkey(color) #makes the bg of the image transparent

    return image

frame0 = getImage(spriteSheetFile, 0, boxSize, boxSize, 1, BLACK)

# Main loop
run = True
while run:
    # Fill screen with background color
    screen.fill("pink")

    # Draw grid
    for row in grid:
        for box in row:
            pygame.draw.rect(screen, RED, box)

    #show frame image
    screen.blit(frame0, grid[0][0].topleft) #moves the image to a location 

    # Update the display
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


# Quit pygame
pygame.quit()





UPDATE 11/26: flipping with the sprite underneath 
import pygame,random
#initialize pygame ? 
pygame.init()

#Screen Dimensions
# If it takes up your whole screen GOOD 
# if you want to close it click alt tab and ex it out manually
SCREENWIDTH = 500
SCREENHEIGHT = 500
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("I hope you stub your toe extra hard today")

#Grid and Box parameters
boxSize = 50 #Later on when we make functions for each individual level, we can change the box size and spacing to make the grid smaller 
spacing = 20 


#Grid Dimensions
'''Basically the width and height is the amount of boxes and to get the correct spacing you need to add however many spaced times the spacing variable so for 3 spaces in a 4x4 it would be 4 * boxSize + 3 * spacing '''
gridWidth = 3 * boxSize + 2 * spacing
gridHeight = 3 * boxSize + 2 * spacing

#Centering to screen
'''Initial x and y is at top left so to get to the center you take the the SCREEN w & h - the GRID w & h '''
initialX = (SCREENWIDTH - gridWidth) // 2
initialY = (SCREENHEIGHT - gridHeight) // 2

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
colors = random.choice([RED,GREEN])

#Uploading sprite sheet test
spriteSheetFile = pygame.image.load("sprite.png").convert_alpha()

'''Tracks whether or not the square is hidden or revealed'''

grid = [] #Make a list for the grid

for row in range(3):
    row_list = [] #Make a list for each row
    for column in range(3):
        x = initialX + column * (boxSize + spacing)
        y = initialY + row * (boxSize + spacing)
        rect = pygame.Rect(x, y, boxSize, boxSize) #Makes a rectangle for each box
        row_list.append({"not_revealed": rect, "revealed": True, "flip": True, "progress": 0})
        #flip progress ranges from 0-100 (50 is the half way point, so it will disappear when it gets halfway)
        #True = revealed
    grid.append(row_list) #Add the row list too the grid list

#Getting the image and frame
def getImage(sheet, frame, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha() #transparency 
    image.blit(sheet, (0,0), ((frame * width),5, width, height)) #take the picture on the sheet, and show it on the image
                             #^^^chooses specific areas of the sheet to display (0,0 is the top left corner)
    image = pygame.transform.scale(image, (width * scale, height * scale)) #scaling the image (if you want it bigger)
    image.set_colorkey(color) #makes the bg of the image transparent
    return image

frame0 = getImage(spriteSheetFile, 0, boxSize, boxSize, 1, BLACK)
 
#Main Loop
run = True
FPS = pygame.time.Clock() #helps to keep track of FPS
while run:
        
    screen.fill("pink")

    #Draw 3x3
    for row in grid:
        for box in row: #for each box in thr row
            rect = box["not_revealed"] #the box chillin
            if box["flip"]:
                box["progress"] += 5 #when box is flipping, add 5 to the motion 
            if box["progress"] >= 100: #until the flipping motion is complete 
                box["flip"] = False #Flipped box will be false (not revealed)
                box["revealed"] = not box["revealed"] #reveals the box
                box["progress"] = 0 #reset

            #This actually does the flipping motion (tbh i really have no idea how it works, im just assuming)
            scale = (100 - box["progress"]) / 100
            width = int(boxSize * scale)
            x_scale = (boxSize - width) // 2 #box size will decrease until the halfway point 

            if box["revealed"] and not box["progress"]: #if the box is revealed and the flipping is done
                screen.blit(frame0, rect.topleft) #insert image 
            else: 
                pygame.draw.rect(screen, RED, (rect.x + x_scale, rect.y, width, boxSize)) #otherwise keep the square 

    #update display
    pygame.display.flip()

    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for row in grid:
                for box in row:
                    if box["not_revealed"].collidepoint(event.pos) and not box["flip"]: #collidepoint checks if a point is inside a rectangle
                        box["flip"] = True 
    FPS.tick(60) #speed of flipping

pygame.quit()





UPDATE 11/27: I MADE THEM INTO FUNCTIONS 
import pygame,random
#initialize pygame ? 
screen = pygame.init()

#Screen Dimensions
# If it takes up your whole screen GOOD 
# if you want to close it click alt tab and ex it out manually
SCREENWIDTH = 500
SCREENHEIGHT = 500
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Azeem has the brain of a chicken")

#Grid and Box parameters
boxSize = 50 #Later on when we make functions for each individual level, we can change the box size and spacing to make the grid smaller 
spacing = 20 

#Grid Dimensions
'''Basically the width and height is the amount of boxes and to get the correct spacing you need to add however many spaced times the spacing variable so for 3 spaces in a 4x4 it would be 4 * boxSize + 3 * spacing '''
ROWS = 3
COLS = 3
gridWidth = ROWS * boxSize + (COLS - 1) * spacing
gridHeight = COLS * boxSize + (ROWS - 1) * spacing

#Centering to screen
'''Initial x and y is at top left so to get to the center you take the the SCREEN w & h - the GRID w & h '''
initialX = (SCREENWIDTH - gridWidth) // 2
initialY = (SCREENHEIGHT - gridHeight) // 2

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)

def drawGrid(rows, cols, initialX, initialY, boxSize, spacing):
    grid = [] #Make a list for the grid
    for row in range(3):
        row_list = [] #Make a list for each row
        for column in range(3):
            x = initialX + column * (boxSize + spacing)
            y = initialY + row * (boxSize + spacing)
            rect = pygame.Rect(x, y, boxSize, boxSize) #Makes a rectangle for each box
            row_list.append({"not_revealed": rect, "revealed": True, "flip": True, "progress": 0})
            #flip progress ranges from 0-100 (50 is the half way point, so it will disappear when it gets halfway)
            #True = revealed
        grid.append(row_list) #Add the row list to the grid list
    return grid

grid = drawGrid(ROWS, COLS, initialX, initialY, boxSize, spacing)

#Uploading sprite sheet test
spriteSheetFile = pygame.image.load("sprite.png").convert_alpha()
spriteSheetFile2 = pygame.image.load("cat fighting.png").convert_alpha()

def getImage(sheet, frame, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha() #transparency 
    image.blit(sheet, (0,0), ((frame * width),5, width, height)) #take the picture on the sheet, and show it on the image
                             #^^^chooses specific areas of the sheet to display (0,0 is the top left corner)
    image = pygame.transform.scale(image, (width * scale, height * scale)) #scaling the image (if you want it bigger)
    image.set_colorkey(color) #makes the bg of the image transparent
    return image

frame0 = getImage(spriteSheetFile, 0, 50, 50, 1, BLACK) #one frame = 50 x 50 (for both)
frame1 = getImage(spriteSheetFile2, 0, 50, 50, 1, BLACK)
mystery = random.choice([frame0, frame1])


def flipAnimation(screen, grid, boxSize, frame0, frame1):
    for row in grid:
        for box in row: #for each box in thr row
            rect = box["not_revealed"] #the box chillin
            if box["flip"]:
                box["progress"] += 5 #when box is flipping, add 5 to the motion 
            if box["progress"] >= 100: #until the flipping motion is complete 
                box["flip"] = False #Flipped box will be false (not revealed)
                box["revealed"] = not box["revealed"] #reveals the box
                box["progress"] = 0 #reset

            #This actually does the flipping motion (tbh i really have no idea how it works, im just assuming)
            scale = (100 - box["progress"]) / 100
            width = int(boxSize * scale)
            x_scale = (boxSize - width) // 2 #box size will decrease until the halfway point 

            if box["revealed"] and not box["progress"]: #if the box is revealed and the flipping is done
                screen.blit(frame0, rect.topleft) or screen.blit(frame1, rect.topleft)
            else: 
                pygame.draw.rect(screen, RED, (rect.x + x_scale, rect.y, width, boxSize))

def mouseHandling(event, grid):
    if event.type == pygame.MOUSEBUTTONDOWN:
        for row in grid:
            for box in row:
                if box["not_revealed"].collidepoint(event.pos) and not box["flip"]: #collidepoint checks if a point is inside a rectangle
                    box["flip"] = True

def main():
    run = True
    FPS = pygame.time.Clock() #helps to keep track of FPS
    while run:
        
        screen.fill("pink")

        flipAnimation(screen, grid, boxSize, frame0, frame1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            mouseHandling(event, grid)
    
        pygame.display.flip()
        FPS.tick(60)
    pygame.quit()

main()
