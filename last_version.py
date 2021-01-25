import pygame, math, sys, time
from pygame.locals import *
import time
from turn_based import *

list_of_blocks = []
player1_items =[]
player2_items= []


def game_fight(screen):
	window_height = 660
	window_width = 1024
	screen = pygame.display.set_mode((window_width, window_height))
	player_1_inventory=player1_items
	player_2_inventory=player2_items
	clock = pygame.time.Clock()
	rect = screen.get_rect()

	while 1:
		deltat = clock.tick(500)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		screen.fill((255, 255, 255))

	

	

def mountain():
	block_multiplier("block_dirt.png", 0,100, 2, 1)  # 1
	block_multiplier("block_dirt.png", 75, 200, 2, 1)  # 2
	block_multiplier("block_dirt.png", 325, 200, 2, 1)  # 3
	block_multiplier("block_dirt.png", 575, 200, 2, 1)  # 4
	block_multiplier("block_dirt.png", 825, 200, 2, 1)  # 5
	block_multiplier("block_dirt.png", 500, 200, 2, 1)  # 6
	block_multiplier("block_dirt.png", 974, 200, 2, 1)  # 7
	block_multiplier("block_dirt.png", 150, 300, 2, 1)  # 8
	block_multiplier("block_dirt.png", 400,300 , 2, 1)  # 9
	block_multiplier("block_dirt.png", 650, 300, 2, 1)  # 10
	block_multiplier("block_dirt.png", 900, 300, 2, 1)  # 11
	block_multiplier("block_dirt.png", 925, 350, 2, 1)  # 12
	block_multiplier("block_dirt.png", 0, 370, 2, 1)
	block_multiplier("block_dirt.png", 150, 400, 2, 1)  # 4
	block_multiplier("block_dirt.png", 974, 400, 2, 1)  # 5
	block_multiplier("block_dirt.png", 480, 435, 2, 1)  # 6
	block_multiplier("block_dirt.png", 50, 480, 2, 1)  # 7
	block_multiplier("block_dirt.png", 200, 520, 2, 1)  # 8
	block_multiplier("block_dirt.png", 974,475 , 2, 1)  # 9
	block_multiplier("block_dirt.png", 974, 570, 2, 1)  # 10
	block_multiplier("block_dirt.png", 974, 625, 2, 1)  # 11
	block_multiplier("block_dirt.png", 50, 560, 2, 1)  # 12
	block_multiplier("block_dirt.png", 250, 600, 2, 1)
	block_multiplier("block_dirt.png", 0, 650, 60, 1)


def block_multiplier( image,x, y, right, down):
	x_tempor = x
	y_tempor = y
	right_temp = right
	# list_of_blocks=[]

	while down > 0:
		right = right_temp
		x_tempor = x
		while right > 0:
			list_of_blocks.append(Block(image,(x_tempor, y)))
			right += -1
			x_tempor += 25
		y += 25
		down += -1


class Block(pygame.sprite.Sprite):
	def __init__(self,image, position):
		pygame.sprite.Sprite.__init__(self)
		# there is the regular bottle image
		# and the broken bottle image
		self.image = pygame.image.load(image)
		self.rect = pygame.Rect(self.image.get_rect())
		self.rect.center = position


class Player(pygame.sprite.Sprite):
	def __init__(self, image, position):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.image = pygame.image.load(image)
		self.speed = self.direction = 0
		self.k_left = self.k_right = self.k_up = self.k_down = 0
		self.rect = pygame.rect.Rect(self.position, self.image.get_size())
		self.isjumping = True
		self.velocity = 1
		self.gravity = 15
		self.healthbar= 180

	def update(self, dt, collision, upkey, rightkey, leftkey):

		# if collision:
		# 	self.rect.x+=1
		# if collision:
		# 	self.rect.x-=2
	
		pos= self.rect.y

		key_dict = pygame.key.get_pressed()
		x_vel = -10

		if collision:
			self.rect.y = pos
		



		if key_dict[leftkey]:
			self.rect.x -= 5

		if key_dict[rightkey]:
			self.rect.x += 5

		if self.isjumping == False and not collision: 
			x_vel -= self.gravity * .05
			self.rect.y -= x_vel

		if self.velocity != 15:
			self.velocity -= self.gravity * .05
			self.rect.y -= self.velocity
			#print(self.rect.y)
			if collision:
				#print(self.rect.y)
				self.velocity = 15
				self.isjumping = False

		# Key movements for P2

		if key_dict[upkey]:
			# self.velocity = 15
			self.isjumping = True
			if self.isjumping:
				self.velocity -= self.gravity * .05
				self.rect.y -= self.velocity
			if collision:
				self.isjumping = False



		# Setting boundaries for P2
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > window_height:
			self.rect.bottom = window_height
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > window_width:
			self.rect.right = window_width

	


