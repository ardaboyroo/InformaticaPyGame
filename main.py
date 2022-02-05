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
Gray = (25, 25, 25)
DarkPurple = (55, 25, 103)
MainPurple = (110, 50, 205)
LightPurple = (154, 153, 235)
Red = (255, 0, 60)
Blue = (58, 134, 255)
Pink = (250, 172, 215)
White = (255, 255, 255)
PoneColour = (255, 0, 60)
# PtwoColour = (0, 255, 242)

# De volgende Variables zijn voor de Main Menu
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


# De volgende Variables zijn de bool values voor de games
Game1 = False       # Simon Says
Game2 = False       # Sumo
Game3 = False
Game4 = False
Game5 = False
Game6 = False

# De volgende Variables zijn voor Game1
GameStarted = False
SimonList = ["Blue", "Green", "Red", "Yellow"]
PoneList = []
PtwoList = []

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

    ScorePoneTxt = SmallFont.render("Hamudt: "+str(ScorePone), True, PoneColour, PoneBGC)   # Update de score van Hamudt
    ScorePtwoTxt = SmallFont.render("Eduardo: "+str(ScorePtwo), True, Blue, PtwoBGC)  # Update de score van Eduardo

    Key = pygame.key.get_pressed()
    if Key[pygame.K_ESCAPE]:
        Menu = True
        GameStarted = False
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

    if Menu:
        win.fill(MainPurple)
        for x in range(1, 100):  # Deze for-loop zorgt voor een "Retro Scan Lines" effect
            pygame.draw.rect(win, Black, (0, (x * 9 - 4), ScreenWidth, 2))

        if Key[pygame.K_y]:
            ScorePone, ScorePtwo = 0, 0

        win.blit(ScorePoneTxt, ScorePoneTxt.get_rect(center=(ScreenWidth/16, ScreenHeight/16)))     # Draw de score van Hamudt
        win.blit(ScorePtwoTxt, ScorePtwoTxt.get_rect(center=(ScreenWidth/1.1, ScreenHeight / 16)))  # Draw de score van Eduardo
        win.blit(TitleTxt, TitleTxt.get_rect(center=(ScreenWidth / 2, ScreenHeight / 16)))

        Game1Icon = pygame.draw.rect(win, Black, (100, 150, 100, 50))

        PoneBGC, PtwoBGC = White, White

        SumoH2 = pygame.transform.scale(SumoH, (ScreenWidth*0.075, ScreenHeight*0.1))
        SumoE2 = pygame.transform.scale(SumoE, (ScreenWidth*0.075, ScreenHeight*0.1))
        win.blit(SumoE2, SumoE2.get_rect(center=(ScreenWidth/2, ScreenHeight/2)))
        win.blit(SumoH2, SumoH2.get_rect(center=(ScreenWidth/2-86, ScreenHeight/2)))

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
        win.blit(ScorePoneTxt, ScorePoneTxt.get_rect(center=(ScreenWidth/16, ScreenHeight/16)))     # Draw de score van Hamudt
        win.blit(ScorePtwoTxt, ScorePtwoTxt.get_rect(center=(ScreenWidth/1.1, ScreenHeight / 16)))  # Draw de score van Eduardo

        pygame.draw.rect(win, White, (math.floor(ScreenWidth/2-10), 0, 10, ScreenHeight))       # Draw een witte lijn

        pygame.draw.rect(win, Blue, (math.floor(ScreenWidth/5), ScreenHeight/6, 100, 50))
        pygame.draw.rect(win, Red, (math.floor(ScreenWidth/5), ScreenHeight/6, 100, 50))


        if GameStarted:
            AppRand = SimonList[random.randint(0,3)]
            PoneList.append(AppRand)

            # for x in PoneList:
            #     print(x)
            # for x in range(len(PoneList)):
            #     print(PoneList[x])

    if LoadingEnd:
        if not LoadingTime == 0:
            pygame.draw.rect(win, Black, (0, 0, ScreenWidth, math.floor(ScreenHeight*(LoadingTime/LoadingStep))))
            pygame.display.update()
            LoadingTime -= 1
            if LoadingTime == 0:
                LoadingEnd = False

    pygame.display.update()
pygame.quit()
