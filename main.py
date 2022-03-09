import pygame
import random
import math
import time

pygame.init()
pygame.mixer.init()

ScreenWidth = 1200  # De breedte van het scherm in pixels
ScreenHeight = 700  # De hoogte van het scherm in pixels
win = pygame.display.set_mode((ScreenWidth, ScreenHeight))  # Breedte en Hoogte van het scherm in aantal pixels
pygame.display.set_caption("Arda en Nieks Reetro(met een C) Arkade")  # De caption van de window

""" Dit is voor FULLSCREEN
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# get the default size
ScreenX, ScreenY = win.get_size()
"""

# De volgende Variables zijn de kleuren van de gekozen ColourScheme
Black = (0, 0, 0)
Gray = (35, 35, 35)
DarkPurple = (55, 25, 103)
MainPurple = (110, 50, 205)
LightPurple = (154, 153, 235)
Pink = (250, 172, 215)
White = (255, 255, 255)
Blue = (58, 134, 255)
Green = (136, 255, 38)
Red = (255, 0, 60)
Yellow = (255, 225, 0)

# De volgende Variables zijn de bool values voor de games
Game1 = False  # Simone Zegt
Game2 = False  # Gunter
Game3 = False  # Pong
Game4 = False  # Henk en Piet 2.0 (Turkish Version)
Game5 = False  # Sumo


# De volgende Variables zijn veelgebruikte Values
Img1 = pygame.transform.scale(pygame.image.load("Sprites/1.png"), (100, 100))
Img2 = pygame.transform.scale(pygame.image.load("Sprites/2.png"), (100, 100))
Img3 = pygame.transform.scale(pygame.image.load("Sprites/3.png"), (100, 100))
Game1Img = pygame.transform.scale(pygame.image.load("Sprites/InkedGame1_LI.jpg"), (150, 100))
Game2Img = pygame.transform.scale(pygame.image.load("Sprites/GUNTER.png"), (150, 100))
Game3Img = pygame.transform.scale(pygame.image.load("Sprites/ponk.png"),(150, 100))
Game4Img = pygame.transform.scale(pygame.image.load("Sprites/henkenpiet.png"), (150, 100))
Game5Img = pygame.transform.scale(pygame.image.load("Sprites/SumoLogo.png"), (150, 100))
RandPNG = pygame.transform.scale(pygame.image.load("Sprites/RandomSprite.png"), (150, 100))
hitSound = pygame.mixer.Sound("Sounds/hitmarker_2.mp3")
hitSound.set_volume(0.1)
IsRunning = True  # Een boolean voor de while loop
Menu = True
BigFont = pygame.font.Font("freesansbold.ttf", 32)
MediumFont = pygame.font.Font("freesansbold.ttf", 24)
SmallFont = pygame.font.Font("freesansbold.ttf", 16)
TitleTxt = BigFont.render("Wilkom bij Arda en Niek's Reetro(met een C) Arkade", True, Pink, DarkPurple)
ScorePone = 0
ScorePtwo = 0
LoadingEnd = False
LoadingInt = 16
LoadingTime = LoadingInt
LoadingStep = 16
MouseX = 0
MouseY = 0
MouseRect = pygame.Rect(MouseX, MouseY, 10, 10)
Game1Rect = pygame.Rect(225, 150, 150, 100)
Game2Rect = pygame.Rect(525, 150, 150, 100)
Game3Rect = pygame.Rect(825, 150, 150, 100)
Game4Rect = pygame.Rect(225, 350, 150, 100)
Game5Rect = pygame.Rect(525, 350, 150, 100)
RandomGameRect = pygame.Rect(825, 350, 150, 100)
PoneBGC = Black
PtwoBGC = Black

# -----------------De volgende Variables zijn voor Game1-----------------
GameStarted = False
ColourList = ["Blue", "Green", "Red", "Yellow"]
PoneSimonList = []
PtwoSimonList = []
PoneList = []
PtwoList = []
CountDown = False
CountDownAmount = 3
CheckOne = False
CheckTwo = False
PoneReady = True
PtwoReady = True
PoneLose = False
PtwoLose = False
ScoreDebounce = False
SpaceToStartTxt = MediumFont.render("Druk op spatie om te beginnen", True, Pink, DarkPurple)
SpaceRestartTxt = MediumFont.render("Druk op spatie om opnieuw te spelen", True, Pink, DarkPurple)


def LoseTxtFunc(val):
    global LoseTxt
    PlayerLoseTxt = val
    LoseTTTTTT = "Game over, iemand heeft verloren (Ik zeg niet wie maar het was " + PlayerLoseTxt + ")."
    LoseTxt = MediumFont.render(LoseTTTTTT, True, Pink, DarkPurple)


BluePlaceHolder = (21, 47, 89)
GreenPlaceHolder = (35, 79, 0)
RedPlaceHolder = (87, 0, 20)
YellowPlaceHolder = (87, 76, 0)

PoneSimonBlueColour, PoneSimonGreenColour, PoneSimonRedColour, PoneSimonYellowColour = BluePlaceHolder, GreenPlaceHolder, RedPlaceHolder, YellowPlaceHolder
PtwoSimonBlueColour, PtwoSimonGreenColour, PtwoSimonRedColour, PtwoSimonYellowColour = BluePlaceHolder, GreenPlaceHolder, RedPlaceHolder, YellowPlaceHolder

PoneBlueColour, PoneGreenColour, PoneRedColour, PoneYellowColour = BluePlaceHolder, GreenPlaceHolder, RedPlaceHolder, YellowPlaceHolder
PtwoBlueColour, PtwoGreenColour, PtwoRedColour, PtwoYellowColour = BluePlaceHolder, GreenPlaceHolder, RedPlaceHolder, YellowPlaceHolder


# -----------------De volgende Variables zijn voor Game2-----------------
class Pointer:
    def __init__(self, PointerX):
        self.image = pygame.Surface((5, 28))
        self.image.fill(Black)
        self.rect = self.image.get_rect()
        self.rect.y = ScreenHeight * (7 / 8) - 4
        self.rect.x = PointerX

    def move(self, Sped):
        self.rect.x += Sped


class RedBar:
    def __init__(self):
        self.image = pygame.Surface((5, 20))
        self.image.fill(Red)
        self.rect = self.image.get_rect()
        self.rect.y = ScreenHeight * (7 / 8)

    def SetSize(self, RedBarSize, RedBarPos):
        self.image = pygame.Surface((RedBarSize, 20))
        self.image.fill(Red)
        self.rect = self.image.get_rect()
        self.rect.y = ScreenHeight * (7 / 8)
        self.rect.x = ScreenWidth * (1 / 8) + RedBarPos


class GreenBar:
    def __init__(self):
        self.image = pygame.Surface((5, 20))
        self.image.fill(Green)
        self.rect = self.image.get_rect()
        self.rect.y = ScreenHeight * (7 / 8)

    def SetSize(self, GreenBarPos, ID):
        # self.image = pygame.Surface((5, 20))
        if ID == 1:
            self.image = pygame.Surface((PoneRedBar.image.get_width() / 3, 20))
        if ID == 2:
            self.image = pygame.Surface((PtwoRedBar.image.get_width() / 3, 20))
        self.image.fill(Green)
        self.rect = self.image.get_rect()
        self.rect.y = ScreenHeight * (7 / 8)
        if ID == 1:
            self.rect.x = (PoneRedBar.image.get_width() / 2) + (ScreenWidth * (1 / 8)) + GreenBarPos - (
                        self.image.get_width() / 2)
        if ID == 2:
            self.rect.x = (PtwoRedBar.image.get_width() / 2) + (ScreenWidth * (1 / 8)) + GreenBarPos - (
                        self.image.get_width() / 2)


PonePointerSpeed = 10
PtwoPointerSpeed = 10
PoneRedBarDrawed = False
PoneGreenBarDrawed = False
PtwoRedBarDrawed = False
PtwoGreenBarDrawed = False
PoneWin = False
PtwoWin = False
PoneWinTxt = MediumFont.render("Hamudt heeft gewonnen, Eduardo je moet echt beter worden gap", True, Black)
PtwoWinTxt = MediumFont.render("Eduardo heeft gewonnen, Hamudt je moet echt beter worden gap", True, Black)
PonePointerX = ScreenWidth * 0.25
PtwoPointerX = ScreenWidth * 0.75
PoneStep = 0  # Dit is de "stappenteller" met een maximaal van 20
PtwoStep = 0  # Dit is de "stappenteller" met een maximaal van 20

