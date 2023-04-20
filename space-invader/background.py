import pygame
from pygame.locals import *
pygame.init()
BG = pygame.image.load('bg_main2.png')
BG = pygame.transform.scale(BG, (900, 600))

DISPLAYSURF = pygame.display.set_mode((900, 600))

class Background():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 2
        self.img = BG
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    # ve background
    def draw(self):
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y + self.height)))
