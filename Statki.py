import pygame
import sys

pygame.init() #musi być...

wielkoscOkna = (900,900)

def granicePlanszy(pozycja):
    if pozycja >= 900:
        pozycja = 0
    if pozycja < 0:
        pozycja = 900
    return pozycja

def ruchxAD():
    if pygame.key.get_pressed()[pygame.K_+a]:
        return -1
    elif pygame.key.get_pressed()[pygame.K_d]:
        return 1
    else:
        return 0
def ruchyWS():
    if pygame.key.get_pressed()[pygame.K_w]:
        return -1
    elif pygame.key.get_pressed()[pygame.K_s]:
        return 1
    else:
        return 0
def ruchxLR():
    if pygame.key.get_pressed()[pygame.K_left]:
        return -1
    elif pygame.key.get_pressed()[pygame.K_right]:
        return 1
    else:
        return 0
def ruchyUD():
    if pygame.key.get_pressed()[pygame.K_up]:
        return -1
    elif pygame.key.get_pressed()[pygame.K_down]:
        return 1
    else:
        return 0


obraz = pygame.display.set_mode(wielkoscOkna)
statek_1 = pygame.Rect(50,450,50,50)
statek_2 = pygame.Rect(800,450,50,50)
pocisk_1 = pygame.Rect(901,50,10,10)
pocisk_2 = pygame.Rect(50,901,10,10)
x = 10
while True:
    strzał_1 = 0
    strzał_2 = 0
    obraz.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            strzał_1 = 1
            pocisk_1.x = statek_1.x + 20
            pocisk_1.y = statek_1.y + 20
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            strzał_2 = 2
            pocisk_2.x = statek_2.x + 20
            pocisk_2.y = statek_2.y + 20
    if strzał_1 == 1 or pocisk_1.x < 900:
        pygame.draw.rect(obraz, (255, 0, 0), pocisk_1)
        pocisk_1.x += 1
    if strzał_2 == 2 or pocisk_2.x < 900:
        pygame.draw.rect(obraz, (0, 0, 255), pocisk_2)
        pocisk_2.x -= 1
    if (statek_1.x + 50 > pocisk_2.x and statek_1.x < pocisk_2.x)and\
            (statek_1.y + 50 > pocisk_2.y and statek_1.y < pocisk_2.y):
        statek_1.x = 0
        statek_1.y = 0
    if (statek_2.x + 50 > pocisk_1.x and statek_2.x < pocisk_1.x)and\
            (statek_2.y + 50 > pocisk_1.y and statek_2.y < pocisk_1.y):
        statek_2.x = 850
        statek_2.y = 0

    statek_1.x += ruchxAD()
    #statek_1.y += ruchy()
    #statek_2.x += ruchx()
    #statek_2.y += ruchy()
    statek_1.x = granicePlanszy(statek_1.x)
    statek_1.y = granicePlanszy(statek_1.y)
    statek_2.x = granicePlanszy(statek_2.x)
    statek_2.y = granicePlanszy(statek_2.y)

    pygame.draw.rect(obraz, (255, 0, 0), statek_1)
    pygame.draw.rect(obraz, (0, 0, 255), statek_2)
    pygame.display.flip()