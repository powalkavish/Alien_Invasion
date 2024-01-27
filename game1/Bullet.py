import pygame as pg 
from pygame.sprite import Sprite 

class Bullet(Sprite):
    '''A class to store data about the bullets'''
    def __init__(self,screen,setting,ship0,ship1):
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pg.Rect(0,0,setting.bulletwidth,setting.bulletlength)
        self.rect[0] = ship0 + 35
        self.rect[1] = 530 
        self.flag = False
        
        self.y = float(self.rect[1])
        self.color = setting.bulletcolor 
        self.speed = setting.bulletspeed
    
    def update(self):
        self.y = self.y - self.speed
        self.rect.y = self.y
        
    def drawbullet(self):
        pg.draw.rect(self.screen ,self.color , self.rect)