import pygame
import pygame_menu
import time
import math
import random
import sys
#cd D:\game

pygame.init()
pygame.mixer.init()

width = 640
height = 640
width_half = width/2
height_half = height/2

p_width = 10
p_height = 10

p2_width = 10
p2_height = 10

FPS = 100

soundVictory = pygame.mixer.Sound("win.wav")


countEnemyX = 0
countEnemyX2 = 0

countEnemyY = 0
countEnemyY2 = 0

vTrue = False

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((p_width,p_height))
		self.image.fill((0,0,255))
		self.rect = self.image.get_rect()
		self.rect.centerx = 60
		self.rect.bottom = 60
		self.speedx = 0
		self.speedy = 0

	def update(self):
		self.speedx = 0
		self.speedy = 0
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a] and self.rect.left >= 0:
			self.speedx = -3

		if keys[pygame.K_d] and self.rect.right <= width:
			self.speedx = 3

		if keys[pygame.K_w] and self.rect.top >= 0:
			self.speedy = -3

		if keys[pygame.K_s] and self.rect.bottom <= height:
			self.speedy = 3

		self.rect.y += self.speedy
		self.rect.x += self.speedx


class Enemy_x(pygame.sprite.Sprite):
	def __init__(self,spawn_c,spawn_b,xspeed):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((p_width,p_height))
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()
		self.rect.centerx = spawn_c
		self.rect.bottom = spawn_b
		self.speedx = xspeed
		self.speedy = 0

	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx

		if self.rect.top < 0:
			self.speedy *= -1

		if self.rect.bottom > height:
			self.speedy *= -1

		if self.rect.left < 0:
			self.speedx *= -1

		if self.rect.right > width:
			self.speedx *= -1


class Enemy_y(pygame.sprite.Sprite):
	def __init__(self,spawn_c,spawn_b,yspeed):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((p_width,p_height))
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()
		self.rect.centerx = spawn_c
		self.rect.bottom = spawn_b
		self.speedx = 0
		self.speedy = yspeed

	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx

		if self.rect.top < 0:
			self.speedy *= -1

		if self.rect.bottom > height:
			self.speedy *= -1

		if self.rect.left < 0:
			self.speedx *= -1

		if self.rect.right > width:
			self.speedx *= -1


class Nps(pygame.sprite.Sprite):
	def __init__(self,spawn_c,spawn_b):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((p_width,p_height))
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()
		self.rect.centerx = spawn_c
		self.rect.bottom = spawn_b
		self.speedx = random.randrange(1,3)
		self.speedy = random.randrange(1,3)

	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx

		if self.rect.top < 0:
			self.speedy *= -1

		if self.rect.bottom > height:
			self.speedy *= -1

		if self.rect.left < 0:
			self.speedx *= -1

		if self.rect.right > width:
			self.speedx *= -1

class Victory(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((p_width,p_height))
		self.image.fill((0,255,0))
		self.rect = self.image.get_rect()
		self.rect.centerx = 640 - 10
		self.rect.bottom = 640 - 10

clock = pygame.time.Clock()

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Game")

all_sprite_player = pygame.sprite.Group()
all_sprite_enemy = pygame.sprite.Group()
all_sprite_enemy2 = pygame.sprite.Group()
all_sprite_nps = pygame.sprite.Group()

all_sprite_victory = pygame.sprite.Group()

player = Player()

victory = Victory()

all_sprite_player.add(player)
all_sprite_player.add(victory)
all_sprite_victory.add(victory)

for i in range(11):
	countEnemyX += 60
	enemy = Enemy_x(width/2,countEnemyX,2)
	all_sprite_player.add(enemy)
	all_sprite_enemy.add(enemy)

for i in range(11):
	enemy = Enemy_x(width/2,countEnemyX2,-2)
	all_sprite_player.add(enemy)
	all_sprite_enemy.add(enemy)
	countEnemyX2 += 60



for i in range(40):
	nps = Nps(width/2,height/2)
	all_sprite_player.add(nps)
	all_sprite_nps.add(nps)




for i in range(11):
	countEnemyY += 60
	enemy2 = Enemy_y(countEnemyY,height/2,2)
	all_sprite_player.add(enemy2)
	all_sprite_enemy2.add(enemy2)

for i in range(11):
	enemy2 = Enemy_y(countEnemyY2,height/2,-2)
	all_sprite_player.add(enemy2)
	all_sprite_enemy2.add(enemy2)
	countEnemyY2 += 60


while True:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	all_sprite_player.update()
	all_sprite_enemy.update()
	all_sprite_enemy2.update()
	all_sprite_nps.update()

	kils_player = pygame.sprite.spritecollide(player,all_sprite_enemy,False)
	kils_player2 = pygame.sprite.spritecollide(player,all_sprite_enemy2,False)
	kils_player3 = pygame.sprite.spritecollide(player,all_sprite_nps,False)
	win_player = pygame.sprite.spritecollide(player,all_sprite_victory,False)

	if kils_player:
		exit()

	elif win_player:
		soundVictory.play()
		time.sleep(5)
		exit()

	elif kils_player2:
		exit()

	elif kils_player3:
		exit()

	win.fill((0,0,0))
	all_sprite_player.draw(win)
	pygame.display.flip()
pygame.QUIT