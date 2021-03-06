import pygame
from gates import *
from digital_circuit import *
from make_circuit import *
import random
import os
from imagesHandler import *
from equation_parse import *
#from image_recognition import *

#COLORS
WHITE = (255, 255, 255)
BLACK = (0,0,0)
DULL_RED= (161,20,20)
BRIGHT_RED = (255,20,20)
DULL_GREEN= (32,173,0)
BRIGHT_GREEN=(43,235,0)
LIGHT_GRAY=(168,168,168)
GRAY=(100,100,100)
DARK_BLUE=(0,32,66)
DARKER_BLUE=(2,0,36)
LIGHT_YELLOW=(254,255,189)
SOLID_YELLOW=(255,239,15)

class PygameGame(object):
    def __init__(self, width=1538, height=840, fps=30, title="D  I  G  I  T  I  Z  E"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        pygame.init()

    def init(self,screen):
        self.mode="Menu"
        self.analyze=False
        self.error=''
        self.redd=random.choice([True,False])
        self.blued=random.choice([True,False])
        self.greend=random.choice([True,False])
        self.red=random.randint(0,256)
        self.blue=random.randint(0,256)
        self.green=random.randint(0,256)

        #RECT COLORS
        self.titleRectColor=SOLID_YELLOW
        self.playNowRectColor=DULL_GREEN
        self.aboutRectColor=DULL_GREEN
        self.exitRectColor=DULL_GREEN
        self.analyzeRectColor=DULL_RED
        self.sanalyzeRectColor=DULL_RED
        self.buttonAColor=DULL_RED
        self.buttonBColor=DULL_RED
        self.buttonCColor=DULL_RED
        self.buttonDColor=DULL_RED
        self.OColor=DULL_RED

        #FONTS
        self.titleFont=pygame.font.SysFont('Arial',int(self.height*.1))
        self.buttonFont=pygame.font.SysFont('Arial',int(self.height*.045))
        self.inputFont=pygame.font.SysFont('Arial',int(self.height*.02))
        self.analyzeBFont=pygame.font.SysFont('Arial',int(self.height*.12))
        self.titleFont.set_italic(True)

        #RECTS
        self.titleRect=pygame.Rect(self.width*.1,self.height*.04,self.width*.8,self.height*.12)
        self.playNowRect=pygame.Rect(self.width*.425,self.height*.3,self.width*.15,self.height*.07)
        self.aboutRect=pygame.Rect(self.width*.425,self.height*.4,self.width*.15,self.height*.07)
        self.exitRect=pygame.Rect(self.width*.425,self.height*.5,self.width*.15,self.height*.07)
        self.analyzeRect=pygame.Rect(self.width*.3,self.height*.4,self.width*.4,self.height*.2)
        self.sanalyzeRect=pygame.Rect(self.width*.425,self.height*.9,self.width*.15,self.height*.07)

        self.buttonARect=pygame.Rect(self.width*.2,self.height*.55,self.width*.15,self.height*.1)
        self.buttonBRect=pygame.Rect(self.width*.2,self.height*.75,self.width*.15,self.height*.1)
        self.buttonCRect=pygame.Rect(self.width*.5,self.height*.55,self.width*.15,self.height*.1)
        self.buttonDRect=pygame.Rect(self.width*.5,self.height*.75,self.width*.15,self.height*.1)
        self.buttonORect=pygame.Rect(self.width*.8,self.height*.65,self.width*.15,self.height*.1)

        #IMAGES
        self.andGate=pygame.image.load("Gimages/andgate1.png")
        self.orGate=pygame.image.load("Gimages/orgate1.png")
        self.xorGate=pygame.image.load("Gimages/xorgate1.png")
        self.notGate=pygame.image.load("Gimages/notgate1.png")
        self.nandGate=pygame.image.load("Gimages/nandgate1.png")
        self.norGate=pygame.image.load("Gimages/norgate1.png")
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
        self.backImage=pygame.image.load("Back.jpg")
        self.scBackImage=pygame.transform.scale(self.backImage,(self.width,self.height))

        #LIVE
        self.objList=[]
        self.gates=[self.scAndGate,self.scOrGate,self.scXorGate,self.scNotGate,self.scNandGate,self.scNorGate]
        self.wirelen=self.width*.04
        self.spread=self.height*.05
        self.depth=1
        self.sVal=2
        self.dRat=self.sVal/self.depth
        self.AON=False
        self.BON=False
        self.CON=False
        self.DON=False
        self.output=False

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
            os.startfile("README.txt")
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
        if self.redd:
            self.red+=random.randint(1,8)
            if self.red>=256:
                self.red=255
                self.redd=not self.redd
        else:
            self.red-=random.randint(1,8)
            if self.red<0:
                self.red=0
                self.redd=not self.redd
        if self.blued:
            self.blue+=random.randint(1,8)
            if self.blue>=256:
                self.blue=255
                self.blued=not self.blued
        else:
            self.blue-=random.randint(1,8)
            if self.blue<0:
                self.blue=0
                self.blued=not self.blued
        if self.greend:
            self.green+=random.randint(1,8)
            if self.green>=256:
                self.green=255
                self.greend=not self.greend
        else:
            self.green-=random.randint(1,8)
            if self.green<0:
                self.green=0
                self.greend=not self.greend
        self.titleRectColor=(self.red,self.blue,self.green)

    def menuRedrawAll(self, screen):
        screen.blit(self.scBackImage,(0,0))
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
        self.displayText(screen,'LIVE MODE',self.buttonFont,WHITE,center=self.playNowRect.center)
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
        if not self.analyze and self.analyzeRect.collidepoint(x,y):
            self.analyze=True
            circuit=self.createCircuit()
            #circuit=getCircuit()
            if circuit[1]=='':
                self.objList.append(circuit[0])
            else:
                self.error=circuit[1]
        if self.analyze:
            if self.sanalyzeRect.collidepoint(x,y):
                self.error=''
                #circuit=getCircuit()
                circuit=self.createCircuit()
                if circuit[1]=='':
                    self.objList.pop()
                    self.objList.append(circuit[0])
                else:
                    self.error=circuit[1]
            elif self.buttonARect.collidepoint(x,y):
                self.AON= not self.AON
            elif self.buttonBRect.collidepoint(x,y):
                self.BON= not self.BON
            elif self.buttonCRect.collidepoint(x,y):
                self.CON= not self.CON
            elif self.buttonDRect.collidepoint(x,y):
                self.DON= not self.DON

    def liveMouseReleased(self, x, y):
        pass

    def liveMouseMotion(self, x, y):
        pass

    def liveMouseDrag(self, x, y):
        pass

    def liveKeyPressed(self, keyCode, modifier):
        if keyCode==113:
            self.playing=False

    def liveKeyReleased(self, keyCode, modifier):
        pass

    def liveTimerFired(self, dt):
        if self.analyze and self.error=='':
            self.output=parse_equation(self.AON,self.BON,self.CON,self.DON,self.objList[0].userEq)

    def liveRedrawAll(self, screen):
        if not self.analyze:
            if self.analyzeRect.collidepoint(pygame.mouse.get_pos()):
                self.analyzeRectColor=BRIGHT_RED
            else:
                self.analyzeRectColor=DULL_RED
            pygame.draw.rect(screen,self.analyzeRectColor,self.analyzeRect)
            self.displayText(screen,'ANALYZE!',self.analyzeBFont,WHITE,center=self.analyzeRect.center)
        else:
            if self.error!='':
                self.displayText(screen,self.error,self.buttonFont,BLACK,center=(self.width/2,self.height/2))
                if self.sanalyzeRect.collidepoint(pygame.mouse.get_pos()):
                    self.sanalyzeRectColor=BRIGHT_RED
                else:
                    self.sanalyzeRectColor=DULL_RED
                pygame.draw.rect(screen,self.sanalyzeRectColor,self.sanalyzeRect)
                self.displayText(screen,'RE-ANALYZE!',self.buttonFont,WHITE,center=self.sanalyzeRect.center)
            else:
                for obj in self.objList:
                    start=(self.width*.65,self.height*.2)
                    self.drawWire(screen,start,(start[0]-.5*self.wirelen,start[1]))
                    self.drawCircuit(screen,obj,(start[0]-.5*self.wirelen,start[1]))
                    self.displayText(screen,"Output",self.inputFont,BLACK,center=(start[0]+23,start[1]-6))
                
                self.displayText(screen,self.objList[0].userEq,self.inputFont,BLACK,center=(self.width*.2,self.height*.4))
                self.displayText(screen,self.objList[0].get_qm(),self.inputFont,BLACK,center=(self.width*.6,self.height*.4))

                if self.sanalyzeRect.collidepoint(pygame.mouse.get_pos()):
                    self.sanalyzeRectColor=BRIGHT_RED
                else:
                    self.sanalyzeRectColor=DULL_RED
                pygame.draw.rect(screen,self.sanalyzeRectColor,self.sanalyzeRect)
                self.displayText(screen,'RE-ANALYZE!',self.buttonFont,WHITE,center=self.sanalyzeRect.center)
                
                if self.AON:
                    self.buttonAColor=SOLID_YELLOW
                elif self.buttonARect.collidepoint(pygame.mouse.get_pos()):
                    self.buttonAColor=BRIGHT_RED
                else:
                    self.buttonAColor=DULL_RED
                pygame.draw.rect(screen,self.buttonAColor,self.buttonARect)
                self.displayText(screen,'A',self.buttonFont,WHITE,center=self.buttonARect.center)
                
                if self.BON:
                    self.buttonBColor=SOLID_YELLOW
                elif self.buttonBRect.collidepoint(pygame.mouse.get_pos()):
                    self.buttonBColor=BRIGHT_RED
                else:
                    self.buttonBColor=DULL_RED
                pygame.draw.rect(screen,self.buttonBColor,self.buttonBRect)
                self.displayText(screen,'B',self.buttonFont,WHITE,center=self.buttonBRect.center)
                
                if self.CON:
                    self.buttonCColor=SOLID_YELLOW
                elif self.buttonCRect.collidepoint(pygame.mouse.get_pos()):
                    self.buttonCColor=BRIGHT_RED
                else:
                    self.buttonCColor=DULL_RED
                pygame.draw.rect(screen,self.buttonCColor,self.buttonCRect)
                self.displayText(screen,'C',self.buttonFont,WHITE,center=self.buttonCRect.center)
                
                if self.DON:
                    self.buttonDColor=SOLID_YELLOW
                elif self.buttonDRect.collidepoint(pygame.mouse.get_pos()):
                    self.buttonDColor=BRIGHT_RED
                else:
                    self.buttonDColor=DULL_RED
                pygame.draw.rect(screen,self.buttonDColor,self.buttonDRect)
                self.displayText(screen,'D',self.buttonFont,WHITE,center=self.buttonDRect.center)

                if self.output:
                    self.OColor=SOLID_YELLOW
                else:
                    self.OColor=DULL_RED
                pygame.draw.rect(screen,self.OColor,self.buttonORect)
                self.displayText(screen,'Output',self.buttonFont,WHITE,center=self.buttonORect.center)

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

    def getLowerBound(self,circuit,start):
        curLow=start
        if isinstance(circuit,CInput): 
            return curLow
        elif isinstance(circuit,Circuit):
            curLow+=circuit.image.get_height()/2
            start=0
            if not isinstance(circuit,NotGate):
                start-=circuit.image.get_height()/4
            if isinstance(circuit.in2,CInput):
                return curLow
            elif isinstance(circuit.in2,Circuit) and isinstance(circuit.in1,CInput):
                self.depth+=1
                return curLow+self.getLowerBound(circuit.in2,0)
            elif isinstance(circuit.in2,Circuit) and isinstance(circuit.in1,Circuit):
                curLow+=self.spread*self.dRat+start
                self.depth+=1
                return curLow+self.getLowerBound(circuit.in2,0)
            else:
                return curLow+self.getLowerBound(circuit.in1,0)

    def getUpperBound(self,circuit):
        curHi=start
        if isinstance(circuit,CInput): 
            return curHi
        elif isinstance(circuit,Circuit):
            curHi-=circuit.image.get_height()/2
            if not isinstance(circuit,NotGate):
                start+=circuit.image.get_height()/4
            if isinstance(circuit.in1,CInput):
                return curHi
            elif isinstance(circuit.in1,Circuit) and isinstance(circuit.in1,CInput):
                self.depth+=1
                return curLow-self.getLowerBound(circuit.in1,0)
            elif isinstance(circuit.in1,Circuit) and isinstance(circuit.in1,Circuit):
                curLow-=self.spread*self.dRat
                self.depth+=1
                return curHi-self.getLowerBound(circuit.in1,0)


    def displayText(self,screen,text, font, color, pos=(0,0), center=None):
        textSurface=font.render(text,True,color)
        textRect=textSurface.get_rect()
        if center!=None:
            textRect.center=center
            screen.blit(textSurface,textRect)
        else:
            textRect
            screen.blit(textSurface,pos)

    def drawGate(self,screen,gate,pos):
        screen.blit(gate.image,pos)

    def drawWire(self,screen,initial,final):
        if initial[1]==final[1]:
            pygame.draw.line(screen,BLACK,initial,final,2)
        else:
            lineLen=abs(final[0]-initial[0])
            pygame.draw.line(screen,BLACK,initial,(int(initial[0]-lineLen*.25),initial[1]),2)
            pygame.draw.line(screen,BLACK,(int(initial[0]-lineLen*.25),initial[1]),(int(initial[0]-lineLen*.25),final[1]),2)
            pygame.draw.line(screen,BLACK,(int(initial[0]-lineLen*.25),final[1]),final,2)

    def drawCircuit(self,screen,circuit,start):
        self.dRat=self.sVal/self.depth
        if isinstance(circuit,CInput):
            self.displayText(screen,circuit.name,self.inputFont,BLACK,center=(start[0]-8,start[1]))
        elif isinstance(circuit,Circuit):
            self.getImage(circuit)
            gateWidth=circuit.image.get_width()
            gateHeight=circuit.image.get_height()
            self.drawGate(screen,circuit,(start[0]-gateWidth,start[1]-gateHeight/2))
            if isinstance(circuit,NotGate):
                if isinstance(circuit.in1,Circuit):
                    self.drawWire(screen,(start[0]-gateWidth,start[1]),
                        (start[0]-gateWidth-self.wirelen,start[1]))
                    self.depth+=1
                    self.drawCircuit(screen,circuit.in1,(start[0]-gateWidth-self.wirelen,start[1]))
                    self.depth-=1
                else:
                    self.drawWire(screen,(start[0]-gateWidth,start[1]),
                        (start[0]-gateWidth-.5*self.wirelen,start[1]))
                    self.drawCircuit(screen,circuit.in1,(start[0]-gateWidth-.5*self.wirelen,start[1]))
            else:
                start1=(start[0]-gateWidth,start[1]-gateHeight/4)
                start2=(start[0]-gateWidth,start[1]+gateHeight/4)
                if isinstance(circuit.in1,Circuit) and isinstance(circuit.in2,Circuit):
                    self.drawWire(screen,start1,(start1[0]-self.wirelen,start1[1]-self.spread*self.dRat))
                    self.depth+=1
                    self.drawCircuit(screen,circuit.in1,(start1[0]-self.wirelen,start1[1]-self.spread*self.dRat))
                    self.depth-=1
                    self.drawWire(screen,start2,(start1[0]-self.wirelen,start2[1]+self.spread*self.dRat))
                    self.depth+=1
                    self.drawCircuit(screen,circuit.in2,(start1[0]-self.wirelen,start2[1]+self.spread*self.dRat))
                    self.depth-=1
                else:
                    if isinstance(circuit.in1,Circuit):
                        self.drawWire(screen,start1,(start1[0]-self.wirelen,start1[1]))
                        self.depth+=1
                        self.drawCircuit(screen,circuit.in1,(start1[0]-self.wirelen,start1[1]))
                        self.depth-=1
                        self.drawWire(screen,start2,(start2[0]-.5*self.wirelen,start2[1]))
                        self.drawCircuit(screen,circuit.in2,(start2[0]-.5*self.wirelen,start2[1]))
                    elif isinstance(circuit.in2,Circuit):
                        self.drawWire(screen,start1,(start1[0]-.5*self.wirelen,start1[1]))
                        self.drawCircuit(screen,circuit.in1,(start1[0]-.5*self.wirelen,start1[1]))
                        self.drawWire(screen,start2,(start2[0]-self.wirelen,start2[1]))
                        self.depth+=1
                        self.drawCircuit(screen,circuit.in2,(start2[0]-self.wirelen,start2[1]))
                        self.depth-=1
                    else:
                        self.drawWire(screen,start1,(start1[0]-.5*self.wirelen,start1[1]))
                        self.drawCircuit(screen,circuit.in1,(start1[0]-.5*self.wirelen,start1[1]))
                        self.drawWire(screen,start2,(start2[0]-.5*self.wirelen,start2[1]))
                        self.drawCircuit(screen,circuit.in2,(start2[0]-.5*self.wirelen,start2[1]))

    def drawNGCircuit(self,screen,circuit,start):
        if isinstance(circuit,CInput):
            self.displayText(screen,circuit.name,self.inputFont,BLACK,center=(start[0]-8,start[1]))
        elif isinstance(circuit,Circuit):
            self.getImage(circuit)
            gateWidth=circuit.image.get_width()
            gateHeight=circuit.image.get_height()
            if isinstance(circuit,NotGate):
                self.drawWire(screen,(start[0]-gateWidth,start[1]),(start[0]-gateWidth-self.wirelen,start[1]))
                self.drawNGCircuit(screen,circuit.in1,(start[0]-gateWidth-self.wirelen,start[1]))
            else:
                start1=(start[0]-gateWidth,start[1]-gateHeight/4)
                start2=(start[0]-gateWidth,start[1]+gateHeight/4)
                if isinstance(circuit.in1,circuit):
                    self.drawWire(screen,start1,(start1[0]-self.wirelen,start1[1]-self.spread))
                    self.drawWire(screen,start2,(start1[0]-self.wirelen,start2[1]+self.spread))
                    self.drawNGCircuit(screen,circuit.in1,(start[0]-gateWidth-self.wirelen,start[1]-gateHeight/4-self.spread))
                    self.drawNGCircuit(screen,circuit.in2,(start[0]-gateWidth-self.wirelen,start[1]+gateHeight/4+self.spread))

    def createCircuit(self):
        A=CInput('A')
        B=CInput('B')
        C=CInput('C')
        cir1=OrGate(B,C)
        cir2=AndGate(A,cir1)
        cir3=NotGate(B)
        cir4=AndGate(cir2,cir3)
        return (cir4,"")

    def getImage(self,circuit):
        if isinstance(circuit,AndGate):
            circuit.image=self.scAndGate
        elif isinstance(circuit,OrGate):
            circuit.image=self.scOrGate
        elif isinstance(circuit,NotGate):
            circuit.image=self.scNotGate
        elif isinstance(circuit,XorGate):
            circuit.image=self.scXorGate
        elif isinstance(circuit,NandGate):
            circuit.image=self.scNandGate
        elif isinstance(circuit,NorGate):
            circuit.image=self.scNorGate
        else:
            raise Exception("Unknown Circuit")

def getCircuit():
    get_img()
    getGridImages("CVTEST.jpg")
    array=images2Circ(filter_images())
    return get_circuit(array)

try:
    game=PygameGame()
    game.run()
finally:
    pygame.quit()