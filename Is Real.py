# Imporando as bibliotecas necessárias:
import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CardiBee')

# Grantindo FPS máximo de 30Hz:
FPS = 30 

CORONAVIRUS_WIDTH = 50
CORONAVIRUS_HEIGHT = 38
CARDIB_WIDTH = 100
CARDIB_HEIGHT = 120

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('Assets/Images/background.jpg').convert()
    assets['coronavirus_img'] = pygame.image.load('Assets/Images/coronavirus.png').convert_alpha()
    assets['coronavirus_img'] = pygame.transform.scale(assets['coronavirus_img'], (CORONAVIRUS_WIDTH, CORONAVIRUS_HEIGHT))
    assets['cardib_img'] = pygame.image.load('Assets/Images/cardib.png').convert_alpha()
    assets['cardib_img'] = pygame.transform.scale(assets['cardib_img'], (CARDIB_WIDTH, CARDIB_HEIGHT))

    return assets

class Cardib (pygame.sprite.Sprite):

    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['cardib_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.groups = groups
        self.assets = assets

    def update (self):
        # Atualização da posição da personagem
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Coronavirus (pygame.sprite.Sprite):

    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['coronavirus_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-CORONAVIRUS_WIDTH)
        self.rect.y = random.randint(-100, -CORONAVIRUS_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update (self):
        # Atualizando a posição do vírus
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-CORONAVIRUS_WIDTH)
            self.rect.y = random.randint(-100, -CORONAVIRUS_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

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
    for i in range(7):
        coronavirus = Coronavirus(assets)
        all_sprites.add(coronavirus)
        all_coronavirus.add(coronavirus)

    END = 0
    PLAYING = 1
    state = PLAYING

    # keys_down = {}
    # score = 0
    # lives = 3

    while state != END:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state = END
 
            if state == PLAYING:
 
                if event.type == pygame.KEYDOWN:
                #keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8

                if event.type == pygame.KEYUP:
                    #if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_LEFT:
                        player.speedx += 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx -= 8

        all_sprites.update()

        if state == PLAYING:

            hits = pygame.sprite.spritecollide(player, all_coronavirus, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                state = END

        window.fill((0, 0, 0)) 
        window.blit(assets['background'], (0, 0))
        all_sprites.draw(window)
        pygame.display.update()

game_screen(window)

pygame.quit() 
