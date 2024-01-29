import pygame as pg

class GameStats():
    
    def __init__(self,setting):
        self.setting = setting
        self.rounds = 1
        self.score = 0
        self.gameflag = False
        self.resetstats()
        
    def resetstats(self):
        self.rounds = 1
        self.score = 1
        self.livesleft = self.setting.lives
        
    def blitrounds(self,screen):
        font = pg.font.Font(None,20)
        self.rounddisplay = font.render('Round =' + str(self.rounds),True,(255,255,255),self.setting.screen_bg_color)
        screen.blit(self.rounddisplay,(1100,10))
        
    def blitscore(self,screen):
        font = pg.font.Font(None,20)
        self.scoredisplay = font.render('score = ' + str(int(self.score)),True,(255,255,255),self.setting.screen_bg_color)
        screen.blit(self.scoredisplay,(1100,25))
        
    def blitlives(self,screen):
        font = pg.font.Font(None,20)
        self.livesdisplay = font.render('lives = ' + str(int(self.livesleft)),True,(255,255,255),self.setting.screen_bg_color)
        screen.blit(self.livesdisplay,(1100,40))