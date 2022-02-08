import pygame
import random
import math

pygame.init()
pygame.mixer.init()
oofSound = pygame.mixer.Sound("roblox-death-sound_1.mp3")
hitSound = pygame.mixer.Sound("hitmarker_2.mp3")
hitSound.set_volume(0.1)

ScreenWidth = 1200  # De breedte van het scherm in pixels
ScreenHeight = 700  # De hoogte van het scherm in pixels
win = pygame.display.set_mode((ScreenWidth, ScreenHeight))  # Breedte en Hoogte van het scherm in aantal pixels
pygame.display.set_caption("Arda en Nieks reetro Arkade")   # De caption van de window

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
Red = (255, 0, 60)
Blue = (58, 134, 255)
Pink = (250, 172, 215)
White = (255, 255, 255)
Yellow = (255, 225, 0)
Green = (136, 255, 38)
# PtwoColour = (0, 255, 242)

# De volgende Variables zijn de bool values voor de games
Game1 = False       # Simon Says
Game2 = False       # Sumo
Game3 = False
Game4 = False
Game5 = False
Game6 = False

# De volgende Variables zijn veelgebruikte Values
Img1 = pygame.transform.scale(pygame.image.load("1.png"), (100, 100))
Img2 = pygame.transform.scale(pygame.image.load("2.png"), (100, 100))
Img3 = pygame.transform.scale(pygame.image.load("3.png"), (100, 100))
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
Game1Rect = pygame.Rect(100, 150, 100, 50)
PoneBGC = Black
PtwoBGC = Black

# De volgende Variables zijn voor Game1
GameStarted = False
ColourList = ["Blue", "Green", "Red", "Yellow"]
PoneSimonList = []
PtwoSimonList = []
PoneList = []
PtwoList = []
CountDown = False
CountDownAmount = 3
SimonTurn = True
SimonTimer = 0

BluePlaceHolder = (21, 47, 89)
GreenPlaceHolder = (35, 79, 0)
RedPlaceHolder = (87, 0, 20)
YellowPlaceHolder = (87, 76, 0)

PoneSimonBlueColour = BluePlaceHolder
PoneSimonGreenColour = GreenPlaceHolder
PoneSimonRedColour = RedPlaceHolder
PoneSimonYellowColour = YellowPlaceHolder

PoneBlueColour = BluePlaceHolder
PoneGreenColour = GreenPlaceHolder
PoneRedColour = RedPlaceHolder
PoneYellowColour = YellowPlaceHolder


# De volgende Variables zijn voor Game2
SumoH = pygame.image.load("SumoH.png")
SumoE = pygame.image.load("SumoE.png")


