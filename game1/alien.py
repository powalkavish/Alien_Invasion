import pygame as pg 
import time
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class to store variables about the alien of the game'''
    def __init__(self,setting,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.setting = setting
        self.size = self.setting.aliensize  
        
        self.image = pg.image.load('images/alien1.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.size[0]
        self.rect.y = self.size[1]
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.i = 0
        
    def update(self):
        speed = self.setting.alienspeed  
        self.y += speed
        self.rect.y = self.y
        
    def blitme(self):
        '''A function to print the bullets on the screen'''
        self.image = pg.transform.scale(self.image,self.size)
        self.screen.blit (self.image,self.rect)