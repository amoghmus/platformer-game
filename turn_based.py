import pygame, math, sys
from pygame.locals import *
import time
import random
from richard import *


class Fight():
	def __init__(self, screen, player_1_inventory, player_2_inventory):
		GameStage= 0
		GameStage2=0
		stuff_to_print=[]
		stuff_to_print2=[]
		item_temp=[]
		item_temp2=[]
		clock = pygame.time.Clock()
		rect = screen.get_rect()

		player_1 = Player('player1model.png', (0, 250))
		

		player_2 = Player('player2model.png', (1000, 250))


		#DEFINING ITEMS
			#shields
			# shield = Item("shield.png",(900,280),-1,False, 1, 'Shield')
			# black_hole_shield = Item("black_hole_shield.png",(275, 280),-1,False,math.inf,'Black Hole Shield')
			# rubber_shield= Item("rubber_shield.png",(175,280),-1,False,math.inf,'Rubber Shield')
			# 	#weapons
			# plastic_knife=Item('plastic_knife.png',(175,50),1,True,math.inf,'Plastic Knife')
			# stick=Item('stick.png',(200,50),20,True,math.inf,'Stick')
			# baton=Item('baton.png',(225,50),30,True,math.inf,'Baton')
			# baseball_bat=Item('baseball_bat.png',(250,50),40,True,math.inf,'Baseball Bat')
			# spiked_club=Item('spiked_club.png',(150,50),50,True,math.inf,'Spiked Club')
			# trident=Item("trident.png",(125,50),60,True,math.inf,'Trident')
			# silver_sword= Item("silver_sword.png",(925,335),60, True, math.inf,'Silver Sword')
			# golden_sword= Item("golden_sword.png",(480,400),90, True, math.inf,'Golden Sword')
			# 	#SPECIALS
			# lightning=Item('lightning.png',(50,50), 0, False, math.inf,'Lightning')
			# heart=Item('heart.png',(75,50),0,False,math.inf,'Heart')
			# dice=Item('dice.png',(100,50),0,False,math.inf,'Dice')

		
		lightning_counter_1 = False
		lightning_counter_2 = False
		while player_1.healthbar>0 and player_2.healthbar>0:


			deltat = clock.tick(500)
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()


			if len(item_temp)==0 or len(item_temp2)==0:

				x=120
				y=80		
				for i in range(len(player_1_inventory)):
					item_to_print=player_1_inventory[i]
					item_to_print.rect= pygame.Rect(item_to_print.image.get_rect())
					item_to_print.rect.center = (x,y)
					stuff_to_print.append(item_to_print)
					y+=100
					

				a=900
				b=80
				for i in range(len(player_2_inventory)):
					item_to_print2= player_2_inventory[i]
					item_to_print2.rect= pygame.Rect(item_to_print.image.get_rect())
					item_to_print2.rect.center = (a,b)
					stuff_to_print2.append(item_to_print2)
					b+=100
				

				
				key_dict = pygame.key.get_pressed()
				if key_dict[K_z]:
					if GameStage==0:
						item_add= player_1_inventory[0]
						item_temp.append(item_add)
						GameStage += 1
				if key_dict[K_x]:
					if GameStage==0:
						item_add= player_1_inventory[1]
						item_temp.append(item_add)
						GameStage += 1
				if key_dict[K_c]:
					if GameStage==0:
						item_add= player_1_inventory[2]
						item_temp.append(item_add)
						GameStage += 1
				if key_dict[K_v]:
					if GameStage==0:
						item_add= player_1_inventory[3]
						item_temp.append(item_add)
						GameStage += 1
				if key_dict[K_b]:
					if GameStage==0:
						item_add= player_1_inventory[4]
						item_temp.append(item_add)
						GameStage += 1
				if key_dict[K_n]:
					if GameStage==0:
						item_add= player_1_inventory[5]
						item_temp.append(item_add)
						GameStage += 1


				key_dict = pygame.key.get_pressed()
				if key_dict[K_1]:
					if GameStage2==0:
						item_add_2= player_2_inventory[0]
						item_temp2.append(item_add_2)
						GameStage2+= 1
				if key_dict[K_2]:
					if GameStage2==0:
						item_add_2= player_2_inventory[1]
						item_temp2.append(item_add_2)
						GameStage2 += 1
				if key_dict[K_3]:
					if GameStage2==0:
						item_add_2= player_2_inventory[2]
						item_temp2.append(item_add_2)
						GameStage2 += 1
				if key_dict[K_4]:
					if GameStage2==0:
						item_add_2= player_2_inventory[3]
						item_temp2.append(item_add_2)
						GameStage2 += 1
				if key_dict[K_5]:
					if GameStage2==0:
						item_add_2= player_2_inventory[4]
						item_temp2.append(item_add_2)
						GameStage2 += 1
				if key_dict[K_6]:
					if GameStage2==0:
						item_add_2= player_2_inventory[5]
						item_temp2.append(item_add_2)
						GameStage2 += 1


				print("stuff: " + str(stuff_to_print) + "\n")

				font = pygame.font.Font('freesansbold.ttf', 30) 
				screen.fill((255,255,255))
				health_text = font.render('Player 1: Health    ' + str(player_1.healthbar), True, (0, 0, 0), (255, 255, 255))
				textRect = health_text.get_rect()
				textRect.center = (500, 100) 
				screen.blit(health_text, textRect) 
				

				health_text2 = font.render('Player 2: Health    ' + str(player_2.healthbar), True, (0, 0, 0), (255, 255, 255))
				textRect2 = health_text.get_rect()
				textRect2.center = (500, 600) 
				screen.blit(health_text2, textRect2) 
				

				baba_1 = font.render(' :1', True, (0, 0, 0), (255, 255, 255))
				babaRect = baba_1.get_rect()
				babaRect.center = (140, 80)  
				screen.blit(baba_1,babaRect)
				

				baba_2 = font.render(' :2' , True, (0, 0, 0), (255, 255, 255))
				babaRect2 = baba_2.get_rect()
				babaRect2.center = (140, 180)  
				screen.blit(baba_2,babaRect2)


				baba_3 = font.render(' :3' , True, (0, 0, 0), (255, 255, 255))
				babaRect3 = baba_3.get_rect()
				babaRect3.center = (140, 280)  
				screen.blit(baba_3,babaRect3)


				baba_4 = font.render(' :4' , True, (0, 0, 0), (255, 255, 255))
				babaRect4 = baba_4.get_rect()
				babaRect4.center = (140, 380)  
				screen.blit(baba_4,babaRect4)


				baba_5 = font.render(' :5' , True, (0, 0, 0), (255, 255, 255))
				babaRect5 = baba_5.get_rect()
				babaRect5.center = (140, 480)  
				screen.blit(baba_5,babaRect5)
			  


				baba_z = font.render('z: ', True, (0, 0, 0), (255, 255, 255))
				babaRectz = baba_z.get_rect()
				babaRectz.center = (870, 80)  
				screen.blit(baba_z,babaRectz)
				

				baba_x = font.render('x: ' , True, (0, 0, 0), (255, 255, 255))
				babaRectx = baba_x.get_rect()
				babaRectx.center = (870, 180)  
				screen.blit(baba_x,babaRectx)


				baba_c = font.render('c: ', True, (0, 0, 0), (255, 255, 255))
				babaRectc = baba_c.get_rect()
				babaRectc.center = (870, 280)  
				screen.blit(baba_c,babaRectc)


				baba_v = font.render('v: ' , True, (0, 0, 0), (255, 255, 255))
				babaRectv = baba_v.get_rect()
				babaRectv.center = (870, 380)  
				screen.blit(baba_v,babaRectv)


				baba_b = font.render('b: ' , True, (0, 0, 0), (255, 255, 255))
				babaRectb = baba_b.get_rect()
				babaRectb.center = (870, 480)  
				screen.blit(baba_b,babaRectb)



				
				player_group = pygame.sprite.RenderPlain(player_1)
				player_group_2 = pygame.sprite.RenderPlain(player_2)
				item_print_group=pygame.sprite.RenderPlain(*stuff_to_print)
				item_print_group2=pygame.sprite.RenderPlain(*stuff_to_print2)
				player_group.draw(screen)
				player_group_2.draw(screen)
				item_print_group2.draw(screen)
				item_print_group.draw(screen)
				pygame.display.flip()

				stuff_to_print.clear()
				stuff_to_print2.clear() 

				