while IsRunning:
    pygame.time.delay(33)  # Framerate in 1/milliseconden

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # if statement om de game af te sluiten met de rode kruis
            IsRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # if statement for de hit sound
            hitSound.play()
        MouseRect.move_ip(-MouseX, -MouseY)
        MouseX = pygame.mouse.get_pos()[0]
        MouseY = pygame.mouse.get_pos()[1]
        MouseRect.move_ip(MouseX, MouseY)

        if Game1:
            if event.type == pygame.KEYUP:
                if not SimonTurn:
                    if not len(PoneList) >= len(PoneSimonList):
                        if event.key == pygame.K_w:
                            PoneList.append(ColourList[0])
                            print(PoneList)
                        if event.key == pygame.K_a:
                            PoneList.append(ColourList[1])
                        if event.key == pygame.K_s:
                            PoneList.append(ColourList[2])
                        if event.key == pygame.K_d:
                            PoneList.append(ColourList[3])
                    else:
                        SimonTurn = True

                if event.key == pygame.K_UP:
                    PtwoList.append(ColourList[0])
                if event.key == pygame.K_LEFT:
                    PtwoList.append(ColourList[1])
                if event.key == pygame.K_DOWN:
                    PtwoList.append(ColourList[2])
                if event.key == pygame.K_RIGHT:
                    PtwoList.append(ColourList[3])

    def loading(val):
        for y in range(1, LoadingTime):
            pygame.draw.rect(win, Black, (0, 0, ScreenWidth, math.floor(ScreenHeight*(y/LoadingStep))))
            pygame.display.update()
            pygame.time.wait(33)
        pygame.draw.rect(win, Black, (0, 0, ScreenWidth, ScreenHeight))
        pygame.display.update()
        pygame.time.wait(250)
        val = True
        return val

    ScorePoneTxt = SmallFont.render("Hamudt: "+str(ScorePone), True, Red, PoneBGC)   # Update de score van Hamudt
    ScorePtwoTxt = SmallFont.render("Eduardo: "+str(ScorePtwo), True, Blue, PtwoBGC)  # Update de score van Eduardo

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
        LoadingTime = LoadingInt
        LoadingEnd = loading(LoadingEnd)

    if Key[pygame.K_SPACE]:
        GameStarted = True
        CountDown = True

    if Menu:
        win.fill(MainPurple)
        PoneBGC, PtwoBGC = White, White
        for x in range(1, 100):  # Deze for-loop zorgt voor een "Retro Scan Lines" effect
            pygame.draw.rect(win, Black, (0, (x * 9 - 4), ScreenWidth, 2))

        if Key[pygame.K_y]:
            ScorePone, ScorePtwo = 0, 0

        win.blit(ScorePoneTxt, ScorePoneTxt.get_rect(center=(ScreenWidth/16, ScreenHeight/16)))     # Draw de score van Hamudt
        win.blit(ScorePtwoTxt, ScorePtwoTxt.get_rect(center=(ScreenWidth/1.1, ScreenHeight / 16)))  # Draw de score van Eduardo
        win.blit(TitleTxt, TitleTxt.get_rect(center=(ScreenWidth / 2, ScreenHeight / 16)))

        Game1Icon = pygame.draw.rect(win, Black, (100, 150, 100, 50))

        if pygame.mouse.get_pressed()[0]:
            MouseX = pygame.mouse.get_pos()[0]
            MouseY = pygame.mouse.get_pos()[1]

            if MouseRect.colliderect(Game1Rect):
                Menu = False
                Game1 = True
                LoadingTime = LoadingInt
                LoadingEnd = loading(LoadingEnd)

    if Game1:
        win.fill(Gray)
        PoneBGC, PtwoBGC = Gray, Gray
        win.blit(ScorePoneTxt, ScorePoneTxt.get_rect(center=(ScreenWidth/16, ScreenHeight/16)))     # Draw de score van Hamudt
        win.blit(ScorePtwoTxt, ScorePtwoTxt.get_rect(center=(ScreenWidth/1.1, ScreenHeight / 16)))  # Draw de score van Eduardo

        pygame.draw.rect(win, White, (math.floor(ScreenWidth/2-10), 0, 10, ScreenHeight))       # Draw een witte lijn

        # Simon voor Player One
        pygame.draw.rect(win, PoneSimonBlueColour, (math.floor(ScreenWidth / 5), math.floor(ScreenHeight / 6), 100, 50))
        pygame.draw.rect(win, PoneSimonRedColour, (math.floor(ScreenWidth / 5), math.floor(ScreenHeight / 6 + 100), 100, 50))
        pygame.draw.rect(win, PoneSimonGreenColour, (math.floor(ScreenWidth / 5 - 100), math.floor(ScreenHeight / 6 + 50), 100, 50))
        pygame.draw.rect(win, PoneSimonYellowColour, (math.floor(ScreenWidth / 5 + 100), math.floor(ScreenHeight / 6 + 50), 100, 50))
        # Player One
        pygame.draw.rect(win, PoneBlueColour, (math.floor(ScreenWidth / 5 + 25), math.floor(ScreenHeight / 1.5), 50, 25))
        pygame.draw.rect(win, PoneRedColour, (math.floor(ScreenWidth / 5 + 25), math.floor(ScreenHeight / 1.5 + 50), 50, 25))
        pygame.draw.rect(win, PoneGreenColour, (math.floor(ScreenWidth / 5 - 25), math.floor(ScreenHeight / 1.5 + 25), 50, 25))
        pygame.draw.rect(win, PoneYellowColour, (math.floor(ScreenWidth / 5 + 75), math.floor(ScreenHeight / 1.5 + 25), 50, 25))

        def ColourUpdate():
            pygame.draw.rect(win, PoneSimonBlueColour, (math.floor(ScreenWidth / 5), math.floor(ScreenHeight / 6), 100, 50))
            pygame.draw.rect(win, PoneSimonRedColour, (math.floor(ScreenWidth / 5), math.floor(ScreenHeight / 6 + 100), 100, 50))
            pygame.draw.rect(win, PoneSimonGreenColour, (math.floor(ScreenWidth / 5 - 100), math.floor(ScreenHeight / 6 + 50), 100, 50))
            pygame.draw.rect(win, PoneSimonYellowColour, (math.floor(ScreenWidth / 5 + 100), math.floor(ScreenHeight / 6 + 50), 100, 50))
            pygame.display.update()

        if GameStarted:
            print(PoneList, PoneSimonList)
            if CountDown:
                if CountDownAmount == 1:
                    pygame.draw.rect(win, White, (ScreenWidth/2-50, ScreenHeight/3, 100, 100))
                    win.blit(Img1, (ScreenWidth/2-50, ScreenHeight/3))
                    CountDownAmount = 4
                    CountDown = False
                if CountDownAmount == 2:
                    pygame.draw.rect(win, White, (ScreenWidth/2-50, ScreenHeight/3, 100, 100))
                    win.blit(Img2, (ScreenWidth/2-50, ScreenHeight/3))
                if CountDownAmount == 3:
                    pygame.draw.rect(win, White, (ScreenWidth/2-50, ScreenHeight/3, 100, 100))
                    win.blit(Img3, (ScreenWidth/2-50, ScreenHeight/3))
                CountDownAmount -= 1
                pygame.display.update()
                pygame.time.delay(500)
            else:
                if SimonTurn:
                    if len(PoneList) == len(PoneSimonList):
                        randomInt = random.randint(0, 3)
                        PoneSimonList.append(ColourList[randomInt])

                        PoneBlueColour = BluePlaceHolder
                        PoneGreenColour = GreenPlaceHolder
                        PoneRedColour = RedPlaceHolder
                        PoneYellowColour = YellowPlaceHolder

                        for x in PoneSimonList:
                            if x == "Blue":
                                PoneSimonBlueColour = Blue
                                ColourUpdate()
                                pygame.time.delay(750)
                                PoneSimonBlueColour = BluePlaceHolder
                                ColourUpdate()
                                pygame.time.delay(250)
                            elif x == "Green":
                                PoneSimonGreenColour = Green
                                ColourUpdate()
                                pygame.time.delay(750)
                                PoneSimonGreenColour = GreenPlaceHolder
                                ColourUpdate()
                                pygame.time.delay(250)
                            elif x == "Red":
                                PoneSimonRedColour = Red
                                ColourUpdate()
                                pygame.time.delay(750)
                                PoneSimonRedColour = RedPlaceHolder
                                ColourUpdate()
                                pygame.time.delay(250)
                            elif x == "Yellow":
                                PoneSimonYellowColour = Yellow
                                ColourUpdate()
                                pygame.time.delay(750)
                                PoneSimonYellowColour = YellowPlaceHolder
                                ColourUpdate()
                                pygame.time.delay(250)
                    else:
                        SimonTurn = False
                        PoneList = [] # Reset de list van PlayerOne na elke beurt
                else:
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

                    if len(PoneList) == len(PoneSimonList):
                        SimonTurn = True
        else:
            PoneSimonList = []      # Reset de list van PlayerOneSimon
            PtwoSimonList = []      # Reset de list van PlayerTwoSimon
            PoneList = []           # Reset de list van PlayerOne
            PtwoList = []           # Reset de list van PlayerTwo

    if LoadingEnd:
        if not LoadingTime == 0:
            pygame.draw.rect(win, Black, (0, 0, ScreenWidth, math.floor(ScreenHeight*(LoadingTime/LoadingStep))))
            pygame.display.update()
            LoadingTime -= 1
            if LoadingTime == 0:
                LoadingEnd = False

    pygame.display.update()
pygame.quit()
