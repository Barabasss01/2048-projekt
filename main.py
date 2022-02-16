"""

import pygame, sys
pygame.init()

size = width, height = 560, 560
screen = pygame.display.set_mode(size)
screen.fill("azure")
pygame.display.set_caption('2048 Játék')
font = pygame.font.Font('freesansbold.ttf', 64)
text = font.render('Győztél!', True, (0,0,0))
textRect = text.get_rect()
textRect.center = (width // 2, height // 2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(text, textRect)
    pygame.display.flip()
pygame.quit()
"""

import pygame
from random import randint

pygame.init()
pygame.font.init()
comicSans = pygame.font.SysFont('Comic Sans MS', 30)

FRAMES = 60
GRIDSIZE = 5
TILESIZE = 100
GAPSIZE = 10
BORDERSIZE = 5

class Square:
    def __init__(self, row, col):
        self.rectPos = (row*(TILESIZE+GAPSIZE)+GAPSIZE, col*(TILESIZE+GAPSIZE)+GAPSIZE)
        self.rect = pygame.Rect(row*(TILESIZE+GAPSIZE)+GAPSIZE+BORDERSIZE, col*(TILESIZE+GAPSIZE)+GAPSIZE+BORDERSIZE, TILESIZE-BORDERSIZE*2, TILESIZE-BORDERSIZE*2)
        self.borderRect = pygame.Rect(row*(TILESIZE+GAPSIZE)+GAPSIZE, col*(TILESIZE+GAPSIZE)+GAPSIZE, TILESIZE, TILESIZE)
    
    value = 0
    color = (255, 255, 255)
    border = (255, 255, 255)
    def _GetColor(self):
        if self.value == 0:
            self.color = (255, 255, 255)
            self.border = (255, 255, 255)
        elif self.value == 2:
            self.color = (255, 210, 210)
            self.border = (0, 0, 0)
        elif self.value == 4:
            self.color = (255, 170, 170)
            self.border = (0, 0, 0)
        elif self.value == 8:
            self.color = (255, 140, 140)
            self.border = (0, 0, 0)
        elif self.value == 16:
            self.color = (255, 100, 100)
            self.border = (0, 0, 0)
        elif self.value == 32:
            self.color = (255, 60, 60)
            self.border = (0, 0, 0)
        elif self.value == 64:
            self.color = (255, 20, 20)
            self.border = (0, 0, 0)
        elif self.value == 128:
            self.color = (235, 0, 0)
            self.border = (0, 0, 0)
        elif self.value == 256:
            self.color = (200, 0, 0)
            self.border = (0, 0, 0)
        elif self.value == 512:
            self.color = (160, 0, 0)
            self.border = (0, 0, 0)
        elif self.value == 1024:
            self.color = (120, 0, 0)
            self.border = (0, 0, 0)

    def SetValue(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value) 
    
    def Draw(self, screen):
        self._GetColor()
        pygame.draw.rect(screen, self.border, self.borderRect)
        pygame.draw.rect(screen, self.color, self.rect)
        if self.value > 0:
            font = comicSans.render(str(self.value), 1, "black")
            size = comicSans.size(str(self.value))
            screen.blit(font, (self.rectPos[0]+TILESIZE/2-size[0]/2, self.rectPos[1]+TILESIZE/2-size[1]/2))

class Game:
    def __init__(self):
        self.size = (GRIDSIZE*TILESIZE+(GRIDSIZE+1)*GAPSIZE, GRIDSIZE*TILESIZE+(GRIDSIZE+1)*GAPSIZE)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size)
        self.squares = [[Square(i, k) for k in range(GRIDSIZE)] for i in range(GRIDSIZE)]
        self.squares[randint(0, GRIDSIZE-1)][randint(0, GRIDSIZE-1)].SetValue(2)

    def Render(self):
        self.screen.fill((200, 200, 200))
        for i in self.squares:
            for rect in i:
                rect.Draw(self.screen)
        self.clock.tick(FRAMES)

    def Move(self, dire):
        recurse = False
        print("Move")
        for colIndex, col in enumerate(self.squares):
            for Index, square in enumerate(col):
                if not square.value > 0: continue
                if dire == 0:
                    if Index == 0: continue
                    if not self.squares[colIndex][Index-1].value == 0:
                        if self.squares[colIndex][Index-1].value == self.squares[colIndex][Index].value:
                            recurse = True
                            self.squares[colIndex][Index-1].SetValue(square.value+square.value)
                            self.squares[colIndex][Index].SetValue(0)
                            continue
                        else:
                            continue

                    recurse = True
                    self.squares[colIndex][Index-1].SetValue(square.value)
                    self.squares[colIndex][Index].SetValue(0)
                elif dire == 1:
                    if colIndex == len(self.squares)-1: continue
                    if not self.squares[colIndex+1][Index].value == 0:
                        if self.squares[colIndex+1][Index].value == self.squares[colIndex][Index].value:
                            recurse = True
                            self.squares[colIndex+1][Index].SetValue(square.value+square.value)
                            self.squares[colIndex][Index].SetValue(0)
                            continue
                        else:
                            continue
                    recurse = True
                    self.squares[colIndex+1][Index].SetValue(square.value)
                    self.squares[colIndex][Index].SetValue(0)
                elif dire == 2:
                    if Index == len(col)-1: continue
                    if not self.squares[colIndex][Index+1].value == 0:
                        if self.squares[colIndex][Index+1].value == self.squares[colIndex][Index].value:
                            recurse = True
                            self.squares[colIndex][Index+1].SetValue(square.value+square.value)
                            self.squares[colIndex][Index].SetValue(0)
                            continue
                        else:
                            continue
                    recurse = True
                    self.squares[colIndex][Index+1].SetValue(square.value)
                    self.squares[colIndex][Index].SetValue(0)
                elif dire == 3:
                    if colIndex == 0: continue
                    if not self.squares[colIndex-1][Index].value == 0:
                        if self.squares[colIndex-1][Index].value == self.squares[colIndex][Index].value:
                            recurse = True
                            self.squares[colIndex-1][Index].SetValue(square.value+square.value)
                            self.squares[colIndex][Index].SetValue(0)
                            continue
                        else:
                            continue
                    recurse = True
                    self.squares[colIndex-1][Index].SetValue(square.value)
                    self.squares[colIndex][Index].SetValue(0)
        
        if recurse:
            self.Move(dire)
            return
        space = False
        for col in self.squares:
            for square in col:
                if square.value == 0:
                    print("space")
                    space = True
                    break
        if not space: return
        random = self.squares[randint(0, GRIDSIZE-1)][randint(0, GRIDSIZE-1)]
        while not random.value == 0:
            random = self.squares[randint(0, GRIDSIZE-1)][randint(0, GRIDSIZE-1)]
        random.SetValue(2)


    def KeyPress(self, key):
        if key == pygame.K_UP:
            self.Move(0)
        elif key == pygame.K_RIGHT:
            self.Move(1)
        elif key == pygame.K_DOWN:
            self.Move(2)
        elif key == pygame.K_LEFT:
            self.Move(3)



Instance = Game()

keypress = 0

end = 0
while not end:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            end = 1
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                end = 1
            if not keypress:
                keypress = e.key
                Instance.KeyPress(e.key)
        if e.type == pygame.KEYUP:
            if keypress == e.key:
                keypress = 0
    
    Instance.Render()
    pygame.display.flip()
