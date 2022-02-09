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