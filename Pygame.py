# import pygame

# pygame.init()               # khoi tao

# screen = pygame.display.set_mode(size=(700,700))        # set size window

# pygame.display.set_caption("APU")                       # set name title window

# icon = pygame.image.load("Orc-icon.png")                # set icon
# pygame.display.set_icon(icon)

# screen.fill(color="red")                                # change background 

# # game loop
# running = True
# while running:
#        for event in pygame.event.get():
#               if event.type == pygame.QUIT:
#                      running = False
                     
#        # moi thay doi ben trong cua so phai duoc dat trong game loop
       
       
#        pygame.display.update()

# ----------------------------------------- add image in window and move  --------------------------------------

# import pygame as py
# import time,math,random

# from pygame import mixer           # them am nhac 
# def ship(x,y):
#       screen.blit(image_ship,(x,y)) 

# def enemy(x,y):
#       screen.blit(image_enemy,(x,y))

# def bullet(x,y):
#       screen.blit(image_bullet,(x,y))     


# def shooter(anwser,x,y):
#        if anwser == "yes":
#               bullet(x,y)
                     
              
       
              
       

# if __name__ == "__main__":
#        py.init()
#        screen = py.display.set_mode(size=(700,700))
       
#        # them anh vao window
       
#        # ship image
#        image_ship = py.image.load("space-ship_2.png")
#        image_ship_x = 100
#        image_ship_y = 100
#        image_ship_change_x = 0
#        image_ship_change_y = 0
       
#        # enemy image
       
#        image_enemy = py.image.load("enemy.png")
#        image_enemy_x = 0
#        image_enemy_y = 0
#        image_enemy_change_x = 5
#        image_enemy_change_y = image_enemy.get_height()/2
       
#        Clock = py.time.Clock()
       
#        # background image
       
#        image_background = py.image.load("spacejpg.jpg")
#        image_background_x = 0
#        image_background_y = 0 
#        image_background= py.transform.scale2x(image_background)              # keo dai image theo chieu x 2 lan 
       
#        # bullets image
       
#        image_bullet = py.image.load("bullet.png")
#        image_bullet_x = 1000
#        image_bullet_y = 1000
#        command = "no" 
       
#        # muiti enemy 
#        image_enemys = []
#        image_enemys_x = []
#        image_enemys_y = []
#        image_enemys_change_x = []
#        image_enemys_change_y = []
#        number_enemy = 6
#        for i in range (0,6):
#               image_enemys.append(py.image.load("enemy.png"))
#               image_enemys_y.append(0)
#               image_enemys_x.append(random.randint(10,500) + image_enemy.get_width() )
#               image_enemys_change_x.append(5)
#               image_enemys_change_y.append(image_enemy.get_height()/2)
              
#        # score
       
#        score_value = 0
#        font = py.font.Font(None,30)
       
#        score_x = 10
#        score_y = 10
       
#        # background music 
#        mixer.music.load(filename="background.wav")
#        mixer.music.play(-1)                             # cho nhac phai lai 
       
#        # game over
#        over = "no"
           
       
#               # game loop - giong mainloop ben tkinter
#        running = True
#        while running:
#               for event in py.event.get():
#                      if event.type == py.QUIT:
#                             running = False
#                      if event.type == py.KEYDOWN:
#                             if event.key == py.K_LEFT:
#                                    image_ship_change_x -= 5
#                             if event.key == py.K_RIGHT:
#                                    image_ship_change_x += 5
#                             if event.key == py.K_UP:
#                                    image_ship_change_y -= 5
#                             if event.key == py.K_DOWN:
#                                    image_ship_change_y += 5
#                             if event.key == py.K_SPACE:
#                                    if command == "no":
#                                           command = "yes"
#                                           bullet_sound = mixer.Sound("laser.wav")          # sound khi ban != music
#                                           bullet_sound.play()
#                                           image_bullet_x = image_ship_x + image_ship.get_width()/2
#                                           image_bullet_y = image_ship_y
                                             
#                      if event.type == py.KEYUP:
#                             if event.key == py.K_LEFT or event.key == py.K_RIGHT:
#                                    image_ship_change_x = 0
#                             if event.key == py.K_DOWN or event.key == py.K_UP:
#                                    image_ship_change_y = 0
                            
#               if over == "no":      
#                      # screen.fill("white")                      # phai som mau lai roi moi ve len --> no moi chuyen dong 
#                      screen.blit(image_background,(image_background_x,image_background_y))
                     
#                      score = font.render("Score: "+str(score_value),True,"white")
#                      screen.blit(score,(score_x,score_y))
                     
