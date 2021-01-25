import pygame, math, sys
list_of_blocks = []
player1_items = []
player2_items = []

# def item_collusion():
# 	if len(pygame.sprite.spritecollide(player_1, shield, True)) > 0:
# 		player1_items.append(shield)
# 		print(player1_items)

# 	if len(pygame.sprite.spritecollide(player_2, shield, True)) > 0:
# 		player2_items.append(shield)
# 		print(player2_items)

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
	block_multiplier("block_dirt.png", 974, 675, 2, 1)  # 11
	block_multiplier("block_dirt.png", 50, 560, 2, 1)  # 12
	block_multiplier("block_dirt.png", 250, 650, 2, 1)
	block_multiplier("block_dirt.png", 0, 700, 60, 1)


def block_multiplier( image,x, y, right, down):
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
		self.velocity = 2
		self.gravity = 25
		self.healthbar=180

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
	def __init__(self, image, position, damage, loseable, uses):
		pygame.sprite.Sprite.__init__(self)
		# there is the regular bottle image
		# and the broken bottle image
		self.image = pygame.image.load(image)
		self.rect = pygame.Rect(self.image.get_rect())
		self.rect.center = position

		self.damage = damage
		self.loseable = loseable
		self.uses = uses

class Game():
	def main(self, screen):
		clock = pygame.time.Clock()
		rect = screen.get_rect()
		player_1 = Player('player1model.png', (0, 250))
		player_group = pygame.sprite.RenderPlain(player_1)

		player_2 = Player('player2model.png', (0, 250))
		player_group_2 = pygame.sprite.RenderPlain(player_2)

		#shield
		shield = Item("shield.png",(900,280),0,False, 1)
		shield_group=pygame.sprite.RenderPlain(shield)

		rubber_shield= Item("rubber_shield.png",(200,230),0,False,1)
		rubber_shield_group=pygame.sprite.RenderPlain(rubber_shield)

		#golden_sword
		golden_sword= Item("golden_sword.png",(480,460),90, False, 1)
		golden_sword_group=pygame.sprite.RenderPlain(golden_sword)

		#silver_sword
		silver_sword= Item("silver_sword.png",(925,335),40, False, math.inf)
		silver_sword_group=pygame.sprite.RenderPlain(silver_sword)



		mountain()
		block_group = pygame.sprite.RenderPlain(*list_of_blocks)

		while 1:
			deltat = clock.tick(500)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
			screen.fill((255, 255, 255))

			player_group.update(deltat/1000, len(pygame.sprite.spritecollide(player_1, block_group, False)) > 0, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT)

			player_group_2.update(deltat/1000, len(pygame.sprite.spritecollide(player_2, block_group, False)) > 0, pygame.K_w, pygame.K_d, pygame.K_a)






















			#shield
			if len(pygame.sprite.spritecollide(player_1, shield_group, True)) > 0:
				player1_items.append(shield)
				print(player1_items)

			if len(pygame.sprite.spritecollide(player_2, shield_group, True)) > 0:
				player2_items.append(shield)
				print(player2_items)

			#rubber_shield

			if len(pygame.sprite.spritecollide(player_1, rubber_shield_group, True)) > 0:
				player1_items.append(rubber_shield)
				print(player1_items)

			if len(pygame.sprite.spritecollide(player_2, rubber_shield_group, True)) > 0:
				player2_items.append(rubber_shield)
				print(player2_items)

			#golden sword

			if len(pygame.sprite.spritecollide(player_1, golden_sword_group, True)) > 0:
				player1_items.append(golden_sword)
				print(player1_items)

			if len(pygame.sprite.spritecollide(player_2, golden_sword_group, True)) > 0:
				player2_items.append(golden_sword)
				print(player2_items)

			#silver sword

			if len(pygame.sprite.spritecollide(player_1, silver_sword_group, True)) > 0:
				player1_items.append(silver_sword)
				print(player1_items)

			if len(pygame.sprite.spritecollide(player_2, silver_sword_group, True)) > 0:
				player2_items.append(silver_sword)
				print(player2_items)

			golden_sword_group.draw(screen)
			silver_sword_group.draw(screen)
			shield_group.draw(screen)
			rubber_shield_group.draw(screen)


			player_group.draw(screen)
			player_group_2.draw(screen)
			block_group.draw(screen)
			pygame.display.flip()


# pygame.init()
window_height = 760
window_width = 1024
# screen = pygame.display.set_mode((window_width, window_height))
# Game().main(screen)
