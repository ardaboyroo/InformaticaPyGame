import pygame
import math
import random

pygame.init()

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
ScoreArnold = 0
ScoreEduardo = 0

while IsRunning:
    pygame.time.delay(33)  # Framerate in 1/milliseconden
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IsRunning = False

    ScoreArnoldTxt = SmallFont.render("Arnold: "+str(ScoreArnold),True,White)
    ScoreEduardoTxt = SmallFont.render("Eduardo: "+str(ScoreEduardo),True,White)

    if Menu:
        win.fill(MainPurple)
        for x in range(1, 85):  # Deze for-loop zorgt voor een "Retro Scan Lines" effect
            pygame.draw.rect(win, Black, (0, (x * 9 - 4), ScreenWidth, 2))

        win.blit(ScoreArnoldTxt,ScoreArnoldTxt.get_rect(center=(ScreenWidth/16,ScreenHeight/16)))
        win.blit(ScoreEduardoTxt, ScoreEduardoTxt.get_rect(center=(ScreenWidth/1.1 , ScreenHeight / 16)))
        win.blit(TitleTxt, TitleTxt.get_rect(center=(ScreenWidth / 2, ScreenHeight / 16)))

        if pygame.mouse.get_pressed()[0]:
            MouseX = pygame.mouse.get_pos()[0]
            MouseY = pygame.mouse.get_pos()[1]
            print(MouseX,MouseY)


    pygame.display.update()
pygame.quit()