class Item(pygame.sprite.Sprite):
	def __init__(self, image, position, damage, loseable, uses, name):
		pygame.sprite.Sprite.__init__(self)
		# there is the regular bottle image
		# and the broken bottle image
		self.image = pygame.image.load(image)
		self.rect = pygame.Rect(self.image.get_rect())
		self.rect.center = position

		self.damage = damage
		self.loseable = loseable
		self.uses = uses
		self.name = name

	def __str__(self):
		return self.name


#DEFINING ITEMS
	#shields
shield = Item("shield.png",(900,280),-1,False, 1, 'Shield')
black_hole_shield = Item("black_hole_shield.png",(275, 280),-1,False,1,'Black Hole Shield')
rubber_shield= Item("rubber_shield.png",(175,280),-1,False,1,'Rubber Shield')
	#weapons
plastic_knife=Item('plastic_knife.png',(700,700),1,True,math.inf,'Plastic Knife')
stick=Item('stick.png',(500,500),20,True,math.inf,'Stick')
baton=Item('baton.png',(350,350),30,True,math.inf,'Baton')
baseball_bat=Item('baseball_bat.png',(1000,800),40,True,math.inf,'Baseball Bat')
spiked_club=Item('spiked_club.png',(800,800),50,True,math.inf,'Spiked Club')
trident=Item("trident.png",(600,400),60,True,math.inf,'Trident')
silver_sword= Item("silver_sword.png",(925,335),60, True, math.inf,'Silver Sword')
golden_sword= Item("golden_sword.png",(480,400),90, True, 1,'Golden Sword')
	#SPECIALS
lightning=Item('lightning.png',(50,50), 0, False, 1,'Lightning')
heart=Item('heart.png',(75,75),0,False,1,'Heart')
dice=Item('dice.png',(100,100),0,False,1,'Dice')



class Player1(pygame.sprite.Sprite):

	def __init__(self, image, position):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.image = pygame.image.load('player1model.png')
		self.speed = self.direction = 0
		self.k_left = self.k_right = self.k_up = self.k_down = 0
		self.rect = pygame.rect.Rect(self.position, self.image.get_size())
		self.isjumping = False
		self.gravity = 25
		self.velocity = 2

	def update(self, dt, collision):

		if collision:
			self.rect.y += 1
		if collision:
			self.rect.y += -2

		key_dict = pygame.key.get_pressed()

		if self.velocity != 15:
			self.velocity -= self.gravity * .05
			self.rect.y -= self.velocity
			#print(self.rect.y)
			if collision:
				#print(self.rect.y)
				self.velocity = 15
				self.isjumping = False
				return self.rect.y


		# Key movements for P1
		if key_dict[pygame.K_LEFT]:
			self.rect.x -= 10

		if key_dict[pygame.K_RIGHT]:
			self.rect.x += 10

		if key_dict[pygame.K_UP]:
			#self.velocity = 15
			self.isjumping = True
			if self.isjumping:
				self.velocity -= self.gravity * .05
				self.rect.y -= self.velocity
			if self.rect.y >= collision:
				self.isjumping = False
				return self.rect.y

		# Setting boundaries for P1
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > window_height:
			self.rect.bottom = window_height
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > window_width:
			self.rect.right = window_width







	def update(self, dt,collision):

		# if collision:
		# 	self.rect.x+=1
		# if collision:
		# 	self.rect.x-=2

		if collision:
			self.rect.y+=1
		if collision:
			self.rect.y+= -2

		key_dict = pygame.key.get_pressed()

		if self.velocity != 15:
			self.velocity -= self.gravity * .05
			self.rect.y -= self.velocity
			#print(self.rect.y)
			if self.rect.y >= 670:
				#print(self.rect.y)
				self.rect.y = 670
				self.velocity = 15
				self.isjumping = False


		# Key movements for P2
		if key_dict[pygame.K_a]:
			self.speed = 16
			# if self.rect.x > 0:
			# 	while speed > 0:
			# 		self.rect.x += int(math.sqrt(speed))
			# 		speed -= int(math.sqrt(speed))
			self.rect.x -= 16
		if key_dict[pygame.K_d]:
			self.rect.x += 16

		if key_dict[pygame.K_w]:
			# self.velocity = 15
			self.isjumping = True
			if self.isjumping:
				self.velocity -= self.gravity * .05
				self.rect.y -= self.velocity
			if self.rect.y >= 670:
				self.rect.y = 670
				self.isjumping = False

		# Setting boundaries for P2
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > window_height:
			self.rect.bottom = window_height
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > window_width:
			self.rect.right = window_width

