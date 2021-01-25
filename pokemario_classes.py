import pygame, math, sys
from pygame.locals import *
import time
list_of_blocks = []
player1_items = []
player2_items = []


def gravity(obj, collision, x_vel):
	if not obj.isjumping and not collision:
		x_vel -= obj.gravity * .1
		obj.rect.y -= x_vel
		return obj.rect.y

"""
def collision_check(collider, collision, x_vel, is_jumping, gravity):
	# blocks_collided = pygame.sprite.spritecollide(collider, collided_list, False)
	is_below = False
	is_above = False
	is_left = False
	is_right = False
	for n in range(len(list_of_blocks)):
		# Left collision
		if collider.x + 30 == list_of_blocks[n].rect.x:  # or self.rect.y == (wood.rect.y + n):
			collider.x = list_of_blocks[n].rect.x - 1

		# Bottom Collision
		if collider.y == list_of_blocks[n].rect.y + 25:
			collider.y = list_of_blocks[n].rect.y + 26

		# Right collision
		if collider.x == list_of_blocks[n].rect.x + 25:
			collider.x = list_of_blocks[n].rect.x + 26

		# Top collision
		if collider.y + 50 == list_of_blocks[n].rect.y:
			collider.y = list_of_blocks[n].rect.y + 1
"""


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


def block_multiplier(image, x, y, right, down):
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


def collision_check(collider, block_group):
	blocks_collided = pygame.sprite.spritecollide(collider, block_group, False)
	is_above = False
	is_below = False
	is_left = False
	is_right = False
	if len(blocks_collided) >= 1:
		# Top collision
		#if collider.rect.y + 50 > blocks_collided[0].rect.y:
		#	collider.rect.y = blocks_collided[0].rect.y - 1

		# Left collision
		if collider.rect.x + 31 > blocks_collided[0].rect.x:
			collider.rect.x = blocks_collided[0].rect.x - 1

		# Bottom Collision
		#if collider.rect.y < blocks_collided[0].rect.y + 25:
		#	collider.rect.y = blocks_collided[0].rect.y + 26

		# Right collision
		#if collider.rect.x < blocks_collided[0].rect.x + 25:
		#	collider.rect.x = blocks_collided[0].rect.x + 26


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
		self.isjumping = False
		self.gravity = 30
		self.healthbar = 180
		self.injump = False
		self.x_Vel = 0
		self.y_Vel = 15

	def collide(self, x_vel, y_vel, blocks, collision):
		for n in blocks:
			if collision:
				if x_vel > 0:
					self.rect.right = n.rect.left
				if x_vel < 0:
					self.rect.left = n.rect.right
				if y_vel > 0:
					self.rect.bottom = n.rect.top
				if y_vel < 0:
					self.rect.top = n.rect.bottom



	def update(self, collision, upkey, rightkey, leftkey, block_group):
		x_vel = -10
		key_dict = pygame.key.get_pressed()
		gravity(self, collision, x_vel)

		"""
		if collision:
			is_above = False
			self.rect.y -= 1
		else:
			is_above = True
		"""

		if key_dict[leftkey]:
			self.x_Vel -= 16
			if self.rect.left < 0:
				self.x_Vel = 0
			self.collide(self.x_Vel, self.y_Vel, block_group, collision)

		if key_dict[rightkey]:
			self.x_Vel += 16
			if self.rect.right > window_width:
				self.x_Vel = 0
			self.collide(self.x_Vel, self.y_Vel, block_group, collision)

		self.rect.left += self.x_Vel

		if not key_dict[leftkey] and key_dict[rightkey]:
			self.x_Vel = 0

		if key_dict[upkey]:
			self.isjumping = True
			if self.isjumping and not self.injump:
				self.y_Vel -= self.gravity * .05
				self.rect.y -= self.y_Vel
				self.collide(self.x_Vel, self.y_Vel, block_group, collision)
			if collision:
				self.isjumping = False

		if self.y_Vel != 15:
			self.injump = True
			if self.injump:
				self.y_Vel -= self.gravity * .1
				self.rect.y -= self.y_Vel
			if collision:
				self.velocity = 15
				self.isjumping = False
				self.injump = False

		# Setting boundaries for Players
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > window_height:
			self.rect.bottom = window_height
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > window_width:
			self.rect.right = window_width

	def get_rect(self):
		return self.rect


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


class Game:
	def main(self, screen):
		clock = pygame.time.Clock()
		rect = screen.get_rect()
		player_1 = Player('player1model.png', (0, 250))
		player_group = pygame.sprite.RenderPlain(player_1)

		player_2 = Player('player2model.png', (0, 250))
		player_group_2 = pygame.sprite.RenderPlain(player_2)

		# shield
		shield = Item("shield.png",(900,280),0,False, 1)
		shield_group = pygame.sprite.RenderPlain(shield)

		rubber_shield = Item("rubber_shield.png",(200,230),0,False,1)
		rubber_shield_group = pygame.sprite.RenderPlain(rubber_shield)

		# golden_sword
		golden_sword = Item("golden_sword.png",(480,460),90, False, 1)
		golden_sword_group = pygame.sprite.RenderPlain(golden_sword)

		# silver_sword
		silver_sword = Item("silver_sword.png",(925,335),40, False, math.inf)
		silver_sword_group = pygame.sprite.RenderPlain(silver_sword)

		mountain()
		block_group = pygame.sprite.RenderPlain(*list_of_blocks)

		while 1:
			deltat = clock.tick(500)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
			screen.fill((255, 255, 255))

			player_group.update(len(pygame.sprite.spritecollide(player_1, block_group, False)) > 0,
								pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT, block_group)

			player_group_2.update(len(pygame.sprite.spritecollide(player_2, block_group, False)) > 0,
								pygame.K_w, pygame.K_d, pygame.K_a, block_group)

			# shield
			if len(pygame.sprite.spritecollide(player_1, shield_group, True)) > 0:
				player1_items.append(shield)
				print(player1_items)
			if len(pygame.sprite.spritecollide(player_2, shield_group, True)) > 0:
				player2_items.append(shield)
				print(player2_items)

			# rubber_shield

			if len(pygame.sprite.spritecollide(player_1, rubber_shield_group, True)) > 0:
				player1_items.append(rubber_shield)
				print(player1_items)
			if len(pygame.sprite.spritecollide(player_2, rubber_shield_group, True)) > 0:
				player2_items.append(rubber_shield)
				print(player2_items)

			# golden sword

			if len(pygame.sprite.spritecollide(player_1, golden_sword_group, True)) > 0:
				player1_items.append(golden_sword)
				print(player1_items)
			if len(pygame.sprite.spritecollide(player_2, golden_sword_group, True)) > 0:
				player2_items.append(golden_sword)
				print(player2_items)

			# silver sword

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


pygame.init()
window_height = 760
window_width = 1024
screen = pygame.display.set_mode((window_width, window_height))
Game().main(screen)
