from pygame import *

def gravity(obj, is_jumping, collision, x_vel, gravity):
	if not is_jumping and not collision:
		x_vel -= gravity * .05
		obj.rect.y -= x_vel


class Player(pygame.sprite.Sprite):
	def __init__(self, image, position):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.image = pygame.image.load(image)
		self.speed = self.direction = 0
		self.k_left = self.k_right = self.k_up = self.k_down = 0
		self.rect = pygame.rect.Rect(self.position, self.image.get_size())
		self.isjumping = False
		self.velocity = 15
		self.gravity = 30
		self.healthbar = 180
		self.injump = False

    def collision_check(self, collision, x_vel, is_jumping, gravity):
        # blocks_collided = pygame.sprite.spritecollide(collider, collided_list, False)
        # is_below = False
        # is_above = False
        # is_left = False
        # is_right = False
        for n in range(len(list_of_blocks)):
            # Left collision
            if self.rect.x + 30 == list_of_blocks[n].rect.x:  # or self.rect.y == (wood.rect.y + n):
                self.rect.x = list_of_blocks[n].rect.x - 1

            # Bottom Collision
            elif self.rect.y == list_of_blocks[n].rect.y + 25:
                self.rect.y = list_of_blocks[n].rect.y + 26

            # Right collision
            elif self.rect.x == list_of_blocks[n].rect.x + 25:
                self.rect.x = list_of_blocks[n].rect.x + 26

            # Top collision
            elif self.rect.y + 50 == list_of_blocks[n].rect.y:
                self.rect.y = list_of_blocks[n].rect.y - 1

	def update(self, collision, upkey, rightkey, leftkey):

		key_dict = pygame.key.get_pressed()
		x_vel = -10

		# if collision:
			# pos = self.rect.y
			# self.rect.y = pos

		# gravity(self, collision, x_vel)

		if key_dict[leftkey]:
			for n in range(16):
				self.rect.x -= 1
				collision_check(self.rect, collision, x_vel, self.isjumping, self.gravity)
			# collision_check(self.rect, )
			# gravity(self, collision, x_vel)

		if key_dict[rightkey]:
			for n in range(16):
				self.rect.x += 1
				collision_check(self.rect, collision, x_vel, self.isjumping, self.gravity)
			# gravity(self, collision, x_vel)

		if self.velocity != 15:
			self.injump = True
			if self.injump:
				self.velocity -= self.gravity * .05
				self.rect.y -= self.velocity
			if collision:
				self.velocity = 15
				self.isjumping = False
				self.injump = False

		if key_dict[upkey]:
			self.isjumping = True
			if self.isjumping and not self.injump:
				self.velocity -= self.gravity * .05
				self.rect.y -= self.velocity
			if collision:
				self.isjumping = False

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