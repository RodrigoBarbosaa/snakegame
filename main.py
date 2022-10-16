import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
x = largura/2
y = altura/2
x_maca = 100
y_maca = 250
pontos = 0
lista_cobra = []
comprimento_inicial = 3
morreu = False

x_controle = 10
y_controle = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('WADSBF')
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont('arial', 40, True, False)
fonte2 = pygame.font.SysFont('arial', 26, True, False)


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


while True:
    mensagem = f'Pontos: {pontos}'

    relogio.tick(30)
    tela.fill((255, 255, 255))
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == 10:
                    pass
                else:
                    x_controle = -10
                    y_controle = 0

            if event.key == K_d:
                if x_controle == -10:
                    pass
                else:
                    x_controle = 10
                    y_controle = 0

            if event.key == K_w:
                if y_controle == 10:
                    pass
                else:
                    y_controle = -10
                    x_controle = 0

            if event.key == K_s:
                if y_controle == -10:
                    pass
                else:
                    y_controle = +10
                    x_controle = 0

    x += x_controle
    y += y_controle

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x, y, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca = randint(20, 620)
        y_maca = randint(20, 460)
        pontos += 1
        comprimento_inicial += 1

    lista_cabeca = []
    lista_cabeca.append(x)
    lista_cabeca.append(y)
    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    if lista_cobra.count(lista_cabeca) > 1:
        morreu = True
        while morreu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_r:
                        pontos = 0
                        comprimento_inicial = 3
                        lista_cabeca = []
                        lista_cobra = []
                        x_maca = randint(20, 620)
                        y_maca = randint(20, 460)
                        morreu = False

            tela.fill((255, 255, 255))
            mensagem1 = f'Você morrreu! Aperte R para voltar ao jogo.'
            texto_formatado1 = fonte2.render(mensagem1, True, (0, 0, 0))
            tela.blit(texto_formatado1, (45, 220))
            pygame.display.update()

    if x > largura:
        x = 0
    if x < 0:
        x = largura
    if y > altura:
        y = 0
    if y < 0:
        y = largura
    aumenta_cobra(lista_cobra)
    tela.blit(texto_formatado, (420, 10))
    pygame.display.update()
