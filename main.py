from ast import Try
import pygame
from sys import exit

#class
class player(pygame.sprite.Sprite):
    max = 0
    def __init__(self,image,image1, scale,scale1,jump,jump_scl,slide,slide_scl):
        super().__init__()  
        self.__image = image
        self.__image1 = image1
        self.__jump = jump
        self.__scale = scale1
        self.__transform = scale
        self.__scale1 = jump_scl
        self.__slide = slide
        self.__slide_scl = slide_scl
        self.gravity = 0
        self.player_run1 = [self.__transform,self.__scale]
        self.player_run = [self.__image,self.__image1]
        self.player_index = 0
        self.img = self.player_run[self.player_index]
        self.img1 = self.player_run1[self.player_index]
        self.rect = self.img1.get_rect(midtop = (100,575))
        self.down = False
    def get_transform(self):
        return self.img1
    def get_image(self):
        return self.img
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.max < 2 and self.rect.bottom > 705:
            self.gravity = -20
            player.max += 1
        if keys[pygame.K_DOWN] and self.rect.bottom == 705:
            self.down = True
            self.gravity = 10   
            self.rect.y = 600
    def player_gravity(self):
        if self.down:
            self.gravity -= 0.3
            self.rect.y += self.gravity
            if self.rect.bottom <= 705:
                self.rect.bottom = 705
                self.down = False
        else:
            self.gravity += 1
            self.rect.y += self.gravity
            if self.rect.bottom >= 705:
                self.rect.bottom = 705
                player.max = 0
    def animation(self):
        if self.rect.bottom < 705:
            self.img = self.__jump
            self.img1 = self.__scale1
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_run): 
                self.player_index = 0
            self.img = self.player_run[int(self.player_index)]
            self.img1 = self.player_run1[int(self.player_index)]
        if self.down:
            self.img = self.__slide
            self.img1 = self.__slide_scl
    def update(self):
        self.player_input()
        self.player_gravity()
        self.animation()
class player1(player):
    def __init__(self,image,image1, scale,scale1,jump,jump_scl,slide,slide_scl):
        super().__init__(image,image1, scale,scale1,jump,jump_scl,slide,slide_scl)
        self.__image = image
        self.__image1 = image1
        self.__jump= jump
        self.__jump_scl = jump_scl
        self.__scale1 = scale1
        self.__scale = scale
        self.__slide = slide
        self.__slide_scl = slide_scl

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
class obstacle3(obstacle):
    def __init__(self, image, scale, rect):
        super().__init__(image, scale, rect)
        self.__image = image
        self.__scale = scale
        self.rect = rect

#score
def score():
    time = int(pygame.time.get_ticks()/1000) - score_time
    score = font.render(f'score :{time}',False,"white")
    score_rect = score.get_rect(center = (1100,100))
    window.blit(score,score_rect)
    try :
        bestscore = int(HighestScore())
    except:
        bestscore = 0
    if(time>bestscore):
        bestscore = time
    with open("HighestScore.txt", "w") as file:
        file.write(str(bestscore))
    screenbestscore = font.render(f'Highest Score :{bestscore}',False,"white")
    bestscore_rect = screenbestscore.get_rect(center = (1050,150))
    window.blit(screenbestscore, bestscore_rect)
    
#score end
def HighestScore():
    with open("HighestScore.txt", "r") as file:
        return file.read()
#score end

#class end

pygame.init()
game = True
window = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Last Ninja')
clock = pygame.time.Clock() 
font = pygame.font.Font('graphic/last_ninja/lastninja.ttf',20)
font1 = pygame.font.Font('graphic/last_ninja/lastninja.ttf',10)
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
# score_text = font.render('Score : 0',False,"white")
# score_rect = score_text.get_rect(center = (1100,100))
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

obs3 = pygame.image.load('graphic/grumpy block tilesets game obstacles/PNG/4.png').convert_alpha()
obs33 = pygame.transform.scale(obs3, (90,90))
obs3_rect = obs33.get_rect(midtop = (900,500))
obs3 = obstacle3(obs3,obs33,obs3_rect)

