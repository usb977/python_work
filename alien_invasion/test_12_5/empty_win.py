import sys
import pygame

class EmptyWin():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300,300))

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
            self.screen.fill((255,255,255))
            pygame.display.flip()

if __name__== '__main__':
    ew = EmptyWin()
    ew.run_game()