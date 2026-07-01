import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen_ = ai_game.screen_  #屏幕
        self.screen_rect_ = ai_game.screen_.get_rect()    #为了将飞船放到屏幕的合适位置，首先要获取屏幕的位置属性

        self.image_ = pygame.image.load('images/ship.bmp')
        self.rect_ = self.image_.get_rect()

        self.rect_.midbottom = self.screen_rect_.midbottom   #飞船的底部和屏幕的底部 边缘对齐

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen_.blit(self.image_, self.rect_)