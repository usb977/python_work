class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width_ = 1200
        self.screen_height_ = 800
        self.bg_color_ = (230, 230, 230)
        self.ship_speed_ = 2.5

        #子弹设置
        self.bullet_speed_ = 2.0
        self.bullet_width_ = 3
        self.bullet_height_ = 15
        self.bullet_color_ = (60, 60, 60)
        self.bullet_allowed_ = 3