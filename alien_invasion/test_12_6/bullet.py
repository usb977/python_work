import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船所发射的子弹的类"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.color = (60, 60, 60)

        #在(0,0)处手动创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,15,3)
        self.rect.midright = ai_game.ship_rect.midright
        
    def update(self):
        """向右发射子弹"""
        self.rect.x += 1
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)