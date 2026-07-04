import sys
import pygame
from drop import Drop

class SwingDrop():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        self.screen_rect = self.screen.get_rect()
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("看雨滴坠落")
        self.raindrops = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.drop_fall_step = 1.0
        self.create_drops()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            self.screen.fill(self.bg_color)
            self.update_drops()
            self.raindrops.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(30)

    def create_drops(self):
        """创建雨滴群组"""
        drop_new = Drop(self)
        current_x = drop_new.rect.x
        current_y = drop_new.rect.y   #获取第一个雨滴的坐标
        drop_width = drop_new.rect.x
        drop_height = drop_new.rect.y 

        while current_y <= (self.screen_rect.bottom - 5 * drop_height):
            while current_x <= (self.screen_rect.right - 2 * drop_width):
                new_drop = Drop(self)
                new_drop.rect.x = current_x
                new_drop.rect.y = current_y
                self.raindrops.add(new_drop)
                current_x += 2*drop_width
            current_x = drop_width
            current_y += 2*drop_height

    def create_drops_line(self):
        """仅创建一行雨滴"""
        drop_new = Drop(self)
        current_x = drop_new.rect.x
        current_y = drop_new.rect.y   #获取第一个雨滴的坐标
        drop_width = drop_new.rect.x
        drop_height = drop_new.rect.y 

        while current_x <= (self.screen_rect.right - 2 * drop_width):
            new_drop = Drop(self)
            new_drop.rect.x = current_x
            new_drop.rect.y = current_y
            self.raindrops.add(new_drop)
            current_x += 2*drop_width

    def update_drops(self):
        for drop in self.raindrops.copy():
            drop.rect.y += self.drop_fall_step
            if drop.rect.top > self.screen_rect.bottom:
                self.raindrops.remove(drop)
                self.create_drops_line()
            
if __name__ == '__main__':
    sd = SwingDrop()
    sd.run_game()