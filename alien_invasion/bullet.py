import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船所发射的子弹的类"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen_ = ai_game.screen_
        self.settings_ = ai_game.settings_
        self.color_ = self.settings_.bullet_color_

        #在(0,0)处手动创建一个表示子弹的矩形，再设置正确的位置
        self.rect_ = pygame.Rect(0,0,self.settings_.bullet_width_, self.settings_.bullet_height_)
        self.rect_.midtop = ai_game.ship_.rect_.midtop
        
        #将子弹的高度坐标存为浮点数
        self.y_ = float(self.rect_.y)
    
    def update(self):
        """向上移动子弹"""
        self.y_ -= self.settings_.bullet_speed_
        self.rect_.y = self.y_
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen_, self.color_, self.rect_)