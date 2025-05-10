import pygame
from random import randint
from sys import exit


pygame.init()

LARGURA = 640
ALTURA =  480

vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

x = LARGURA / 2
y = ALTURA / 2
x_random = randint(0, LARGURA)
y_random = randint(0, ALTURA)

lado_quadrado = 40

pontos = 0

fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('teste')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    pygame.mixer.music.set_volume(0.75)
    musica_de_fundo = pygame.mixer.music.load('sons/somFundo.wav')
    pygame.mixer.music.play(-1)

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

    retangulo_vermelho = pygame.draw.rect(tela, vermelho, (x, y, lado_quadrado, lado_quadrado))
    retangulo_azul = pygame.draw.rect(tela, azul, (x_random, y_random, lado_quadrado, lado_quadrado))

    if retangulo_vermelho.colliderect(retangulo_azul):
        som_colisao = pygame.mixer.music.load('sons/pickupCoin.wav')
        pygame.mixer.music.play()

        x_random = randint(0, LARGURA)
        y_random = randint(0, ALTURA)
        retangulo_azul = pygame.draw.rect(tela, azul, (x_random, y_random, lado_quadrado, lado_quadrado))
        pontos += 1

    tela.blit(texto_formatado, (20, 20))
    pygame.display.update()
