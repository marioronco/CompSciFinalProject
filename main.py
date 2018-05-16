"""
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/


import pygame
import random
 
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# classes 
 
class Block(pygame.sprite.Sprite):
" This class represents the block. """
def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Update the player's position. """
        # current mouse position. This returns the position as a list 

        pos = pygame.mouse.get_pos()
 
        # Set the player x position tp the mouse postion 
        self.rect.x = pos[0]
 
 
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class Sprite
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3
 
 
# Initialize Pygame
pygame.init()
 
# screen deminsions 
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# --- Sprite lists
 
 #list of sprites, blocks, and players
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()
 

for i in range(50):
    # represents a block 
    block = Block(BLUE)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(350)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = Player()
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# how fast the screen updates
clock = pygame.time.Clock()

# font to draw text on the screen
font = pygame.font.Font(None, 40)
 
score = 0

level = 1 

player.rect.y = 370
 

while not done:
    # processing game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # bullet location so it is where the player is 
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            # bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
 
 
    # Call the update() method on all the sprites
    all_sprites_list.update()
 
    # specific function for each bullet
    for bullet in bullet_list:
 
        # Sees if the bullet hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        # For each block hit, add to score and get rid of the bullet
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
 
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Draw all the spites
    all_sprites_list.draw(screen)

    text = font.render("Score: "+str(score), True, BLACK)
    screen.blit(text, [10, 10])
         
    text = font.render("Level: "+str(level), True, BLACK)
    screen.blit(text, [10, 40])
    
 
    # update screen
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()