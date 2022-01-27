import pygame

pygame.init()
pygame.mixer.init()
oofSound = pygame.mixer.Sound("roblox-death-sound_1.mp3")
hitSound = pygame.mixer.Sound("hitmarker_2.mp3")
hitSoundDeb = False

ScreenWidth = 1200  # De breedte van het scherm in pixels
ScreenHeight = 700  # De hoogte van het scherm in pixels

""" #Dit zijn ongebruikte code, het wordt gebruikt als Refference
TextCenter = TitleTxt.get_rect(center=(ScreenWidth/2, ScreenHeight/16))
"""

IsRunning = True  # Een boolean voor de while loop
win = pygame.display.set_mode((ScreenWidth, ScreenHeight))  # Breedte en Hoogte van het scherm in aantal pixels
pygame.display.set_caption("Arda en Nieks reetro Arkade")   # De caption van de window

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
Game2 = False
Game3 = False
Game4 = False
Game5 = False
Game6 = False

while IsRunning:
    pygame.time.delay(33)  # Framerate in 1/milliseconden

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # if statement om de game af te sluiten met de rode kruis
            IsRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN and not hitSoundDeb:    # if statement for de hit sound
            hitSound.play()
            hitSoundDeb = True
        if event.type == pygame.MOUSEBUTTONUP:
            hitSoundDeb = False

    ScorePoneTxt = SmallFont.render("Hamudt: "+str(ScorePone), True, White)   # Update de score van Hamudt
    ScorePtwoTxt = SmallFont.render("Eduardo: "+str(ScorePtwo), True, White)  # Update de score van Eduardo

    win.fill(Black)     # Als er niks actief is is de achtergrond zwart

    Key = pygame.key.get_pressed()
    if Key[pygame.K_ESCAPE]:
        Menu = True
        Game1 = False
        Game2 = False
        Game3 = False
        Game4 = False
        Game5 = False
        Game6 = False
    if Key[pygame.K_y]:
        if Menu:
            if ScorePone > 0 or ScorePtwo > 0:
                ScorePone = 0
                ScorePtwo = 0

    if Menu:
        win.fill(MainPurple)
        for x in range(1, 85):  # Deze for-loop zorgt voor een "Retro Scan Lines" effect
            pygame.draw.rect(win, Black, (0, (x * 9 - 4), ScreenWidth, 2))

        win.blit(ScorePoneTxt, ScorePoneTxt.get_rect(center=(ScreenWidth/16, ScreenHeight/16)))     # Draw de score van Hamudt
        win.blit(ScorePtwoTxt, ScorePtwoTxt.get_rect(center=(ScreenWidth/1.1, ScreenHeight / 16)))  # Draw de score van Eduardo
        win.blit(TitleTxt, TitleTxt.get_rect(center=(ScreenWidth / 2, ScreenHeight / 16)))

        Game1Icon = pygame.draw.rect(win, Black, (100, 150, 100, 50))

        if pygame.mouse.get_pressed()[0]:
            MouseX = pygame.mouse.get_pos()[0]
            MouseY = pygame.mouse.get_pos()[1]

            if 100 <= MouseX <= 200 and 150 <= MouseY <= 200:
                Menu = False
                Game1 = True

    if Game1:
        win.fill(Blue)

    pygame.display.update()
pygame.quit()
