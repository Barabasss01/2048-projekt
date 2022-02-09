import pygame
from random import randint

pygame.init()
pygame.font.init()
comicSans = pygame.font.SysFont('Comic Sans MS', 30)

GRIDSIZE = 5
TILESIZE = 100
GAPSIZE = 10

clock = pygame.time.Clock()
size = (GRIDSIZE*TILESIZE+(GRIDSIZE+1)*GAPSIZE, GRIDSIZE*TILESIZE+(GRIDSIZE+1)*GAPSIZE)

screen = pygame.display.set_mode(size)

class Square:
    def __init__(self, row, col):
        self.rectPos = (row*(TILESIZE+GAPSIZE)+GAPSIZE, col*(TILESIZE+GAPSIZE)+GAPSIZE)
        self.rect = pygame.Rect(row*(TILESIZE+GAPSIZE)+GAPSIZE, col*(TILESIZE+GAPSIZE)+GAPSIZE, TILESIZE, TILESIZE)
    
    value = 0
    def _GetColor(self):
        return "white"

    def SetValue(self, value):
        self.value = value
    
    def Draw(self):
        pygame.draw.rect(screen, self._GetColor(), self.rect)
        if self.value > 0:
            font = comicSans.render(str(self.value), 1, "black")
            size = comicSans.size(str(self.value))
            screen.blit(font, (self.rectPos[0]+TILESIZE/2-size[0]/2, self.rectPos[1]+TILESIZE/2-size[1]/2))

squares = [[Square(i, k) for k in range(GRIDSIZE)] for i in range(GRIDSIZE)]

squares[randint(0, GRIDSIZE-1)][randint(0, GRIDSIZE-1)].SetValue(10)

keypress = 0

while 1:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
            if not keypress:
                keypress = e.key
                print(f"{e.key} was pressed")
        if e.type == pygame.KEYUP:
            if keypress == e.key:
                keypress = 0
                print(f"{e.key} was released")

    screen.fill((200, 200, 200))
    for i in squares:
        for rect in i:
            rect.Draw()
    clock.tick(60)
    pygame.display.flip()