# Imporando as bibliotecas necessárias:
import pygame
import random

pygame.init()
pygame.mixer.init()
WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CardiBee')

# Grantindo FPS máximo de 30Hz:
FPS = 60 

CORONAVIRUS_WIDTH = 50
CORONAVIRUS_HEIGHT = 38
CARDIB_WIDTH = 100
CARDIB_HEIGHT = 120

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('Assets/Images/background.jpg').convert()
    assets['background'] = pygame.transform.scale(assets['background'], (600,600))
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
        self.rect.left = 10
        self.rect.centery = HEIGHT/ 2
        self.speedy = 0 
        self.speedx = 0
        self.groups = groups
        self.assets = assets

    def update(self):
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
        self.rect.x = random.randint(600, WIDTH +CORONAVIRUS_WIDTH)
        self.rect.y = random.randint(-CORONAVIRUS_HEIGHT, HEIGHT-CORONAVIRUS_HEIGHT)
        self.speedx = random.randint(2, 5)
        self.speedy = random.randint(-4, 9)



    def update (self):
        # Atualizando a posição do vírus
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(600, WIDTH +CORONAVIRUS_WIDTH)
            self.rect.y = random.randint(-CORONAVIRUS_HEIGHT, HEIGHT-CORONAVIRUS_HEIGHT)
            self.speedx = random.randint(-6, -2)
            self.speedy = random.randint(-3,3)

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
                    if event.key == pygame.K_UP:
                        player.speedy -= 8
                    if event.key == pygame.K_DOWN:
                        player.speedy += 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8 
                    if event.key == pygame.K_LEFT:
                        player.speedx -=8
                if event.type == pygame.KEYUP:
                    #if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_UP:
                        player.speedy += 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx -= 8
                    if event.key == pygame.K_DOWN:
                        player.speedy -= 8
                    if event.key == pygame.K_LEFT:
                        player.speedx += 8

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