PonePoint = Pointer(PonePointerX)
PtwoPoint = Pointer(PtwoPointerX)
PoneRedBar = RedBar()
PtwoRedBar = RedBar()
PoneGreenBar = GreenBar()
PtwoGreenBar = GreenBar()


# -----------------De volgende Variables zijn voor Game3-----------------


# classes

class PongBar:
    def __init__(self, locationx, locationy, ):
        self.image = pygame.Surface((20, 200))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = locationx
        self.rect.y = locationy

    def move(self, speed):
        self.rect.y -= speed


class Ball:
    def __init__(self, locationx, locationy, size):
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = locationx
        self.rect.y = locationy

    def move(self, xspeed, yspeed):
        self.rect.x += xspeed
        self.rect.y -= yspeed

    def teleport(self, locationx, locationy):
        self.rect.x = locationx
        self.rect.y = locationy


class Portal:
    def __init__(self, locationx, locationy, colour, xsize, ysize):
        self.image = pygame.Surface((xsize, ysize))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = locationx
        self.rect.y = locationy

    def reset(self):
        self.rect.x = -2000
        self.rect.y = -2000


class powerup:
    def __init__(self, locationx, locationy):
        self.image = pygame.Surface((60, 60))
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = locationx
        self.rect.y = locationy


Player1 = PongBar((ScreenWidth / 10), 200)
Player2 = PongBar(((ScreenWidth / 10) * 9), 200)
ball0 = Ball(ScreenWidth / 2, random.randint(1, ScreenHeight - 21), 20)
balllist = [ball0]
yspeedlist = [10]
xspeedlist = [10]
Leftballlist = [False]
Upballlist = [True]
Hportals = False
Vportals = False
Hteleported = False
Vteleported = False
i = 0
barrierUp = pygame.Rect(0, -10, ScreenWidth, 10)
barrierDown = pygame.Rect(0, ScreenHeight, ScreenWidth, 10)
secs = 0
powerdUp = False
# -----------------De volgende Variables zijn voor Game4-----------------\
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
    def __init__(self, Playerx, Playery, image):
        self.image = image
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
        self.rect.y = rivernumber - 10

    def move(self, Movex, Movey):
        self.rect.x += Movex
        self.rect.y += Movey




def henkreset():
    global Universalspeed
    global flowdirection
    global F
    global flowdirection1
    global F1
    global flownum
    global flownum1
    global flow
    global flow1
    global bridge1x
    global bridgex
    global C
    global HenkLife
    global PietLife
    global deathbarrier
    global deathbarrier1
    global player1
    global cosnumber
    global cosN
    global Missilespeed
    global Missile
    global gameover
    global Henkwins
    global Pietwins
    global singleflow
    global Flowright
    global bridge1
    global bridge2
    global Bulletis
    global airbombis
    global Bullet
    global KillerFish
    global SPED
    global henk
    global piet
    global river1
    global river2
    Universalspeed = 10
    flowdirection = -40
    F = 1
    flowdirection1 = 40
    F1 = -1
    flownum = 0
    flownum1 = 0
    flow = "left"
    flow1 = "right"
    bridge1x = 400
    bridgex = 800
    C = 255
    HenkLife = True
    PietLife = True
    player1 = "Runner"
    cosnumber = 0
    cosN = 1
    gameover = False
    Henkwins = False
    Pietwins = False
    singleflow = 0
    Flowright = False
    deathbarrier = pygame.Rect(0, 0, 50, 700)
    deathbarrier1 = pygame.Rect(1155, 0, 100, 700)
    henk = Runner(600, 200, Runnerimage)
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
    Missilespeed = 0
    henk = Runner(600, 200, Runnerimage)
    piet = Chaser(600, 600, Chaserimage)
    river1 = River(0, 300)
    river2 = River(0, -200)
    river1.rect.y = 300
    river2.rect.y = -200
    bridge1 = Bridge(bridge1x, river1.rect.y)
    bridge2 = Bridge(bridgex, river2.rect.y)
    randomplayer()
Missile = pygame.transform.scale(pygame.image.load("Sprites/missile.png"), (32, 64))
Killer = pygame.transform.scale(pygame.image.load("Sprites/KillerFish.png"), (74, 114))
Eduardoplane = pygame.transform.scale(pygame.image.load("Sprites/EduardoPlane.png"), (75, 75))
Hamudplane = pygame.transform.scale(pygame.image.load("Sprites/HamudtPlane.png"), (75, 75))
Chaserimage = Eduardoplane
Hamudroller = pygame.transform.scale(pygame.image.load("Sprites/Hamudroller.png"), (75, 75))
Eduardoroller = pygame.transform.scale(pygame.image.load("Sprites/eduardoroller.png"), (50, 75))
Runnerimage = Hamudroller
brug = pygame.transform.scale(pygame.image.load("Sprites/brug.png"), (150, 139))
Universalspeed = 10
flowdirection = -40
F = 1
flowdirection1 = 40
F1 = -1
flownum = 0
flownum1 = 0
flow = "left"
flow1 = "right"
bridge1x = 400
bridgex = 800
C = 255
HenkLife = True
PietLife = True
player1 = "Runner"
cosnumber = 0
cosN = 1
gameover = False
Henkwins = False
Pietwins = False
singleflow = 0
Flowright = False
deathbarrier = pygame.Rect(0, 0, 50, 700)
deathbarrier1 = pygame.Rect(1155, 0, 100, 700)
Bulletis = False
airbombis = False
SPED = -4
Missilespeed = 0
henk = Runner(600, 200, Runnerimage)
piet = Chaser(600, 600, Chaserimage)
river1 = River(0, 300)
river2 = River(0, -200)
bridge1 = Bridge(bridge1x, river1.rect.y)
bridge2 = Bridge(bridgex, river2.rect.y)
Bullet = bullet(piet.rect.x + 20, piet.rect.y + 25, Missile)
KillerFish = bullet(henk.rect.x + 33, henk.rect.y, Killer)



def randomplayer():
    R = random.randint(1, 2)
    global player1
    global Chaserimage
    global Runnerimage
    if R == 1:
        player1 = "Chaser"
        Chaserimage = Hamudplane
        Runnerimage = Eduardoroller
    else:
        player1 = "Runner"
        Chaserimage = Eduardoplane
        Runnerimage = Hamudroller


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


randomplayer()
henk = Runner(600, 200, Runnerimage)
piet = Chaser(600, 600, Chaserimage)
river1 = River(0, 300)
river2 = River(0, -200)
bridge1 = Bridge(bridge1x, river1.rect.y)
bridge2 = Bridge(bridgex, river2.rect.y)
# -----------------De volgende Variables zijn voor Game5-----------------

Sgamestart = False
Sgamestarttimer = 0
Startsumotimer = False
Sload1 = pygame.transform.scale(pygame.image.load("Sprites/1.png"), (100, 100))
Sload2 = pygame.transform.scale(pygame.image.load("Sprites/2.png"), (100, 100))
Sload3 = pygame.transform.scale(pygame.image.load("Sprites/3.png"), (100, 100))
Sfont = pygame.font.Font("freesansbold.ttf", 50)
Stext = Sfont.render("Press the Spacebar to start!", True, (225, 225, 225), (0, 0, 0))
Stextrect = Stext.get_rect()
Stextrect.center = (600, 150)
# player variables
Splayer1 = 1
Splayer2 = 1
Splayer1live = True
Splayer2live = True
Splayer1x = 200
Splayer1y = 275
Splayer2x = 900
Splayer2y = 275
Splayer1rect = pygame.Rect(200, 275, 100, 100)
Splayer2rect = pygame.Rect(900, 275, 100, 100)
SPlayer1image = pygame.image.load("Sprites/SumoH.png")
SPlayer1image = pygame.transform.scale(SPlayer1image, (105, 105))
SPlayer2image = pygame.image.load("Sprites/SumoE.png")
SPlayer2image = pygame.transform.scale(SPlayer2image, (105, 105))
Stextwin1 = Sfont.render("Player 1 wins", True, (225, 225, 225), (0, 0, 0))
Stextrectwin1 = Stextwin1.get_rect()
Stextrectwin1.center = (600, 150)
Stextwin2 = Sfont.render("Player 2 wins", True, (225, 225, 225), (0, 0, 0))
Stextrectwin2 = Stextwin2.get_rect()
Stextrectwin2.center = (600, 150)
# power push
Sumorantimer = 0
Stime = 0
Srandomdirection = 0
Sdownarrow = pygame.image.load("Sprites/downarrow.png")
Sdownarrow = pygame.transform.scale(Sdownarrow, (100, 100))
Sleftarrow = pygame.image.load("Sprites/leftarrow.png")
Sleftarrow = pygame.transform.scale(Sleftarrow, (100, 100))
Srightarrow = pygame.image.load("Sprites/rightarrow.png")
Srightarrow = pygame.transform.scale(Srightarrow, (100, 100))
Skeyassigned = "no"
S1 = 0
Sp1F = 0
Sp2F = 0
# essential stuff
deathbarrect = pygame.Rect(1100, 0, 10, 1000)
deathbarrect1 = pygame.Rect(100, 0, 10, 1000)
win = pygame.display.set_mode((1200, 700))
Sumogamedone = False
SS = 0
gavescoreScoreplayer2 = False
gavescoreScoreplayer1 = False
def Sumoreset():
    global Splayer2x
    global Splayer1x
    global Splayer1rect
    global Splayer2rect
    global Splayer1live
    global Splayer2live
    global SS
    global Sgamestart
    global gavescoreScoreplayer2
    global gavescoreScoreplayer1
    Splayer2x = 900
    Splayer1x = 200
    Splayer1rect = pygame.Rect(200, 275, 100, 100)
    Splayer2rect = pygame.Rect(900, 275, 100, 100)
    Splayer1live = True
    Splayer2live = True
    SS = 0
    Sgamestart = False
    gavescoreScoreplayer2 = False
    gavescoreScoreplayer1 = False
