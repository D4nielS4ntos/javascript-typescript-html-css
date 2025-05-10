import pygame
from random import randint
from sys import exit


LARGURA = 640
ALTURA =  480

VELOCIDADE = 10
LADO_QUADRADO = 20

vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

x_cobra = int(LARGURA / 2)
y_cobra = int(ALTURA / 2)

x_controle = 0
y_controle = 0

x_random = randint(0, LARGURA)
y_random = randint(0, ALTURA)

pontos = 0
comprimento_cobra = 5
lista_cobra = []

pygame.init()
fonte = pygame.font.SysFont('arial', 20, True, True)
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('teste')
relogio = pygame.time.Clock()


def aumenta_cobra(lista_cobra):
    for posicaoXeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (posicaoXeY[0], posicaoXeY[1], 20, 20))


def ask(input):
    if event.key == pygame.K_ESCAPE:
        playing = False
    if event.key == pygame.K_q:
        input = input + "q"
    if event.key == pygame.K_w:
        input = input + "w"
    if event.key == pygame.K_e:
        input = input + "e"
    if event.key == pygame.K_r:
        input = input + "r"
    if event.key == pygame.K_t:
        input = input + "t"
    if event.key == pygame.K_y:
        input = input + "y"
    if event.key == pygame.K_u:
        input = input + "u"
    if event.key == pygame.K_i:
        input = input + "i"
    if event.key == pygame.K_o:
        input = input + "o"
    if event.key == pygame.K_p:
        input = input + "p"
    if event.key == pygame.K_a:
        input = input + "a"
    if event.key == pygame.K_s:
        input = input + "s"
    if event.key == pygame.K_d:
        input = input + "d"
    if event.key == pygame.K_f:
        input = input + "f"
    if event.key == pygame.K_g:
        input = input + "g"
    if event.key == pygame.K_h:
        input = input + "h"
    if event.key == pygame.K_j:
        input = input + "j"
    if event.key == pygame.K_k:
        input = input + "k"
    if event.key == pygame.K_l:
        input = input + "l"
    if event.key == pygame.K_z:
        input = input + "z"
    if event.key == pygame.K_x:
        input = input + "x"
    if event.key == pygame.K_c:
        input = input + "c"
    if event.key == pygame.K_v:
        input = input + "v"
    if event.key == pygame.K_b:
        input = input + "b"
    if event.key == pygame.K_n:
        input = input + "n"
    if event.key == pygame.K_m:
        input = input + "m"
    return input
# input = ask(input)s
input = ''


def reiniciar_jogo():
    global x_cobra, y_cobra, x_controle, y_controle, x_random, y_random, lista_cobra, lista_cabeca, pontos, comprimento_cobra, morreu

    x_cobra = int(LARGURA / 2)
    y_cobra = int(ALTURA / 2)

    x_controle = 0
    y_controle = 0

    x_random = randint(0, LARGURA)
    y_random = randint(0, ALTURA)


    lista_cobra = []
    lista_cabeca = []

    pontos = 0
    comprimento_cobra = 5

    morreu = False


while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))

    mensagem = f'Pontos: {pontos}' +input.upper()
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    tela.blit(texto_formatado, (20, 20))

    pygame.mixer.music.set_volume(0.75)
    musica_de_fundo = pygame.mixer.music.load('sons/somFundo.wav')
    pygame.mixer.music.play(-1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            input = ask(input)
            if event.key == pygame.K_w:
                if y_controle == VELOCIDADE:
                    pass
                else:
                    x_controle = 0
                    y_controle -= VELOCIDADE

            if event.key == pygame.K_a:

                if x_controle == VELOCIDADE:
                    pass
                else:
                    x_controle -= VELOCIDADE
                    y_controle = 0

            if event.key == pygame.K_s:

                if y_controle == -VELOCIDADE:
                    pass
                else:
                    x_controle = 0
                    y_controle += VELOCIDADE

            if event.key == pygame.K_d:

                if x_controle == -VELOCIDADE:
                    pass
                else:
                    x_controle += VELOCIDADE
                    y_controle = 0

    x_cobra += x_controle
    y_cobra += y_controle

    cobra = pygame.draw.rect(tela, verde, (x_cobra, y_cobra, LADO_QUADRADO, LADO_QUADRADO))
    maca = pygame.draw.rect(tela, vermelho, (x_random, y_random, LADO_QUADRADO, LADO_QUADRADO))

    if cobra.colliderect(maca):
        som_colisao = pygame.mixer.music.load('sons/pickupCoin.wav')
        pygame.mixer.music.play()

        x_random = randint(x_cobra, LARGURA) - x_cobra
        y_random = randint(y_cobra, ALTURA) - y_cobra
        maca = pygame.draw.rect(tela, vermelho, (x_random, y_random, LADO_QUADRADO, LADO_QUADRADO))
        pontos += 1
        comprimento_cobra += 1

    if x_cobra >= LARGURA: 
        x_cobra = 0
        x_controle = VELOCIDADE

    elif x_cobra<= 0: 
        x_cobra = LARGURA - LADO_QUADRADO
        x_controle = -VELOCIDADE

    elif y_cobra >= ALTURA: 
        y_cobra = 0
        y_controle = VELOCIDADE

    elif y_cobra <= 0: 
        y_cobra = ALTURA - LADO_QUADRADO
        y_controle = -VELOCIDADE

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1 and comprimento_cobra > 5:
        fonte_restart = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte_restart.render(mensagem, True, (0, 0, 0))
        rect_texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            tela.fill(( ))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reiniciar_jogo()
            rect_texto.center = (LARGURA//2, ALTURA//2)
            tela.blit(texto_formatado, rect_texto)
            pygame.display.update()


    if len(lista_cobra) > comprimento_cobra:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    pygame.display.update()
