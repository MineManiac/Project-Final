import random
import pygame
from config import WIDTH, HEIGHT, METEOR_WIDTH, METEOR_HEIGHT, SHIP_WIDTH, SHIP_HEIGHT
from assets import CORONAVIRUS_IMG, CARDIB_IMG

class Cardib (pygame.sprite.Sprite):
    def __init__(self, groups, assets):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets[CARDIB_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2   ###
        self.rect.bottom = HEIGHT - 10  ###
        self.speedy = 0 
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição da personagem:
        self.rect.y += self.speedy 

        # Mantendo a imagem dentro da tela:
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Coronavirus (pygame.sprite.Sprite):
    def __init__(self, assets):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets[CORONAVIRUS_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-CORONAVIRUS_WIDTH)
        self.rect.y = random.randint(-100, -CORONAVIRUS_HEIGHT)
        self.speedx = random.randint(2, 5)
        self.speedy = random.randint(-4, 9)

    def update(self):
        # Atualizando a posição do vírus
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-CARDIB_WIDTH)
            self.rect.y = random.randint(-100, -CARDIB_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)
