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

lado_quadrado = 40

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= lado_quadrado
            if event.key == pygame.K_a:
                x -= lado_quadrado
            if event.key == pygame.K_s:
                y += lado_quadrado
            if event.key == pygame.K_d:
                x += lado_quadrado
        # if pygame.key.get_pressed()[pygame.K_w]:
        #     y -= 10
        # if pygame.key.get_pressed()[pygame.K_a]:
        #     x -= 10
        # if pygame.key.get_pressed()[pygame.K_s]:
        #     y += 10
        # if pygame.key.get_pressed()[pygame.K_d]:
        #     x += 10

    pygame.draw.rect(tela, vermelho, (x, y, lado_quadrado, lado_quadrado))

    pygame.display.update()
