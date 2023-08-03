from random import *
from pygame import *

win_height = 700
win_width = 500
x1=350
y1=370
y2=-10
window=display.set_mode((700,500))
clock = time.Clock()
FPS=60
display.set_caption("Marwin factory")
background=transform.scale(image.load("factory.png"),(win_height,win_width))
preview=transform.scale(image.load("main.png"),(win_height,win_width))
window.blit(background,(0,0))
dusts =sprite.Group()
toys1=sprite.Group()
toys2=sprite.Group()
toys3=sprite.Group()
toys4=sprite.Group()
toys5=sprite.Group()
toys6=sprite.Group()
font.init()
fontl=font.SysFont('Arial', 36)
lost=0
total=0
lifes=10
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, height, weight):
        super().__init__()
        self.image=transform.scale(image.load(player_image), (height,weight))
        self.speed=player_speed
        self.rect = self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Cart(GameSprite):
    def update(self):
        global lost 
        global total
        global lifes
        if total<10 and lost<5 and lifes>0:
            keys_pressed=key.get_pressed()
            if keys_pressed[K_a] and self.rect.x >-50:
                self.rect.x -=self.speed
            if keys_pressed[K_d] and self.rect.x <595:
                self.rect.x +=self.speed
        
class Toys(GameSprite):
    def update(self):
        global lost
        global total
        global lifes
        if total>=10 or lost>=5 or lifes<=0:
            self.kill()
        self.rect.y+=self.speed
        if self.rect.y==500:
            lost+=1
        
class Dust(GameSprite):
    def update(self):
        global lost
        global total
        global lifes
        if total>10 or lost>5 or lifes<=0:
            self.kill()
        self.rect.y+=self.speed
        

cart =Cart('cart.png', x1, y1,4, 100,130)
font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN!', True, (255,0,0))
lose = font.render('YOU LOSE!', True, (255,0,0))
death=font.render('YOU DIED!', True, (169,0,0))
game=True
finish = False
mixer.init()
mixer.music.load('music.ogg')
mixer.music.play()

wait=200#игрушки1
wait2=120#обновление
wait0=290#пыль
wait3=280#игрушки2
wait4=360#игрушки3
wait5=300#игрушки4
wait6=200#игрушки5
wait7=240#игрушки6
n=120
while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
    while n!=0:
        window.blit(preview,(0,0))
        display.update()
        n-=1
    window.blit(background,(0,0))
    cart.reset()
    cart.update()
    if finish!=True:
        if wait==0:
            wait=200
            toys1.add(Toys('toy1.png', randint(5,550), y2, randint(2,4),70,120))
        else:
            wait-=1
        if wait0==0:
            wait0=290
            dusts.add(Dust('dust.png', randint(5,550), y2, randint(3,7),90,90))
        else:
            wait0-=1
        if wait3==0:
            wait3=280
            toys2.add(Toys('toy2.png', randint(5,550), y2, randint(3,5),110,160))
        else:
            wait3-=1
        if wait4==0:
            wait4=360
            toys3.add(Toys('toy3.png', randint(5,550), y2, randint(3,5),90,110))
        else:
            wait4-=1
        if wait5==0:
            wait5=300
            toys4.add(Toys('toy4.png', randint(5,550), y2, randint(3,5),70,100))
        else:
            wait5-=1
        if wait6==0:
            wait6=200
            toys5.add(Toys('toy5.png', randint(5,550), y2, randint(3,5),60,120))
        else:
            wait6-=1
        if wait7==0:
            wait7=240
            toys6.add(Toys('toy6.png', randint(5,550), y2, randint(3,5),70,110))
        else:
            wait7-=1
        dusts.draw(window)
        toys3.draw(window)
        toys2.draw(window)
        toys1.draw(window)
        toys4.draw(window)
        toys5.draw(window)
        toys6.draw(window)
        for e in event.get():
            if e.type == QUIT:
                game=False
        text_lose=fontl.render("lost:"+str(lost), 1,(255,255,255))
        text_win=fontl.render("total:"+str(total),1,(255,255,255))
        text_lifes=fontl.render(str(lifes),1,(255,0,0))
        window.blit(text_lose,(2,2))
        window.blit(text_win,(2,30))
        window.blit(text_lifes,(660,1))
    if total==10:
        window.blit(win,(200,200))
        finish=True
        if wait2 == 0:
            wait2 = 120
            lost=0
            total=0
            lifes=10
            finish=False
        else:
            wait2-=1
    if lost==5:
        finish=True
        window.blit(lose,(200,200))
        if wait2 == 0:
            wait2 = 120
            lost=0
            total=0
            lifes=10
            finish=False
        else:
            wait2-=1
    if lifes==0:
        finish=True
        window.blit(death,(200,200))
        if wait2 == 0:
            wait2 = 120
            lost=0
            lifes=10
            total=0
            finish=False
        else:
            wait2-=1
    sprite_list=sprite.spritecollide(cart, toys1,True)
    sprite_list2=sprite.spritecollide(cart, dusts,True)
    sprite_list3=sprite.spritecollide(cart, toys2,True)
    sprite_list4=sprite.spritecollide(cart, toys3,True)
    sprite_list5=sprite.spritecollide(cart, toys4,True)
    sprite_list6=sprite.spritecollide(cart, toys5,True)
    sprite_list7=sprite.spritecollide(cart, toys6,True)
    for f in sprite_list2: 
        lifes-=1
        mixer.music.load('wtf.ogg')
        mixer.music.play()
    for s in sprite_list: 
        total+=1
    for d in sprite_list3: 
        total+=1
    for j in sprite_list4: 
        total+=1
    for u in sprite_list5: 
        total+=1
    for w in sprite_list6: 
        total+=1
    for x in sprite_list7: 
        total+=1
    toys3.update()
    toys2.update()
    toys1.update()
    toys4.update()
    toys5.update()
    toys6.update()
    dusts.update()
    print(wait2)
    display.update()
    clock.tick(FPS)