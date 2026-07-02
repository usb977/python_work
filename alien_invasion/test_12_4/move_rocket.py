import sys
import pygame

class RocketMove():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,1200))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("控制火箭")
        self.bg = (255,255,255)
        self.rocket = pygame.image.load('rocket.bmp')
        self.rocket_rect = self.rocket.get_rect()
        self.rocket_rect.center = self.screen_rect.center
        
        self.Flag_left = False
        self.Flag_right = False
        self.Flag_up = False
        self.Flag_down = False

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.Flag_left = True
                    elif event.key == pygame.K_RIGHT:
                        self.Flag_right = True
                    elif event.key == pygame.K_UP:
                        self.Flag_up = True
                    elif event.key == pygame.K_DOWN:
                        self.Flag_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.Flag_left = False
                    elif event.key == pygame.K_RIGHT:
                        self.Flag_right = False
                    elif event.key == pygame.K_UP:
                        self.Flag_up = False
                    elif event.key == pygame.K_DOWN:
                        self.Flag_down = False
            self.screen.fill(self.bg)
            self.__rock_move()
            self.screen.blit(self.rocket, self.rocket_rect)
            pygame.display.flip()

    def __rock_move(self):
        if self.Flag_left and (self.rocket_rect.x > 0):
            self.rocket_rect.x -= 1
        if self.Flag_right and (self.rocket_rect.right < self.screen_rect.right):
            self.rocket_rect.x += 1
        if self.Flag_down and (self.rocket_rect.bottom < self.screen_rect.bottom):
            self.rocket_rect.y += 1
        if self.Flag_up and (self.rocket_rect.y > 0):
            self.rocket_rect.y -= 1
            
if __name__ == '__main__':
    rc = RocketMove()
    rc.run_game()