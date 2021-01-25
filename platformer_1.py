import pygame, math, sys
from pygame.locals import *


#def is_there_collusion(player_1, dirt):
#	return pygame.sprite.spritecollide(player_1, dirt, False)
#def item_rendering():

#	knife = Knife('knife.jpg', (750,345))


#	knife_group = pygame.sprite.RenderPlain(knife)



#class Knife():
#	def __init__(self, position):
#		pygame.sprite.Sprite.__init__(self)
		#there is the regular bottle image
		#and the broken bottle image
#		self.image = pygame.image.load('knife.jpg')
		
#		self.rect = pygame.Rect(self.image.get_rect())
#		self.rect.center = position

def mountain():



	block_multiplier(dirt,0,60, 9, 1)#1
	block_multiplier(dirt,330,60, 1, 2)#2
	block_multiplier(dirt,500,40, 1, 1)#3
	block_multiplier(stone,800,685, 2, 1)#4
	block_multiplier(stone,1000,40, 1, 1)#5
	block_multiplier(stone,500,320, 15, 1)#6
	block_multiplier(stone,700,350, 8, 1)#7
	block_multiplier(stone,800,650, 1, 4)#8
	block_multiplier(fire,865,670, 1, 1)#9
	block_multiplier(fire,700,400, 1, 6)#10
	block_multiplier(fire,0,350, 10, 1)#11
	block_multiplier(fire,400,500, 1, 5)#12
	
list_of_blocks=[]

def block_multiplier(classname,x,y, right, down):

	x_tempor= x
	y_tempor= y
	right_temp= right
	# list_of_blocks=[]

	while down>0:

		right= right_temp
		x_tempor=x

	
		while right > 0 :

			list_of_blocks.append(classname((x_tempor,y)))
			
			right+= -1
			x_tempor+= 25


		y+= 25
		down+= -1

	# block_group=pygame.sprite.RenderPlain(*list_of_blocks)

	# block_group.draw(screen)

class fire(pygame.sprite.Sprite):
	def __init__(self, position):
		pygame.sprite.Sprite.__init__(self)
		#there is the regular bottle image
		#and the broken bottle image
		self.image = pygame.image.load('block_fire.png')
		
		self.rect = pygame.Rect(self.image.get_rect())
		self.rect.center = position

class dirt(pygame.sprite.Sprite):
	def __init__(self, position):
		pygame.sprite.Sprite.__init__(self)
		#there is the regular bottle image
		#and the broken bottle image
		self.image = pygame.image.load('block_dirt.png')
		
		self.rect = pygame.Rect(self.image.get_rect())
		self.rect.center = position

class stone(pygame.sprite.Sprite):
	def __init__(self, position):
		pygame.sprite.Sprite.__init__(self)
		#there is the regular bottle image
		#and the broken bottle image
		self.image = pygame.image.load('block_stone.png')
		
		self.rect = pygame.Rect(self.image.get_rect())
		self.rect.center = position

class wood(pygame.sprite.Sprite):
	def __init__(self, position):
		pygame.sprite.Sprite.__init__(self)
		#there is the regular bottle image
		#and the broken bottle image
		self.image = pygame.image.load('block_wood.png')
		
		self.rect = pygame.Rect(self.image.get_rect())
		self.rect.center = position

class snow(pygame.sprite.Sprite):
	def __init__(self, position):
		pygame.sprite.Sprite.__init__(self)
		#there is the regular bottle image
		#and the broken bottle image
		self.image = pygame.image.load('block_snow.png')
		
		self.rect = pygame.Rect(self.image.get_rect())
		self.rect.center = position


class Player1(pygame.sprite.Sprite):

	def __init__(self, image, position):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.image = pygame.image.load('player1model.png')
		self.speed = self.direction = 0
		self.k_left = self.k_right = self.k_up = self.k_down = 0
	#	self.new_size = pygame.transform.scale(self.image, (10, 10))
		self.rect = pygame.rect.Rect(self.position, self.image.get_size())


	def update(self, dt, collision):

		
		# if collision:
		# 	self.rect.x+=1
		# if collision:
		# 	self.rect.x-=2
		if collision:
			self.rect.y+=1
		if collision:
			self.rect.y+= -2


		else : 
			key_dict = pygame.key.get_pressed()
			if key_dict[pygame.K_LEFT]:
				self.rect.x -= 5
			if key_dict[pygame.K_RIGHT]:
				self.rect.x += 5
			if key_dict[pygame.K_UP]:
				self.rect.y -= 5
			if key_dict[pygame.K_DOWN]:
				self.rect.y += 5

			

class Player2(pygame.sprite.Sprite):

	def __init__(self, image, position):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.image = pygame.image.load('player2model.png')
		self.speed = self.direction = 0
		self.k_left = self.k_right = self.k_up = self.k_down = 0
		self.rect = pygame.rect.Rect(self.position, self.image.get_size())

	


	def update(self, dt,collision):

		# if collision:
		# 	self.rect.x+=1
		# if collision:
		# 	self.rect.x-=2
		if collision:
			self.rect.y+=1
		if collision:
			self.rect.y+= -2
		
			
		#	key_dict = pygame.key.get_pressed()
		#	if key_dict[pygame.K_RIGHT]:
		#		self.rect.x -= 10
		#	if key_dict[pygame.K_LEFT]:
		#		self.rect.x += 10
		#	if key_dict[pygame.K_DOWN]:
		#		self.rect.y -= 10
		#	if key_dict[pygame.K_UP]:
		#		self.rect.y += 10

		else:
			key_dict = pygame.key.get_pressed()
			if key_dict[pygame.K_a]:
				self.rect.x-= 5
			if key_dict[pygame.K_d]:
				self.rect.x+=5
			if key_dict[pygame.K_w]:
				self.rect.y-= 5
			if key_dict[pygame.K_s]:
				self.rect.y+= 5

class Game():
	def main(self, screen):

		clock = pygame.time.Clock()	
		
		rect = screen.get_rect()

		player_1 = Player1('player1model.png', (0,250))

		player_group = pygame.sprite.RenderPlain(player_1)


		player_2 = Player2('player2model.png', (0,250))

		player_group_2 = pygame.sprite.RenderPlain(player_2)

		mountain()
		block_group = pygame.sprite.RenderPlain(*list_of_blocks)
		

		#knife = Knife((710,390))

		#knife_group = pygame.sprite.RenderPlain(knife)



		while 1:
			deltat = clock.tick(500)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			screen.fill((255, 255, 255))


			player_group.update(deltat / 1000, len(pygame.sprite.spritecollide(player_1, block_group, False))>0)

			player_group_2.update(deltat / 1000, len(pygame.sprite.spritecollide(player_2, block_group, False))>0)


			#knife_group.draw(screen)
			player_group.draw(screen)
			player_group_2.draw(screen)
			block_group.draw(screen)
			pygame.display.flip()

		



pygame.init()
screen = pygame.display.set_mode((1024, 760))
Game().main(screen)