# --------------------------------------------------------------------Main while loop-----------------------------------------------------------------------------------

while IsRunning:
    pygame.time.delay(33)  # Framerate in 1/milliseconden

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if statement om de game af te sluiten met de rode kruis
            IsRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # if statement for de hit sound
            hitSound.play()
        MouseRect.move_ip(-MouseX, -MouseY)
        MouseX = pygame.mouse.get_pos()[0]
        MouseY = pygame.mouse.get_pos()[1]
        MouseRect.move_ip(MouseX, MouseY)

        if Game1:
            if event.type == pygame.KEYUP:
                if not len(PoneList) >= len(PoneSimonList):
                    if event.key == pygame.K_w:
                        PoneList.append(ColourList[0])
                        CheckOne = True
                    if event.key == pygame.K_a:
                        PoneList.append(ColourList[1])
                        CheckOne = True
                    if event.key == pygame.K_s:
                        PoneList.append(ColourList[2])
                        CheckOne = True
                    if event.key == pygame.K_d:
                        PoneList.append(ColourList[3])
                        CheckOne = True
                else:
                    PoneReady = True
                if not len(PtwoList) >= len(PtwoSimonList):
                    if event.key == pygame.K_UP:
                        PtwoList.append(ColourList[0])
                        CheckTwo = True
                    if event.key == pygame.K_LEFT:
                        PtwoList.append(ColourList[1])
                        CheckTwo = True
                    if event.key == pygame.K_DOWN:
                        PtwoList.append(ColourList[2])
                        CheckTwo = True
                    if event.key == pygame.K_RIGHT:
                        PtwoList.append(ColourList[3])
                        CheckTwo = True
                else:
                    pygame.draw.rect(win, PtwoBlueColour,
                                     (math.floor(ScreenWidth / 5 + 25), math.floor(ScreenHeight / 1.5), 50, 25))
                    pygame.draw.rect(win, PtwoRedColour,
                                     (math.floor(ScreenWidth / 5 + 25), math.floor(ScreenHeight / 1.5 + 50), 50, 25))
                    pygame.draw.rect(win, PtwoGreenColour,
                                     (math.floor(ScreenWidth / 5 - 25), math.floor(ScreenHeight / 1.5 + 25), 50, 25))
                    pygame.draw.rect(win, PtwoYellowColour,
                                     (math.floor(ScreenWidth / 5 + 75), math.floor(ScreenHeight / 1.5 + 25), 50, 25))
                    PtwoReady = True

        if Game2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if PonePoint.rect.colliderect(
                            PoneGreenBar.rect) and PoneStep <= 20:  # Check of de Pointer collide met de GreenBar
                        PoneStep += 1
                        PoneRedBarDrawed = False
                        PoneGreenBarDrawed = False
                    elif PonePoint.rect.colliderect(
                            PoneRedBar.rect):  # Checkt of de player alleen met de RedBar collide wanneer het klikt
                        if PoneStep - 2 < 0:
                            PoneStep = 0
                        else:
                            PoneStep -= 2
                        PoneRedBarDrawed = False
                        PoneGreenBarDrawed = False
                if event.key == pygame.K_UP:
                    if PtwoPoint.rect.colliderect(PtwoGreenBar.rect) and PtwoStep <= 20:
                        PtwoStep += 1
                        PtwoRedBarDrawed = False
                        PtwoGreenBarDrawed = False
                    elif PtwoPoint.rect.colliderect(PtwoRedBar.rect):
                        if PtwoStep - 2 < 0:
                            PtwoStep = 0
                        else:
                            PtwoStep -= 2
                        PtwoRedBarDrawed = False
                        PtwoGreenBarDrawed = False

        if Game5:
            if Sgamestart:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w and Splayer1live and Splayer2live:
                        Splayer1x += 20
                        Splayer1rect.move_ip(20, 0)
                        if Splayer1rect.colliderect(Splayer2rect):
                            Splayer2x += 20
                            Splayer2rect.move_ip(20, 0)
                if event.type == pygame.KEYUP and Splayer2live and Splayer1live:
                    if event.key == pygame.K_UP:
                        Splayer2x -= 20
                        Splayer2rect.move_ip(-20, 0)
                        if Splayer2rect.colliderect(Splayer1rect):
                            Splayer1x -= 20
                            Splayer1rect.move_ip(-20, 0)


    # """
    def loading(val):
        for y in range(1, LoadingTime):
            pygame.draw.rect(win, Black, (0, 0, ScreenWidth, math.floor(ScreenHeight * (y / LoadingStep))))
            pygame.display.update()
            pygame.time.wait(33)
        pygame.draw.rect(win, Black, (0, 0, ScreenWidth, ScreenHeight))
        pygame.display.update()
        pygame.time.wait(250)
        val = True
        return val


    ScorePoneTxt = SmallFont.render("Hamudt: " + str(ScorePone), True, Red, PoneBGC)  # Update de score van Hamudt
    ScorePtwoTxt = SmallFont.render("Eduardo: " + str(ScorePtwo), True, Blue, PtwoBGC)  # Update de score van Eduardo
# this is to stop playing the games
    Key = pygame.key.get_pressed()
    if Key[pygame.K_ESCAPE]:
        Menu = True
        GameStarted = False
        CountDown = False
        Game1 = False
        Game2 = False
        Game3 = False
        Game4 = False
        Game5 = False
        Game6 = False
        ScoreDebounce = False
        PoneLose, PtwoLose = False, False
        LoadingTime = LoadingInt
        LoadingEnd = loading(LoadingEnd)
        # Resets game 4
        henkreset()
        # Resets game 4
        Sumoreset()

    if Key[pygame.K_SPACE]:  # Hiermeer worden alle games gestart
        if not Menu:
            if not GameStarted:
                GameStarted = True
                CountDown = True
                PoneReady, PtwoReady = True, True
                PoneLose, PtwoLose = False, False
                PoneStep, PtwoStep = 0, 0
                PoneWin, PtwoWin = False, False
                ScoreDebounce = False

    if Menu:
        win.fill(MainPurple)
        pygame.display.set_caption("Arda en Nieks Reetro(met een C) Arkade")  # De caption van de window
        PoneBGC, PtwoBGC = White, White
        for x in range(1, 100):  # Deze for-loop zorgt voor een "Retro Scan Lines" effect
            pygame.draw.rect(win, Black, (0, (x * 9 - 4), ScreenWidth, 2))

        if Key[pygame.K_y]:
            ScorePone, ScorePtwo = 0, 0

        win.blit(ScorePoneTxt,
                 ScorePoneTxt.get_rect(center=(ScreenWidth / 16, ScreenHeight / 16)))  # Draw de score van Hamudt
        win.blit(ScorePtwoTxt,
                 ScorePtwoTxt.get_rect(center=(ScreenWidth / 1.1, ScreenHeight / 16)))  # Draw de score van Eduardo
        win.blit(TitleTxt, TitleTxt.get_rect(center=(ScreenWidth / 2, ScreenHeight / 16)))

        win.blit(Game1Img, (225, 150))
        win.blit(Game2Img, (525, 150))
        win.blit(Game3Img, (825, 150))
        win.blit(Game4Img, (225, 350))
        win.blit(Game5Img, (525, 350))
        win.blit(RandPNG, (825, 350))
        win.blit(RandPNG, (825, 350))

        if pygame.mouse.get_pressed()[0]:
            MouseX = pygame.mouse.get_pos()[0]
            MouseY = pygame.mouse.get_pos()[1]

            if MouseRect.colliderect(Game1Rect):
                Menu = False
                Game1 = True
                LoadingTime = LoadingInt
                LoadingEnd = loading(LoadingEnd)
            if MouseRect.colliderect(Game2Rect):
                Menu = False
                Game2 = True
                LoadingTime = LoadingInt
                LoadingEnd = loading(LoadingEnd)
            if MouseRect.colliderect(Game3Rect):
                Menu = False
                Game3 = True
                LoadingTime = LoadingInt
                LoadingEnd = loading(LoadingEnd)
            if MouseRect.colliderect(Game4Rect):
                Menu = False
                Game4 = True
                LoadingTime = LoadingInt
                LoadingEnd = loading(LoadingEnd)
            if MouseRect.colliderect(Game5Rect):
                Menu = False
                Game5 = True
                LoadingTime = LoadingInt
                LoadingEnd = loading(LoadingEnd)
            if MouseRect.colliderect(RandomGameRect):
                Menu = False
                randInt = random.randint(1, 6)  # Kijk of randInt wel getallen geeft tussen 1 en 6
                if randInt == 1:
                    Game1 = True
                if randInt == 2:
                    Game2 = True
                if randInt == 3:
                    Game3 = True
                if randInt == 4:
                    Game4 = True
                if randInt == 5:
                    Game5 = True
                if randInt == 6:
                    Game6 = True
                LoadingTime = LoadingInt
                LoadingEnd = loading(LoadingEnd)
