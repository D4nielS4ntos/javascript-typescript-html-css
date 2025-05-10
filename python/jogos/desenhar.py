import pygame
from sys import exit

pygame.init()

LARGURA = 640
ALTURA =  480

vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('teste')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, verde, (290, 190, 20, 40))
    pygame.draw.rect(tela, verde, (330, 250, 20, 40))
    pygame.draw.rect(tela, verde, (290, 250, 20, 40))
    pygame.draw.rect(tela, verde, (330, 190, 20, 40))
    pygame.draw.circle(tela, vermelho, (320, 240), 10)
    pygame.draw.line(tela, azul, (0, 0), (640, 480))
    pygame.draw.line(tela, azul, (640, 0), (0, 480))
    pygame.display.update()
