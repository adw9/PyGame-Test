import pygame
pygame.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First PyGame!")
x = 50
y = 50
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
                x += 8
            elif event.key == pygame.K_LEFT:
                x -= 8
            elif event.key == pygame.K_DOWN:
                y += 8
            elif event.key == pygame.K_UP:
                y -= 8
    pygame.draw.rect(screen,(0,0,0),(0,0,1000,1000))
    pygame.draw.rect(screen,(255,255,255),(x,y,20,25))
    pygame.display.flip()
     
     # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
