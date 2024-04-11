import pygame
import time
import random
import sys
from pygame.locals import *

pygame.init()

speed = 5
score = 0
score2 = 0
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load('images/enemy.png'), (100, 120))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40, 360),0) 
 
      def move(self):
        global score
        self.rect.move_ip(0, speed)
        if (self.rect.bottom > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0) 



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load('images/player.png'), (50, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < 400:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load('images/coin.webp'), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40, 360), random.randint(20, 110)) 
 
    def move(self):
        self.rect.move_ip(0, speed)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0) 


class Big_coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load('images/coin2.png'), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40, 360), random.randint(20, 110)) 
 
    def move(self):
        self.rect.move_ip(0, speed)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0) 

width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer")
pygame.display.set_icon(pygame.image.load("images/icon.png"))
screen.fill("white")

p1 = Player()
e1 = Enemy()
c1 = Coin()

enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
big_coins = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)
COIN = pygame.USEREVENT + 2
pygame.time.set_timer(COIN, 3000)
BIG_COIN = pygame.USEREVENT + 3
pygame.time.set_timer(BIG_COIN, 5000)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 15)
game_over = font.render("Game Over", True, "black")

background = pygame.transform.scale(pygame.image.load("images/road.png"), (400, 600))

FPS = pygame.time.Clock()
k = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            if k == 0 and score2 > 15:
                speed += 1.5
                k = 1
            else:
                speed += 0.5
        if event.type == pygame.QUIT:
            running = False
        if event.type == COIN:
            c1 = Coin()
            coins.add(c1)
        if event.type == BIG_COIN:
            c2 = Big_coin()
            big_coins.add(c2)

    screen.blit(background, (0,0))
    scores = font_small.render("Overall score: " + str(score), True, "black")
    screen.blit(scores, (10,10))
    scores2 = font_small.render("Score of coins: " + str(score2), True, "black")
    screen.blit(scores2, (250, 10))
    
    for coin in coins:
        screen.blit(coin.image, coin.rect)
        coin.move()
    
    for coin in big_coins:
        screen.blit(coin.image, coin.rect)
        coin.move()

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(p1, coins):
        score2 += 1
        pygame.mixer.Sound('sound/coin.mp3').play()
        for entity in coins:
                entity.kill()
    
    if pygame.sprite.spritecollideany(p1, big_coins):
        score2 += 5
        pygame.mixer.Sound('sound/coin.mp3').play()
        for entity in big_coins:
                entity.kill()


    if pygame.sprite.spritecollideany(p1, enemies):
          pygame.mixer.Sound('sound/crash.mp3').play()
          time.sleep(0.5)
          screen.fill("red")
          screen.blit(game_over, (30, 250))
          pygame.display.update()
          for entity in all_sprites:
            entity.kill() 
          time.sleep(2)
          pygame.quit()       
          sys.exit()
    pygame.display.update()
    FPS.tick(60)
    

