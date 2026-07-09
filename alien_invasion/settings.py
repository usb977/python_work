class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width_ = 1200
        self.screen_height_ = 800
        self.bg_color_ = (230, 230, 230)
        #飞船设置：3条命
        self.ship_limit = 3

        #子弹设置
        self.bullet_width_ = 3000
        self.bullet_height_ = 15
        self.bullet_color_ = (60, 60, 60)
        self.bullet_allowed_ = 3
        #外星人设置
        self.fleet_drop_speed = 10    #向下移动的速度

        #以什么速度加快游戏的节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):  #还原游戏的初始设置
        self.ship_speed_ = 1.5
        self.bullet_speed_ = 2.5
        self.alien_speed = 1.0
        self.fleet_direction = 1     #fleet_direction为方向控制，1为向右，-1为向左
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_ *= self.speedup_scale
        self.bullet_speed_ *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        