#                      # di chuyen ship  
#                      image_ship_x += image_ship_change_x
#                      image_ship_y += image_ship_change_y
                     
                     
#                      # khong cho no vuot khung window
#                      if image_ship_x <=0:
#                             image_ship_x = 0
#                      if image_ship_x >=700-image_ship.get_width():
#                             image_ship_x = 700-image_ship.get_width()
#                      if image_ship_y <=0:
#                             image_ship_y = 0
#                      if image_ship_y >=700-image_ship.get_height():
#                             image_ship_y = 700 - image_ship.get_height()
                     
                     
#                      ship(image_ship_x,image_ship_y)           # draw ship
                     
                     
#                      # di chuyen tu dong enemy
#                      for i in range(number_enemy):
                            
#                             image_enemys_x[i] += image_enemys_change_x[i]
#                             if image_enemys_x[i] <=0:
#                                    image_enemys_change_x[i] = image_enemys_change_x[i] * -1
#                                    image_enemys_y[i] = image_enemys_y[i] + image_enemys_change_y[i]
#                             if image_enemys_x[i] >=700-image_enemy.get_width():
#                                    image_enemys_change_x[i] = image_enemys_change_x[i] * -1
#                                    image_enemys_y[i] = image_enemys_y[i] + image_enemys_change_y[i]
                            
#                             enemy(image_enemys_x[i],image_enemys_y[i])
                     
 
#                      # bullets
#                      if command == "yes"  :
                            
#                             if  image_bullet_y <= 0:
#                                    command = "no"
#                                    image_bullet_x = 1000
#                                    image_bullet_y = 1000
#                             else:
                                   
                                   
#                                    image_bullet_y = image_bullet_y - 5
#                                    shooter(command,image_bullet_x,image_bullet_y)
                     
                     
#                      # shoot enemy
                     
#                      # khoang cach (x,y) của viên đạn và (x,y) của ênmy phải bé hơn kc chiều dài ennemy 
                     
#                      # print(kc)
                     
                     
#                      for i in range(number_enemy):
#                             kc = math.sqrt(math.pow((- image_bullet_x + image_enemys_x[i]),2) + math.pow((-image_bullet_y + image_enemys_y[i]),2))
#                             if kc <= image_enemy.get_width() :
#                                    kill_sound = mixer.Sound("explosion.wav")          # sound khi ban != music
#                                    kill_sound.play()
#                                    score_value += 1
                                   
#                             # làm viên đạn biến mất 
#                                    command = "no"
#                                    image_bullet_x = 1000              # set lại tọa độ ban đầu
#                                    image_bullet_y = 1000              # set lại tòa đọ ban đầu 
                            
#                                    # random vị trí mới của enemy      
#                                    image_enemys_x[i] = random.randint(10,600)
#                                    image_enemys_y[i] = 0
                            
                     
#                      # game over 
                     
#                      for i in range(number_enemy):
#                             kc = math.sqrt(math.pow((- image_ship_x + image_enemys_x[i]),2) + math.pow((-image_ship_y + image_enemys_y[i]),2))
#                             if kc <= image_enemy.get_width() :
#                                    game_over = font.render("GAME OVER",True,"white")
#                                    screen.blit(game_over,(250,350))
#                                    over = "yes"
#                                    mixer.music.stop()
                                   
                                   
                            
#               Clock.tick(60)                            # FPS 
#               py.display.update()     

# ---------------------------------------------- GAME 2 -------------------------------------------
import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_walk_1 = pygame.image.load('player_walk_1.png').convert_alpha()
		player_walk_2 = pygame.image.load('player_walk_2.png').convert_alpha()
		self.player_walk = [player_walk_1,player_walk_2]
		self.player_index = 0
		self.player_jump = pygame.image.load('jump.png').convert_alpha()

		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom = (80,300))
		self.gravity = 0

		self.jump_sound = pygame.mixer.Sound('audio_jump.mp3')
		self.jump_sound.set_volume(0.5)

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
			self.gravity = -10
			self.jump_sound.play()

	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 300:
			self.rect.bottom = 300

	def animation_state(self):
		if self.rect.bottom < 300: 
			self.image = self.player_jump
		else:
			self.player_index += 0.1
			if self.player_index >= len(self.player_walk):self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]

	def update(self):
		self.player_input()
		self.apply_gravity()
		self.animation_state()

