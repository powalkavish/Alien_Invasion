import sys
import time
import random
import pygame as pg 
from alien import Alien
from Bullet import Bullet

def check_keydown(event,ship,setting,screen,bullet):
    if event.key == pg.K_RIGHT: #for right moment
        ship.rightflag = True    
    if event.key == pg.K_LEFT: #for left moment
        ship.leftflag = True
    if event.key == pg.K_SPACE:
        ship0 = ship.rect[0]
        ship1 = ship.rect[1]
        firebullets(ship0,ship1,setting,bullet,screen)
    if event.key == pg.K_q:
        sys.exit()

def check_keyup(event,ship): 
    if event.key == pg.K_RIGHT:
        ship.rightflag = False
    if event.key == pg.K_LEFT:
        ship.leftflag = False   

def check_events(setting,screen,ship,bullet):
    '''A function to check keypress'''
    if ship.rect[0] >= 1130.00:
        ship.rightflag = False
    if ship.rect[0] <= 00.00:
        ship.leftflag = False
    for event in pg.event.get():#for loop to check if a buttom is pressed 
        if event.type == pg.QUIT: #to quit
            sys.exit()
        elif event.type  == pg.KEYDOWN: 
            check_keydown(event,ship,setting,screen,bullet)
        elif event.type == pg.KEYUP:
            check_keyup(event,ship)
         
def update_screen(setting,screen,spaceship,bullets,alien):
    for bullet in bullets:
        bullet.drawbullet()
    for alien in alien:
        alien.blitme()
    spaceship.blitme()
    alien.blitme()
    pg.display.update()
    screen.fill(setting.screen_bg_color) #set the screen background color
    pg.display.flip()
    
def update_bullets(aliens,bullets):
    for bullet in bullets:
        if bullet.rect.y < 0:
            bullets.remove(bullet)
    checkcollision_bullet_alien(bullets,aliens)
            
def update_aliens(aliens,bullets,setting,ship,screen,stats):
    aliens.update()
    if len(aliens) == 0:
        time.sleep(1)
        bullets.empty()
        createfleet(setting,screen,aliens,ship)
    if pg.sprite.spritecollideany(ship,aliens):
        shiphit(aliens,bullets,setting,ship,screen,stats)
    check_aliensbottom(aliens,bullets,setting,ship,screen,stats)

def firebullets(ship0,ship1,setting,bullet,screen):
    '''A function to fire bullets'''
    if setting.maxbulletscount > len(bullet):
        newbullet = Bullet(screen,setting,ship0,ship1)
        bullet.add(newbullet) 
 
def createfleet(setting,screen,aliens,ship):
    '''create a fleet of aliens'''
    alien = Alien(setting,screen)
    alien_width = alien.size[0]
    fleetcount = random.randint(setting.minfleet,setting.maxfleet)

    for j in range(fleetcount):
        aliencount = random.randint(setting.minaliens,setting.maxaliens)
        for i in range(aliencount):
            newalien = Alien(setting,screen)
            newalien.rect.x = (setting.screen_length - newalien.size[0]) // 2 + 2 * alien_width * i
            newalien.rect.y = 2*alien_width*j
            aliens.add(newalien)

def checkcollision_bullet_alien(bullets,aliens):
    collisions = pg.sprite.groupcollide(bullets, aliens, True, True)

def shiphit(aliens,bullets,setting,ship,screen,stats):
    stats.livesleft -= 1
    if stats.livesleft > 0:
        time.sleep(0.5)
        bullets.empty()
        aliens.empty()
        createfleet(setting,screen,aliens,ship)
        ship.defaultposition()
    else:
        stats.gameflag = False
 
def check_aliensbottom(aliens,bullets,setting,ship,screen,stats):
    for alien in aliens.sprites():
        if alien.rect.y >= 530:
            shiphit(aliens,bullets,setting,ship,screen,stats)