#  ---------------------------------------------------Game 1--------------------------------------
    if Game1:
        win.fill(Gray)  # Teken de achtergrond
        pygame.display.set_caption(
            "Arda en Nieks Reetro(met een C) Arkade: Simone zegt")  # Zet de caption met het huidige spel
        PoneBGC, PtwoBGC = Gray, Gray  # Achtergrond voor de score names
        win.blit(ScorePoneTxt,
                 ScorePoneTxt.get_rect(center=(ScreenWidth / 16, ScreenHeight / 16)))  # Draw de score van Hamudt
        win.blit(ScorePtwoTxt,
                 ScorePtwoTxt.get_rect(center=(ScreenWidth / 1.1, ScreenHeight / 16)))  # Draw de score van Eduardo

        pygame.draw.rect(win, White, (math.floor(ScreenWidth / 2 - 10), 0, 10, ScreenHeight))  # Draw een witte lijn

        # Simon voor Player One
        pygame.draw.rect(win, PoneSimonBlueColour, (math.floor(ScreenWidth / 5), math.floor(ScreenHeight / 6), 100, 50))
        pygame.draw.rect(win, PoneSimonRedColour,
                         (math.floor(ScreenWidth / 5), math.floor(ScreenHeight / 6 + 100), 100, 50))
        pygame.draw.rect(win, PoneSimonGreenColour,
                         (math.floor(ScreenWidth / 5 - 100), math.floor(ScreenHeight / 6 + 50), 100, 50))
        pygame.draw.rect(win, PoneSimonYellowColour,
                         (math.floor(ScreenWidth / 5 + 100), math.floor(ScreenHeight / 6 + 50), 100, 50))
        # Player One
        pygame.draw.rect(win, PoneBlueColour,
                         (math.floor(ScreenWidth / 5 + 25), math.floor(ScreenHeight / 1.5), 50, 25))
        pygame.draw.rect(win, PoneRedColour,
                         (math.floor(ScreenWidth / 5 + 25), math.floor(ScreenHeight / 1.5 + 50), 50, 25))
        pygame.draw.rect(win, PoneGreenColour,
                         (math.floor(ScreenWidth / 5 - 25), math.floor(ScreenHeight / 1.5 + 25), 50, 25))
        pygame.draw.rect(win, PoneYellowColour,
                         (math.floor(ScreenWidth / 5 + 75), math.floor(ScreenHeight / 1.5 + 25), 50, 25))

        # Simon voor Player Two
        pygame.draw.rect(win, PtwoSimonBlueColour,
                         (math.floor(ScreenWidth / 1.35), math.floor(ScreenHeight / 6), 100, 50))
        pygame.draw.rect(win, PtwoSimonRedColour,
                         (math.floor(ScreenWidth / 1.35), math.floor(ScreenHeight / 6 + 100), 100, 50))
        pygame.draw.rect(win, PtwoSimonGreenColour,
                         (math.floor(ScreenWidth / 1.35 - 100), math.floor(ScreenHeight / 6 + 50), 100, 50))
        pygame.draw.rect(win, PtwoSimonYellowColour,
                         (math.floor(ScreenWidth / 1.35 + 100), math.floor(ScreenHeight / 6 + 50), 100, 50))
        # Player Two
        pygame.draw.rect(win, PtwoBlueColour,
                         (math.floor(ScreenWidth / 1.35 + 25), math.floor(ScreenHeight / 1.5), 50, 25))
        pygame.draw.rect(win, PtwoRedColour,
                         (math.floor(ScreenWidth / 1.35 + 25), math.floor(ScreenHeight / 1.5 + 50), 50, 25))
        pygame.draw.rect(win, PtwoGreenColour,
                         (math.floor(ScreenWidth / 1.35 - 25), math.floor(ScreenHeight / 1.5 + 25), 50, 25))
        pygame.draw.rect(win, PtwoYellowColour,
                         (math.floor(ScreenWidth / 1.35 + 75), math.floor(ScreenHeight / 1.5 + 25), 50, 25))


        def PoneSimonColourUpdate():
            pygame.draw.rect(win, PoneSimonBlueColour,
                             (math.floor(ScreenWidth / 5), math.floor(ScreenHeight / 6), 100, 50))
            pygame.draw.rect(win, PoneSimonRedColour,
                             (math.floor(ScreenWidth / 5), math.floor(ScreenHeight / 6 + 100), 100, 50))
            pygame.draw.rect(win, PoneSimonGreenColour,
                             (math.floor(ScreenWidth / 5 - 100), math.floor(ScreenHeight / 6 + 50), 100, 50))
            pygame.draw.rect(win, PoneSimonYellowColour,
                             (math.floor(ScreenWidth / 5 + 100), math.floor(ScreenHeight / 6 + 50), 100, 50))
            pygame.draw.rect(win, PtwoSimonBlueColour,
                             (math.floor(ScreenWidth / 1.35), math.floor(ScreenHeight / 6), 100, 50))
            pygame.draw.rect(win, PtwoSimonRedColour,
                             (math.floor(ScreenWidth / 1.35), math.floor(ScreenHeight / 6 + 100), 100, 50))
            pygame.draw.rect(win, PtwoSimonGreenColour,
                             (math.floor(ScreenWidth / 1.35 - 100), math.floor(ScreenHeight / 6 + 50), 100, 50))
            pygame.draw.rect(win, PtwoSimonYellowColour,
                             (math.floor(ScreenWidth / 1.35 + 100), math.floor(ScreenHeight / 6 + 50), 100, 50))
            pygame.display.update()


        if CheckOne:
            for x in range(0, len(PoneList) + 1):
                if len(PoneList) == len(PoneSimonList):
                    if PoneList == PoneSimonList:
                        PoneReady = True
                for i in range(len(PoneList)):
                    if not PoneList[i] == PoneSimonList[i]:
                        PoneReady = False
                        GameStarted = False
                        PoneLose = True
            CheckOne = False

        if CheckTwo:
            for x in range(0, len(PtwoList) + 1):
                if len(PtwoList) == len(PtwoSimonList):
                    if PtwoList == PtwoSimonList:
                        PtwoReady = True
                for i in range(len(PtwoList)):
                    if not PtwoList[i] == PtwoSimonList[i]:
                        PtwoReady = False
                        GameStarted = False
                        PtwoLose = True
            CheckTwo = False

        if GameStarted and not PoneLose and not PtwoLose:
            if CountDown:
                if CountDownAmount == 1:
                    pygame.draw.rect(win, White,
                                     (math.floor(ScreenWidth / 2 - 50), math.floor(ScreenHeight / 3), 100, 100))
                    win.blit(Img1, (ScreenWidth / 2 - 50, ScreenHeight / 3))
                    CountDownAmount = 4
                    CountDown = False
                if CountDownAmount == 2:
                    pygame.draw.rect(win, White,
                                     (math.floor(ScreenWidth / 2 - 50), math.floor(ScreenHeight / 3), 100, 100))
                    win.blit(Img2, (ScreenWidth / 2 - 50, ScreenHeight / 3))
                if CountDownAmount == 3:
                    pygame.draw.rect(win, White,
                                     (math.floor(ScreenWidth / 2 - 50), math.floor(ScreenHeight / 3), 100, 100))
                    win.blit(Img3, (ScreenWidth / 2 - 50, ScreenHeight / 3))
                CountDownAmount -= 1
                pygame.display.update()
                pygame.time.delay(500)
                PoneSimonList = []  # Reset de list van PlayerOneSimon
                PtwoSimonList = []  # Reset de list van PlayerTwoSimon
                PoneList = []  # Reset de list van PlayerOne
                PtwoList = []  # Reset de list van PlayerTwo
            else:  # Als het spel is begonnen gaat de volgende code runnen
                if PoneReady and PtwoReady:
                    # Reset de kleuren van de player na elke beurt
                    PoneBlueColour, PoneGreenColour, PoneRedColour, PoneYellowColour = BluePlaceHolder, GreenPlaceHolder, RedPlaceHolder, YellowPlaceHolder
                    PtwoBlueColour, PtwoGreenColour, PtwoRedColour, PtwoYellowColour = BluePlaceHolder, GreenPlaceHolder, RedPlaceHolder, YellowPlaceHolder

                    pygame.draw.rect(win, PoneBlueColour,
                                     (math.floor(ScreenWidth / 5 + 25), math.floor(ScreenHeight / 1.5), 50, 25))
                    pygame.draw.rect(win, PoneRedColour,
                                     (math.floor(ScreenWidth / 5 + 25), math.floor(ScreenHeight / 1.5 + 50), 50, 25))
                    pygame.draw.rect(win, PoneGreenColour,
                                     (math.floor(ScreenWidth / 5 - 25), math.floor(ScreenHeight / 1.5 + 25), 50, 25))
                    pygame.draw.rect(win, PoneYellowColour,
                                     (math.floor(ScreenWidth / 5 + 75), math.floor(ScreenHeight / 1.5 + 25), 50, 25))
                    pygame.display.update()
                    if len(PoneList) == len(PoneSimonList):
                        randomInt = random.randint(0, 3)
                        randomIntTwo = random.randint(0, 3)
                        PoneSimonList.append(ColourList[randomInt])
                        PtwoSimonList.append(ColourList[randomIntTwo])
                        for (x, y) in zip(PoneSimonList,
                                          PtwoSimonList):  # Hiermee kunnen er twee lists in een for loop worden gebruikt
                            pygame.draw.rect(win, White,
                                             (math.floor(ScreenWidth / 5), math.floor(ScreenHeight / 6 + 50), 100, 50))
                            pygame.draw.rect(win, White, (
                                math.floor(ScreenWidth / 1.35), math.floor(ScreenHeight / 6 + 50), 100, 50))
                            if x == "Blue":
                                PoneSimonBlueColour = Blue
                            if x == "Green":
                                PoneSimonGreenColour = Green
                            if x == "Red":
                                PoneSimonRedColour = Red
                            if x == "Yellow":
                                PoneSimonYellowColour = Yellow

                            if y == "Blue":
                                PtwoSimonBlueColour = Blue
                            if y == "Green":
                                PtwoSimonGreenColour = Green
                            if y == "Red":
                                PtwoSimonRedColour = Red
                            if y == "Yellow":
                                PtwoSimonYellowColour = Yellow
                            PoneSimonColourUpdate()
                            pygame.time.delay(750 - (5 * int(len(PoneSimonList))))
                            PoneSimonBlueColour = BluePlaceHolder
                            PoneSimonGreenColour = GreenPlaceHolder
                            PoneSimonRedColour = RedPlaceHolder
                            PoneSimonYellowColour = YellowPlaceHolder
                            PtwoSimonBlueColour = BluePlaceHolder
                            PtwoSimonGreenColour = GreenPlaceHolder
                            PtwoSimonRedColour = RedPlaceHolder
                            PtwoSimonYellowColour = YellowPlaceHolder
                            PoneSimonColourUpdate()
                            pygame.time.delay(250 - (5 * int(len(PoneSimonList))))

                    else:
                        PoneReady, PtwoReady = False, False
                        PoneList = []  # Reset de list van PlayerOne na elke beurt
                        PtwoList = []

                else:
                    if not PoneReady:
                        pygame.draw.rect(win, White, (
                            math.floor(ScreenWidth / 5 + 25), math.floor(ScreenHeight / 1.5 + 25), 50, 25))
                    if not PtwoReady:
                        pygame.draw.rect(win, White, (
                            math.floor(ScreenWidth / 1.35 + 25), math.floor(ScreenHeight / 1.5 + 25), 50, 25))
                    if Key[pygame.K_w]:
                        PoneBlueColour = Blue
                    else:
                        PoneBlueColour = BluePlaceHolder
                    if Key[pygame.K_a]:
                        PoneGreenColour = Green
                    else:
                        PoneGreenColour = GreenPlaceHolder
                    if Key[pygame.K_s]:
                        PoneRedColour = Red
                    else:
                        PoneRedColour = RedPlaceHolder
                    if Key[pygame.K_d]:
                        PoneYellowColour = Yellow
                    else:
                        PoneYellowColour = YellowPlaceHolder

                    if Key[pygame.K_UP]:
                        PtwoBlueColour = Blue
                    else:
                        PtwoBlueColour = BluePlaceHolder
                    if Key[pygame.K_LEFT]:
                        PtwoGreenColour = Green
                    else:
                        PtwoGreenColour = GreenPlaceHolder
                    if Key[pygame.K_DOWN]:
                        PtwoRedColour = Red
                    else:
                        PtwoRedColour = RedPlaceHolder
                    if Key[pygame.K_RIGHT]:
                        PtwoYellowColour = Yellow
                    else:
                        PtwoYellowColour = YellowPlaceHolder
        if not GameStarted and not PoneLose and not PtwoLose:
            PoneSimonList = []  # Reset de list van PlayerOneSimon
            PtwoSimonList = []  # Reset de list van PlayerTwoSimon
            PoneList = []  # Reset de list van PlayerOne
            PtwoList = []  # Reset de list van PlayerTwo
            # win.blit(SpaceToStartTxt, SpaceToStartTxt.get_rect(center=(ScreenWidth / 2, ScreenHeight / 2)))
        if not GameStarted and PoneLose:
            PoneSimonList = []
            PtwoSimonList = []
            PoneList = []
            PtwoList = []
            if not ScoreDebounce:
                ScorePtwo += 1  # Geef de tegenstander een punt
                ScoreDebounce = True
            LoseTxtFunc("Hamudt")
            win.blit(LoseTxt, LoseTxt.get_rect(center=(ScreenWidth / 2, ScreenHeight / 16)))
            win.blit(SpaceRestartTxt, SpaceRestartTxt.get_rect(center=(ScreenWidth / 2, ScreenHeight / 1.2)))
        if not GameStarted and PtwoLose:
            PoneSimonList = []
            PtwoSimonList = []
            PoneList = []
            PtwoList = []
            if not ScoreDebounce:
                ScorePone += 1  # Geef de tegenstander een punt
                ScoreDebounce = True
            LoseTxtFunc("Eduardo")
            win.blit(LoseTxt, LoseTxt.get_rect(center=(ScreenWidth / 2, ScreenHeight / 16)))
            win.blit(SpaceRestartTxt, SpaceRestartTxt.get_rect(center=(ScreenWidth / 2, ScreenHeight / 1.2)))