class Obstacle(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
		
		if type == 'fly':
			fly_1 = pygame.image.load('fly1.png').convert_alpha()
			fly_2 = pygame.image.load('fly2.png').convert_alpha()
			self.frames = [fly_1,fly_2]
			y_pos = 210
		else:
			snail_1 = pygame.image.load('snail1.png').convert_alpha()
			snail_2 = pygame.image.load('snail2.png').convert_alpha()
			self.frames = [snail_1,snail_2]
			y_pos  = 300

		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

	def animation_state(self):
		self.animation_index += 0.1 
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]

	def update(self):
		self.animation_state()
		self.rect.x -= 6
		self.destroy()

	def destroy(self):
		if self.rect.x <= -100: 
			self.kill()


def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
	score_rect = score_surf.get_rect(center = (400,50))
	screen.blit(score_surf,score_rect)
	return current_time

# def obstacle_movement(obstacle_list):
# 	if obstacle_list:
# 		for obstacle_rect in obstacle_list:
# 			obstacle_rect.x -= 10 

# 			if obstacle_rect.bottom == 300: screen.blit(snail_surf,obstacle_rect)
# 			else: screen.blit(fly_surf,obstacle_rect)

# 		obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

# 		return obstacle_list
# 	else: return []

# def collisions(player,obstacles):
# 	if obstacles:
# 		for obstacle_rect in obstacles:
# 			if player.colliderect(obstacle_rect): return False
# 	return True

def collision_sprite():
	# if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
	# 	obstacle_group.empty()
	# 	return False
	# else: return True
       return True

# def player_animation():
# 	global player_surf, player_index

# 	if player_rect.bottom < 300:
# 		player_surf = player_jump
# 	else:
# 		player_index += 0.1
# 		if player_index >= len(player_walk):player_index = 0
# 		player_surf = player_walk[int(player_index)]

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('music.wav')
bg_music.play(loops = -1)

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('Sky.png').convert()
ground_surface = pygame.image.load('ground.png').convert()

# score_surf = test_font.render('My game', False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

