#creating a game using the "sprite" function in pygame
 
import pygame
import random


 
# Defining color parameters
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
 
# Parameters represent the ball        
#"Sprite" class in Pygame
class Block(pygame.sprite.Sprite):
     
    # Constructor. Pass in the color of the block, 
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__() 
 
        # using block image and filling it.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
 
#Pygame
pygame.init()
 
# Set the height and width of the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#list of "sprites" within pygame that manages the blocks in groups
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(10):
    # This represents a block
    block = Block(BLACK, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(SCREEN_WIDTH)
    block.rect.y = random.randrange(SCREEN_HEIGHT)
     
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a RED player block
player = Block(RED, 20, 15)
all_sprites_list.add(player)
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)
 
# Current score
score = 0
 
# Current level
level = 1
 
while not done:
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
   
    
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]
     
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)  
     
    #collisons
    for block in blocks_hit_list:
        score += 1
        print( score )
 
    # Check to see if all the blocks are gone. If they are, level up.
    if len(block_list) == 0:
        # Add one to the level
        level += 1
 
        # Add more blocks. Adds more depending on the level.
        for i in range(level * 10):
            # This represents a block
            block = Block(BLACK, 20, 15)
 
            # Set a random location for the block
            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(SCREEN_HEIGHT)
             
            # Add the block to the list of objects
            block_list.add(block)
            all_sprites_list.add(block)
  
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Draw all the spites
    all_sprites_list.draw(screen)
     
    text = font.render("Score: "+str(score), True, BLACK)
    screen.blit(text, [10, 10])
         
    text = font.render("Level: "+str(level), True, BLACK)
    screen.blit(text, [10, 40])
    
    pygame.display.flip()
 
    # Limit to 80 frames per second
    clock.tick(80)
 
 
pygame.quit()