import pygame as pg
import game_funtions as gf
from gamestats import GameStats 
from button import Button
from setting import setting as set
from space_ship import Space_ship
from pygame.sprite import Group

def run_game():
  # Initialize pygame and create a screen object using the settings.py code .
  pg.init()
  setting = set()
  stats = GameStats(setting)
  bullets = Group()
  screen = pg.display.set_mode((setting.screen_length, setting.screen_width))
  pg.display.set_caption("Alien Invasion")
 
  spaceship = Space_ship(screen)
  
  play_button = Button(setting,screen,'Play')
 
  #alien = Alien(setting,screen)
  aliens = Group()
  gf.createfleet(setting,screen,aliens,spaceship)

  while True: 
    gf.check_events(setting,screen,spaceship,bullets,stats,play_button,aliens)
    gf.update_screen(setting,screen,stats,spaceship,bullets,aliens,play_button)
    if stats.gameflag:
     bullets.update()
     gf.update_bullets(aliens,bullets,stats) 
     gf.update_aliens(aliens,bullets,setting,spaceship,screen,stats) 
  
run_game()