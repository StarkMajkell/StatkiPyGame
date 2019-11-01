import pygame
import sys

pygame.init()  # musi być
#górna belka
pygame.display.set_caption('Statki')
a = pygame.image.load('Logo.png')
pygame.display.set_icon(a)

# moduł ze zmiennymi
wysokoscOkna = 600
szerokoscOkna = 1360
rozmiargracza_1 = 50
rozmiargracza_2 = 50
rozmiarpocisku_1 = 10
rozmiarpocisku_2 = 10
kolorstatku1 = 255
kolorstatku2 = 255
rozmiarOkna = (szerokoscOkna, wysokoscOkna)
obraz = pygame.display.set_mode(rozmiarOkna)
statek_1 = pygame.Rect(0, wysokoscOkna / 2, rozmiargracza_1, rozmiargracza_1)
statek_2 = pygame.Rect(szerokoscOkna - rozmiargracza_2, (wysokoscOkna / 2), rozmiargracza_2, rozmiargracza_2)
pocisk_1 = pygame.Rect(szerokoscOkna, 50, rozmiarpocisku_1, rozmiarpocisku_1)
pocisk_2 = pygame.Rect(50, wysokoscOkna, rozmiarpocisku_2, rozmiarpocisku_2)


# moduł funkcji
def granicePlanszyX(pozycja):
    if pozycja >= szerokoscOkna:
        pozycja = 0
    if pozycja < 0:
        pozycja = szerokoscOkna
    return pozycja
def granicePlanszyY(pozycja):
    if pozycja >= wysokoscOkna:
        pozycja = 0
    if pozycja < 0:
        pozycja = wysokoscOkna
    return pozycja
def ruchxAD():
    if pygame.key.get_pressed()[pygame.K_a]:
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
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        return -1
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        return 1
    else:
        return 0
def ruchyUD():
    if pygame.key.get_pressed()[pygame.K_UP]:
        return -1
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        return 1
    else:
        return 0
def off():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)


# pętla programu program
while True:
    obraz.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            pocisk_1.x = statek_1.x + rozmiargracza_1 / 2
            pocisk_1.y = statek_1.y + rozmiargracza_1 / 2 - rozmiarpocisku_1 / 2
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pocisk_2.x = statek_2.x + rozmiargracza_2 / 2
            pocisk_2.y = statek_2.y + rozmiargracza_2 / 2 - rozmiarpocisku_2 / 2

    if pocisk_1.x < szerokoscOkna:
        pygame.draw.rect(obraz, (255, 0, 0), pocisk_1)
        pocisk_1.x += 2
    if pocisk_2.x < szerokoscOkna:
        pygame.draw.rect(obraz, (0, 0, 255), pocisk_2)
        pocisk_2.x -= 2
    if (statek_1.x + rozmiargracza_1 > pocisk_2.x and statek_1.x < pocisk_2.x) and \
            (statek_1.y + rozmiargracza_1 > pocisk_2.y and statek_1.y < pocisk_2.y):
        kolorstatku1 -= 25
        pocisk_2 = pygame.Rect(50, wysokoscOkna, rozmiarpocisku_2, rozmiarpocisku_2)
    if (statek_2.x + rozmiargracza_2 > pocisk_1.x and statek_2.x < pocisk_1.x) and \
            (statek_2.y + rozmiargracza_2 > pocisk_1.y and statek_2.y < pocisk_1.y):
        kolorstatku2 -= 25
        pocisk_1 = pygame.Rect(szerokoscOkna, 50, rozmiarpocisku_1, rozmiarpocisku_1)
    # poruszanie sie
    statek_1.x += ruchxAD()
    statek_1.y += ruchyWS()
    statek_2.x += ruchxLR()
    statek_2.y += ruchyUD()
    # teleportacja na granicach mapy
    statek_1.x = granicePlanszyX(statek_1.x)
    statek_1.y = granicePlanszyY(statek_1.y)
    statek_2.x = granicePlanszyX(statek_2.x)
    statek_2.y = granicePlanszyY(statek_2.y)

    pygame.draw.rect(obraz, (kolorstatku1, 0, 0), statek_1)
    pygame.draw.rect(obraz, (0, 0, kolorstatku2), statek_2)
    pygame.display.flip()
    off()