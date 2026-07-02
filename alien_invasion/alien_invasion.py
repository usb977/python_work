import sys       #退出游戏的时候需要用到
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock_ = pygame.time.Clock()                       #创建一个时钟对象
        self.settings_ = Settings()
        self.screen_ = pygame.display.set_mode((self.settings_.screen_width_, self.settings_.screen_height_)) 
        # self.screen_ = pygame.display.set_mode((0,0),pygame.FULLSCREEN)      #实参是一个元组，返回一个surface对象：显示窗口
        # self.settings_.screen_width_ = self.screen_.get_rect().width
        # self.settings_.screen_height_ = self.screen_.get_rect().height      #先创建屏幕对象，然后再全屏显示
        pygame.display.set_caption("外星人入侵")                    #标题栏
        self.ship_ = Ship(self)
        self.bullets_ = pygame.sprite.Group()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship_.update()
            self._update_bullets()     #更新编组中所有子弹的位置
            self._update_screen()
            self.clock_.tick(60)       #游戏的帧率设为60
    
    def _check_events(self):             #将事件管理和更新屏幕等游戏循环动作隔离
        #监听键盘和鼠标事件,for循环处理
            for event in pygame.event.get():      #get()返回的是列表
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按下事件"""
        if event.key == pygame.K_RIGHT:
            self.ship_.moving_right_ = True
        elif event.key == pygame.K_LEFT:        #这里可以用elif，因为两个键同时按下是两个事件，可以分别处理
            self.ship_.moving_left_ = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """响应按键释放事件"""
        if event.key == pygame.K_RIGHT:
            self.ship_.moving_right_ = False
        elif event.key == pygame.K_LEFT:
            self.ship_.moving_left_ = False

    def _fire_bullet(self):
        if len(self.bullets_) < self.settings_.bullet_allowed_:
            new_bullet = Bullet(self)
            self.bullets_.add(new_bullet)   #将新的子弹加入编组，类似列表

    def _update_screen(self):
        """每次更新屏幕上的图像，并切换到新屏幕"""
        self.screen_.fill(self.settings_.bg_color_)
        for bullet in self.bullets_.sprites():   #返回一个包含编组所有元素的列表
            bullet.draw_bullet()
        self.ship_.blitme()     #飞船的画面更新放后面，可以避免子弹出现在飞船上面
        #将绘制好的后台画图内容“翻”到台前
        pygame.display.flip()   

    def _update_bullets(self):
        self.bullets_.update()
        #删除消失的子弹
        for bullet in self.bullets_.copy():
                if bullet.rect_.bottom <= 0:
                    self.bullets_.remove(bullet)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

