import pygame
from TileSet import TileSet
from Character import Character, CharacterEmotes
from Objects import Objects
from random import randint

pygame.init()

#GENERIC SETTINGS
SCREEN_SIZE = (1000, 700)
win = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
gameClock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
MOUSE_X = 0
MOUSE_Y = 0

#importing assets
bg = pygame.image.load("png\\BG\\BG.png")
tileSet = []
heroIdle = []
heroWalking = []
heroRun = []
heroJump = []
#Tileset
for i in range(1, 19):
    tileSet.append(pygame.image.load(f"png\\Tiles\\{i}.png"))
#Hero Idle
for i in range(1, 10):
    heroIdle.append(pygame.image.load(f"png\\Knight\\Idle ({i}).png"))
# Hero Walking
for i in range(1, 11):
    heroWalking.append(pygame.image.load(f"png\\Knight\\Walk ({i}).png"))
# Hero Running
for i in range(1, 10):
    heroRun.append(pygame.image.load(f"png\\Knight\\Run ({i}).png"))
# Hero Jumping
for i in range(1, 11):
    heroJump.append(pygame.image.load(f"png\\Knight\\Jump ({i}).png"))
# A tree
tree = pygame.image.load("png\\Object\\Tree_3.png")

# Creating characters and tiles

# The main loop controller
RUN = True 

# creates the tileSet 
localTiles = TileSet(tileSet, 0, 0, win) 

# creates an instance of character for hero
hero = Character(10, 700-256, win) 
objLocal = Objects(win)
heroEmote = CharacterEmotes(hero)
heroEmote.setJumpLevel(8)
heroEmote.setJumpAnimation("jump-right")


# adding idle animation
hero.addAnimation(heroIdle, "idle")
# adding walking right animation
hero.addAnimation(heroWalking, "right")
# creating walking left animation by flipping
hero.createFlipped("right", "left", 0, 1)
# creating idle left animation by flipping
hero.createFlipped("idle", "flippedIdle", 0, 1)
#Run animation for hero
hero.addAnimation(heroRun, "run-right")
#creating left animation
hero.createFlipped("run-right", "run-left", 0, 1)
#Jump animation for hero
hero.addAnimation(heroJump, "jump-right")
#creating left jump
hero.createFlipped("jump-right", "jump-left", 0, 1)
# adding tree
objLocal.addObject(tree, "tree1")

# saving the last movement
lastAnim = "idle" 
hero.resizeChar(0.2) # resizing the character by a factor of 2

# Event handler
def eventHandler():
    keys = pygame.key.get_pressed() # Gets the list of keys pressed
    if keys[pygame.K_RIGHT] and not(keys[pygame.K_RSHIFT]):
        # Checks whether the right arrow key is clicked
        localTiles.moveForward(5) # moves the platform/tile
        hero.playAnimation("right") # sets the player animation to walk right
        global lastAnim
        lastAnim = "idle" # setting the last move to normal/right

    elif keys[pygame.K_LEFT] and not(keys[pygame.K_RSHIFT]):
        # Checks whether the left arrow key is pressed
        localTiles.moveBackward(5) # moves the platform/tile
        hero.playAnimation("left") # sets the player animation to walkleft
        lastAnim = "flippedIdle" # sets the last move to left

    elif keys[pygame.K_RSHIFT] and keys[pygame.K_LEFT]:
        localTiles.moveBackward(8)
        hero.playAnimation("run-left")
    
    elif keys[pygame.K_RSHIFT] and keys[pygame.K_RIGHT]:
        localTiles.moveForward(8)
        hero.playAnimation("run-right")

    else:
        # if no key is pressed then play the last move animation
        hero.playAnimation(lastAnim)

# xpos for tree
xPositions = []
for i in range(0, 10):
    xPositions.append(randint(1300, 100000))

# Update
def windowUpdate():
    win.blit(bg, (0, 0))

    #Draw here
    MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
    localTiles.customBaseTile(0, 700-128, 100)
    objLocal.count = (localTiles.xOff)
    objLocal.draw("tree1", 800, 700-(275+128))
    for i in range(0, 10):
        objLocal.draw("tree1", xPositions[i], 700-(275+128))
    #localTiles.baseTile(0, 700 - 128)

    hero.updateChar() # updating the character
    heroEmote.jump(pygame.K_SPACE)
    eventHandler() # calling the event handler
    # Some texts for run time debugging
    win.blit(font.render(f"Distance: {abs(localTiles.xOff)}", True, (0, 0, 0)), (50, 50))
    win.blit(font.render(f"Frame Rate: {round(gameClock.get_fps())}", True, (0, 0, 0)), (50, 70))
    win.blit(font.render(f"x: { MOUSE_X }", True, (0, 0, 0)), (50, 90))
    win.blit(font.render(f"y: { MOUSE_Y }", True, (0, 0, 0)), (50, 110))
    pygame.display.update()


# Main Game Loop
while RUN:
    gameClock.tick(60) # setting frame rate
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    
    windowUpdate()

pygame.quit()