import pygame
import sys

pygame.init()  # musi być

#moduł ze zmiennymi
wysokoscOkna=600
szerokoscOkna=1360
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
pocisk_1 = pygame.Rect(szerokoscOkna+1, 50, rozmiarpocisku_1, rozmiarpocisku_1)
pocisk_2 = pygame.Rect(50, wysokoscOkna+1, rozmiarpocisku_2, rozmiarpocisku_2)
my_missile_list=[]

#moduł funkcji


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

##MOduł funkcji od strzelania

class Projectile():
    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def missile(self):
        self.x += self.vx
        self.y += self.vy
        pygame.draw.rect(obraz, (255,0,0), [self.x, self.y, rozmiarpocisku_1, rozmiarpocisku_2])
        if self.x >= szerokoscOkna:
            self.x=0
        if self.x <0:
            self.x=szerokoscOkna

while True:
    obraz.fill((0, 0, 0))


    for event in pygame.event.get():
        #gracz 1 strzelanie
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            my_missile_list.append(Projectile(shotplayer1x,shotplayer1y,1,0))

        #gracz drugi strzelanie
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            my_missile_list.append(Projectile(shotplayer2x,shotplayer2y,-1,0))

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
    shotplayer1y = statek_1.y + rozmiargracza_1 / 2 - rozmiarpocisku_1 / 2
    shotplayer2x = statek_2.x + rozmiargracza_2 / 2
    shotplayer2y = statek_2.y + rozmiargracza_2 / 2 - rozmiarpocisku_2 / 2

    for b in my_missile_list:
        b.missile()

    pygame.draw.rect(obraz, (kolorstatku1, 0, 0), statek_1)
    pygame.draw.rect(obraz, (0, 0, kolorstatku2), statek_2)
    pygame.display.flip()
    off()