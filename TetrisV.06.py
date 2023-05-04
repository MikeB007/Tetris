import pygame
import pygame.mixer
import random
#import TConst
import numpy as np
from datetime import datetime


SHAPE= 2
SCREEN_HEIGTH = 800
SCREEN_WIDTH  = 800
SPACE = 1
THICK = 3
SIZE=30
SHIFT=int(SIZE*.3)

TETRIS_COLS=10
TETRIS_ROWS=21         

START_POS_X = int(TETRIS_COLS/2)
START_POS_Y = int(1)    

END_POS_X = int(SCREEN_WIDTH/SIZE)
END_POS_Y= int(SCREEN_HEIGTH/SIZE)

PLAY_SCREEN_WIDTH  = SIZE*TETRIS_COLS
PLAY_SCREEN_HEIGTH = SIZE*TETRIS_ROWS
    
   
#######################################################

ROW_START_POS = 2*SIZE
COL_START_POS = SCREEN_WIDTH - PLAY_SCREEN_WIDTH-10*SIZE

  
shape_colors=['black','red','green','purple','orange','yellow','blue','sienna','lightgrey','tomato','yellowgreen','indigo','navajowhite','lightyellow','midnightblue','peru','grey','darkred','darkgreen','darkviolet','darkorange','darkgoldenrod','navy','saddlebrown','darkgrey']


colors=['red','green','purple','orange','yellow','blue','brown']


print ("Tetris")
def rnd(num):
    return random.randint(1,num)
def ps(s):
    #print ("shape1:",np.shape(s))
    return
def pc(s,msg=":"):
    print(s.__str__())
def psv(s):
    print ("shappce values:",s)

class myConst():
   a=1
   
