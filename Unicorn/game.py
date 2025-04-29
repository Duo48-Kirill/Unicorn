import pygame
from g12 import g12
from g8 import g8
import time

pygame.init()

WIDTH = 400  # 50 300 50
HEIGHT = 600  # 50 200 100 200 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))

sprites = pygame.sprite.Group()

settings = pygame.sprite.Sprite(sprites)
settings.image = pygame.image.load("static/set/settings .png")
settings.rect = settings.image.get_rect()
settings.rect.left = 0
settings.rect.top = 0

sprites.draw(screen)
pygame.display.update()

cycle_1 = True
ch = 0

field = [[0 for i in range(8)] for i in range(12)]
CELLx = WIDTH // 8
CELLy = HEIGHT // 12

while cycle_1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            i = x // CELLx
            j = y // CELLy

            if 1 < i and i < 7 and 1 < j and j < 5:
                ch = 1
            if 1 < i and i < 7 and 8 < j and j < 11:
                ch = 2

    if ch == 1 or ch == 2:
        cycle_1 = False

pygame.quit()


time.sleep(3)

if ch == 1:
    g8()
if ch == 2:
    g12()
