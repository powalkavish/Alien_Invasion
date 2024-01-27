class GameStats():
    
    def __init__(self,setting):
        self.setting = setting
        self.gameflag = True
        self.resetstats()
        
    def resetstats(self):
        self.livesleft = self.setting.lives