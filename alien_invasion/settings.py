class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width_ = 1200
        self.screen_height_ = 800
        self.bg_color_ = (230, 230, 230)
        #飞船设置：3条命
        self.ship_speed_ = 2.5
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed_ = 3.0
        self.bullet_width_ = 3
        self.bullet_height_ = 15
        self.bullet_color_ = (60, 60, 60)
        self.bullet_allowed_ = 3
        #外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10    #向下移动的速度
        self.fleet_direction = 1     #fleet_direction为方向控制，1为向右，-1为向左