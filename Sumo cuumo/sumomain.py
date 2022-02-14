import time

import pygame
import random
pygame.init()


# start timer
Sgamestart = False
Sgamestarttimer = 0
Startsumotimer = False
Sload1 = pygame.transform.scale(pygame.image.load("1.png"), (100, 100))
Sload2 = pygame.transform.scale(pygame.image.load("2.png"), (100, 100))
Sload3 = pygame.transform.scale(pygame.image.load("3.png"), (100, 100))
Sfont = pygame.font.Font("freesansbold.ttf", 50)
Stext = Sfont.render("Press the Spacebar to start!", True, (225,225,225), (0,0,0))
Stextrect = Stext.get_rect()
Stextrect.center = (600, 150)
# player variables
Splayer1 = 1
Splayer2 = 1
Splayer1live = True
Splayer2live = True
Splayer1x, Splayer1y = 200, 275
Splayer2x, Splayer2y = 900, 275
Splayer1rect = pygame.Rect(200, 275, 100, 100)
Splayer2rect = pygame.Rect(900, 275, 100, 100)
SPlayer1image = pygame.transform.scale(pygame.image.load("SumoH.png"), (105, 105))
SPlayer2image = pygame.transform.scale(pygame.image.load("SumoE.png"), (105, 105))
Stextwin1 = Sfont.render("Player 1 wins", True, (225,225,225), (0,0,0))
Stextrectwin1 = Stextwin1.get_rect()
Stextrectwin1.center = (600, 150)
Stextwin2 = Sfont.render("Player 2 wins", True, (225,225,225), (0,0,0))
Stextrectwin2 = Stextwin2.get_rect()
Stextrectwin2.center = (600, 150)
# power push
Sumorantimer = 0
Stime = 0
Srandomdirection = 0
Sdownarrow = pygame.transform.scale(pygame.image.load("downarrow.png"), (100, 100))
Sleftarrow = pygame.transform.scale(pygame.image.load("leftarrow.png"), (100, 100))
Srightarrow = pygame.transform.scale(pygame.image.load("rightarrow.png"), (100, 100))
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
pygame.display.set_caption("sumoprot")


run = True

while run:
    win.fill((10, 10, 255))
    pygame.time.delay(33)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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
    Sumostartkey = pygame.key.get_pressed()        # Power push
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
            win.blit(Stext,Stextrect)
        if Sumostartkey[pygame.K_SPACE]:
            Startsumotimer = True
        if Startsumotimer:
            Sgamestarttimer += 1
            if 0 < Sgamestarttimer < 33:
                win.blit(Sload3, (550, 200))
            if 33 < Sgamestarttimer < 66:
                win.blit(Sload2, (550, 200))
            if 66 < Sgamestarttimer <= 99:
                win.blit(Sload1, (550, 200))
        if Sgamestarttimer > 99:
            Sgamestarttimer = 0
            Startsumotimer = False
            Sgamestart = True
    pygame.draw.rect(win, (161, 96, 6), (150, 375, 900, 100))
    pygame.draw.rect(win, (161, 96, 6), (525, 375, 150, 1000))
    if Splayer2rect.colliderect(deathbarrect):
        Splayer2live = False
        win.blit(Stextwin1,Stextrectwin1)
        SS += 1

    else:
        win.blit(SPlayer2image, (Splayer2x, Splayer2y))
    if Splayer1rect.colliderect(deathbarrect1):
        Splayer1live = False
        win.blit(Stextwin2, Stextrectwin2)
        SS += 1
    if SS == 33:
        Splayer2x = 900
        Splayer1x = 200
        Splayer1rect = pygame.Rect(200, 275, 100, 100)
        Splayer2rect = pygame.Rect(900, 275, 100, 100)
        Splayer1live = True
        Splayer2live = True
        SS = 0
        Sgamestart = False
    else:
        win.blit(SPlayer1image, (Splayer1x, Splayer1y))


    pygame.display.update()

pygame.quit()