#  -------------------------------------Game 2 --------------------------------
    if Game2:
        win.fill(Blue)
        pygame.draw.rect(win, (44, 200, 44), (0, 150, ScreenWidth, ScreenHeight))  # Gras
        pygame.draw.rect(win, (115, 44, 0), (0, 160, ScreenWidth, ScreenHeight))  # Eerste aardlaag
        pygame.draw.rect(win, (160, 88, 44), (0, 250, ScreenWidth, ScreenHeight))  # Tweede aardlaag
        pygame.draw.rect(win, (200, 120, 80), (0, 350, ScreenWidth, ScreenHeight))  # Derde aardlaag
        pygame.draw.rect(win, (255, 180, 105), (0, 450, ScreenWidth, ScreenHeight))  # Zand
        pygame.draw.rect(win, (163, 159, 155), (0, 600, ScreenWidth, ScreenHeight))  # Steen

        pygame.display.set_caption(
            "Arda en Nieks Reetro(met een C) Arkade: Gunter")  # Zet de caption met het huidige spel
        PoneBGC, PtwoBGC = Gray, PoneBGC  # Achtergrond voor de score names
        win.blit(ScorePoneTxt,
                 ScorePoneTxt.get_rect(center=(ScreenWidth / 16, ScreenHeight / 16)))  # Draw de score van Hamudt
        win.blit(ScorePtwoTxt,
                 ScorePtwoTxt.get_rect(center=(ScreenWidth / 1.1, ScreenHeight / 16)))  # Draw de score van Eduardo

        pygame.draw.rect(win, Red, (275, 500 - PoneStep * 20, 50, 50))  # Dit is Hamudt
        pygame.draw.rect(win, Blue, (875, 500 - PtwoStep * 20, 50, 50))  # Dit is Eduardo

        # Volgorde:
        # background
        # lijn voor onderscheid
        # Gray bar/area voor de players
        # Rode Bar
        # Ultiem Rood
        # Groene Bar
        # Gele Bar
        # Pointer

        Barz = (255, 140, 140)
        pygame.draw.rect(win, Barz, (
        ScreenWidth * (1 / 8), ScreenHeight * (7 / 8), ScreenWidth * (1 / 4), 20))  # Outline voor Hamudt
        pygame.draw.rect(win, Barz, (
        ScreenWidth * (5 / 8), ScreenHeight * (7 / 8), ScreenWidth * (1 / 4), 20))  # Outline voor Eduardo

        if CountDown:
            if CountDownAmount == 1:
                pygame.draw.rect(win, White, (math.floor(ScreenWidth / 2 - 50), math.floor(ScreenHeight / 3), 100, 100))
                win.blit(Img1, (ScreenWidth / 2 - 50, ScreenHeight / 3))
                CountDownAmount = 4
                CountDown = False
            if CountDownAmount == 2:
                pygame.draw.rect(win, White, (math.floor(ScreenWidth / 2 - 50), math.floor(ScreenHeight / 3), 100, 100))
                win.blit(Img2, (ScreenWidth / 2 - 50, ScreenHeight / 3))
            if CountDownAmount == 3:
                pygame.draw.rect(win, White, (math.floor(ScreenWidth / 2 - 50), math.floor(ScreenHeight / 3), 100, 100))
                win.blit(Img3, (ScreenWidth / 2 - 50, ScreenHeight / 3))
            CountDownAmount -= 1
            pygame.display.update()
            pygame.time.delay(500)
        else:

            if GameStarted and not PoneWin and not PtwoWin:
                if PonePoint.rect.x > ScreenWidth * (3 / 8) - 10:  # Heen en weer gaan van de PonePointer
                    PonePointerSpeed *= -1
                elif PonePoint.rect.x < ScreenWidth * (1 / 8) + 5:
                    PonePointerSpeed *= -1
                if PtwoPoint.rect.x > ScreenWidth * (7 / 8) - 10:  # Heen en weer gaan van de PtwoPointer
                    PtwoPointerSpeed *= -1
                elif PtwoPoint.rect.x < ScreenWidth * (5 / 8) + 5:
                    PtwoPointerSpeed *= -1

                """
                20 stappen
                elk stap is een deel van het scherm/pixels
                Groen = 1 stap
                Rood = -2 stap
                Roze = -1 stap
                Ultiem Rood = -5
                """

                PonePoint.move(PonePointerSpeed)  # Beweeg de PonePointer
                PtwoPoint.move(PtwoPointerSpeed)  # Beweeg de PtwoPointer

                PoneRedRandSize = math.floor((ScreenWidth * (1 / 10)) - (4 * PoneStep))
                PoneRedRandPos = random.randint(0, ScreenWidth * (2 / 8) - PoneRedRandSize)

                PtwoRedRandSize = math.floor((ScreenWidth * (1 / 10)) - (4 * PtwoStep))
                PtwoRedRandPos = random.randint(0, ScreenWidth * (2 / 8) - PtwoRedRandSize) + ScreenWidth * (4 / 8)

                if PoneStep >= 20:
                    GameStarted = False
                    PoneWin = True
                elif PtwoStep >= 20:
                    GameStarted = False
                    PtwoWin = True

                if not PoneRedBarDrawed:  # Een debounce om het maar een keer een random positie en size te geven
                    PoneRedBar.SetSize(PoneRedRandSize, PoneRedRandPos)
                    PoneRedBarDrawed = True
                if not PtwoRedBarDrawed:
                    PtwoRedBar.SetSize(PtwoRedRandSize, PtwoRedRandPos)
                    PtwoRedBarDrawed = True

                if not PoneGreenBarDrawed:
                    PoneGreenBar.SetSize(PoneRedRandPos, 1)
                    PoneGreenBarDrawed = True
                if not PtwoGreenBarDrawed:
                    PtwoGreenBar.SetSize(PtwoRedRandPos, 2)
                    PtwoGreenBarDrawed = True

                win.blit(PoneRedBar.image, PoneRedBar.rect)  # Draw de RedBar voor Hamudt
                win.blit(PoneGreenBar.image, PoneGreenBar.rect)  # Draw de GreenBar voor Hamudt
                win.blit(PtwoRedBar.image, PtwoRedBar.rect)  # Draw de RedBar voor Hamudt
                win.blit(PtwoGreenBar.image, PtwoGreenBar.rect)  # Draw de GreenBar voor Hamudt

                win.blit(PonePoint.image, PonePoint.rect)  # Draw de Pointer voor Hamudt
                win.blit(PtwoPoint.image, PtwoPoint.rect)  # Draw de Pointer voor Eduardo

            elif PoneWin:
                if not ScoreDebounce:
                    ScorePone += 1
                    ScoreDebounce = True
                win.blit(PoneWinTxt, PoneWinTxt.get_rect(center=(ScreenWidth / 2, ScreenHeight / 16)))
            elif PtwoWin:
                if not ScoreDebounce:
                    ScorePtwo += 1
                    ScoreDebounce = True
                win.blit(PtwoWinTxt, PtwoWinTxt.get_rect(center=(ScreenWidth / 2, ScreenHeight / 16)))
