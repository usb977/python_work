from pathlib import Path

class GameStats:
    """跟踪游戏的统计信息"""
    def __init__(self, ai_game):
        """初始化统计信息"""
        self.ai_game = ai_game
        self.settings = ai_game.settings_
        self.score = 0
        self.level = 1
        self.reset_stats()
        self.check_high_score()
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit  #剩下的飞船数量，一般属性都放在__init__()方法里面
        self.score = 0
        self.level = 1

    def check_high_score(self):
        if self.ai_game.path:
            content = self.ai_game.path.read_text()
            self.high_score = int(content) if content.strip() else 0
        else:
            self.high_score = 0