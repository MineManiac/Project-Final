# Importando as bibliotecas necessárias:
import pygame
import random
import os
from os import path

pygame.init()
pygame.mixer.init()
WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CardiBee')

# Grantindo FPS máximo de 30Hz:
FPS = 60 

CORONAVIRUS_WIDTH =  65
CORONAVIRUS_HEIGHT = 50
CARDIB_WIDTH = 98
CARDIB_HEIGHT = 90
MASK_WIDTH = 65
MASK_HEIGHT = 50
HEART_WIDTH = 30
HEART_HEIGHT = 50

SOUND_DIR = path.join(path.dirname(__file__), 'Assets', 'Sounds')

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('Assets/Images/background.jpg').convert()
    assets['background'] = pygame.transform.scale(assets['background'], (WIDTH, HEIGHT))
    assets['coronavirus_img'] = pygame.image.load('Assets/Images/coronavirus.png').convert_alpha()
    assets['coronavirus_img'] = pygame.transform.scale(assets['coronavirus_img'], (CORONAVIRUS_WIDTH, CORONAVIRUS_HEIGHT))
    assets['cardib_img'] = pygame.image.load('Assets/Images/cardib.png').convert_alpha()
    assets['cardib_img'] = pygame.transform.scale(assets['cardib_img'], (CARDIB_WIDTH, CARDIB_HEIGHT))
    assets['heart_img'] = pygame.image.load('Assets/Images/Heart.png').convert_alpha()
    assets['heart_img'] = pygame.transform.scale(assets['heart_img'], (HEART_WIDTH, HEART_HEIGHT))
    assets['mask_img'] = pygame.image.load('Assets/Images/mask.png').convert_alpha()
    assets['mask_img'] = pygame.transform.scale(assets['mask_img'], (MASK_WIDTH, MASK_HEIGHT))
       

#Sons do jogo
    pygame.mixer.music.load(os.path.join(SOUND_DIR, 'Main Song.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets['CardiB'] = pygame.mixer.Sound(os.path.join(SOUND_DIR, 'CardiB.wav'))

    return assets

class Cardib (pygame.sprite.Sprite):

    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['cardib_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left = 10
        self.rect.centery = HEIGHT/ 2
        self.speedy = 0 
        self.speedx = 0
        self.groups = groups
        self.assets = assets

    def update (self):
        # Atualização da posição da personagem:
        self.rect.y += self.speedy 
        self.rect.x += self.speedx
        # Mantendo a imagem dentro da tela:
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right >= HEIGHT:
            self.rect.right = HEIGHT
        if self.rect.left <= 0 :
            self.rect.left = 0

class Coronavirus (pygame.sprite.Sprite):

    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['coronavirus_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH, WIDTH + CORONAVIRUS_WIDTH)
        self.rect.y = random.randint(-CORONAVIRUS_HEIGHT, HEIGHT - CORONAVIRUS_HEIGHT)
        self.speedx = random.randint(2, 5)
        self.speedy = random.randint(-4, 9)

    def update (self):
        # Atualizando a posição do vírus
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(WIDTH, WIDTH + CORONAVIRUS_WIDTH)
            self.rect.y = random.randint(-CORONAVIRUS_HEIGHT, HEIGHT - CORONAVIRUS_HEIGHT)
            self.speedx = random.randint(-6, -2)
            self.speedy = random.randint(-3, 3)

class Mask (pygame.sprite.Sprite):

    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['mask_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH/2)
        self.rect.y = random.randint(0, HEIGHT)
        self.speedx = 0
        self.speedy = 0       

#  def main_menu (screen):

#     running = True
#     clock = pygame.time.Clock()
#     menu_background = pygame.

#     while running:
#         clock.tick(FPS)

#         for event in pygame.event.get:


def game_screen (window):
    # Criando objeto para controle das atualizações:
    clock = pygame.time.Clock() 

    assets = load_assets()

    # Criando um grupo de coronavírus:
    all_sprites = pygame.sprite.Group()
    all_coronavirus = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_coronavirus'] = all_coronavirus

    # Criando o jogador
    player = Cardib(groups, assets)
    all_sprites.add(player)

    # Criando os vírus
    for i in range(10):
        coronavirus = Coronavirus(assets)
        all_sprites.add(coronavirus)
        all_coronavirus.add(coronavirus)

    END = 0
    PLAYING = 1
    state = PLAYING

    # score = 0
    # lives = 3
    player_dead = False
    #   ---Loop do jogo---
    pygame.mixer.music.play(loops=-1)

    time = pygame.time.get_ticks()

    mask = None
    contador = 0
    counter_mask = 0
    while state != END:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state = END
 
            if state == PLAYING:
 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.speedy -= 8
                    if event.key == pygame.K_DOWN:
                        player.speedy += 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8 
                    if event.key == pygame.K_LEFT:
                        player.speedx -=8

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        player.speedy += 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx -= 8
                    if event.key == pygame.K_DOWN:
                        player.speedy -= 8
                    if event.key == pygame.K_LEFT:
                        player.speedx += 8

        time2 = pygame.time.get_ticks()

        if time2 - time > 5000:
            if mask == None:
                mask = Mask(assets)
                all_sprites.add(mask)
                time = pygame.time.get_ticks()
                time2 = pygame.time.get_ticks()

        all_sprites.update()

        if state == PLAYING:

            hits = pygame.sprite.spritecollide(player, all_coronavirus, True, pygame.sprite.collide_mask)
            
            invulnerable = True
           # while counter_mask < 5 :
            #    invulnerable = False
             #   counter_mask =+ 1

            if mask != None:
                hits2 = pygame.sprite.collide_rect(player, mask)
                time3 = pygame.time.get_ticks()
                # while time3 < 5000:
                #     len(hits) = 0 

            if mask != None and hits2 == True:
                mask.kill()
                mask = None
                counter_mask = 0
            if invulnerable:
                if len(hits) > 0:
                    contador+=1
                    if contador == 1 :
                        assets['CardiB'].play()
                    timer = pygame.time.get_ticks()
                    player_dead = True
                    player.kill()
                

            if player_dead == True:
                NOW = pygame.time.get_ticks()
                if NOW - timer > 2500:
                    state = END

        window.fill((0, 0, 0)) 
        window.blit(assets['background'], (0, 0))
        all_sprites.draw(window)
        pygame.display.update()

game_screen(window)

pygame.quit() 
