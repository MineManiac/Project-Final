import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED 
from assets import load_assets, BACKGROUND, SCORE_FONT ###
from sprites import Coronavirus, Cardib 

def game_screen (window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    all_coronavirus = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_coronavirus'] = all_coronavirus

    # Criando o jogador
    player = Cardib(groups, assets)
    all_sprites.add(player)

    # Criando os vírus
    for i in range(7):
        coronavirus = Coronavirus(assets)
        all_sprites.add(coronavirus)
        all_meteors.add(coronavirus)

    DONE = 0
    PLAYING = 1
    state = PLAYING