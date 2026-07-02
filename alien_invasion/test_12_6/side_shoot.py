import sys
import pygame
from bullet import Bullet

class SideShoot():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        self.ship = pygame.image.load('images/ship.bmp')
        self.screen_rect = self.screen.get_rect()
        self.ship_rect = self.ship.get_rect()
        self.ship_rect.midleft = self.screen_rect.midleft
        self.flag_up = False
        self.flag_down = False
        self.bg = (230, 230, 230)
        self.clock = pygame.time.Clock()
        self.buttles = pygame.sprite.Group()

        pygame.display.set_caption("横向射击")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.flag_up = True
                    elif event.key == pygame.K_DOWN:
                        self.flag_down = True
                    elif event.key == pygame.K_SPACE:
                        new_buttle = Bullet(self)
                        self.buttles.add(new_buttle)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.flag_up = False
                    elif event.key == pygame.K_DOWN:
                        self.flag_down = False

            self.screen.fill(self.bg)

            self.buttles.update()
            for buttle in self.buttles.copy():
                if buttle.rect.x >= self.screen_rect.right:
                    self.buttles.remove(buttle)
                    
            for buttle in self.buttles.sprites():   #返回一个包含编组所有元素的列表
                buttle.draw_bullet()

            print(len(self.buttles))

            self.screen.blit(self.ship,self.ship_rect)
            self.ship_ctl()
            pygame.display.flip()
            self.clock.tick(60)
    
    def ship_ctl(self):
        if self.flag_up and self.ship_rect.y > 0:
            self.ship_rect.y -= 1
        if self.flag_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.ship_rect.y += 1

if __name__ == '__main__':
    ss = SideShoot()
    ss.run_game()        