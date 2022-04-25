from ast import And
from importlib.resources import path
from tkinter import EventType
from turtle import width
from urllib.request import ProxyDigestAuthHandler
import pygame
from sys import exit

#class
class player(pygame.sprite.Sprite):
    max = 0
    def __init__(self,image,scale,rect):
        super().__init__()
        self.__image = image
        self.__transform = scale
        self.rect = rect
        self.gravity = 0
    def get_transform(self):
        return self.__transform
    def get_image(self):
        return self.__image
    def player_input(self):
        if even.type == pygame.KEYDOWN and player.max < 2 and self.rect.bottom > 705:
            self.gravity = -20
            player.max += 1
    def player_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 705:
            self.rect.bottom = 705
            player.max = 0
    def update(self):
        self.player_input()
        self.player_gravity()


class player1(player):
    def __init__(self, image, scale, rect):
        super().__init__(image, scale, rect)
        self.__image = image
        self.__scale = scale
        self.rect = rect
    
class obstacle(pygame.sprite.Sprite):
    def __init__(self,image,scale,rect):
        super().__init__()
        self.__image = image
        self.__transform = scale
        self.rect = rect
    def get_scale(self):
        return self.__transform
    def get_image(self):
        return self.__image

class obstacle1(obstacle):
    def __init__(self, image, scale, rect):
        super().__init__(image, scale, rect)
        self.__image = image
        self.__scale = scale
        self.rect = rect

class obstacle2(obstacle):
    def __init__(self, image, scale, rect):
        super().__init__(image, scale, rect)
        self.__image = image
        self.__scale = scale
        self.rect = rect



#class end

pygame.init()
game = True
window = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Nama Game')
clock = pygame.time.Clock() 
font = pygame.font.Font('graphic/last_ninja/lastninja.ttf',20)
fonttitle = pygame.font.Font('graphic/last_ninja/lastninja.ttf',60)

#background
background = pygame.image.load('graphic/parallax-industrial-pack/parallax-industrial-pack/layers/skill-desc_0003_bg.png').convert_alpha()
bg1 = pygame.transform.scale(background,(1200,800)) 

background1 = pygame.image.load('graphic/parallax-industrial-pack/parallax-industrial-pack/layers/skill-desc_0001_buildings.png').convert_alpha()
bg2 = pygame.transform.scale(background1,(700,450))

background3 = pygame.image.load('graphic/parallax-industrial-pack/parallax-industrial-pack/layers/skill-desc_0000_foreground.png').convert_alpha()
bg3 = pygame.transform.scale(background3,(500,250))
#background end

#title
title = fonttitle.render('Last+ninja',False,"black")
title_rect = title.get_rect(center = (600,100))
#title end

#score
score_text = font.render('Score : 0',False,"white")
score_rect = score_text.get_rect(center = (1100,100))
#score end

#ground
ground = pygame.image.load('graphic/ground_2/ground 2/ground_2.png').convert_alpha()
ground1 = pygame.transform.scale(ground,(1200,100))
#ground end

#obstacle
obs_img = pygame.image.load('graphic/little_shadow_monster_sprites/sprites/a_000.png').convert_alpha()
obs_scl = pygame.transform.scale(obs_img,(90,90))
obs_rect = obs_scl.get_rect(midtop = (500,615))
obs1 = obstacle1(obs_img,obs_scl,obs_rect)

obs1_img = pygame.image.load('graphic/grumpy block tilesets game obstacles/PNG/2.png').convert_alpha()
obs1_scl = pygame.transform.scale(obs1_img,(90,90))
obs1_rect = obs1_scl.get_rect(midtop = (600,615))
obs2 = obstacle2(obs1_img,obs1_scl,obs1_rect)

obs3 = pygame.image.load('graphic/grumpy block tilesets game obstacles/PNG/2.png').convert_alpha()
obs33 = pygame.transform.scale(obs3, (90,90))
obs3_rect = obs33.get_rect()

obs4 = pygame.image.load('graphic/grumpy block tilesets game obstacles/PNG/3.png').convert_alpha()
obs44 = pygame.transform.scale(obs4 , (90,90))
obs4_rect = pygame
#obstacle

#player1
player_img = pygame.image.load('graphic/NinjaRun/png/Idle__000.png').convert_alpha()
player_scl = pygame.transform.scale(player_img,(90,130))
player_rect = player_scl.get_rect(midtop = (100,575))
player = player(player_img,player_scl,player_rect)
#player1 end

player.max = 0
i=0
width = 1200
obs1_x = 500
obs2_x = 600
player_gravity = 0
while True:
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game == True:
            if even.type == pygame.KEYDOWN and player.max < 2:
                player.max += 1
                player.gravity = -20
        else:
            if even.type == pygame.KEYDOWN:
                game = True
                obs1.rect.right = 800
                obs2.rect.right = 1200

    #reapeat background
    if game == True:
        window.fill((0,0,0))
        window.blit(bg1,(i,0))
        window.blit(bg1,(width+i,0))
        window.blit(bg2,(i,270))
        window.blit(bg2,(width+i,270))
        window.blit(bg2,(700+i,270))
        window.blit(bg2,(700+width+i,270))
        window.blit(bg3,(500+i,470))
        window.blit(bg3,(500+width+i,470))
        window.blit(ground1,(i,700))
        window.blit(ground1,(width+i,700))
    #background end

    #title
    window.blit(title,title_rect)
    #title

    #obstacle
    if game == True :
        obs1.rect.x -= 10
        obs2.rect.x -= 8
        if obs1.rect.left < -100 : obs1.rect.right = 1300
        if obs2.rect.left < -100 : obs2.rect.right = 1300
        window.blit(obs1.get_scale(),obs1.rect)
        window.blit(obs2.get_scale(),obs2.rect)
    #obstacle end

    #score
        window.blit(score_text, score_rect)
    #score end

    #player
        # player_gravity += 1
        # player.rect.y += player_gravity
        # if player.rect.bottom >= 705 : 
        #     player.rect.bottom = 705
        #     max_jump = 0
        player.update()
        window.blit(player.get_transform(),player.rect)
    #player end

    #background move
        if i == -width:
            window.blit(bg1,(width+i,0))
            window.blit(bg2,(width+i,270))
            window.blit(bg2,(700+width+i,470))
            window.blit(bg3,(width+i+500,470))
            window.blit(ground1,(width+i,700))
            i=0
        i-=5
    #background end

    #input
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_UP]:
        #print("loncat")
    #input end
    else:
        window.fill("black")

    #crash player
    if player.rect.colliderect(obs1.rect) or player.rect.colliderect(obs2.rect):
        game = False
    #crash end

    
    pygame.display.update()
    clock.tick(60)