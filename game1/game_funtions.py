import sys
import time
import random
import pygame as pg 
from alien import Alien
from Bullet import Bullet

def check_keydown(event,ship,setting,screen,bullet,stats,play_button,aliens):
    if event.key == pg.K_RIGHT: #for right moment
        ship.rightflag = True    
    if event.key == pg.K_LEFT: #for left moment
        ship.leftflag = True
    if event.key == pg.K_SPACE:
        ship0 = ship.rect[0]
        ship1 = ship.rect[1]
        firebullets(ship0,ship1,setting,bullet,screen)
    if event.key ==pg.K_p:
        if not stats.gameflag:
            pg.mouse.set_visible(False)
            stats.resetstats()
            aliens.empty()
            bullet.empty()
            stats.gameflag = True
        
        createfleet(setting,screen,aliens,ship)
        ship.defaultposition()
    if event.key == pg.K_q:
        sys.exit()

def check_keyup(event,ship): 
    if event.key == pg.K_RIGHT:
        ship.rightflag = False
    if event.key == pg.K_LEFT:
        ship.leftflag = False   

def check_events(setting,screen,ship,bullet,stats,play_button,aliens):
    '''A function to check keypress'''
    if ship.rect[0] >= 1130.00:
        ship.rightflag = False
    if ship.rect[0] <= 00.00:
        ship.leftflag = False
    for event in pg.event.get():#for loop to check if a buttom is pressed 
        if event.type == pg.QUIT: #to quit
            sys.exit()
        elif event.type  == pg.KEYDOWN: 
            check_keydown(event,ship,setting,screen,bullet,stats,play_button,aliens)
        elif event.type == pg.KEYUP:
            check_keyup(event,ship)
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pg.mouse.get_pos()
            checkplaybutton(stats,play_button,mouse_x,mouse_y,aliens,bullet,ship,setting,screen)
         
def update_screen(setting,screen,stats,spaceship,bullets,alien,play_button):
    if not stats.gameflag :
        play_button.drawbutton()
    for bullet in bullets:
        bullet.drawbullet()
    for alien in alien:
        alien.blitme()
    stats.blitrounds(screen)
    stats.blitscore(screen)
    stats.blitlives(screen)
    spaceship.blitme()
    alien.blitme()
    pg.display.update()
    screen.fill(setting.screen_bg_color) #set the screen background color
    #pg.display.flip()
    
def update_bullets(aliens,bullets,stats):
    for bullet in bullets:
        if bullet.rect.y < 0:
            bullets.remove(bullet)
    checkcollision_bullet_alien(bullets,aliens,stats)
            
def update_aliens(aliens,bullets,setting,ship,screen,stats):
    aliens.update()
    if len(aliens) == 0:
        stats.rounds += 1
        stats.score += 5
        setting.levelup(ship)
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
    fleetcount = random.randint(int(setting.minfleet),int(setting.maxfleet))
    for j in  range(fleetcount):
        aliencount = random.randint(int(setting.minaliens),int(setting.maxaliens))
        for i in range(aliencount):
            newalien = Alien(setting,screen)
            newalien.rect.x = (setting.screen_length - newalien.size[0]) // 2 + 2 * alien_width * i
            newalien.rect.y = 2*alien_width*j
            aliens.add(newalien)

def checkcollision_bullet_alien(bullets,aliens,stats):
    stats.score += 0.005
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
        pg.mouse.set_visible(True)
        stats.gameflag = False
 
def check_aliensbottom(aliens,bullets,setting,ship,screen,stats):
    for alien in aliens.sprites():
        if alien.rect.y >= 530:
            shiphit(aliens,bullets,setting,ship,screen,stats)
            
def checkplaybutton(stats,play_button,mouse_x,mouse_y,aliens,bullets,ship,setting,screen):
    buttonclicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if buttonclicked and not stats.gameflag:
        pg.mouse.set_visible(False)
        stats.resetstats()
        aliens.empty()
        bullets.empty()
        stats.gameflag = True
        
        createfleet(setting,screen,aliens,ship)
        ship.defaultposition()