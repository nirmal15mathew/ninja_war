import pygame

class Character(object):
    """
        This class helps to create a character for the pygame library. This class helps to
        add, play and manage animations, and resize characters and do a lot of stuff with them.
        All of this needs pygame so pygame must be installed

        for getting values:
            x positon --> character.x
            y positon --> character.y
            current surface = character.win
            current animations (dict ) --> character.animations
            frame number / count --> character.frameCount
            to get names of added animations --> character.names
        """
    def __init__(self, x, y, surface=None):
        self.x = x
        self.y = y
        self.win = surface
        self.animations = {}
        self.frameCount = 0
        self.names = []
        self.currentAnimation = ""
    
    def updateChar(self):
        """

          This method must be called in the main game loop for the character to have its animation.
          No arguments needed.
        """
        if self.frameCount + 1< 27:
            # If the animation count(which is maximum a multiple of sprites) is less than multiple, adds
            self.frameCount += 1
        else:
            # Otherwise sets it to 0
            self.frameCount = 0

    def addAnimation(self, spriteSheet=[], name=""):
        """

          This method helps to add a new animation to the current character. Don't call this method in the loop,
          but call this in the initialisation. The first argument must be a list of pygame surfaces / images, the
          second argument is the unique name for this animation. Both arguments are mandatory

          NB: please give unique names for animations
        """
        self.animations[name] = spriteSheet # setting new key and value in the animation  dictionary
        self.names.append(name) # adding this animation name to the list of animations
    
    def removeAnimation(self, name):
        """

          This method can be used to remove any animations from the current character.Helps to save space.
          Only argument is the name of the animation to be removed
        """
        if self.animations[name]:
            # Checks its existence
            self.animations.pop(name)
        else:
            # If not found raises an error
            print("Didn't found the specified name, did you add it ?")
            raise KeyError
    
    def playAnimation(self, name):
        """

          This method helps to play the animation of the character. This method should be called in the main loop.
          Only the saved/added animations can be played. First argument is the name of the animation to identify 
          the animation to be played.Only one animation must be played at a time.

          NB: The name is the name given when adding the animation
        """
        animations = self.animations[name] # creating a local buffer

        if animations:
            # If it exists
            self.currentAnimation = name
            frame = animations[self.frameCount // 3] # The current frame to be displayed
            self.win.blit(frame, (self.x, self.y)) # Displaying the frame
    
    def resizeChar(self, factor):
        """

          This method help to resize all the sprites. All the animations which are added will be affected.
          This only argument is by what factor (eg: 2 or 0.3) the sprites must be scaled.Any float can be provided.

          NB: it is advised to use this in the initialisation or the setup ( i.e not in loop). Since it is a slow
          proccess
        """
        # For resizing the character
        if factor == 1:
            # IF the factor is one, ignoring it
            pass
        else:
            # OTherwise
            for name in self.names:
                # Name of the animation
                anim = self.animations[name]
                new = [] # creating the buffer
                if anim:
                    # if it exists
                    for animation in anim:
                        # Changing the size for each of the frame
                        w, h = animation.get_size() # getting the measurements
                        # Resizing the animation with the help of pygame.transform
                        animation = pygame.transform.smoothscale(animation, (round(w*factor), round(h*factor)))
                        new.append(animation) # adding it to the buffer
                self.animations[name] = new # setting the animation to the buffer
    
    def createFlipped(self, name, flipName, vertical=0, horizontal=0):
        """

          This method helps to create a flipped version of any provided animation and flip it.
          The first argument is the name of the animation to be flipped (existing), next is the new name
          or the name for the flipped one, the third is whether to flip it vertically ( default = 0), last 
          whether to flip it horizontally (default = 0)
        """
        # creates a flipped animation
        sprites = self.animations[name]
        new = []
        for sprite in sprites:
            new.append(pygame.transform.flip(sprite, horizontal, vertical))
        self.addAnimation(new, flipName)
         

class CharacterEmotes(object):
    def __init__(self, obj):
        self.obj = obj
        self.maxJumpLevel = 10
        self.jumpCount = self.maxJumpLevel
        self.isJump = False
        self.jumpAnimation = None

    def setJumpLevel(self, level):
        self.maxJumpLevel = level
        self.jumpCount = self.maxJumpLevel
        
    def setJumpAnimation(self, animation):
        self.jumpAnimation = animation

    def jump(self, key):
        keys = pygame.key.get_pressed() # Gets the list of keys pressed
        if not(self.isJump):
            if keys[key]:
                #Detects spacebar to jump
                self.isJump = True

        else:
            # If it is jumping
            self.obj.playAnimation(self.jumpAnimation)
            if self.jumpCount >= -(self.maxJumpLevel):
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.obj.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = self.maxJumpLevel