class Brick():
      
    col=0
    row=0
    shapeInt=0
    empty=True        
    def __init__(self,c=1,r=1, shapeInt = 1):
        self.col=c
        self.row=r
        self.shapeInt=shapeInt        
        self.empty=True    
    def setON(self):
         self.empty= False
    def setOFF(self):
         self.empty= True
    def getEmpty(self):
        return self.empty;
    def isEmpty(self):
        return self.empty;   
    def getRow(self):
        return self.row;   
    def getCol(self):
        return self.col;   
    def increaseRow(self):
        self.row+=1;
    
    def savePos(self, p,shapeInt):
        self.col = p[0]
        self.row = p[1]  
        self.shapeInt = shapeInt
                
    def drawIt(self,s):
        print("Frame")
        self.drawFancyRect1(s,ROW_START_POS,COL_START_POS)
        
    #def  drawRECT(self):
    #    pygame.draw.rect(screen,self.color,(230+self.col*SIZE,ROW_START_POS+self.row*SIZE-SIZE,SIZE, SIZE), THICK)       
    
        
    def drawFancyRect2(self,s):
        for i in range(3,SIZE-1):   
            pygame.draw.rect(s,shape_colors[self.shapeInt],(COL_START_POS+self.col*SIZE+i-SIZE,ROW_START_POS+self.row*SIZE-SIZE+i,SIZE-2*i, SIZE-2*i), THICK) 
        
        
    def drawFancyRect0(self,s):
        for i in range(3,SIZE-1):   
            pygame.draw.rect(s,shape_colors[self.shapeInt],(COL_START_POS+self.col*SIZE+i-SIZE,ROW_START_POS+self.row*SIZE-SIZE+i,SIZE-2*i, SIZE-2*i), THICK) 


   #################################################
    def drawFancyRect1(self,s,Y_pos_Reference,X_pos_Reference):
        shadow = int(SIZE*0.17) 
        lightColorIndx=8+self.shapeInt
        darkColorIndx= 16+self.shapeInt
                
        for i in range(3,SIZE-1):   
            pygame.draw.rect(s,shape_colors[self.shapeInt],(X_pos_Reference+self.col*SIZE+i-SIZE,Y_pos_Reference+self.row*SIZE-SIZE+i,SIZE-2*i, SIZE-2*i), THICK) 
       
        #right  
        for i in (range(shadow)):   
            pygame.draw.line(s,shape_colors[darkColorIndx],\
                             (-7+X_pos_Reference+self.col*SIZE+i,\
                              -9+Y_pos_Reference+self.row*SIZE+i),\
                             (-7+X_pos_Reference+self.col*SIZE+i,\
                              -18+Y_pos_Reference+self.row*SIZE-SIZE+20-i+5), 1) 
        # bottom
        for i in range(shadow):           
            pygame.draw.line(s,shape_colors[darkColorIndx],\
                             (2+X_pos_Reference+self.col*SIZE-SIZE+i,\
                              -4+Y_pos_Reference+self.row*SIZE-i),\
                             (-3+X_pos_Reference+self.col*SIZE-i,\
                              -4+Y_pos_Reference+self.row*SIZE-i), 2)
        #lightLines
        #vertical
        pygame.draw.line(s,shape_colors[lightColorIndx],\
                        (7+X_pos_Reference+self.col*SIZE-SIZE,\
                         10+Y_pos_Reference+self.row*SIZE-SIZE),\
                        (7+X_pos_Reference+self.col*SIZE-SIZE,\
                         -10+Y_pos_Reference+self.row*SIZE), 2)  
        #forizontal
        pygame.draw.line(s,shape_colors[lightColorIndx],\
                        (7+X_pos_Reference+self.col*SIZE-SIZE,\
                         10+Y_pos_Reference+self.row*SIZE-SIZE),\
                        (-10+X_pos_Reference+self.col*SIZE,\
                         10+Y_pos_Reference+self.row*SIZE-SIZE), 2)          
            
    ###################################################  
              
           
    def drawFancyRect5(self,s):
        for i in range(2,int(SIZE/2)-1):   
            pygame.draw.circle(s,shape_colors[self.shapeInt],(COL_START_POS+self.col*SIZE-SIZE+SIZE/2,ROW_START_POS+self.row*SIZE-SIZE/2),SIZE/2-i, THICK) 
    
    def drawFancyRect1l(self,s):
        for i in range(2,int(SIZE/2)-1):   
            pygame.draw.circle(s,'tomato',(-100+COL_START_POS+self.col*SIZE-SIZE+SIZE/2,ROW_START_POS+self.row*SIZE-SIZE/2),SIZE/2-i, THICK) 
    
    def drawFancyRect1d(self,s):
        for i in range(2,int(SIZE/2)-1):   
            pygame.draw.circle(s,'darkred',(100+COL_START_POS+self.col*SIZE-SIZE+SIZE/2,ROW_START_POS+self.row*SIZE-SIZE/2),SIZE/2-i, THICK) 
        
    
    def drawFancyRectCircle(self,s):
        for i in range (len(shape_colors)):
            self.drawFancyRect1l(s)
        
        for i in range(2,int(SIZE/2)-1):   
            pygame.draw.circle(s,'red',(COL_START_POS+self.col*SIZE-SIZE+SIZE/2,ROW_START_POS+self.row*SIZE-SIZE/2),SIZE/2-i, THICK) 
    
        self.drawFancyRect1d(s)
         
    
    def drawFancyRect4(self,s):
        for i in range(3,SIZE-1):   
            pygame.draw.ellipse(s,shape_colors[self.shapeInt],(COL_START_POS+self.col*SIZE+i-SIZE,ROW_START_POS+self.row*SIZE-SIZE+i,SIZE/2-2*i, SIZE-2/2*i), THICK) 
              
             
