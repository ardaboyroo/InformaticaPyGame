import pygame
import random
pygame.init()
win = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("henki")
run = True
Universalspeed = 10
flowdirection = -40
F = 1
flowdirection1 = 40
F1= -1
flownum = 0
flownum1 = 0
flow = "left"
flow1 = "right"
bridge1x = 400
bridgex = 800
C = 255
HenkLife = True
PietLife = True
deathbarrier = pygame.Rect(0, 0, 50, 700)
deathbarrier1 = pygame.Rect(1155, 0, 100, 700)
player1 = "Runner"
cosnumber = 0
cosN = 1
Missilespeed = 0
Missile = pygame.transform.scale(pygame.image.load("missile.png"), (32, 64))
Killer = pygame.transform.scale(pygame.image.load("KillerFish.png"), (74, 114))
Eduardoplane = pygame.transform.scale(pygame.image.load("EduardoPlane.png"), (75, 75))
Hamudplane = pygame.transform.scale(pygame.image.load("HamudtPlane.png"), (75, 75))
Chaserimage = Eduardoplane
brug = pygame.transform.scale(pygame.image.load("brug.png"), (150, 139))
gameover = False
Henkwins = False
Pietwins = False
def randomplayer():
    R = random.randint(1,2)
    global player1
    global Chaserimage
    if R == 1:
        player1 = "Chaser"
        Chaserimage = Hamudplane
    else:
        player1 = "Runner"
        Chaserimage = Eduardoplane
def flowrandom():
    flownum = random.randint(1, 2)
    global flowdirection
    global flow
    global F
    if flownum == 1:
        flowdirection = -40
        flow = "left"
        F = 1
    else:
        flowdirection = 40
        flow = "right"
        F = -1
def flowrandom1():
    flownum1 = random.randint(1, 2)
    global flowdirection1
    global flow1
    global F1
    if flownum1 == 1:
        flowdirection1 = -40
        flow1 = "left"
        F1 = 1
    else:
        flowdirection1 = 40
        flow1 = "right"
        F1 = -1

def setbridge1x():
    global bridge1x
    global bridge1
    if flow1 == "left":
        bridge1x = random.randint(300, 800)
    if flow1 == "right":
        bridge1x = random.randint(100, 500)
    bridge1 = Bridge(bridge1x, river1.rect.y)
def setbridgex():
    global bridgex
    global bridge2
    if flow == "left":
        bridgex = random.randint(300, 800)
    if flow == "right":
        bridgex = random.randint(100, 500)
    bridge2 = Bridge(bridgex, river2.rect.y)


class bullet:
   def __init__(self, Xbullet, Ybullet, image):
       self.image = image
       self.rect = self.image.get_rect()
       self.rect.x = Xbullet
       self.rect.y = Ybullet

   def move(self, yspeed, xspeed):
       self.rect.y -= yspeed
       self.rect.x += xspeed
class Runner:
   def __init__(self, Playerx, Playery):
       self.image = pygame.Surface((75, 75))
       self.image.fill((C, C, C))
       self.rect = self.image.get_rect()
       self.rect.x = Playerx
       self.rect.y = Playery

   def move(self, Movex, Movey):
       self.rect.x += Movex
       self.rect.y += Movey

class Chaser:
   def __init__(self, Chaserx, Chasery, image):
       self.image = image
       self.rect = self.image.get_rect()
       self.rect.x = Chaserx
       self.rect.y = Chasery

   def move(self, Chaserspeed):
       self.rect.x += Chaserspeed

class River:
   def __init__(self, Riverx, Rivery):
       self.image = pygame.Surface((1500, 125))
       self.image.fill((0, 50, 255))
       self.rect = self.image.get_rect()
       self.rect.x = Riverx
       self.rect.y = Rivery

   def down(self, fallspeed):
       self.rect.y += fallspeed

class Bridge:
    def __init__(self, bridgenumber, rivernumber):
        self.image = brug
        self.rect = self.image.get_rect()
        self.rect.x = bridgenumber
        self.rect.y = rivernumber-10

    def move(self, Movex, Movey):
       self.rect.x += Movex
       self.rect.y += Movey
randomplayer()
singleflow = 0
Flowright = False
henk = Runner(600, 200)
piet = Chaser(600, 600, Chaserimage)
river1 = River(0, 300)
river2 = River(0, -200)
bridge1 = Bridge(bridge1x, river1.rect.y)
bridge2 = Bridge(bridgex, river2.rect.y)
Bulletis = False
airbombis = False
Bullet = bullet(piet.rect.x + 20, piet.rect.y + 25, Missile)
KillerFish = bullet(henk.rect.x + 33, henk.rect.y, Killer)
SPED = -4
def shoot():
    global Bulletis
    global Bullet
    global Missilespeed
    global SPED
    if Bulletis:
        if Bullet.rect.y < -17000:
            Bullet.rect.x = piet.rect.x + 20
            Bullet.rect.y = piet.rect.y + 10
            Missilespeed = 0
            SPED = -2
    else:
        Bullet = bullet(piet.rect.x + 20, piet.rect.y + 25, Missile)
        Bulletis = True
        Missilespeed = 0
        SPED = -2