class Game():
	def main(self, screen):
		clock = pygame.time.Clock()
		rect = screen.get_rect()
		
#PLACEMENT OF ITEMS, PLAYERS

	#PLAYERS
		player_1 = Player('player1model.png', (0, 250))
		player_group = pygame.sprite.RenderPlain(player_1)

		player_2 = Player('player2model.png', (30, 250))
		player_group_2 = pygame.sprite.RenderPlain(player_2)

	#SHIELDS

		#shield
		shield_group=pygame.sprite.RenderPlain(shield)

		#blackhole shield
		black_hole_shield_group=pygame.sprite.RenderPlain(black_hole_shield)

		#rubber shield
		rubber_shield_group=pygame.sprite.RenderPlain(rubber_shield)


	#WEAPONS

		#pknife
		plastic_knife_group=pygame.sprite.RenderPlain(plastic_knife)

		#stick
		stick_group=pygame.sprite.RenderPlain(stick)

		#baton
		baton_group=pygame.sprite.RenderPlain(baton)

		#bbat
		baseball_bat_group=pygame.sprite.RenderPlain(baseball_bat)

		#spikedclub
		spiked_club_group=pygame.sprite.RenderPlain(spiked_club)

		#trident
		trident_group=pygame.sprite.RenderPlain(trident)

		#silver_sword
		silver_sword_group=pygame.sprite.RenderPlain(silver_sword)

		#golden_sword
		golden_sword_group=pygame.sprite.RenderPlain(golden_sword)


	#SPECIALS

		#lightning
		lightning_group=pygame.sprite.RenderPlain(lightning)

		#heart
		heart_group=pygame.sprite.RenderPlain(heart)

		#dice
		dice_group=pygame.sprite.RenderPlain(dice)



	#rendering the landscape
		mountain()
		block_group = pygame.sprite.RenderPlain(*list_of_blocks)
		 #or time runs out
					
		while len(player1_items) < 5 and len(player2_items) < 5:
			deltat = clock.tick(500)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
			screen.fill((255, 255, 255))

			player_group.update(deltat/1000, len(pygame.sprite.spritecollide(player_1, block_group, False)) > 0, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT)

			player_group_2.update(deltat/1000, len(pygame.sprite.spritecollide(player_2, block_group, False)) > 0, pygame.K_w, pygame.K_d, pygame.K_a)


	#ITEM PICKUP

		#SHIELDS

			#shield
			if len(pygame.sprite.spritecollide(player_1, shield_group, True)) > 0:
				player1_items.append(shield)
			if len(pygame.sprite.spritecollide(player_2, shield_group, True)) > 0:
				player2_items.append(shield)
		
			#rubshield
			if len(pygame.sprite.spritecollide(player_1, rubber_shield_group, True)) > 0:
				player1_items.append(rubber_shield)
			if len(pygame.sprite.spritecollide(player_2, rubber_shield_group, True)) > 0:
				player2_items.append(rubber_shield)
			
				#blackholeshield
			if len(pygame.sprite.spritecollide(player_1, black_hole_shield_group, True)) > 0:
				player1_items.append(rubber_shield)
			if len(pygame.sprite.spritecollide(player_2, black_hole_shield_group, True)) > 0:
				player2_items.append(rubber_shield)



		#WEAPONS

				#plasticknife
			if len(pygame.sprite.spritecollide(player_1, plastic_knife_group, True)) > 0:
				player1_items.append(plastic_knife)
			if len(pygame.sprite.spritecollide(player_2, plastic_knife_group, True)) > 0:
				player2_items.append(plastic_knife)

				#stick
			if len(pygame.sprite.spritecollide(player_1, stick_group, True)) > 0:
				player1_items.append(stick)
			if len(pygame.sprite.spritecollide(player_2, stick_group, True)) > 0:
				player2_items.append(stick)
				

				#baton
			if len(pygame.sprite.spritecollide(player_1, baton_group, True)) > 0:
				player1_items.append(baton)
			if len(pygame.sprite.spritecollide(player_2, baton_group, True)) > 0:
				player2_items.append(baton)

				#baseballbat
			if len(pygame.sprite.spritecollide(player_1, baseball_bat_group, True)) > 0:
				player1_items.append(baseball_bat)
			if len(pygame.sprite.spritecollide(player_2, baseball_bat_group, True)) > 0:
				player2_items.append(baseball_bat)

				#spikedclub
			if len(pygame.sprite.spritecollide(player_1, spiked_club_group, True)) > 0:
				player1_items.append(spiked_club)
			if len(pygame.sprite.spritecollide(player_2, spiked_club_group, True)) > 0:
				player2_items.append(spiked_club)

				#trident
			if len(pygame.sprite.spritecollide(player_1, trident_group, True)) > 0:
				player1_items.append(trident)
			if len(pygame.sprite.spritecollide(player_2, trident_group, True)) > 0:
				player2_items.append(trident)

				#ssword
			if len(pygame.sprite.spritecollide(player_1, silver_sword_group, True)) > 0:
				player1_items.append(silver_sword)
				print(player1_items)
			if len(pygame.sprite.spritecollide(player_2, silver_sword_group, True)) > 0:
				player2_items.append(silver_sword)
				
				#gsword
			if len(pygame.sprite.spritecollide(player_1, golden_sword_group, True)) > 0:
				player1_items.append(golden_sword)
			if len(pygame.sprite.spritecollide(player_2, golden_sword_group, True)) > 0:
				player2_items.append(golden_sword)
	

		#SPECIALS

			#lightning
			if len(pygame.sprite.spritecollide(player_1, lightning_group, True)) > 0:
				player1_items.append(lightning)
			if len(pygame.sprite.spritecollide(player_2, lightning_group, True)) > 0:
				player2_items.append(lightning)

			#heart
			if len(pygame.sprite.spritecollide(player_1, heart_group, True)) > 0:
				player1_items.append(heart)
			if len(pygame.sprite.spritecollide(player_2, heart_group, True)) > 0:
				player2_items.append(heart)


			#dice
			if len(pygame.sprite.spritecollide(player_1, dice_group, True)) > 0:
				player1_items.append(dice)
			if len(pygame.sprite.spritecollide(player_2, dice_group, True)) > 0:
				player2_items.append(dice)

				

		#RENDERING ON SCREEN
			
			#shields
			shield_group.draw(screen)
			black_hole_shield_group.draw(screen)
			rubber_shield_group.draw(screen)
			
			#weapons
			plastic_knife_group.draw(screen)
			stick_group.draw(screen)
			baton_group.draw(screen)
			baseball_bat_group.draw(screen)
			spiked_club_group.draw(screen)
			trident_group.draw(screen)
			silver_sword_group.draw(screen)
			golden_sword_group.draw(screen)

			#specials
			lightning_group.draw(screen)
			heart_group.draw(screen)
			dice_group.draw(screen)

			#players, blocks
			player_group.draw(screen)
			player_group_2.draw(screen)
			block_group.draw(screen)
			pygame.display.flip()

	
	
		baba= Fight(screen, player1_items, player2_items)
		


pygame.init()
window_height = 660
window_width = 1024
screen = pygame.display.set_mode((window_width, window_height))
Game().main(screen)