class Shape():
    
    s000=['']
    
    s01=['.....',
         '1111.',
         '.....']
    
    s02=['.....',
         '.11..',
         '.11..']
    
    s03=['.....',
         '...11',
         '..11.']
    
    s04=['.....',
         '.11..',
         '..11.']
    
    s05=['.....',
         '.111.',
         '...1.']
    
    s06=['.....',
         '.111.',
         '.1...']
    
    s07=['.....',
         '.111.',
         '..1..']
    
    s11=['.....',
         '..1..',
         '..1..',
         '..1..',
         '..1...']
    
    s12=['.....',
         '.11..',
         '.11..',
         '.....',
         '.....']
    
    s13=['.1...',
         '.11..',
         '..1..',
         '.....',
         '.....']
    
    s14=['...1.',
         '..11.',
         '..1..',
         '.....',
         '.....']
    
    s15=['..1..',
         '..1..',
         '.11..',
         '.....',
         '.....',]
    
    s16=['..1..',
         '..1..',
         '..11.',
         '.....',
         '.....']
    
    s17=['..1..',
         '.11..',
         '..1..',
         '.....',
         '.....']
    
    
    s21=['.....',
         '.1111',
         '.....']
    
    s22=['.....',
         '.11..',
         '.11..']
    
    s23=['.....',
         '..11.',
         '.11.']
    
    s24=['.....',
         '.11..',
         '..11.']
    
    s25=['.1...',
         '.111.',
         '.....']
    
    s26=['...1.',
         '.111.',
         '.....']
    
    s27=['..1..',
         '.111.',
         '.....']
    
    s31=['.....',
         '...1.',
         '...1.',
         '...1.',
         '...1.']
    
    s32=['.....',
         '.11..',
         '.11..',
         '.....',
         '.....']
    
    s33=['.1...',
         '.11..',
         '..1..',
         '.....',
         '.....']
    
    s34=['...1.',
         '..11.',
         '..1..',
         '.....',
         '.....']
    
    s35=['..11.',
         '..1..',
         '..1..',
         '.....',
         '.....']
    
    s36=['.11..',
         '..1..',
         '..1..',
         '.....',
         '.....']
    
    s37=['..1..',
         '..11.',
         '..1..',
         '.....',
         '.....']
    
    shapes=[s000,s01,s02,s03,s04,s05,s06,s07,s11,s12,s13,s14,s15,s16,s17,s21,s22,s23,s24,s25,s26,s27,s31,s32,s33,s34,s35,s36,s37]
     
    shape=[]
    shapeInt=0
    
    shapeType= [7] 
    shapType = range(1,7)
    random.shuffle(shapeType)
    
    def __init__(self,sInt):
        self.shape=[]
        self.shapeInt=sInt
        
    def  __str__(self):
        return f"shape{self.shape}  color:{self.shapeInt}"
    def saveShape(self,s,sInt,which="Other"):
        #pc(s)
        for a in s:
            self.shape.append(a)
            #print (a)
            if (a[0] >10 or a[0] < 1):
                #print(which)
                #print ("out of range column", a)
                sInt=sInt
            
            if (a[1] >21 or a[1] < 1):
                #print(which)
                #print ("out of range row", a)
                sInt=sInt
                        
        self.shapeInt=sInt
    
    def resetShape2(self,sInt):
        self.shape = []
        self.shapeInt=sInt
            
    def resetShape(self,sInt):
        self.shape = []
        self.shapeInt = sInt
        
    def resetShapeParams(self,s):
        self.shape = s
        
    def getShape(self):
        return self.shape
    def getColor(self):
        return shape_colors[self.shapeInt]
    def getshapeInt(self):
        return self.shapeInt
           
    def drawFancyRect(self,s,col,row):
        for i in range(3,SIZE-1):
            pygame.draw.rect(s,shape_colors[self.shapeInt],(230+col*SIZE+i,ROW_START_POS+row*SIZE-SIZE+i,SIZE-2*i, SIZE-2*i), THICK) 
        #pygame.draw.rect(s,shape_colors[self.shapeInt],(230+col*SIZE,ROW_START_POS+row*SIZE-SIZE,SIZE, SIZE), THICK) 
    
    def old_drawOneRECT(self,s,col,row):
        #print(col,row) 
        self.drawFancyRect(s,shape_colors[self.shapeInt],col,row)
        #pygame.draw.rect(s,shape_colors[self.shapeInt],(230+col*SIZE,ROW_START_POS+row*SIZE-SIZE,SIZE, SIZE), THICK) 

    
    def getRectPOosition(self,col,row,l1):
        rectPos=[]
        col1=0
        l2=str(l1)
        for a in range(0,len(l2)):
                if (l2[a]=='1'):
                    col1 = col+a
                    rectPos.append((col1,row))    
        return rectPos;
    
    def drawShapeLine(self,s,sInt):
        for r in self.shape:
                if r[0] >0:
                    brick = Brick(r[0],r[1],sInt)
                    brick.drawFancyRect1(s,ROW_START_POS,COL_START_POS) 
        

    def createShapeDetails(self,s,col,row,angle):              
        tShape=Shape(self.shapeInt)
        tShape.resetShape2(self.shapeInt) 
        self.resetShape2(self.shapeInt)
        thisShapeTemaplte=self.shapes[self.shapeInt+7*angle]
        for i in range(len(thisShapeTemaplte)):
            tShape.saveShape(self.getRectPOosition(col,row+i,thisShapeTemaplte[i]),self.shapeInt)
        self.resetShapeParams(tShape.shape)
        self.drawShapeLine(s,self.shapeInt)      

    def createTempShapeDetails(self,s,col,row,angle):
        tShape= Shape(self.shapeInt)
        tShape.resetShape2(self.shapeInt)
        self.resetShape2(self.shapeInt)
        shapeindex = self.shapeInt+angle*7
        thisShapeTemaplte=self.shapes[shapeindex]

        for i in range(len(thisShapeTemaplte)):
            tShape.saveShape(self.getRectPOosition(col,row+i,thisShapeTemaplte[i]),self.shapeInt,"Temp")
        self.saveShape(tShape.shape,self.shapeInt)    
        #if (len(self.shape) < 4):
            #pc(validShape)
                
                
    def drawCube(self,s,col,row):
            pygame.draw.rect(s, shape_colors[self.shapeInt], (col*SIZE, row*SIZE, SIZE, SIZE), THICK)  # width = 3    
    def drawShapes(self,s,col,row):
        pygame.draw.rect(s, shape_colors[self.shapeInt], (col*SIZE, row*SIZE, SIZE, SIZE), THICK)  # width = 3    
    def drawShape(self,s,col,row,angle):
            self.createShapeDetails(s,col,row, angle)
            
    def drawNextShape(self,shapeInt):
        self.shapeInt =shapeInt
        self.drawShape(screen,13,5,1)   
        
    
            
    
        
