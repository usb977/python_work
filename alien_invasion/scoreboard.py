import pygame.font

class ScoreBoard:
    """显示得分的类"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen_
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings_
        self.stats = ai_game.stats
        #显示得分的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font(None, 48)

        self.prep_score()

    def prep_score(self):
        """获取得分并确定显示位置"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,self.settings.bg_color_)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)