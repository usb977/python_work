import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen_ = ai_game.screen_  #屏幕
        self.screen_rect_ = ai_game.screen_.get_rect()    #为了将飞船放到屏幕的合适位置，首先要获取屏幕的位置属性
        self.settings_ = ai_game.settings_

        self.image_ = pygame.image.load('images/ship.bmp')
        self.rect_ = self.image_.get_rect()

        self.rect_.midbottom = self.screen_rect_.midbottom   #飞船的底部和屏幕的底部 边缘对齐
        self.x_ = float(self.rect_.x)
        self.moving_right_ = False
        self.moving_left_ = False

    def update(self):
        """根据flag来调整飞船的位置"""
        if self.moving_right_ and self.rect_.right < self.screen_rect_.right:
            self.x_ += self.settings_.ship_speed_
        if self.moving_left_ and self.rect_.left > 0:     #此处不能用elif语句
            self.x_ -= self.settings_.ship_speed_
        #将更新后的飞船的x_属性赋值给飞船自身矩形的属性,仅作为显示
        self.rect_.x = self.x_

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen_.blit(self.image_, self.rect_)