def shoot2():
    global airbombis
    global KillerFish
    if airbombis:
        if KillerFish.rect.y > 700:
            KillerFish.rect.x = henk.rect.x + 33
            KillerFish.rect.y = henk.rect.y + 60
    else:
        KillerFish = bullet(henk.rect.x + 50, henk.rect.y + 25, Killer)
        airbombis = True
while run:
   win.fill((59, 186, 24))
   pygame.time.delay(33)
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
# player 1 movement
   press = pygame.key.get_pressed()
   if player1 == "Runner":
       if press[pygame.K_s]:
           henk.move(0, 15)
       if press[pygame.K_d]:
           henk.move(15, 0)
       if press[pygame.K_w]:
           henk.move(0, -15)
       if press[pygame.K_a]:
           henk.move(-15, 0)
    #player 2 movement
       if press[pygame.K_LEFT] and piet.rect.x > 100:
           piet.move(-10)
       if press[pygame.K_RIGHT] and piet.rect.x <= 1020:
           piet.move(10)
   else:
       if press[pygame.K_a] and piet.rect.x > 100:
           piet.move(-10)
       if press[pygame.K_d] and piet.rect.x <= 1020:
           piet.move(10)
       # player 2 movement
       if press[pygame.K_DOWN]:
           henk.move(0, 15)
       if press[pygame.K_RIGHT]:
           henk.move(15, 0)
       if press[pygame.K_UP]:
           henk.move(0, -15)
       if press[pygame.K_LEFT]:
           henk.move(-15, 0)
   if henk.rect.y < 0:
       henk.move(0, 15)
    # gun and barrels
   if player1 == "Runner":
       if press[pygame.K_RCTRL]:
           shoot()
       if press[pygame.K_SPACE]:
           shoot2()
   else:
       if press[pygame.K_SPACE]:
           shoot()
       if press[pygame.K_RCTRL]:
           shoot2()
   if Bulletis:
       Bullet.move(Missilespeed, 0)
       Missilespeed = Missilespeed + SPED
       SPED += 1
   if airbombis:
       KillerFish.move(-5, cosnumber)
       cosnumber -= cosN
       if cosnumber == 16 or cosnumber == -16:
           cosN *= -1

   # bridgemovement n stuffs

   if flow1 == "left":
       bridge1x -= 5
       bridge1.move(-5, 0)
   if flow1 == "right":
       bridge1x += 5
       bridge1.move(5, 0)
   if flow == "left":
       bridgex -= 5
       bridge2.move(-5, 0)
   if flow == "right":
       bridgex += 5
       bridge2.move(5, 0)

   if henk.rect.colliderect(bridge1):
       henk.move(flowdirection1 + 35*F1, Universalspeed)
   if henk.rect.colliderect(bridge2):
       henk.move(flowdirection + 35*F, Universalspeed)

   #rivermovemet and directions
   if river1.rect.y < 700:
       if henk.rect.colliderect(river1) and not henk.rect.colliderect(bridge1):
           henk.move(flowdirection1, 0)
       if river1.rect.y == 690:
          river1.down(-1000)
          bridge1.move(0, -1000)
       bridge1.move(0, Universalspeed)
       river1.down(Universalspeed)

   if river1.rect.y <= -150:
       flowrandom1()
       setbridge1x()

   if river2.rect.y < 700:
       if henk.rect.colliderect(river2) and not henk.rect.colliderect(bridge2):
           henk.move(flowdirection, 0)
       if river2.rect.y == 690:
           river2.down(-1000)
           bridge2.move(0, -1000)
       bridge2.move(0, Universalspeed)
       river2.down(Universalspeed)

   if river2.rect.y <= -150:
       flowrandom()
       setbridgex()
    #henk gets hit
   if henk.rect.colliderect(Bullet):
       if C != 0:
           C -= 51
       else:
           HenkLife = False
   if henk.rect.colliderect(deathbarrier) or henk.rect.colliderect(deathbarrier1) or henk.rect.y >= 650:
       HenkLife = False
       Pietwins = True
   #piet gets hit
   if piet.rect.colliderect(KillerFish):
       PietLife = False
       Henkwins = True
   #game over
   if not HenkLife or not PietLife:
       gameover = True
   if gameover:
       Universalspeed = 0

       if Henkwins:
           piet.move(1000)
       else:
           C = 0

   # drawing time
   win.blit(river1.image, river1.rect)
   win.blit(river2.image, river2.rect)
   win.blit(bridge1.image, bridge1.rect)
   win.blit(bridge2.image, bridge2.rect)
   pygame.draw.rect(win, (0, 50, 255), (0, 0, 100, 700))
   pygame.draw.rect(win, (0, 50, 255), (1105, 0, 100, 700))
   if Bulletis:
       win.blit(Bullet.image, Bullet.rect)
   if airbombis:
       win.blit(KillerFish.image, KillerFish.rect)
   win.blit(piet.image, piet.rect)
   win.blit(henk.image, henk.rect)
   pygame.draw.rect(win, (C, C, C), (henk.rect.x, henk.rect.y, 75, 75))
   pygame.display.update()

pygame.quit()
