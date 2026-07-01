import sys
import pygame

class Tifa():
    def __init__(self):
        pygame.init()
        self.screen_ = pygame.display.set_mode((1000,1000))
        self.bg_color_ = (0, 0, 0)
        self.tifa_ = pygame.image.load('tifa.bmp')
        self.screen_rect_ = self.screen_.get_rect()
        self.tifa_rect_ = self.tifa_.get_rect()
        self.tifa_rect_.center = self.screen_rect_.center
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen_.fill(self.bg_color_)
            self.screen_.blit(self.tifa_, self.tifa_rect_)
            pygame.display.flip()

if __name__=='__main__':
    tf = Tifa()
    tf.run_game()