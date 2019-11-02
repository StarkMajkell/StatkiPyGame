import pygame
import sys
import pygame.locals

pygame.init()  # musi być
pygame.display.set_caption('Statki')
a = pygame.image.load('Logo.png')
pygame.display.set_icon(a)

# moduł ze zmiennymi
wysokoscOkna = 600
szerokoscOkna = 1280
rozmiargracza_1 = 50
rozmiargracza_2 = 50
kolorstatku1 = 255
kolorstatku2 = 255
rozmiarOkna = (szerokoscOkna, wysokoscOkna)
obraz = pygame.display.set_mode(rozmiarOkna)
statek_1 = pygame.Rect(0, wysokoscOkna / 2, rozmiargracza_1, rozmiargracza_1)
statek_2 = pygame.Rect(szerokoscOkna - rozmiargracza_2, (wysokoscOkna / 2), rozmiargracza_2, rozmiargracza_2)
my_missile_list = []
zyciegracza1 = 0
zyciegracza2 = szerokoscOkna - 200

killRed = 0
killBlue = 0
killRed = str(killRed)
killBlue = str(killBlue)
kolorNapisu = (255, 255, 0)
czcionka = pygame.font.SysFont("Comic Sans MS", 60)

background = pygame.image.load("background.jpg").convert()
statekGrafika_1 = pygame.image.load("Statek1-Blue.png")
statekGrafika_1_mask = pygame.mask.from_surface(statekGrafika_1)
statekGrafika_1_rect = statekGrafika_1.get_rect()
statekGrafika_2 = pygame.image.load("Statek1-Red.png")
statekGrafika_2_mask = pygame.mask.from_surface(statekGrafika_2)
pociskGrafika = pygame.image.load('pocisk.png').convert_alpha()
pociskGrafika_mask = pygame.mask.from_surface(pociskGrafika)
life = pygame.image.load('life.png')

music = pygame.mixer.music.load("pif.mp3")

# moduł resetowania pozycji
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


# moduł poruszania sie
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


##Moduł funkcji od strzelania

class gracz(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pociskGrafika
        self.rect = pociskGrafika.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def missile(self):
        self.x += self.vx
        self.y += self.vy
        obraz.blit(self.image, [self.x, self.y])


class Projectile():
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.kolizja = 0
        self.y = y
        self.vx = vx
        self.vy = vy
        self.image = pociskGrafika
        self.rect = self.image.get_rect()

    def missile(self):
        self.x += self.vx
        self.y += self.vy
        obraz.blit(self.image, [self.x, self.y])

    def siongracz1(self):
        if statek_1.x < (self.x + 12) < (statek_1.x + rozmiargracza_1) and statek_1.y < (self.y + 3) < (
                statek_1.y + rozmiargracza_1):
            self.kolizja = 1


# Moduł od kolizji


def wynikNapis(killRed, killBlue):
    napis = killRed + " : " + killBlue
    label = czcionka.render(napis, 1, kolorNapisu)
    obraz.blit(label, (szerokoscOkna / 2 - 60, 10))


while True:
    obraz.blit(background, [0, 0])
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
    # moduł pod pozycje pocisków
    shotplayer1x = statek_1.x + rozmiargracza_1
    shotplayer1y = statek_1.y + rozmiargracza_1 / 2
    shotplayer2x = statek_2.x + rozmiargracza_2 / 2
    shotplayer2y = statek_2.y + rozmiargracza_2 / 2

    # sprawdzanie zderzenia statków
    offset = (statek_1.x - statek_2.x, statek_1.y - statek_2.y)
    kolizja = statekGrafika_1_mask.overlap(statekGrafika_2_mask, offset)
    if kolizja:
        zyciegracza1 -= 1
        zyciegracza2 += 1

    wynikNapis(killRed, killBlue)

    obraz.blit(statekGrafika_1, [statek_1.x, statek_1.y])
    obraz.blit(statekGrafika_2, [statek_2.x, statek_2.y])

    for b in my_missile_list:
        b.missile()
        b.siongracz1()
        if b.kolizja == 1:
            zyciegracza1 -= 5
            b.kolizja = 0
            b.y = wysokoscOkna + 20

    # zycie
    if zyciegracza1 <= -200:
        zyciegracza1 = 0
        killRed += '1'

    for event in pygame.event.get():
        # gracz 1 strzelanie
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            my_missile_list.append(Projectile(shotplayer1x, shotplayer1y, 2, 0))
            pygame.mixer.music.play(0)
            pygame.mixer.music.play(1)
        if event.type == pygame.KEYUP and event.key == pygame.K_f:  # <---- potezna moc ogniowa dla czerwonego
            my_missile_list.append(Projectile(shotplayer1x, shotplayer1y, 2, 0))
            pygame.mixer.music.play(0)
            pygame.mixer.music.play(1)

        # gracz drugi strzelanie
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            my_missile_list.append(
                Projectile(shotplayer2x, shotplayer2y - 5, -2, 0))  # <--- podwójny strzal dla niebieskiego
            my_missile_list.append(Projectile(shotplayer2x, shotplayer2y + 13, -2, 0))

    obraz.blit(life, [zyciegracza1, 0])
    obraz.blit(life, [zyciegracza2, 0])
    pygame.display.flip()

    off()