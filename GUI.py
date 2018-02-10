import pygame
from CirSymbols import *
import random
import os

#COLORS
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,20,20)
DULL_GREEN= (32,173,0)
BRIGHT_GREEN=(43,235,0)
LIGHT_GRAY=(168,168,168)
GRAY=(100,100,100)
DARK_BLUE=(0,32,66)
DARKER_BLUE=(2,0,36)
LIGHT_YELLOW=(254,255,189)
SOLID_YELLOW=(255,239,15)

class PygameGame(object):
    def __init__(self, width=1000, height=650, fps=30, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        pygame.init()

    def init(self,screen):
        self.mode="Menu"

        #RECT COLORS
        self.titleRectColor=SOLID_YELLOW
        self.playNowRectColor=DULL_GREEN
        self.aboutRectColor=DULL_GREEN
        self.exitRectColor=DULL_GREEN

        #FONTS
        self.titleFont=pygame.font.SysFont('Arial',int(self.height*.1))
        self.buttonFont=pygame.font.SysFont('Arial',int(self.height*.045))

        #RECTS
        self.titleRect=pygame.Rect(self.width*.1,self.height*.04,self.width*.8,self.height*.12)
        self.playNowRect=pygame.Rect(self.width*.425,self.height*.3,self.width*.15,self.height*.07)
        self.aboutRect=pygame.Rect(self.width*.425,self.height*.4,self.width*.15,self.height*.07)
        self.exitRect=pygame.Rect(self.width*.425,self.height*.5,self.width*.15,self.height*.07)

        #IMAGES
        self.andGate=pygame.image.load("andgate1.png")
        self.orGate=pygame.image.load("orgate1.png")
        self.xorGate=pygame.image.load("xorgate1.png")
        self.notGate=pygame.image.load("notgate1.png")
        self.nandGate=pygame.image.load("nandgate1.png")
        self.norGate=pygame.image.load("norgate1.png")
        self.andRatio=self.andGate.get_width()/self.andGate.get_height()
        self.orRatio=self.orGate.get_width()/self.orGate.get_height()
        self.xorRatio=self.xorGate.get_width()/self.xorGate.get_height()
        self.notRatio=self.notGate.get_width()/self.notGate.get_height()
        self.nandRatio=self.nandGate.get_width()/self.nandGate.get_height()
        self.norRatio=self.norGate.get_width()/self.norGate.get_height()
        self.gateHeight=int(0.06*self.height)
        self.scAndGate=pygame.transform.scale(self.andGate,(int(self.gateHeight*self.andRatio),self.gateHeight))
        self.scOrGate=pygame.transform.scale(self.orGate,(int(self.gateHeight*self.orRatio),self.gateHeight))
        self.scXorGate=pygame.transform.scale(self.xorGate,(int(self.gateHeight*self.xorRatio),self.gateHeight))
        self.scNotGate=pygame.transform.scale(self.notGate,(int(self.gateHeight*self.notRatio),self.gateHeight))
        self.scNandGate=pygame.transform.scale(self.nandGate,(int(self.gateHeight*self.nandRatio),self.gateHeight))
        self.scNorGate=pygame.transform.scale(self.norGate,(int(self.gateHeight*self.norRatio),self.gateHeight))

        #LIVE
        self.i=0
        self.objList=[]
        self.gates=[self.scAndGate,self.scOrGate,self.scXorGate,self.scNotGate,self.scNandGate,self.scNorGate]

    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init(screen)
        self.playing = True
        while self.playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    self.playing = False
            screen.fill((255, 255, 255))
            self.redrawAll(screen)
            pygame.display.flip()
        pygame.quit()

    def mousePressed(self, x, y):
        if(self.mode == 'Menu'): self.menuMousePressed(x, y)
        elif(self.mode == 'Live'): self.liveMousePressed(x, y)
        elif(self.mode == 'Help'): self.helpMousePressed(x, y)

    def mouseReleased(self, x, y):
        if(self.mode == 'Menu'): self.menuMouseReleased(x, y)
        elif(self.mode == 'Live'): self.liveMouseReleased(x, y)
        elif(self.mode == 'Help'): self.helpMouseReleased(x, y)

    def mouseMotion(self, x, y):
        if(self.mode == 'Menu'): self.menuMouseMotion(x, y)
        elif(self.mode == 'Live'): self.liveMouseMotion(x, y)
        elif(self.mode == 'Help'): self.helpMouseMotion(x, y)

    def mouseDrag(self, x, y):
        if(self.mode == 'Menu'): self.menuMouseDrag(x, y)
        elif(self.mode == 'Live'): self.liveMouseDrag(x, y)
        elif(self.mode == 'Help'): self.helpMouseDrag(x, y)

    def keyPressed(self, keyCode, modifier):
        if(self.mode == 'Menu'): self.menuKeyPressed(keyCode, modifier)
        elif(self.mode == 'Live'): self.liveKeyPressed(keyCode, modifier)
        elif(self.mode == 'Help'): self.helpKeyPressed(keyCode, modifier)

    def keyReleased(self, keyCode, modifier):
        if(self.mode == 'Menu'): self.menuKeyReleased(keyCode, modifier)
        elif(self.mode == 'Live'): self.liveKeyReleased(keyCode, modifier)
        elif(self.mode == 'Help'): self.helpKeyReleased(keyCode, modifier)

    def timerFired(self, dt):
        if(self.mode == 'Menu'): self.menuTimerFired(dt)
        elif(self.mode == 'Live'): self.liveTimerFired(dt)
        elif(self.mode == 'Help'): self.helpTimerFired(dt)

    def redrawAll(self, screen):
        if(self.mode == 'Menu'): self.menuRedrawAll(screen)
        elif(self.mode == 'Live'): self.liveRedrawAll(screen)
        elif(self.mode == 'Help'): self.helpRedrawAll(screen)

    def isKeyPressed(self, key):
        if(self.mode == 'Menu'): self.menuIsKeyPressed(key)
        elif(self.mode == 'Live'): self.liveIsKeyPressed(key)
        elif(self.mode == 'Help'): self.helpIsKeyPressed(key)



#MENU
    def menuMousePressed(self, x, y):
        if self.playNowRect.collidepoint(x,y):
            self.mode='Live'
        elif self.aboutRect.collidepoint(x,y):
            self.mode='Help'
        elif self.exitRect.collidepoint(x,y):
            self.playing=False

    def menuMouseReleased(self, x, y):
        pass

    def menuMouseMotion(self, x, y):
        pass

    def menuMouseDrag(self, x, y):
        pass

    def menuKeyPressed(self, keyCode, modifier):
        pass

    def menuKeyReleased(self, keyCode, modifier):
        pass

    def menuTimerFired(self, dt):
        pass

    def menuRedrawAll(self, screen):
        #Buttons
        if self.playNowRect.collidepoint(pygame.mouse.get_pos()):
            self.playNowRectColor=BRIGHT_GREEN
        else:
            self.playNowRectColor=DULL_GREEN
        if self.aboutRect.collidepoint(pygame.mouse.get_pos()):
            self.aboutRectColor=BRIGHT_GREEN
        else:
            self.aboutRectColor=DULL_GREEN
        if self.exitRect.collidepoint(pygame.mouse.get_pos()):
            self.exitRectColor=BRIGHT_GREEN
        else:
            self.exitRectColor=DULL_GREEN
        #Title
        pygame.draw.rect(screen,self.titleRectColor,self.titleRect)
        self.displayText(screen,self.title,self.titleFont,WHITE,center=self.titleRect.center)
        #Play Now
        pygame.draw.rect(screen,self.playNowRectColor,self.playNowRect)
        self.displayText(screen,'PLAY NOW!',self.buttonFont,WHITE,center=self.playNowRect.center)
        #About
        pygame.draw.rect(screen,self.aboutRectColor,self.aboutRect)
        self.displayText(screen,'ABOUT',self.buttonFont,WHITE,center=self.aboutRect.center)
        #Exit
        pygame.draw.rect(screen,self.exitRectColor,self.exitRect)
        self.displayText(screen,'EXIT',self.buttonFont,WHITE,center=self.exitRect.center)

    def menuIsKeyPressed(self, key):
        pass



#LIVE
    def liveMousePressed(self, x, y):
        pass

    def liveMouseReleased(self, x, y):
        pass

    def liveMouseMotion(self, x, y):
        pass

    def liveMouseDrag(self, x, y):
        pass

    def liveKeyPressed(self, keyCode, modifier):
        pass

    def liveKeyReleased(self, keyCode, modifier):
        pass

    def liveTimerFired(self, dt):
        pass

    def liveRedrawAll(self, screen):
        for obj in self.objList:
            self.drawCir(screen,obj)

    def liveIsKeyPressed(self, key):
        pass



#HELP
    def helpMousePressed(self, x, y):
        pass

    def helpMouseReleased(self, x, y):
        pass

    def helpMouseMotion(self, x, y):
        pass

    def helpMouseDrag(self, x, y):
        pass

    def helpKeyPressed(self, keyCode, modifier):
        pass

    def helpKeyReleased(self, keyCode, modifier):
        pass

    def helpTimerFired(self, dt):
        pass

    def helpRedrawAll(self, screen):
        pass

    def helpIsKeyPressed(self, key):
        pass

    def displayText(self,screen,text, font, color, pos=(0,0), center=None):
        textSurface=font.render(text,True,color)
        textRect=textSurface.get_rect()
        if center!=None:
            textRect.center=center
            screen.blit(textSurface,textRect)
        else:
            textRect
            screen.blit(textSurface,pos)

    def drawCir(self,screen,cir):
        screen.blit(cir.image,(cir.x,cir.y))

try:
    game=PygameGame()
    game.run()
finally:
    pygame.quit()