class Grid(myConst):  
    row=0
    col=0
    grid=[[]]
    activeShape=Shape(0)
    nextShape=Shape(0)
    validShape=Shape(0)    
        
    def createGrid(self,c,r):
        for c1 in range(0, c):
            for r1 in range(0,r):            
                self.grid[c1][r1] = Brick()
        
    def __init__(self): 
        grid=[[]]
        self.row=TETRIS_ROWS
        self.col=TETRIS_COLS
        self.grid= np.empty(shape=(self.col+1,self.row+1), dtype=object)
        self.createGrid(self.col+1,self.row+1)
    
    def  __str__(self):
        return f"rows:{self.row} cols:{self.col}  total Bricks:{row*col}"   
    
    def addBricks(self,shape):
        for s in shape.getShape():
            b = self.grid[ s[0]] [s[1] ]  
            b.setON()
            b.savePos(s,shape.getshapeInt())
           
    
    def refreshGrid(self,s):
        for c in range(1,self.col+1):
            for r in range(1,self.row+1):            
                if(not self.grid[c][r].isEmpty()):
                    self.grid[c][r].drawFancyRect1(s,ROW_START_POS,COL_START_POS)
                    
    def checkBottomGrid(self,shape):
        for c in range(1,self.col+1):
            for r in range(1,self.row+1):            
                if(not self.grid[c][r].isEmpty()):
                    b = self.grid[c][r]                                          
                    for s in shape:
                        if ((s[0] ==b.getCol()) and (s[1]+1==b.getRow())):
                            return True;        
        for s in shape:                
            if (s[1] == TETRIS_ROWS):
                return True;    
        return False
    
    def isValidMove(self,shape):
        sh1 = shape.getShape()
        for c in range(1,self.col+1):
            for r in range(1,self.row+1):            
                if(not self.grid[c][r].isEmpty()):
                    b = self.grid[c][r]                                          
                    for s in sh1:
                        if ((s[0] ==b.getCol()) and (s[1]==b.getRow())):
                            return False;
        
        for s in sh1:
            if ((s[0] < 1 or s[0]> TETRIS_COLS) or (s[1] < 1 or s[1]> TETRIS_ROWS)):
                return False;         
        return True
    
    def dropDownOneRow(self,lastRow):
        for r in range(1,lastRow+1):  
            for c in range(1,self.col):
                if(not self.grid[c][r].isEmpty()):                                                          
                    self.grid[c][r].increaseRow()        
    
    def RemoveAllBricks(self,s):
        i=0
        for r in range(TETRIS_ROWS,1,-1):
            self.grid = np.delete(self.grid,r,axis = 1)
            self.grid = np.insert(self.grid,1,Brick(),axis = 1)

            for r1 in range(1,r):  
                for c in range(1,TETRIS_COLS):
                    if(not self.grid[c][r1].isEmpty()):  
                        self.grid[c][r1].increaseRow()        
        
        self.refreshGrid(s)
        
            
    def removeCompleteLine(self):
        rdyLines=[]
        i=0
        for r in range(self.row,0,-1):  
            i=0
            for c in range(self.col+1):
                if(not self.grid[c][r].isEmpty()):                                                          
                    if (not self.grid[c][r].isEmpty()):
                        i+=1
            if i >0:
                print(i)
            if (i==10):
                rdyLines.append(r)
        for l in reversed(rdyLines):
            self.grid = np.delete(self.grid,l,axis = 1)
            self.grid = np.insert(self.grid,0,Brick(),axis = 1)
            self.dropDownOneRow(l)                        
            print("Complete Line ",l)
                        
    def drawGridLines(self,screen):
            gridColor=(40,40,40)
            a=0
            for  a in range(0,TETRIS_COLS+1):
                    pygame.draw.line(screen, gridColor,(a*SIZE+COL_START_POS,ROW_START_POS),(a*SIZE +  COL_START_POS,ROW_START_POS + TETRIS_ROWS*SIZE))
                       
            for  a in range(0,TETRIS_ROWS+1):
                    pygame.draw.line(screen, gridColor,(COL_START_POS,ROW_START_POS + a *SIZE ),(COL_START_POS + TETRIS_COLS*SIZE,ROW_START_POS + a *SIZE))
                    
                    
