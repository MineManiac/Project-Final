from os import path

# Diretório dos Assets
IMAGE_DIR = path.join(path.dirname(__file__), 'Assets', 'Images')
SOUND_DIR = path.join(path.dirname(__file__), 'Assets', 'Sounds')
FONT_DIR = path.join(path.dirname(__file__), 'Assets', 'Fonts')


# Ajuste Tela e Frames
WIDTH = 480
HEIGHT = 600
FPS = 60


# Definição de Tamanhos


# Definição de Variáveis com cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# Controle de Fluxo da Aplicação
INIT = 0
GAME = 1
QUIT = 2
