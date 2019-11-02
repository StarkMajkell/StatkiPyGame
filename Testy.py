import pygame
import sys

pygame.init()  # musi być
# górna belka
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
clock_tick_rate = 2000
my_missile_list = []
music = pygame.mixer.music.load("pif.mp3")


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


def wynikNapis(killRed, killBlue):
    napis = killRed + " : " + killBlue
    label = czcionka.render(napis, 1, kolorNapisu)
    obraz.blit(label, (szerokoscOkna / 2 - 60, 10))


background = pygame.image.load("background.jpg").convert()
statekGrafika_1 = pygame.image.load("Statek1-Blue.png")
statekGrafika_2 = pygame.image.load("Statek1-Red.png")
bonusy_speed = pygame.image.load("Speed.png")


# MOduł funkcji od strzelania
class Projectile():
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def missile(self):
        self.x += self.vx
        self.y += self.vy
        pygame.draw.rect(obraz, (255, 0, 0), [self.x, self.y, rozmiarpocisku_1, rozmiarpocisku_2])
        if self.x >= szerokoscOkna:
            pass
        if self.x < 0:
            pass


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

    wynikNapis(killRed, killBlue)
    pygame.display.flip()
    clock.tick(clock_tick_rate)
    obraz.blit(background, [0, 0])
    # obraz.blit(bonusy_speed, [100, 100])
    for b in my_missile_list:
        b.missile()
    obraz.blit(statekGrafika_1, [statek_1.x, statek_1.y])
    obraz.blit(statekGrafika_2, [statek_2.x, statek_2.y])
    # moduł pod pozycje pocisków
    shotplayer1x = statek_1.x + rozmiargracza_1
    shotplayer1y = statek_1.y + rozmiargracza_1 / 2 - rozmiarpocisku_1 / 2
    shotplayer2x = statek_2.x + rozmiargracza_2 / 2
    shotplayer2y = statek_2.y + rozmiargracza_2 / 2 - rozmiarpocisku_2 / 2
    for event in pygame.event.get():
        # gracz 1 strzelanie
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            my_missile_list.append(Projectile(shotplayer1x, shotplayer1y, 1, 0))
            pygame.mixer.music.play(0)
            pygame.mixer.music.play(1)
        # gracz drugi strzelanie
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            my_missile_list.append(Projectile(shotplayer2x, shotplayer2y, -1, 0))
        elif event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)