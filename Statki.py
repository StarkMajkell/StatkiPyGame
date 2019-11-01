import pygame
import sys

pygame.init()  # musi być
#górna belka
pygame.display.set_caption('Statki')
a = pygame.image.load('Logo.png')
pygame.display.set_icon(a)

# moduł ze zmiennymi
wysokoscOkna = 700
szerokoscOkna = 1280
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
killRed = 0
killBlue = 0
killRed = str(killRed)
killBlue = str(killBlue)
kolorNapisu = (255, 255, 0)
czcionka = pygame.font.SysFont("Comic Sans MS", 60)
clock = pygame.time.Clock()
clock_tick_rate=200
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
def wynikNapis(killRed,killBlue):
    napis = killRed + " : " + killBlue
    label = czcionka.render(napis, 1, kolorNapisu)
    obraz.blit(label, (szerokoscOkna/2-60, 10))
background = pygame.image.load("background.jpg").convert()
statekGrafika_1 = pygame.image.load("Statek1-Blue.png")
statekGrafika_2 = pygame.image.load("Statek1-Red.png")
bonusy_speed = pygame.image.load("Speed.png")

# pętla programu program
while True:

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

    wynikNapis(killRed,killBlue)
    pygame.display.flip()
    clock.tick(clock_tick_rate)
    obraz.blit(background, [0, 0])
    obraz.blit(bonusy_speed, [100, 100])
    obraz.blit(statekGrafika_1, [statek_1.x, statek_1.y])
    obraz.blit(statekGrafika_2, [statek_2.x, statek_2.y])

    off()