import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen_
        self.screen_rect = self.screen.get_rect()
        
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)   #创建一个矩形实体，就是按钮
        self.rect.center = self.screen_rect.center
        
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """将字符串渲染为图像，并让文本在按钮对象上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)  #True参数表示确认开启反锯齿
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)