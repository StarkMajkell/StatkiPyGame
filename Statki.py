import pygame
import sys
import random

pygame.init()  # musi być
pygame.display.set_caption('Statki')
a = pygame.image.load('Logo.png')
pygame.display.set_icon(a)

#moduł ze zmiennymi
wysokoscOkna=600
szerokoscOkna=1280
rozmiargracza_1=50
rozmiargracza_2=50
kolorstatku1=255
kolorstatku2=255
rozmiarOkna=(szerokoscOkna,wysokoscOkna)
obraz = pygame.display.set_mode(rozmiarOkna)
statek_1 = pygame.Rect(0, wysokoscOkna/2, rozmiargracza_1, rozmiargracza_1)
statek_2 = pygame.Rect(szerokoscOkna-rozmiargracza_2-40, (wysokoscOkna/2), rozmiargracza_2, rozmiargracza_2)
my_missile_list=[]
zyciegracza1=0
zyciegracza2=szerokoscOkna-200
timer_strzalu=0
timer_strzalu2=0


killRed = 0
killBlue = 0
kolorNapisu = (255, 255, 0)
czcionka = pygame.font.SysFont("Comic Sans MS", 60)

background = pygame.image.load("background.jpg").convert()
statekGrafika_1 = pygame.image.load("Statek1-Blue.png")
statekGrafika_1_mask=pygame.mask.from_surface(statekGrafika_1)
statekGrafika_1_rect=statekGrafika_1.get_rect()
statekGrafika_2 = pygame.image.load("Statek1-Red.png")
statekGrafika_2_mask=pygame.mask.from_surface(statekGrafika_2)
pociskGrafika = pygame.image.load('pocisk.png').convert_alpha()
pociskikolor=[]
pociskikolor.append(pygame.image.load('pocisk.png'))
pociskikolor.append(pygame.image.load('pocisk2.png'))
pociskikolor.append(pygame.image.load('pocisk3.png'))


pociskGrafika_mask=pygame.mask.from_surface(pociskGrafika)
life = pygame.image.load('life.png')
music = pygame.mixer.music.load("pif.mp3")




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

class gracz(pygame.sprite.Sprite):
    def __init__(self,x,y,vx,vy):
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
    def __init__(self,x,y,vx,vy,rozrzut):
        self.x = x
        self.kolizja1 = 0
        self.kolizja2 = 0
        self.y = y
        self.rozrzut=rozrzut
        self.vx = vx
        self.vy = vy +(rozrzut/15)
        #self.image = pociskGrafika
        self.image = pociskikolor[rand]
        self.rect = self.image.get_rect()
        self.istnieje=1
    def missile(self):
        if (self.istnieje==1):
            self.x += self.vx
            self.y += self.vy
            obraz.blit(self.image, [self.x, self.y])
    def siongracz1(self):
        if statek_1.x<(self.x+12)<(statek_1.x+rozmiargracza_1) and statek_1.y<(self.y)<(statek_1.y+rozmiargracza_1) and self.vx<0:
            self.kolizja1=1
    def siongracz2(self):
        if statek_2.x<(self.x)<(statek_2.x+rozmiargracza_2) and statek_2.y<(self.y)<(statek_2.y+rozmiargracza_2)and self.vx>0:
            self.kolizja2=1
    def outofmap(self):
        if self.x>szerokoscOkna or self.x<0:
            self.y = 2*wysokoscOkna+20
            self.istnieje=0
        if self.y>wysokoscOkna or self.y<0:
            self.y = 2*wysokoscOkna+20
            self.istnieje=0






#Moduł od kolizji


def wynikNapis(killRed, killBlue):
    killRed = str(killRed)
    killBlue = str(killBlue)
    napis = killRed + " : " + killBlue
    label = czcionka.render(napis, 1, kolorNapisu)
    obraz.blit(label, (szerokoscOkna / 2 - 60, 10))



while True:
    obraz.blit(background, [0, 0])
    #timer strzalu gracza 1
    if timer_strzalu >0:
        timer_strzalu -=1

    #timer strzalu gracza2
    if timer_strzalu2 > 0:
        timer_strzalu2 -= 1


    rozrzut = random.randint(-2, 2)#róra randomizacja rorzuty góra dół
    rand = random.randint(1, 2)#randomizacja koloru pocisków


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
    #moduł pod pozycje pocisków
    shotplayer1x = statek_1.x + rozmiargracza_1
    shotplayer1y = statek_1.y + rozmiargracza_1 / 2
    shotplayer2x = statek_2.x + rozmiargracza_2 / 2
    shotplayer2y = statek_2.y + rozmiargracza_2 / 2

    #sprawdzanie zderzenia statków
    offset=(statek_1.x-statek_2.x,statek_1.y-statek_2.y)
    kolizja=statekGrafika_1_mask.overlap(statekGrafika_2_mask, offset)
    if kolizja:
        zyciegracza1-=1
        zyciegracza2+=1


    wynikNapis(killRed,killBlue)

    obraz.blit(statekGrafika_1, [statek_1.x, statek_1.y])
    obraz.blit(statekGrafika_2, [statek_2.x, statek_2.y])


    for b in my_missile_list:
        b.missile()
        b.siongracz1()
        if b.kolizja1==1:
            zyciegracza1-=5
            b.kolizja1=0
            b.y=2*wysokoscOkna+20
            b.istnieje=0
            #killRed += 1 #<-------------Odplala licznik kolizji
        b.siongracz2()
        if b.kolizja2 == 1:
            zyciegracza2 += 5
            b.kolizja2 = 0
            b.y = 2*wysokoscOkna+20
            b.istnieje=0
            #killBlue += 1#<-------------Odplala licznik kolizji
        b.outofmap()



    #zycie
    if zyciegracza1 <= -200:
        zyciegracza1 = 0
        killRed += 1
        statek_1 = pygame.Rect(0, 100, rozmiargracza_1, rozmiargracza_1)

    if zyciegracza2 >= szerokoscOkna:
        zyciegracza2 = szerokoscOkna - 200
        killBlue += 1
        statek_2 = pygame.Rect(szerokoscOkna - rozmiargracza_2 - 40, (wysokoscOkna - 100), rozmiargracza_2, rozmiargracza_2)

#moduł wystrzeliwania pocisków
    #gracz 1
    if pygame.key.get_pressed()[pygame.K_f] and timer_strzalu < 2:
        my_missile_list.append(Projectile(shotplayer1x, shotplayer1y, 2.7, 0, rozrzut+(10*ruchyWS())))
        pygame.mixer.music.play(0)
        pygame.mixer.music.play(1)
        timer_strzalu += 13
    #gracz 2)
    if pygame.key.get_pressed()[pygame.K_p] and timer_strzalu2 < 2:
        rand = random.randint(0,0)
        my_missile_list.append(Projectile(shotplayer2x, shotplayer2y - 6, -2.6, 0, rozrzut+(10*ruchyUD())))
        my_missile_list.append(Projectile(shotplayer2x, shotplayer2y - 16, -2.54, 0, rozrzut-0.2+(10*ruchyUD())))
        my_missile_list.append(Projectile(shotplayer2x, shotplayer2y + 13, -2.6, 0, rozrzut+(10*ruchyUD())))
        my_missile_list.append(Projectile(shotplayer2x, shotplayer2y + 23, -2.54, 0, rozrzut+0.2+(10*ruchyUD())))
        pygame.mixer.music.play(0)
        pygame.mixer.music.play(1)
        timer_strzalu2 += 41

    obraz.blit(life, [zyciegracza1, 0])
    obraz.blit(life, [zyciegracza2, 0])
    pygame.display.flip()

    off()