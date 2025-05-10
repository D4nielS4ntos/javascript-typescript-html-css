import pygame
from sys import exit

pygame.init()

LARGURA = 640
ALTURA =  480

vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

x = LARGURA / 2
y = ALTURA / 2

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('teste')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, vermelho, (x, y, 40, 40))
        
    if y >= ALTURA:
        y = 0  
    y += 1
    
    pygame.display.update()
