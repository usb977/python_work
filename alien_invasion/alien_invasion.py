import sys       #退出游戏的时候需要用到
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock_ = pygame.time.Clock()                       #创建一个时钟对象
        self.settings_ = Settings()
        self.screen_ = pygame.display.set_mode(
            (self.settings_.screen_width_, self.settings_.screen_height_))      #实参是一个元组，返回一个surface对象：显示窗口
        pygame.display.set_caption("外星人入侵")                    #标题栏
        self.ship_ = Ship(self)
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock_.tick(60)       #游戏的帧率设为60
    
    def _check_events(self):             #将事件管理和更新屏幕等游戏循环动作隔离
        #监听键盘和鼠标事件,for循环处理
            for event in pygame.event.get():      #get()返回的是列表
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        """每次更新屏幕上的图像，并切换到新屏幕"""
        self.screen_.fill(self.settings_.bg_color_)
        self.ship_.blitme()
        #每次while调用都更新一次屏幕
        pygame.display.flip()   

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

