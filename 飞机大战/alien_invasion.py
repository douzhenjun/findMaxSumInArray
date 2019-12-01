#coding:utf_8
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



def run_game():
	#��ʼ����Ϸ������һ����Ļ����
	pygame.init()
	ai_settings = Settings() 
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#�����ɴ�
	ship = Ship(ai_settings, screen)
	
	#����һ�����ڴ洢�ӵ��ı���
	bullets = Group()
	
	#����һ�����ڴ洢�����˵ı���
	aliens = Group()
	
	#���ñ���ɫ
	bg_color  = (230, 230, 230)
	
	#����������Ⱥ
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#����һ�����ڴ洢��Ϸͳ����Ϣ��ʵ�����������Ƿ���
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	#����play��ť
	play_button = Button(ai_settings, screen, "play")
	
	#��ʼ��Ϸ����ѭ��
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