obs4 = pygame.image.load('graphic/grumpy block tilesets game obstacles/PNG/3.png').convert_alpha()
obs44 = pygame.transform.scale(obs4 , (90,90))
obs4_rect = pygame
#obstacle

#player1
player_img = pygame.image.load('graphic/NinjaRun/png/Run__004.png').convert_alpha()
player_img1 = pygame.image.load('graphic/NinjaRun/png/Run__005.png').convert_alpha()
player_jump = pygame.image.load('graphic/NinjaRun/png/jump__006.png').convert_alpha()
player_slide = pygame.image.load('graphic/NinjaRun/png/Slide__009.png').convert_alpha()
slide_scl = pygame.transform.scale(player_slide,(140,95))
player_jump_scl = pygame.transform.scale(player_jump,(120,170))
player_scl = pygame.transform.scale(player_img,(120,140))
player_scl1 = pygame.transform.scale(player_img1,(120,140))
player = player1(player_img,player_img1,player_scl,player_scl1,player_jump,player_jump_scl,player_slide,slide_scl)
#player1 end

player.max = 0
i=0
width = 1200
obs1_x = 500
obs2_x = 600
player_gravity = 0
score_time = 0
start = False
while True:
    if start == False:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                exit()
        if i == -width:
                window.blit(bg1,(width+i,0))
                window.blit(bg2,(width+i,270))
                window.blit(bg2,(700+width+i,470))
                window.blit(bg3,(width+i+500,470))
                window.blit(ground1,(width+i,700))
                i=0
        i-=5
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
        window.blit(title,title_rect)
        #gambar
        start_img = pygame.image.load('graphic/NinjaRun/png/Jump__006.png').convert_alpha()
        start_scl = pygame.transform.scale(player_img,(190,210))
        window.blit(start_scl,(500,270))
        #gambar end
        #start
        font_start = font.render('Tekan Enter Untuk Memulai Game !!!',False,"white")
        start_rect = font_start.get_rect(center = (600,550))
        window.blit(font_start,start_rect)
        #start end
        pygame.display.update()
        clock.tick(60)
        keys1 = pygame.key.get_pressed()
        if keys1[pygame.K_UP]:
            start = True
    else:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game == True:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] and player.max < 2:
                    player.max += 1
                    player.gravity = -20
                if keys[pygame.K_DOWN]:
                    player.gravity = 5
            else:
                keys1 = pygame.key.get_pressed()
                if keys1[pygame.K_UP]:
                    game = True
                    obs1.rect.right = 800
                    obs2.rect.right = 1200
                    obs3.rect.right = 1100
                    score_time = int(pygame.time.get_ticks()/1000)

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
            obs3.rect.x -= 7
            if obs1.rect.left < -100 : obs1.rect.right = 1300
            if obs2.rect.left < -100 : obs2.rect.right = 1300
            # if obs3.rect.left < -100 : obs3.rect.right = 1300
            window.blit(obs1.get_scale(),obs1.rect)
            window.blit(obs2.get_scale(),obs2.rect)
            # window.blit(obs3.get_scale(),obs3.rect)
        #obstacle end

        #score
            score()
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
            ninja = pygame.image.load('graphic/NinjaRun/png/Dead__009.png').convert_alpha()
            ninja_scl = pygame.transform.scale(ninja,(200,200))
            window.blit(ninja_scl,(500,270))
            popup = font.render(f'& Selamat anda Terlalu NUB untuk game ini &',False,"white")
            popup1 = font.render(f'Tekan Tombol Arrow UP untuk memulai kembali',False,"white")
            popup_rect = popup.get_rect(center = (600,500))
            popup_rect1 = popup1.get_rect(center = (600,550))
            window.blit(popup,popup_rect)
            window.blit(popup1,popup_rect1)


        #crash player
        if player.rect.colliderect(obs1.rect) or player.rect.colliderect(obs2.rect):
            game = False
        #crash end


        pygame.display.update()
        clock.tick(60)