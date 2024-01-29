import pygame as pg

class Space_ship:
    '''A class to story details about the spaceship'''
    def __init__(self,screen):
        self.screen = screen
        self.image = pg.image.load('images/space_ship.bmp') #get the image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #setting the ship"s centerx and bottom position equal to screen's 
        self.rect[0] = 600
        self.rect[1]  = 530
        self.size = (70,70)
        
        #movement flags
        self.rightflag = False
        self.leftflag = False
        
        #speed variable
        self.speed = 1.2
    
    def blitme(self):
        '''A function to print thw spaceship on the screen'''
        if self.rightflag:
            self.rect[0] += self.speed
        if self.leftflag:
            self.rect[0] -= self.speed
        self.image = pg.transform.scale(self.image,self.size)
        self.screen.blit(self.image,self.rect)
    
    def defaultposition(self):
        self.rect[0] = 600
        self.rect[1]  = 530        