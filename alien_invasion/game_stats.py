class GameStats:
    """跟踪游戏的统计信息"""
    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings_
        self.score = 0
        self.reset_stats()
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit  #剩下的飞船数量，一般属性都放在__init__()方法里面