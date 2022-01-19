import pygame
import math
import random
pygame.init()

ScreenWidth = 1200 #De breedte van het scherm in pixels
ScreenHeight = 700 #De hoogte van het scherm in pixels

""" #Dit zijn ongebruikte code, het wordt gebruikt als Refference
TextCenter = TitleTxt.get_rect(center=(ScreenWidth/2, ScreenHeight/16))
"""

IsRunning = True  # Een boolean voor de while loop
win = pygame.display.set_mode((ScreenWidth, ScreenHeight))  # Breedte en Hoogte van het scherm in aantal pixels
pygame.display.set_caption("Arda en Nieks reetro Arkade")

#De volgende Variables zijn de kleuren van de gekozen ColourScheme
Black = (0,0,0)
DarkPurple = (55,25,103)
MainPurple = (110, 50, 205)
LightPurple = (154,153,235)
Blue = (58,134,255)
Pink = (250,172,215)
White = (255,255,255)

#De volgende Variables zijn de Main Data
MenuStart = False
MainFont = pygame.font.Font("freesansbold.ttf", 32)
TitleTxt = MainFont.render("Wilkom bij Arda en Nieks Reetro Arkade",True,Pink,DarkPurple)


while IsRunning:
    pygame.time.delay(33)  # Framerate in 1/milliseconden
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IsRunning = False
    if not MenuStart:
        win.fill(MainPurple)
        win.blit(TitleTxt,TitleTxt.get_rect(center=(ScreenWidth/2,ScreenHeight/16)))

    pygame.display.update()
pygame.quit()
