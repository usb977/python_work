import sys
import pygame
from star import Star
from random import randint

class StarView():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("看星星")
        self.stars = pygame.sprite.Group()  #用来放星星的群组
        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0,0,0))
            self.update_star()
            self.stars.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(1)
            self.stars.empty()
    
    def update_star(self):
        new_star = Star(self)
        width = new_star.rect.x
        height = new_star.rect.y
        star_center_x = 2*width
        current_y = height    #为了赋值

        while current_y < (self.screen_rect.bottom - 2*height ):
            while star_center_x < (self.screen_rect.right - 3*width):
                new_star = Star(self)
                random_number = randint(-10,10)
                new_star.x = star_center_x + (width * random_number) / 10.0
                new_star.rect.x = new_star.x
                new_star.rect.y = current_y
                self.stars.add(new_star)
                star_center_x += 3*width
            star_center_x = 2*width
            current_y += 2*height

if __name__ == '__main__':
    sv = StarView()
    sv.run_game()