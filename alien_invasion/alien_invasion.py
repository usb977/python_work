import sys       #退出游戏的时候需要用到
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock_ = pygame.time.Clock()                    #创建一个时钟对象
        self.settings_ = Settings()
        self.screen_ = pygame.display.set_mode((self.settings_.screen_width_, self.settings_.screen_height_)) 
        pygame.display.set_caption("外星人入侵")                   #标题栏
        self.ship_ = Ship(self)
        self.bullets_ = pygame.sprite.Group()
        self.aliens_ = pygame.sprite.Group()
        self._create_fleet()                      #初始化的时候就创建一个外星人

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship_.update()
            self._update_bullets()     #更新编组中所有子弹的位置
            self._update_aliens()     #先更新子弹，再更新外星人位置，看是否有击中
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

    def _create_fleet(self):
        """创建一个外星舰队"""
        alien = Alien(self)   
        alien_width, alien_height = alien.rect.size        #创建该对象仅为获得尺寸信息，不实际加入编队

        current_x, current_y = alien_width, alien_height    #表示下一个外星人的位置
        while current_y < (self.settings_.screen_height_ - 3*alien_height):
            while current_x< (self.settings_.screen_width_-2*alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2*alien_width
            current_x = alien_width
            current_y += 2*alien_height
    
    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position          #浮点数的位置
        new_alien.rect.x = x_position   
        new_alien.rect.y = y_position     #调整对象的实际显示位置
        self.aliens_.add(new_alien)

    def _update_aliens(self):
        """检查是否有外星人位于屏幕边缘，并更新外星舰队中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens_.update()
        #检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship_, self.aliens_):    #返回第一个与飞船碰撞的外星人
            print('Ship hit!!!')

    def _check_fleet_edges(self):
        """在有外星人移动到屏幕边缘的时候采取相应的措施"""
        for alien in self.aliens_.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整个舰队下移一个步长，并改变左右移动方向"""
        for alien in self.aliens_.sprites():
            alien.rect.y += self.settings_.fleet_drop_speed
        self.settings_.fleet_direction *= -1

    def _update_screen(self):
        """每次更新屏幕上的图像，并切换到新屏幕"""
        self.screen_.fill(self.settings_.bg_color_)
        for bullet in self.bullets_.sprites():   #返回一个包含编组所有元素的列表
            bullet.draw_bullet()
        self.ship_.blitme()     #飞船的画面更新放后面，可以避免子弹出现在飞船上面
        self.aliens_.draw(self.screen_)
        #将绘制好的后台画图内容“翻”到台前
        pygame.display.flip()   

    def _update_bullets(self):
        self.bullets_.update()
        #删除消失的子弹
        for bullet in self.bullets_.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets_.remove(bullet)
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        #检测子弹与外星人是否有碰撞，有就分别删除
        collisions = pygame.sprite.groupcollide(self.bullets_, self.aliens_, True, True)
        if not self.aliens_:
            self.bullets_.empty()
            self._create_fleet()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

