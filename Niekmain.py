
import time
import pygame
import random
pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong ")

green = (0,225,0)
red = (255,0,0)
henkx = 50
henky = 250
pietx = 750
piety = 250
marcusx = 350
marcusy = 70
mikex = 350
mikey = 550
snelheidmikey = 15
snelheidmarcus = 15
scoremarcus = 0
scoremike = 0
Lasttouched = 0
balx = 150
baly = 50
balgaatnaarrechts = True
balgaatnaarboven = True
breedtebatje = 20
breedtema = 100
breedtemi = 100
hoogtebatjehenk = 100
hoogtebatjepiet = 100
hoogtebatjemarcusenmike = 20

snelheidbalx = 10
snelheidbaly = 10
snelheidbatjeP = 15
snelheidbatjeH = 15
scorehenk = 0
scorepiet = 0
menuestart = False
randomlength = False
QPlayer = False
F = pygame.font.Font('freesansbold.ttf', 32)
Stext = F.render("START THE MADNESS", True ,green, (0,0,0) )
textRectS = Stext.get_rect()
Rtext = F.render("random", True ,green, (0,0,0) )
RtextF = F.render("random", True ,red, (0,0,0) )
textRectR = Rtext.get_rect()
Qtext = F.render("4 player", True ,green, (0,0,0) )
QtextF = F.render("4 player", True ,red, (0,0,0) )
textRectQ = Qtext.get_rect()



font = pygame.font.Font('freesansbold.ttf', 12)
scorehenktekst = font.render('Punten Henk: ' + str(scorehenk), True, (255, 255, 255), (0, 0, 0))
scorepiettekst = font.render('Punten Piet: ' + str(scorepiet), True, (255, 255, 255), (0, 0, 0))
scoremarcustekst = font.render('Punten Marcus: ' + str(scoremarcus), True, (255, 255, 255), (0, 0, 0))
scoremiketekst = font.render('Punten Mike: ' + str(scoremike), True, (255, 255, 255), (0, 0, 0))

textRecthenk = scorehenktekst.get_rect()
textRecthenk.center = (200, 30)
textRectpiet = scorepiettekst.get_rect()
textRectpiet.center = (600, 30)
textRectmarcus = scoremarcustekst.get_rect()
textRectmarcus.center = (600, 50)
textRectmike = scoremiketekst.get_rect()
textRectmike.center = (200, 50)
run = True

