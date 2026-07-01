import sys
import pygame

class BlueSky():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,400))
        pygame.display.set_caption("蓝色天空")  
        self.bg = (0,0,255)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg)
            pygame.display.flip()   
            
if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()