#  ----------------------------------------Game 3 -------------------------------------
    if Game3:
        pygame.display.set_caption("Arda en Nieks Reetro(met een C) Arkade: Pong")
        # variables bars
        movespeedP2 = 10
        movespeedP1 = 10
        Player1score = 0
        Player2score = 0


        def TruOrFal(list):
            i = random.randint(1, 2)
            if i > 1:
                i = True
            else:
                i = False
            list.append(i)


        # makes new horizontal portals
        def new_V_portals():
            global portalC
            global portalD
            global teleportC
            global teleportD
            global Vportals
            global Vteleported
            T = random.randint(0, ScreenHeight - 200)
            U = random.randint(int(ScreenWidth / 10 + 20), int(ScreenWidth / 10) * 9 - 20)
            portalC = Portal(U, T, (0, 255, 0), 10, 200)
            teleportC = [U, T + 100]
            E = random.randint(0, ScreenHeight - 200)
            O = random.randint(int(ScreenWidth / 10 + 20), int(ScreenWidth / 10) * 9 - 20)
            portalD = Portal(O, E, (0, 0, 255), 10, 200)
            teleportD = [O, E + 100]
            Vportals = True
            Vteleported = False


        def new_H_portals():
            global portalA
            global portalB
            global teleportA
            global teleportB
            global Hportals
            global Hteleported
            global isbottomA
            global isbottomB
            # decides if its on the bottom or top
            i = random.randint(1, 2)
            if i == 1:
                T = ScreenHeight - 10
                isbottomA = 1
            else:
                T = 0
                isbottomA = 0
            U = random.randint(int(ScreenWidth / 10), int(ScreenWidth / 10) * 9 - 200)
            portalA = Portal(U, T, (0, 0, 255), 200, 10)
            teleportA = [U + 100, T]
            R = random.randint(1, 2)
            if R == 1:
                E = ScreenHeight - 10
                isbottomB = 1
            else:
                E = 0
                isbottomB = 0
            O = random.randint(int(ScreenWidth / 10), int(ScreenWidth / 10) * 9 - 200)
            portalB = Portal(O, E, (255, 150, 0), 200, 10)
            teleportB = [O + 100, E]
            Hportals = True
            Hteleported = False


        def restart():
            global Player1
            global Player2
            global balllist
            global yspeedlist
            global xspeedlist
            global Leftballlist
            global Upballlist
            global Hportals
            global Vportals
            global portalA
            global portalB
            global portalC
            global portalD
            global Hteleported
            global Vteleported
            global i
            global secs
            global powerdUp
            Player1 = PongBar((ScreenWidth / 10), 200)
            Player2 = PongBar(((ScreenWidth / 10) * 9), 200)
            ball0 = Ball(ScreenWidth / 2, random.randint(1, ScreenHeight - 21), 20)
            balllist = [ball0]
            yspeedlist = [10]
            xspeedlist = [10]
            Leftballlist = [False]
            Upballlist = [True]
            TruOrFal(Leftballlist)
            TruOrFal(Upballlist)
            if Hportals:
                portalA.reset()
                portalB.reset()
                Hportals = False
            if Vportals:
                portalC.reset()
                portalD.reset()
                Vportals = False
            Hteleported = False
            Vteleported = False
            i = 0
            secs = 0
            powerdUp = False


        def addball():
            global i
            i += 1
            size = random.randint(1, 60)
            ball = Ball((ScreenWidth / 2), random.randint(1, ScreenHeight - (size + 1)), size)
            TruOrFal(Leftballlist)
            TruOrFal(Upballlist)
            if Upballlist[i]:
                yspeed = random.randint(-20, -1)
            else:
                yspeed = random.randint(1, 20)
            if Leftballlist[i]:
                xspeed = random.randint(-20, -1)
            else:
                xspeed = random.randint(1, 20)
            yspeedlist.append(yspeed)
            xspeedlist.append(xspeed)
            balllist.append(ball)
        win.blit(Player2.image, Player2.rect)
        win.blit(Player1.image, Player1.rect)
        if not GameStarted:
            win.blit(Stext, Stextrect)
        if CountDown:
            if CountDownAmount == 1:
                pygame.draw.rect(win, White, (math.floor(ScreenWidth / 2 - 50), math.floor(ScreenHeight / 3), 100, 100))
                win.blit(Img1, (ScreenWidth / 2 - 50, ScreenHeight / 3))
                CountDownAmount = 4
                CountDown = False
            if CountDownAmount == 2:
                pygame.draw.rect(win, White, (math.floor(ScreenWidth / 2 - 50), math.floor(ScreenHeight / 3), 100, 100))
                win.blit(Img2, (ScreenWidth / 2 - 50, ScreenHeight / 3))
            if CountDownAmount == 3:
                pygame.draw.rect(win, White, (math.floor(ScreenWidth / 2 - 50), math.floor(ScreenHeight / 3), 100, 100))
                win.blit(Img3, (ScreenWidth / 2 - 50, ScreenHeight / 3))
            CountDownAmount -= 1
            pygame.display.update()
            pygame.time.delay(500)

        else:
            if GameStarted:
                # DA GAME
                win.fill((0, 0, 0))
                PoneBGC, PtwoBGC = Black, PoneBGC  # Achtergrond voor de score names
                win.blit(ScorePoneTxt,
                         ScorePoneTxt.get_rect(center=(ScreenWidth / 16, ScreenHeight / 16)))  # Draw de score van Hamudt
                win.blit(ScorePtwoTxt,
                         ScorePtwoTxt.get_rect(center=(ScreenWidth / 1.1, ScreenHeight / 16)))  # Draw de score van Eduardo

                # controls
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] and not Player1.rect.y < 0:
                    Player1.move(movespeedP1)
                if keys[pygame.K_s] and not Player1.rect.y > (ScreenHeight - 200):
                    Player1.move(-movespeedP1)
                if keys[pygame.K_UP] and not Player2.rect.y < 0:
                    Player2.move(movespeedP2)
                if keys[pygame.K_DOWN] and not Player2.rect.y > (ScreenHeight - 200):
                    Player2.move(-movespeedP2)

                # ball
                for u in range(len(balllist)):
                    if balllist[u].rect.colliderect(barrierUp) or balllist[u].rect.colliderect(barrierDown):
                        yspeedlist[u] *= -1
                    if balllist[u].rect.colliderect(Player1) and Leftballlist[u]:
                        xspeedlist[u] *= -1
                        Leftballlist[u] = False
                    if balllist[u].rect.colliderect(Player2) and not Leftballlist[u]:
                        xspeedlist[u] *= -1
                        Leftballlist[u] = True
                    if balllist[u].rect.x < 0:
                        ScorePtwo += 1
                        time.sleep(0.5)
                        restart()
                        break
                    if balllist[u].rect.x > ScreenWidth - balllist[u].rect.width:
                        ScorePone += 1
                        time.sleep(0.5)
                        restart()
                        break
                    if Hportals:
                        if balllist[u].rect.colliderect(portalA) and not Hteleported:
                            balllist[u].teleport(teleportB[0], teleportB[1] + balllist[u].rect.height * isbottomB)
                            Hportals = False
                            Hteleported = True
                            portalA.reset()
                            portalB.reset()
                        if balllist[u].rect.colliderect(portalB) and not Hteleported:
                            balllist[u].teleport(teleportA[0], teleportA[1] + balllist[u].rect.height * isbottomA)
                            Hportals = False
                            Hteleported = True
                            portalB.reset()
                            portalA.reset()
                    if Vportals:
                        if balllist[u].rect.colliderect(portalC) and not Vteleported:
                            balllist[u].teleport(teleportD[0], teleportD[1])
                            Vportals = False
                            Vteleported = True
                            portalC.reset()
                            portalD.reset()
                        if balllist[u].rect.colliderect(portalD) and not Vteleported:
                            balllist[u].teleport(teleportC[0], teleportC[1])
                            Vportals = False
                            Vteleported = True
                            portalD.reset()
                            portalC.reset()
                    if powerdUp:
                        if balllist[u].rect.colliderect(power):
                            power.rect.x = - 200
                            power.rect.y = - 200
                            P = random.randint(1, 3)
                            if P == 1:
                                addball()
                            elif P == 2:
                                new_H_portals()
                            else:
                                new_V_portals()
                            powerdUp = False
                    balllist[u].move(xspeedlist[u], yspeedlist[u])
                    win.blit(balllist[u].image, balllist[u].rect)
                # Powerups
                secs += 1
                if secs == 33:
                    if not powerdUp:
                        G = random.randint(1, 4)
                        if G == 4:
                            x = random.randint((ScreenWidth / 10 + 60), (ScreenWidth / 10) * 9 - 60)
                            y = random.randint(10, ScreenHeight - 70)
                            power = powerup(x, y)
                            powerdUp = True
                    secs = 0
                # draw
                if powerdUp:
                    win.blit(power.image, power.rect)
                if Vportals:
                    win.blit(portalC.image, portalC.rect)
                    win.blit(portalD.image, portalD.rect)
                if Hportals:
                    win.blit(portalA.image, portalA.rect)
                    win.blit(portalB.image, portalB.rect)
                win.blit(Player2.image, Player2.rect)
                win.blit(Player1.image, Player1.rect)
            pygame.display.update()

    #     --------------------------------------- GAME 4 ----------------------------------------

    if Game4:
        win.fill((59, 186, 24))
        pygame.display.set_caption("Arda en Nieks Reetro(met een C) Arkade: Henk en Piet 2.0")
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
        PoneBGC, PtwoBGC = White, PoneBGC  # Achtergrond voor de score names
        win.blit(ScorePoneTxt,
                 ScorePoneTxt.get_rect(center=(ScreenWidth / 16, ScreenHeight / 16)))  # Draw de score van Hamudt
        win.blit(ScorePtwoTxt,
                 ScorePtwoTxt.get_rect(center=(ScreenWidth / 1.1, ScreenHeight / 16)))  # Draw de score van Eduardo
        if not GameStarted:
            win.blit(Stext, Stextrect)
        pygame.display.update()
        if CountDown:
            if CountDownAmount == 1:
                pygame.draw.rect(win, White, (math.floor(ScreenWidth / 2 - 50), math.floor(ScreenHeight / 3), 100, 100))
                win.blit(Img1, (ScreenWidth / 2 - 50, ScreenHeight / 3))
                CountDownAmount = 4
                CountDown = False
            if CountDownAmount == 2:
                pygame.draw.rect(win, White, (math.floor(ScreenWidth / 2 - 50), math.floor(ScreenHeight / 3), 100, 100))
                win.blit(Img2, (ScreenWidth / 2 - 50, ScreenHeight / 3))
            if CountDownAmount == 3:
                pygame.draw.rect(win, White, (math.floor(ScreenWidth / 2 - 50), math.floor(ScreenHeight / 3), 100, 100))
                win.blit(Img3, (ScreenWidth / 2 - 50, ScreenHeight / 3))
            CountDownAmount -= 1
            pygame.display.update()
            pygame.time.delay(500)

        else:

            if GameStarted:
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
                    # player 2 movement
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
                    henk.move(flowdirection1 + 35 * F1, Universalspeed)
                if henk.rect.colliderect(bridge2):
                    henk.move(flowdirection + 35 * F, Universalspeed)

                # rivermovemet and directions
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
                # henk gets hit
                if henk.rect.colliderect(deathbarrier) or henk.rect.colliderect(
                        deathbarrier1) or henk.rect.y >= 650 or henk.rect.colliderect(Bullet):
                    HenkLife = False
                    Pietwins = True
                # piet gets hit
                if piet.rect.colliderect(KillerFish):
                    PietLife = False
                    Henkwins = True
                # game over
                if not HenkLife or not PietLife:
                    gameover = True
                if gameover:
                    Universalspeed = 0

                    if Henkwins:
                        piet.move(1000)
                    else:
                        henk.move(10000, 10000)
                    henkreset()
                    GameStarted = False