class Game():
    P_DELAY=200
    pygame.mixer.Sound
    dropTimer = 4
    dropTimerFast = 4
    LEVEL_FAST = 23
    level=1
    l=1    
    ang=0
    pendingSelectedShape=1
    # game parameters
    ###################################
    start_Game= 1
    in_Game = 0
    gameOver = False
    need_Shape = 1
    shapeAngle=0
    selectedShape=1
    
    moveDownActive = 0    
    
    p=0
    lastPressed= datetime.utcnow() - datetime(1970, 1, 1)
    pressed    = datetime.utcnow() - datetime(1970, 1, 1)
    lMilliseconds=0
    pMilliseconds=0
    keyPressAngle=0         
    
    grd=Grid() 
    
    posX = START_POS_X 
    posY = START_POS_Y    
    
    def selectShape(self,n):
        sh=1
        for i in range (random.randint(1,100)):
             sh = random.randint(1,n)           
        return sh                    
        
    def __init__(self): 
        self.l=1
        self.level=15
        self.dropTimer=2
        self.dropTimerFast=2
        self.LEVEL_FAST= 23 
        self.lastPressed= datetime.utcnow() - datetime(1970, 1, 1)
        self.pressed    = datetime.utcnow() - datetime(1970, 1, 1)
        self.lMouldDropilliseconds=0
        self.pMilliseconds=0
        self.keyPressAngle=0    
        grd = Grid()
        selectedShape=self.selectShape(7)
        pendingSelecedtShape=self.selectShape(7)
        self.posX = START_POS_X   
        self.posY = START_POS_Y            
    
    def resetGame(self):
        self.__init__()     
     
      
    def shouldDrop(self):
        tmr = int(120*(.9-self.level/30.0))+1
        self.dropTimer=(self.dropTimer % tmr)+1
 
    def shouldDropFast(self):
        tmr = int(120*(.6-self.level/30.0))+1
        self.dropTimerFast=(self.dropTimerFast % tmr)+1
                       
    def LevelUP(self):
            #level up yea        
            if (self.level< 20):
                    self.level += 1
            elif (self.level < 22):
                    self.level += +.1
            elif (self.level<23.5):
                    self.level +=.005 
            else:
                    self.level = 15 
            self.l +=1
            
    def moveShape(self,keys):
            self.p=0
            self.pressed= datetime.utcnow() - datetime(1970, 1, 1)
            self.pSeconds =(self.pressed.total_seconds())
            self.pMilliseconds = round(self.pSeconds*1000)
            
            self.grd.validShape.resetShape(self.selectedShape) 
            
            if ((self.pMilliseconds - self.lMilliseconds) > self.P_DELAY):
                if (keys[pygame.K_LEFT]):   
                        self.posX-=1
                        self.grd.validShape.createTempShapeDetails(screen,self.posX,self.posY,self.keyPressAngle)                                       
                        if not self.grd.isValidMove(game.grd.validShape):
                            self.posX+=1
                        self.p=1
                if (keys[pygame.K_RIGHT]):                     
                        self.posX +=1
                        self.grd.validShape.createTempShapeDetails(screen,self.posX,self.posY,self.keyPressAngle)                                       
                        if not self.grd.isValidMove(game.grd.validShape):
                            self.posX-=1
                        self.p=1 
                if (keys[pygame.K_DOWN]):            
                        self.posY +=1
                        self.grd.validShape.createTempShapeDetails(screen,self.posX,self.posY,self.keyPressAngle)                                       
                        if not self.grd.isValidMove(game.grd.validShape):
                            self.posY -=1
                        else:    
                            self.moveDownActive = 1                        
                        self.p=1                 
                elif (keys[pygame.K_UP]):                 
                        self.p=1
                        lastAngle=self.keyPressAngle
                        self.keyPressAngle += 1
                        if (self.keyPressAngle ==4):
                                self.keyPressAngle = 0
                        self.grd.validShape.createTempShapeDetails(screen,self.posX,self.posY,self.keyPressAngle)                                       
                        if not self.grd.isValidMove(game.grd.validShape):
                            self.keyPressAngle=lastAngle                        
                        self.p=1
                else:
                    if (self.gameOver== False):
                        #print(self.posY)
                        if (self.posY==21):
                            print("21")
                        self.grd.validShape.createTempShapeDetails(screen,self.posX,self.posY,self.keyPressAngle)                                       
                        if not self.grd.isValidMove(game.grd.validShape):
                            self.gameOver = True
                            #print("Game Over")

                if (self.p==1):
                    self.lastPressed = datetime.utcnow() - datetime(1970, 1, 1)
                    self.lSeconds =(self.lastPressed.total_seconds())
                    self.lMilliseconds = round(self.lSeconds*1000)    
 
    def processNextShape(self):
        self.pendingSelectedShape = r(7)
        self.grd.nextShape.drawNextShape(self.pendingSelectedShape)
    
    def drowFrame(self,s):
            for r in range(TETRIS_ROWS+2):                        
                b1= Brick(0,r,8)
                b2= Brick(TETRIS_COLS+1,r,8)
                b1.drawIt(s)
                b2.drawIt(s)
            for c in range(TETRIS_COLS+1):
                b1= Brick(c,0,8)
                b2= Brick(c,TETRIS_ROWS+1,8)
                b1.drawIt(s)                     
                b2.drawIt(s)         
        
        
            for c in range(11,20,1):
                b1= Brick(c,0,8)
                b2= Brick(c,15,8)
                b1.drawIt(s)                     
                b2.drawIt(s)         
    
            for r in range(1,15,1):
                b1= Brick(19,r,8)
                b1.drawIt(s)                     
                           
    
        
          
    def play(self,keys,screen):
        
        if (self.gameOver):
            self.grd.RemoveAllBricks(screen)
            return
        self.grd.drawGridLines(screen)
        
        self.drowFrame(screen)
    
        if (self.gameOver):
            print("GameOver")
            game.resetGame()
            self.start_Game = 1
            self.gameOver=False
            self.in_Game = 0
                       
        self.moveShape(keys) 
        #dis.fill((0, 0, 0))
        self.line_color = (0, 0, 0)
        self.shouldDrop()
    
        if (game.dropTimer==1):
            self.posY +=1
            self.grd.validShape.createTempShapeDetails(screen,self.posX,self.posY,self.keyPressAngle)                                       
            if not self.grd.isValidMove(game.grd.validShape):
                self.posY -=1
            a=6       
            self.LevelUP()       
        
        if (game.dropTimerFast==1):
            self.posY +=1
            self.grd.validShape.createTempShapeDetails(screen,self.posX,self.posY,self.keyPressAngle)                                       
            if not self.grd.isValidMove(game.grd.validShape):
                self.posY -=1
            a=6       
            self.LevelUP()      
          
        hitBottom = self.grd.checkBottomGrid(self.grd.activeShape.getShape())  
        self.grd.validShape.createTempShapeDetails(screen,self.posX,self.posY,self.keyPressAngle)                                       
        if not self.grd.isValidMove(game.grd.validShape):
            print("not valid")
        if (hitBottom):
            self.grd.addBricks(self.grd.activeShape)
            self.grd.removeCompleteLine()
            self.posX = START_POS_X   
            self.posY = START_POS_Y
            self.need_Shape = 1
            self.moveDownActive=0
            game.dropTimerFast=0
            
        
        if (self.in_Game == 1 & self.moveDownActive == 1):
            
            game.shouldDropFast()
            #if (self.dropTimerFast==1):                
            #        game.posY = game.posY+1
        
        if  (self.start_Game==1):
                #clearBorad()
                self.in_Game = 1
                self.start_Game = 0
                self.need_Shape= 1
                self.posX = START_POS_X   
        if (self.in_Game==1 & self.need_Shape ==1):
                self.selectedShape = self.pendingSelectedShape
                self.processNextShape()
                self.need_Shape = 0        
        if (self.in_Game==1):
                #object
                self.grd.activeShape.resetShape(self.selectedShape)
                self.grd.activeShape.drawShape(screen,self.posX,self.posY,self.keyPressAngle)
                self.grd.refreshGrid(screen)
                self.grd.nextShape.drawNextShape(self.pendingSelectedShape)      
    
    
        
clock = pygame.time.Clock()

def r(n):
        return random.randint(1,n)
    
pygame.init()
background_colour = (5,5,5)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
image = pygame.image.load("Tetris_Images/Tetris1.jpg")
image = pygame.transform.scale(image,(211,70))
image2 = pygame.image.load("Tetris_Images/Wall.jpg").convert()
image2 = pygame.transform.scale(image2,(300,430))
image2.set_alpha(50)

image3 = pygame.image.load("Tetris_Images/tetriswall.jpeg").convert()
image3 = pygame.transform.scale(image3,(SCREEN_HEIGTH,SCREEN_WIDTH))
image3.set_alpha(50)

screen.fill(background_colour)
pygame.display.update()

game = Game()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False   
    keys = pygame.key.get_pressed()
    screen.fill([20,10,10])    
    screen.blit(image3,(0,0))
    pygame.draw.rect(screen,(0,0,0),(200,40,300,660))
    screen.blit(image2,(200,250))
    screen.blit(image,(530,60))
    game.play(keys,screen)
    
    pygame.display.flip()
    clock.tick(50)

pygame.quit()