#gameplay elements, calculating the health
			
			else:
				GameStage = 0
				GameStage2=0
				item_1= item_temp[0]
				item_2=item_temp2[0]
				if lightning_counter_1:
					item_1.damage = 2 * item_1.damage
				if lightning_counter_2:
					item_2.damage = 2 * item_2.damage

				#player 1 uses weapon
				if item_1.damage > 0:

					#weapon v weapon
					if item_2.damage > 0:
						player_2.healthbar -= item_1.damage
						player_1.healthbar -= item_2.damage
						item_1.uses -= 1
						item_2.uses -= 1

					#weapon vs shield
					elif item_2.damage < 0:
						if item_2 == shield:
							item_1.uses -= 1
						elif item_2 == black_hole_shield and item_1.loseable:
							player_1_inventory.remove(item_1)
						elif item_2 == rubber_shield:
							player_1.healthbar -= (item_1.damage // 2)
							item_1.uses -= 1
						
						item_2.uses -= 1
					
					#weapon vs special
					elif item_2.damage == 0:
						if item_2 == lightning:
							pass
						if item_2 == heart:
							player_2.healthbar *= 2
						if item_2 == dice:
							chance = random.randint(1, 100)
							if chance <= 50:
								player_1.healthbar -= 100
							else:
								player_2.healthbar -= 60
						
						player_2.healthbar -= item_1.damage
						item_1.uses -= 1
						item_2.uses -= 1


				#player 1 uses shield
				if item_1.damage < 0:
					
					#shield v shield
					if item_2.damage < 0:
						pass
					
					#shield vs weapon
					elif item_2.damage > 0:
						if item_1 == shield:
							item_2.uses -= 1
						elif item_1 == black_hole_shield and item_2.loseable:
							player_2_inventory.remove(item_2)
						elif item_1 == rubber_shield:
							player_2.healthbar -= (item_2.damage // 2)
							item_2.uses -= 1
						item_1.uses -= 1
					
					#shield vs special
					elif item_2.damage == 0:
						if item_2 == lightning:
							pass
						if item_2 == heart:
							player_2.healthbar *= 2
						if item_2 == dice:
							chance = random.randint(1, 100)
							if chance <= 50:
								player_1.healthbar -= 100
							else:
								player_2.healthbar -= 60

						item_2.uses -= 1

				#player 1 uses special
				if item_1.damage == 0:
					
					#effects for p1
					if item_1 == lightning:
						pass
					if item_1 == heart:
						player_1.healthbar *= 2
					if item_1 == dice:
						chance = random.randint(1, 100)
						if chance <= 50:
							player_2.healthbar -= 100
						else:
							player_1.healthbar -= 60

					item_1.uses -= 1

					#special vs weapon
					if item_2.damage > 0:
						player_1.healthbar -= item_2.damage
						item_2.uses -= 1

					#special vs shield
					if item_2.damage < 0:
						pass

					#special vs special
					if item_2.damage == 0:
						if item_2 == lightning:
							pass
						if item_2 == heart:
							player_2.healthbar *= 2
						if item_2 == dice:
							chance = random.randint(1, 100)
							if chance <= 50:
								player_1.healthbar -= 100
							else:
								player_2.healthbar -= 60

						item_2.uses -= 1


				if item_1.uses == 0:
					player_1_inventory.remove(item_1)
					#print("Player one lost their " + str(item_1))

				if item_2.uses == 0:
					player_2_inventory.remove(item_2)
					#print("Player two lost their" + str(item_2))
				item_temp.remove(item_1)
				item_temp2.remove(item_2)
				pygame.time.wait(1000)
				
		

			print(player_1.healthbar)
			print(player_2.healthbar)

			
		
#pygame.init()
#window_height = 760
#window_width = 1024
#screen = pygame.display.set_mode((window_width, window_height))
#game_fight().main(screen)