# ------------------------------------------------ Game 5 ------------------------------------
    if Game5:
        win.fill((10, 10, 255))
        pygame.display.set_caption("Arda en Nieks Reetro(met een C) Arkade: Sumo")
        Sumostartkey = pygame.key.get_pressed()  # Power push
        if Sgamestart and Splayer1live and Splayer2live:
            Stime += 1
            Srandom = random.randint(10, 50)
            if Stime == 33:
                Sumorantimer += Srandom
                Stime = 0
            if Sumorantimer >= 100:
                S1 += 1
                if S1 == 1:
                    Srandomdirection = random.randint(1, 3)
                if Srandomdirection == 1:
                    Skeyassigned = "down"
                    win.blit(Sdownarrow, (575, 200))
                if Srandomdirection == 2:
                    Skeyassigned = "left"
                    win.blit(Sleftarrow, (566, 200))
                if Srandomdirection == 3:
                    Skeyassigned = "right"
                    win.blit(Srightarrow, (567, 200))
                if Sumostartkey[pygame.K_s] and Skeyassigned == "down":
                    Splayer2x += 80
                    Splayer1x += 80
                    Splayer2rect.move_ip(80, 0)
                    Splayer1rect.move_ip(80, 0)
                    Sumorantimer = 0
                    Sp1F = 0
                    Sp2F = 0
                    S1 = 0
                if Sp1F < 1:
                    if Skeyassigned == "down" and Sumostartkey[pygame.K_a] or Sumostartkey[pygame.K_d]:
                        Splayer1x -= 60
                        Splayer1rect.move_ip(-60, 0)
                        Sp1F += 1
                if Sumostartkey[pygame.K_DOWN] and Skeyassigned == "down":
                    Splayer2x -= 80
                    Splayer1x -= 80
                    Splayer2rect.move_ip(-80, 0)
                    Splayer1rect.move_ip(-80, 0)
                    Sumorantimer = 0
                    S1 = 0
                    Sp1F = 0
                    Sp2F = 0
                if Sp2F < 1:
                    if Skeyassigned == "down" and Sumostartkey[pygame.K_LEFT] or Sumostartkey[pygame.K_RIGHT]:
                        Splayer2x += 60
                        Splayer2rect.move_ip(60, 0)
                        Sp2F += 1
                if Sumostartkey[pygame.K_a] and Skeyassigned == "left":
                    Splayer2x += 80
                    Splayer1x += 80
                    Splayer2rect.move_ip(80, 0)
                    Splayer1rect.move_ip(80, 0)
                    Sumorantimer = 0
                    S1 = 0
                    Sp1F = 0
                    Sp2F = 0
                if Sp1F < 1:
                    if Skeyassigned == "left" and Sumostartkey[pygame.K_s] or Sumostartkey[pygame.K_d]:
                        Splayer1x -= 60
                        Splayer1rect.move_ip(-60, 0)
                        Sp1F += 1
                if Sumostartkey[pygame.K_LEFT] and Skeyassigned == "left":
                    Splayer2x -= 80
                    Splayer1x -= 80
                    Splayer2rect.move_ip(-80, 0)
                    Splayer1rect.move_ip(-80, 0)
                    Sumorantimer = 0
                    S1 = 0
                    Sp1F = 0
                    Sp2F = 0
                if Sp2F < 1:
                    if Skeyassigned == "left" and Sumostartkey[pygame.K_DOWN] or Sumostartkey[pygame.K_RIGHT]:
                        Splayer2x += 60
                        Splayer2rect.move_ip(60, 0)
                        Sp2F += 1
                if Sumostartkey[pygame.K_d] and Skeyassigned == "right":
                    Splayer2x += 80
                    Splayer1x += 80
                    Splayer2rect.move_ip(60, 0)
                    Splayer1rect.move_ip(60, 0)
                    Sumorantimer = 0
                    S1 = 0
                    Sp1F = 0
                    Sp2F = 0
                if Sp1F < 1:
                    if Skeyassigned == "right" and Sumostartkey[pygame.K_a] or Sumostartkey[pygame.K_s]:
                        Splayer1x -= 60
                        Splayer1rect.move_ip(-60, 0)
                        Sp1F += 1
                if Sumostartkey[pygame.K_RIGHT] and Skeyassigned == "right":
                    Splayer2x -= 80
                    Splayer1x -= 80
                    Splayer2rect.move_ip(-80, 0)
                    Splayer1rect.move_ip(-80, 0)
                    Sumorantimer = 0
                    S1 = 0
                    Sp1F = 0
                    Sp2F = 0
                if Sp2F < 1:
                    if Skeyassigned == "right" and Sumostartkey[pygame.K_DOWN] or Sumostartkey[pygame.K_LEFT]:
                        Splayer2x += 60
                        Splayer2rect.move_ip(60, 0)
                        Sp2F += 1

        # Start timer
        if not Sgamestart:
            if not Startsumotimer:
                win.blit(Stext, Stextrect)
            if Sumostartkey[pygame.K_SPACE]:
                Startsumotimer = True
            if Startsumotimer:
                Sgamestarttimer += 1
                if 0 < Sgamestarttimer < 15:
                    win.blit(Sload3, (550, 200))
                if 15 < Sgamestarttimer < 30:
                    win.blit(Sload2, (550, 200))
                if 30 < Sgamestarttimer <= 45:
                    win.blit(Sload1, (550, 200))
            if Sgamestarttimer > 45:
                Sgamestarttimer = 0
                Startsumotimer = False
                Sgamestart = True
        pygame.draw.rect(win, (161, 96, 6), (150, 375, 900, 100))
        pygame.draw.rect(win, (161, 96, 6), (525, 375, 150, 1000))
        if Splayer2rect.colliderect(deathbarrect):
            Splayer2live = False
            win.blit(Stextwin1, Stextrectwin1)
            SS += 1
            if not gavescoreScoreplayer1:
                ScorePone += 1
                gavescoreScoreplayer1 = True

        else:
            win.blit(SPlayer2image, (Splayer2x, Splayer2y))
        if Splayer1rect.colliderect(deathbarrect1):
            Splayer1live = False
            win.blit(Stextwin2, Stextrectwin2)
            SS += 1
            if not gavescoreScoreplayer2:
                ScorePtwo += 1
                gavescoreScoreplayer2 = True
        if SS == 33:
            Sumoreset()
        else:
            win.blit(SPlayer1image, (Splayer1x, Splayer1y))

        PoneBGC, PtwoBGC = (0, 0, 255), PoneBGC  # Achtergrond voor de score names
        win.blit(ScorePoneTxt,
                 ScorePoneTxt.get_rect(center=(ScreenWidth / 16, ScreenHeight / 16)))  # Draw de score van Hamudt
        win.blit(ScorePtwoTxt,
                 ScorePtwoTxt.get_rect(center=(ScreenWidth / 1.1, ScreenHeight / 16)))  # Draw de score van Eduardo
        pygame.display.update()

    if LoadingEnd:
        if not LoadingTime == 0:
            pygame.draw.rect(win, Black, (0, 0, ScreenWidth, math.floor(ScreenHeight * (LoadingTime / LoadingStep))))
            pygame.display.update()
            LoadingTime -= 1
            if LoadingTime == 0:
                LoadingEnd = False

    pygame.display.update()
pygame.quit()
