import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height    #初始化的坐标在左上角
        self.x = float(self.rect.width)