import pygame
import random
from os import PathLike
from config import IMAGE_DIR, BLACK, FPS, GAME, QUIT

#Criação Tela de inicialização
def init_screen(screen):

    clock = pygame.time.Clock()

    #Load do fundo da tela inicial
    background = pygame.image.load(path.join(IMAGE_DIR, 'Nome do arquivo background PNG')).convert()
    background_rect = background.get_rect()

    RUNNING = True
    while RUNNING:

        #Frames per Second (velocidade do jogo)
        clock.tick(FPS)

        #Processamento de eventos
        for event in pygame.event.get():
            
            #Verificação do fechamento do evento.
            if event.type == pygame.QUIT:
                state = QUIT
                RUNNING = False

            if event.type == pygame.KEYUP: ###
                state = GAME
                running = False
            
        screen.fill(BLACK)
        screen.blit(background, background_rect)


    return state
