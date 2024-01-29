import pygame as pg 
class Button():
    
    def __init__(self,setting,screen,msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.setting = setting
        
        
        self.width , self.height = 200,50
        self.buttoncolor = (0,255,0)
        self.textcolor = (255,255,255)
        self.font = pg.font.SysFont(None,48)
        
        self.rect = pg.Rect(0,0,self.width,self.height)
        self.rect.center =  (600,300)
        
        self.prep_msg(msg)
        
    def prep_msg(self,msg):
        self.msg_image = self.font.render (msg,True,self.textcolor,self.buttoncolor)
        self.msg_imagerect = self.msg_image.get_rect()
        self.msg_imagerect.center = self.rect.center
        
    def drawbutton(self):
        self.screen.fill(self.buttoncolor,self.rect)
        self.screen.blit(self.msg_image,self.msg_imagerect)