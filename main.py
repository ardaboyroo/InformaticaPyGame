import pygame
import math
import random
pygame.init()

win = pygame.display.set_mode((1220, 800))

pygame.display.set_caption("Arda en Nieks reetro Arkade")

IsRunning = True

while IsRunning:
    win.fill((110, 50, 205))
    pygame.time.delay(30) #Framerate in 1/milliseconden
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IsRunning = False

    pygame.display.update()
pygame.quit()