while run:

   if menuestart== False:
      win.fill((90, 210, 10))
      win.blit(Stext, (225,200))
      if randomlength == False:
          win.blit(RtextF, (100,400))
      else:
          win.blit(Rtext,(100,400))
      if QPlayer == False:
          win.blit(QtextF, (300,400))
      else:
          win.blit(Qtext,(300,400))

      scoremarcus = 0
      scoremike = 0
      scorehenk = 0
      scorepiet = 0
      balx = 400
      baly = 300
      pygame.time.delay(1)
      henkx = 50
      henky = 250
      pietx = 750
      piety = 250
      marcusx = 350
      marcusy = 70
      mikex = 350
      mikey = 550
      snelheidmikey = 15
      snelheidmarcus = 15
      breedtebatje = 20
      breedtema = 100
      breedtemi = 100
      hoogtebatjehenk = 100
      hoogtebatjepiet = 100
      hoogtebatjemarcusenmike = 20
      snelheidbalx = 10
      snelheidbaly = 10
      snelheidbatjeP = 15
      snelheidbatjeH = 15
      Lasttouched = 0
      if pygame.mouse.get_pressed()[0]:
          qy = pygame.mouse.get_pos()[1]
          qx = pygame.mouse.get_pos()[0]
          print(qx)
          if qy >= 200 and qy <= 232 and qx >= 255 and qx <=576:
              menuestart = True
          if qy >= 400 and qy <= 432 and qx >= 100 and qx <=219:
              if randomlength == False:
                  randomlength = True
                  time.sleep(0.25)
              else:
                  randomlength = False
                  time.sleep(0.25)

          if qy >= 400 and qy <= 432 and qx >= 300 and qx <=519:
              if QPlayer == False:
                  QPlayer = True
                  time.sleep(0.25)
              else:
                  QPlayer = False
                  time.sleep(0.25)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
          run = False
   if menuestart == True:

       pygame.time.delay(30)
       win.fill((0,0,0))
       keys = pygame.key.get_pressed()
       if keys[pygame.K_w]:
           henky -= snelheidbatjeH
       if keys[pygame.K_s]:
          henky += snelheidbatjeH
       if keys[pygame.K_UP]:
           piety -= snelheidbatjeP
       if keys[pygame.K_DOWN]:
           piety += snelheidbatjeP
       if keys[pygame.K_r]:
           menuestart = False
       if QPlayer == True:
           if keys[pygame.K_m]:
               marcusx += snelheidmarcus
           if keys[pygame.K_n]:
               marcusx -= snelheidmarcus
           if keys[pygame.K_c]:
               mikex -= snelheidmikey
           if keys[pygame.K_v]:
               mikex += snelheidmikey

       pygame.draw.rect(win, (255, 0, 0), (henkx, henky, breedtebatje, hoogtebatjehenk))
       pygame.draw.rect(win, (255, 0, 0), (pietx, piety, breedtebatje, hoogtebatjepiet))
       if QPlayer == True:
           pygame.draw.rect(win, (255, 0, 0),(mikex, mikey, breedtemi, hoogtebatjemarcusenmike))
           pygame.draw.rect(win, (255, 0, 0),(marcusx, marcusy, breedtema, hoogtebatjemarcusenmike))
       pygame.draw.rect(win, (255, 0, 0), (balx, baly, 10, 10))
       recthenk = pygame.Rect(henkx, henky, breedtebatje, hoogtebatjehenk)
       rectpiet = pygame.Rect(pietx, piety, breedtebatje, hoogtebatjepiet)
       rectmarcus = pygame.Rect(marcusx, marcusy, breedtema, hoogtebatjemarcusenmike)
       rectmike = pygame.Rect(mikex, mikey, breedtemi, hoogtebatjemarcusenmike)
       rectbal = pygame.Rect(balx, baly, 10, 10)

       scorehenktekst = font.render('Punten Henk: ' + str(scorehenk), True, (255, 255, 255), (0, 0, 0))
       scorepiettekst = font.render('Punten Piet: ' + str(scorepiet), True, (255, 255, 255), (0, 0, 0))
       win.blit(scorehenktekst, textRecthenk)
       win.blit(scorepiettekst, textRectpiet)
       if QPlayer == True:
           scoremarcustekst = font.render('Punten Marcus: ' + str(scoremarcus), True, (255, 255, 255), (0, 0, 0))
           scoremiketekst = font.render('Punten Mike: ' + str(scoremike), True, (255, 255, 255), (0, 0, 0))
           win.blit(scoremarcustekst, textRectmarcus)
           win.blit(scoremiketekst, textRectmike)

       if henky > 480:
           henky = 480
       if henky < 0:
           henky = 0
       if piety > 480:
           piety = 480
       if piety < 0:
           piety = 0
       if marcusx > 700:
           marcusx = 700
       if marcusx < 0:
           marcusx = 0
       if mikex > 700:
           mikex = 700
       if mikex < 0:
           mikex = 0

       if balgaatnaarrechts == True:
           balx += snelheidbalx
       else:
           balx -= snelheidbalx
           if QPlayer == False:
               baly += snelheidbaly
       if QPlayer == True:
           if balgaatnaarboven == True:
               baly += snelheidbaly
           else:
               baly -= snelheidbaly

       if rectbal.colliderect(recthenk):
           balgaatnaarrechts = True
           if randomlength == True:
               hoogtebatjehenk = random.randint(10, 500)
               snelheidbatjeH = random.randint(1,50)
           if QPlayer == True:
               Lasttouched = 1


       if rectbal.colliderect(rectpiet):
           balgaatnaarrechts = False
           if randomlength == True:
               hoogtebatjepiet = random.randint(10, 500)
               snelheidbatjeP = random.randint(1,50)
               if QPlayer == True:
                   Lasttouched = 2
       if QPlayer == True:
           if rectbal.colliderect(rectmike):
               Lasttouched = 3
               balgaatnaarboven = False
               if randomlength == True:
                   breedtemi = random.randint(10, 500)
                   snelheidmikey = random.randint(1, 50)
           if rectbal.colliderect(rectmarcus):
               Lasttouched = 4
               balgaatnaarboven = True
               breedtema = random.randint(10, 500)
               snelheidmarcus = random.randint(1, 50)


       else:
           if baly > 580 or baly < 20:
               snelheidbaly *= -1
       if balx > 800:
           if QPlayer == False:
               pygame.time.delay(1000)
               scorehenk += 1
               balx = 600
               balgaatnaarrechts = False
           else:
               if Lasttouched == 1:
                   scorehenk += 1
               if Lasttouched == 2:
                   scorepiet += 1
               if Lasttouched == 3:
                   scoremike += 1
               if Lasttouched == 4:
                   scoremarcus += 1
               balx = 400
               baly = 300
               pygame.time.delay(1000)
               e = random.randint(1 , 10)
               E = random.randint(1, 10)
               if e > 5 and E > 5:
                   balgaatnaarboven = True
                   balgaatnaarrechts = True
               if e < 5 and E > 5:
                   balgaatnaarboven = False
                   balgaatnaarrechts = True
               if e > 5 and E < 5:
                   balgaatnaarboven = True
                   balgaatnaarrechts = False
               if e < 5 and E < 5:
                   balgaatnaarboven = False
                   balgaatnaarrechts = False
       if balx < 0:
           if QPlayer == False:
               pygame.time.delay(1000)
               scorepiet += 1
               balx = 200
               balgaatnaarrechts = True
           else:
               if Lasttouched == 1:
                   scorehenk += 1
               if Lasttouched == 2:
                   scorepiet += 1
               if Lasttouched == 3:
                   scoremike += 1
               if Lasttouched == 4:
                   scoremarcus += 1
               balx = 400
               baly = 300
               pygame.time.delay(1000)
               e = random.randint(1, 10)
               E = random.randint(1, 10)
               if e > 5 and E > 5:
                   balgaatnaarboven = True
                   balgaatnaarrechts = True
               if e < 5 and E > 5:
                   balgaatnaarboven = False
                   balgaatnaarrechts = True
               if e > 5 and E < 5:
                   balgaatnaarboven = True
                   balgaatnaarrechts = False
               if e < 5 and E < 5:
                   balgaatnaarboven = False
                   balgaatnaarrechts = False
       if QPlayer == True:
           if baly > 580:
               if Lasttouched == 1:
                   scorehenk += 1
               if Lasttouched == 2:
                   scorepiet += 1
               if Lasttouched == 3:
                   scoremike += 1
               if Lasttouched == 4:
                   scoremarcus += 1
               balx = 400
               baly = 300
               pygame.time.delay(1000)
               e = random.randint(1, 10)
               E = random.randint(1, 10)
               if e > 5 and E > 5:
                   balgaatnaarboven = True
                   balgaatnaarrechts = True
               if e < 5 and E > 5:
                   balgaatnaarboven = False
                   balgaatnaarrechts = True
               if e > 5 and E < 5:
                   balgaatnaarboven = True
                   balgaatnaarrechts = False
               if e < 5 and E < 5:
                   balgaatnaarboven = False
                   balgaatnaarrechts = False
           if baly < 20:
               if Lasttouched == 1:
                   scorehenk += 1
               if Lasttouched == 2:
                   scorepiet += 1
               if Lasttouched == 3:
                   scoremike += 1
               if Lasttouched == 4:
                   scoremarcus += 1
               balx = 400
               baly = 300
               pygame.time.delay(1000)
               e = random.randint(1, 10)
               E = random.randint(1, 10)
               if e > 5 and E > 5:
                   balgaatnaarboven = True
                   balgaatnaarrechts = True
               if e < 5 and E > 5:
                   balgaatnaarboven = False
                   balgaatnaarrechts = True
               if e > 5 and E < 5:
                   balgaatnaarboven = True
                   balgaatnaarrechts = False
               if e < 5 and E < 5:
                   balgaatnaarboven = False
                   balgaatnaarrechts = False
   pygame.display.update()
pygame.quit()
