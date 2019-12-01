#coding:utf_8
class Settings():
#�洢�����������֡����������õ���

	def __init__(self):
		#��ʼ����Ϸ������
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		
		#�ɴ�������
		self.ship_speed_factor = 5
		self.ship_limit = 5
		
		#�ӵ�����
		self.bullet_speed_factor = 3
		self.bullet_width = 50
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 10
		
		#����������
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		#self.fleet_directionΪ1��ʾ���ң�Ϊ-1��ʾ����
		self.fleet_direction = 1
		self.alien_points = 50
		
		#speed up the game
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		'''when restart the game, initialize the speed of above objects'''
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		#fleet_direction be 1 means rightward,-1 means leftward
		self.fleet_direction = 1
			
			
	def increase_speed(self):
		'''this function aims to increase speed by multiple the speedup_scale'''
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
			
			
			
			
			
		
		
		
		
		
		
		
		
		
