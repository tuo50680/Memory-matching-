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
