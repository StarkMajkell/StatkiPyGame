import pygame
import sys

pygame.init()  # musi być
pygame.display.set_caption('Statki')
a = pygame.image.load('Logo.png')
pygame.display.set_icon(a)

#moduł ze zmiennymi
wysokoscOkna=600
szerokoscOkna=1280
rozmiargracza_1=50
rozmiargracza_2=50
rozmiarpocisku_1=12
rozmiarpocisku_2=6
kolorstatku1=255
kolorstatku2=255
rozmiarOkna=(szerokoscOkna,wysokoscOkna)
obraz = pygame.display.set_mode(rozmiarOkna)
statek_1 = pygame.Rect(0, wysokoscOkna/2, rozmiargracza_1, rozmiargracza_1)
statek_2 = pygame.Rect(szerokoscOkna-rozmiargracza_2, (wysokoscOkna/2), rozmiargracza_2, rozmiargracza_2)
my_missile_list=[]

killRed = 0
killBlue = 0
killRed = str(killRed)
killBlue = str(killBlue)
kolorNapisu = (255, 255, 0)
czcionka = pygame.font.SysFont("Comic Sans MS", 60)

background = pygame.image.load("background.jpg").convert()
statekGrafika_1 = pygame.image.load("Statek1-Blue.png")
statekGrafika_2 = pygame.image.load("Statek1-Red.png")
pociskGrafika = pygame.image.load('pocisk.png')

#moduł resetowania pozycji
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

#moduł poruszania sie
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

class Projectile(pygame.sprite.Sprite):
    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        pygame.sprite.Sprite.__init__(self)
        self.image = pociskGrafika
        self.rect = pociskGrafika.get_rect()
    def missile(self):
        self.x += self.vx
        self.y += self.vy
        #pygame.draw.rect(obraz, (255,0,0), [self.x, self.y, rozmiarpocisku_1, rozmiarpocisku_2])
        obraz.blit(self.image, [self.x, self.y])
        #if pygame.sprite.spritecollide(self.rect,statek_1,True):


#Moduł od kolizji
class Game:
    def __init__(self):
        self.dino = Dino()
        self.FPS = 60
        self.fpsClock = pygame.time.Clock()
        self.Projectile = pygame.sprite.Group()



def wynikNapis(killRed,killBlue):
    napis = killRed + " : " + killBlue
    label = czcionka.render(napis, 1, kolorNapisu)
    obraz.blit(label, (szerokoscOkna/2-60, 10))



while True:

# poruszanie sie
    statek_1.x += ruchxAD()
    statek_1.y += ruchyWS()
    statek_2.x += ruchxLR()
    statek_2.y += ruchyUD()

#sprawdzanie kolizji

# teleportacja na granicach mapy
    statek_1.x = granicePlanszyX(statek_1.x)
    statek_1.y = granicePlanszyY(statek_1.y)
    statek_2.x = granicePlanszyX(statek_2.x)
    statek_2.y = granicePlanszyY(statek_2.y)
#moduł pod pozycje pocisków
    shotplayer1x = statek_1.x + rozmiargracza_1
    shotplayer1y = statek_1.y + rozmiargracza_1 / 2 - rozmiarpocisku_1 / 2
    shotplayer2x = statek_2.x + rozmiargracza_2 / 2
    shotplayer2y = statek_2.y + rozmiargracza_2 / 2 - rozmiarpocisku_2 / 2


    wynikNapis(killRed,killBlue)
    obraz.blit(background, [0, 0])
    obraz.blit(statekGrafika_1, [statek_1.x, statek_1.y])
    obraz.blit(statekGrafika_2, [statek_2.x, statek_2.y])

    for b in my_missile_list:
        b.missile()

    for event in pygame.event.get():
        #gracz 1 strzelanie
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            my_missile_list.append(Projectile(shotplayer1x,shotplayer1y,2,0))
        if event.type == pygame.KEYUP and event.key == pygame.K_f:               #<---- potezna moc ogniowa dla czerwonego
            my_missile_list.append(Projectile(shotplayer1x,shotplayer1y,2,0))

        #gracz drugi strzelanie
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            my_missile_list.append(Projectile(shotplayer2x,shotplayer2y-5,-2,0)) #<--- podwójny strzal dla niebieskiego
            my_missile_list.append(Projectile(shotplayer2x,shotplayer2y+13,-2,0))

    pygame.display.flip()

    off()