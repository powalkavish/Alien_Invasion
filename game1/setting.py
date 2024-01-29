from gamestats import GameStats as gs
class setting():
    ''' A class to store all settings of the game'''
    
    def __init__(self):
        #screen settings
        self.screen_width = 600
        self.screen_length = 1200
        self.screen_bg_color = (0,0,0)
        
        #bullet settings
        self.bulletspeed = 1
        self.bulletwidth = 10
        self.bulletlength = 10
        self.bulletcolor = (87,138,215)
        self.maxbulletscount = 5
        
        #alien settings
        self.aliensize = (30,30)
        self.alienspeed = 0.5
        self.minfleet = 1
        self.maxfleet = 2
        self.minaliens = 1 
        self.maxaliens = 5             
        
        #stat settings
        self.lives = 3 
     
    def levelup(self,ship):
        ship.speed += 0.05
        self.maxbulletscount += 0.3
        self.minaliens += 0.5
        self.maxaliens += 0.7
        self.alienspeed += 0.1