import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CardiBee')

FPS = 30
CORONAVIRUS_WIDTH = 50
CORONAVIRUS_HEIGHT = 38
CARDIB_WIDTH = 50
CARDIB_HEIGHT = 38

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('Assets').convert()
    assets['coronavirus_img'] = pygame.image.load('Assets/Images/coronavirus.png').convert_alpha()
    assets['coronavirus_img'] = pygame.transform.scale(assets['coronavirus_img'], (CORONAVIRUS_WIDHT, CORONAVIRUS_HEIGHT))
    assets['cardib_img'] = pygame.image.load('Assets/Images/cardib').convert_alpha()
    assets['cardib_img'] = pygame.transform.scale(assets['cardib_img'], (CARDIB_WIDTH, CARDIB_HEIGHT))

    return assets

class Cardib (self, groups, assets)