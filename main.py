import pygame
import math
import random

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("roblox-death-sound_1.mp3")
hitSound = pygame.mixer.Sound("hitmarker_2.mp3")
clock = pygame.time.Clock()

ScreenWidth = 1200  # De breedte van het scherm in pixels
ScreenHeight = 700  # De hoogte van het scherm in pixels

""" #Dit zijn ongebruikte code, het wordt gebruikt als Refference
TextCenter = TitleTxt.get_rect(center=(ScreenWidth/2, ScreenHeight/16))
"""

IsRunning = True  # Een boolean voor de while loop
win = pygame.display.set_mode((ScreenWidth, ScreenHeight))  # Breedte en Hoogte van het scherm in aantal pixels
pygame.display.set_caption("Arda en Nieks reetro Arkade")

# De volgende Variables zijn de kleuren van de gekozen ColourScheme
Black = (0, 0, 0)
DarkPurple = (55, 25, 103)
MainPurple = (110, 50, 205)
LightPurple = (154, 153, 235)
Blue = (58, 134, 255)
Pink = (250, 172, 215)
White = (255, 255, 255)

# De volgende Variables zijn de Main Data
Menu = True
BigFont = pygame.font.Font("freesansbold.ttf", 32)
MediumFont = pygame.font.Font("freesansbold.ttf", 24)
SmallFont = pygame.font.Font("freesansbold.ttf", 16)

TitleTxt = BigFont.render("Wilkom bij Arda en Niek's Reetro(met een C) Arkade", True, Pink, DarkPurple)
ScorePone = 0
ScorePtwo = 0

# De volgende Variables zijn de bool values voor de games
Game1 = False

Deb = False
Debounce = 0
while IsRunning:
    pygame.time.delay(33)  # Framerate in 1/milliseconden
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IsRunning = False
    print(Deb,Debounce)
    if Deb == True:
        Debounce += 1
    ScorePoneTxt = SmallFont.render("Hamudt: "+str(ScorePone),True,White)
    ScorePtwoTxt = SmallFont.render("Eduardo: "+str(ScorePtwo),True,White)
    win.fill(Black)
    if Menu:
        win.fill(MainPurple)
        for x in range(1, 85):  # Deze for-loop zorgt voor een "Retro Scan Lines" effect
            pygame.draw.rect(win, Black, (0, (x * 9 - 4), ScreenWidth, 2))

        win.blit(ScorePoneTxt,ScorePoneTxt.get_rect(center=(ScreenWidth/16,ScreenHeight/16)))
        win.blit(ScorePtwoTxt, ScorePtwoTxt.get_rect(center=(ScreenWidth/1.1 , ScreenHeight / 16)))
        win.blit(TitleTxt, TitleTxt.get_rect(center=(ScreenWidth / 2, ScreenHeight / 16)))

        lol = pygame.draw.rect(win, Black, (100,150,100,50))

        if pygame.mouse.get_pressed()[0]:
            MouseX = pygame.mouse.get_pos()[0]
            MouseY = pygame.mouse.get_pos()[1]

            if Deb == False:
                hitSound.play()
                Deb = True
            elif Deb and Debounce >= 33:
                Debounce = 0
                Deb = False

            if MouseX >= 100 and MouseX <= 200 and MouseY >= 150 and MouseY <= 200:
                Menu = False
                Game1 = True
            print(MouseX,MouseY)


    pygame.display.update()
pygame.quit()