# Snail 
snail_frame_1 = pygame.image.load('snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

# Fly
fly_frame1 = pygame.image.load('fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []


player_walk_1 = pygame.image.load('player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('player_walk_2.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load('jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Pixel Runner',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		
		if game_active:
			# if event.type == pygame.MOUSEBUTTONDOWN:
			# 	if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
			# 		player_gravity = -20
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
					player_gravity = -20
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				
				start_time = int(pygame.time.get_ticks() / 1000)

		if game_active:
			if event.type == obstacle_timer:
				obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
				# if randint(0,2):
				# 	obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300)))
				# else:
				# 	obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),210)))

			if event.type == snail_animation_timer:
				if snail_frame_index == 0: snail_frame_index = 1
				else: snail_frame_index = 0
				snail_surf = snail_frames[snail_frame_index] 

			if event.type == fly_animation_timer:
				if fly_frame_index == 0: fly_frame_index = 1
				else: fly_frame_index = 0
				fly_surf = fly_frames[fly_frame_index] 


	if game_active:
		screen.blit(sky_surface,(0,0))
		screen.blit(ground_surface,(0,300))
		# pygame.draw.rect(screen,'#c0e8ec',score_rect)
		# pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
		# screen.blit(score_surf,score_rect)
		score = display_score()
		
		# snail_rect.x -= 4
		# if snail_rect.right <= 0: snail_rect.left = 800
		# screen.blit(snail_surf,snail_rect)

		# Player 
		# player_gravity += 1
		# player_rect.y += player_gravity
		# if player_rect.bottom >= 300: player_rect.bottom = 300
		# player_animation()
		# screen.blit(player_surf,player_rect)
		player.draw(screen)
		player.update()

		obstacle_group.draw(screen)
		obstacle_group.update()

		# Obstacle movement 
		# obstacle_rect_list = obstacle_movement(obstacle_rect_list)

		# collision 
		game_active = collision_sprite()
		# game_active = collisions(player_rect,obstacle_rect_list)
		
	else:
		screen.fill((94,129,162))
		screen.blit(player_stand,player_stand_rect)
		obstacle_rect_list.clear()
		player_rect.midbottom = (80,300)
		player_gravity = 0

		score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
		score_message_rect = score_message.get_rect(center = (400,330))
		screen.blit(game_name,game_name_rect)

		if score == 0: screen.blit(game_message,game_message_rect)
		else: screen.blit(score_message,score_message_rect)

	pygame.display.update()
	clock.tick(60)
 
 
 
 
 
# ----------------------------------------------------- nháp ------------------------------------
# import pygame
# from sys import exit
# from random import randint, choice

# class Player(pygame.sprite.Sprite):
# 	def __init__(self):
# 		super().__init__()
# 		player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
# 		player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
# 		self.player_walk = [player_walk_1,player_walk_2]
# 		self.player_index = 0
# 		self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

# 		self.image = self.player_walk[self.player_index]
# 		self.rect = self.image.get_rect(midbottom = (80,300))
# 		self.gravity = 0

# 		self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
# 		self.jump_sound.set_volume(0.5)

# 	def player_input(self):
# 		keys = pygame.key.get_pressed()
# 		if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
# 			self.gravity = -20
# 			self.jump_sound.play()

# 	def apply_gravity(self):
# 		self.gravity += 1
# 		self.rect.y += self.gravity
# 		if self.rect.bottom >= 300:
# 			self.rect.bottom = 300

# 	def animation_state(self):
# 		if self.rect.bottom < 300: 
# 			self.image = self.player_jump
# 		else:
# 			self.player_index += 0.1
# 			if self.player_index >= len(self.player_walk):self.player_index = 0
# 			self.image = self.player_walk[int(self.player_index)]

# 	def update(self):
# 		self.player_input()
# 		self.apply_gravity()
# 		self.animation_state()

# class Obstacle(pygame.sprite.Sprite):
# 	def __init__(self,type):
# 		super().__init__()
		
# 		if type == 'fly':
# 			fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
# 			fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
# 			self.frames = [fly_1,fly_2]
# 			y_pos = 210
# 		else:
# 			snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# 			snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
# 			self.frames = [snail_1,snail_2]
# 			y_pos  = 300

# 		self.animation_index = 0
# 		self.image = self.frames[self.animation_index]
# 		self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

# 	def animation_state(self):
# 		self.animation_index += 0.1 
# 		if self.animation_index >= len(self.frames): self.animation_index = 0
# 		self.image = self.frames[int(self.animation_index)]

# 	def update(self):
# 		self.animation_state()
# 		self.rect.x -= 6
# 		self.destroy()

# 	def destroy(self):
# 		if self.rect.x <= -100: 
# 			self.kill()

# def display_score():
# 	current_time = int(pygame.time.get_ticks() / 1000) - start_time
# 	score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
# 	score_rect = score_surf.get_rect(center = (400,50))
# 	screen.blit(score_surf,score_rect)
# 	return current_time

# def collision_sprite():
# 	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
# 		obstacle_group.empty()
# 		return False
# 	else: return True


# pygame.init()
# screen = pygame.display.set_mode((800,400))
# pygame.display.set_caption('Runner')
# clock = pygame.time.Clock()
# test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
# game_active = False
# start_time = 0
# score = 0
# bg_music = pygame.mixer.Sound('audio/music.wav')
# bg_music.play(loops = -1)

# #Groups
# player = pygame.sprite.GroupSingle()
# player.add(Player())

# obstacle_group = pygame.sprite.Group()

# sky_surface = pygame.image.load('graphics/Sky.png').convert()
# ground_surface = pygame.image.load('graphics/ground.png').convert()

# # Intro screen
# player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
# player_stand = pygame.transform.rotozoom(player_stand,0,2)
# player_stand_rect = player_stand.get_rect(center = (400,200))

# game_name = test_font.render('Pixel Runner',False,(111,196,169))
# game_name_rect = game_name.get_rect(center = (400,80))

# game_message = test_font.render('Press space to run',False,(111,196,169))
# game_message_rect = game_message.get_rect(center = (400,330))

# # Timer 
# obstacle_timer = pygame.USEREVENT + 1
# pygame.time.set_timer(obstacle_timer,1500)

# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			pygame.quit()
# 			exit()

# 		if game_active:
# 			if event.type == obstacle_timer:
# 				obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
		
# 		else:
# 			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
# 				game_active = True
# 				start_time = int(pygame.time.get_ticks() / 1000)


# 	if game_active:
# 		screen.blit(sky_surface,(0,0))
# 		screen.blit(ground_surface,(0,300))
# 		score = display_score()
		
# 		player.draw(screen)
# 		player.update()

# 		obstacle_group.draw(screen)
# 		obstacle_group.update()

# 		game_active = collision_sprite()
		
# 	else:
# 		screen.fill((94,129,162))
# 		screen.blit(player_stand,player_stand_rect)

# 		score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
# 		score_message_rect = score_message.get_rect(center = (400,330))
# 		screen.blit(game_name,game_name_rect)

# 		if score == 0: screen.blit(game_message,game_message_rect)
# 		else: screen.blit(score_message,score_message_rect)

# 	pygame.display.update()
# 	clock.tick(60)