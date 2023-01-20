import pygame
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

#Color Constants
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First PyGame!")
#vars to move square and circle
userX = 350
userY = 300
botX = 400.0
botY = 300.0
botUp = False


# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        
        if event.type == pygame.QUIT:
            carryOn = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                carryOn = False
                break
            elif event.key == pygame.K_RIGHT:
                userX += 20
            elif event.key == pygame.K_LEFT:
                userX -= 20
            elif event.key == pygame.K_DOWN:
                userY += 20
            elif event.key == pygame.K_UP:
                userY -= 20

    #Determine if bot is near edge of screen, change direction
    if(int(botY) > 400):
        botUp = True
    elif(int(botY) < 100):
        botUp = False
    #move Red Circle
    if botUp == True:
        botY -= 1
    elif botUp == False:
        botY += 1

    # Resets screen to black
    pygame.draw.rect(screen,BLACK,(0,0,1000,1000))
    #Enemy Circle
    pygame.draw.circle(screen,RED,(botX,botY),20,0)  
    # Draw user square 
    pygame.draw.rect(screen,WHITE,(userX,userY,20,25))


    pygame.display.flip()
     
     # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
