import pygame
import sys
import random

pygame.init()  # musi być
pygame.display.set_caption('Statki')
a = pygame.image.load('Grafa/Logo.png')
pygame.display.set_icon(a)

clock = pygame.time.Clock()

# moduł ze zmiennymi
wysokoscOkna = 720
szerokoscOkna = 1280
rozmiarOkna = (szerokoscOkna, wysokoscOkna)
obraz = pygame.display.set_mode(rozmiarOkna)
zyciegracza1 = 0
zyciegracza2 = szerokoscOkna - 200
opcjemenu = -1
my_missile_list = []
lista_statków = []
parametryplayer1 = []
parametryplayer2 = []
parametryplayer3 = []
parametryplayer4 = []
globalnytimer = 0
rozrzutmenu = 20
liczbagraczy = 4
rollm = 0
rollmstatic = 0
startmouse = 0
tabPaskow = []

killRed = 0
killBlue = 0
kolorNapisu = (0, 255, 255)
czcionka = pygame.font.Font("Czcionki/digital-7.ttf", 40)
background = pygame.image.load("Grafa/background2.jpg").convert()
menu = pygame.image.load("Grafa/backgroundmenu.jpg").convert()
settings = pygame.image.load('Grafa/settings.jpg').convert()
przyciskback = pygame.image.load('Grafa/przyciskback.png')
przycisk = pygame.image.load('Grafa/przycisk.png')
staty = pygame.image.load('Grafa/staty.png')
pasek = pygame.image.load('Grafa/pasek.png')
czaszka = pygame.image.load('Grafa/czaszka.png')
staty2 = pygame.image.load('Grafa/staty2.png')
staty3 = pygame.image.load('Grafa/staty3.png')
staty4 = pygame.image.load('Grafa/staty4.png')
przycisksettings = pygame.image.load('Grafa/przycisksettings.png')
przyciskstart = pygame.image.load('Grafa/przyciskstart.png')
przyciskexit = pygame.image.load('Grafa/przyciskexit.png')
przycisk2 = pygame.image.load('Grafa/przycisk2.png')
przycisk3 = pygame.image.load('Grafa/przycisk3.png')
przycisk4 = pygame.image.load('Grafa/przycisk4.png')
pustemenu = pygame.image.load('Grafa/pustemenu.jpg')
przycisksilnik = pygame.image.load('Grafa/przycisksilnik.png')
statek1 = pygame.image.load("Grafa/Statek1-Blue1.png")
statek2 = pygame.image.load("Grafa/Statek3.png")
statek3 = pygame.image.load("Grafa/Statek1-Red1.png")
pocisk1 = pygame.image.load('Grafa/pocisk.png')
pocisk2 = pygame.image.load('Grafa/pocisk2.png')
pocisk4 = pygame.image.load('Grafa/pocisk4.png')
pocisk3 = pygame.image.load('Grafa/pocisk3.png')
tabelaplayer1=pygame.image.load('Grafa/statyp1.png')
tabelaplayer2=pygame.image.load('Grafa/statyp2.png')
tabelaplayer3=pygame.image.load('Grafa/statyp3.png')
tabelaplayer4=pygame.image.load('Grafa/statyp4.png')
life1 = pygame.image.load('Grafa/life1.png')
pygame.mixer.music.load("Dźwięki/intel.mp3")
grafaStatków = [statek1, statek2, statek3]
pociski = [pocisk1, pocisk2, pocisk3, pocisk4]
pygame.mixer.music.play(-1)


# moduł resetowania pozycji
def granicePlanszyX(pozycja):
    if pozycja >= szerokoscOkna:
        pozycja = szerokoscOkna
    if pozycja < 0:
        pozycja = 0
    return pozycja


def granicePlanszyY(pozycja):
    if pozycja >= wysokoscOkna:
        pozycja = wysokoscOkna
    if pozycja < 0:
        pozycja = 0
    return pozycja


def hitBox(pozycjax, pozycjay, pozycjax2, pozycjay2, rozmiar):
    if (pozycjax + rozmiar >= pozycjax2) and (pozycjax - rozmiar <= pozycjax2) and (
            pozycjay + rozmiar >= pozycjay2) and (pozycjay - rozmiar <= pozycjay2):
        return 1


# moduł poruszania sie
def ruch(x, y, z, h):
    tab = [0, 0]
    if pygame.key.get_pressed()[x]:
        tab[0] += -1
    elif pygame.key.get_pressed()[y]:
        tab[0] += 1
    else:
        tab[0] += 0
    if pygame.key.get_pressed()[z]:
        tab[1] += -1
    elif pygame.key.get_pressed()[h]:
        tab[1] += 1
    else:
        tab[1] += 0
    return tab[:]


def off():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)


##Klasa gracza
class Statek():
    def __init__(self, pozycjax, pozycjay, nrstatku, player, pozycjaxshot, pozycjayshot, predkoscxshot, predkoscyshot,
                 modyfikatorrozrzutu, modyfikatorrozstrzalu, hp, rodzajpocisku, speed, energia, dmg, firerate):
        self.image = grafaStatków[nrstatku]
        self.x = pozycjax
        self.y = pozycjay
        self.speed = speed
        self.firerate = firerate
        self.player = player
        self.energia = energia
        self.dmg = dmg
        self.pozycjaxshot = pozycjaxshot
        self.pozycjayshot = pozycjayshot
        self.predkoscxshot = predkoscxshot
        self.predkoscyshot = predkoscyshot
        self.modyfikatorrozrzutu = modyfikatorrozrzutu
        self.modyfikatorrozstrzalu = modyfikatorrozstrzalu
        self.hp = hp
        self.basehp = hp
        self.rodzajpocisku = pociski[rodzajpocisku]

    def update(self):
        tab1 = ruch(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        tab2 = ruch(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
        tab3 = ruch(pygame.K_j, pygame.K_l, pygame.K_i, pygame.K_k)
        tab4 = ruch(pygame.K_KP4, pygame.K_KP6, pygame.K_KP8, pygame.K_KP5)
        if self.player == 1:
            self.x += tab1[0] * self.speed / 10
            self.y += tab1[1] * self.speed / 10
            tabPaskow[0].hp= (self.hp/self.basehp)
        #######################################
        if self.player == 2:
            self.x += tab2[0] * self.speed / 10
            self.y += tab2[1] * self.speed / 10
            tabPaskow[1].hp= (self.hp/self.basehp)
        ########################################
        if self.player == 3:
            self.x += tab3[0] * self.speed / 10
            self.y += tab3[1] * self.speed / 10
            tabPaskow[2].hp= (self.hp/self.basehp)
        #########################################
        if self.player == 4:
            self.x += tab4[0] * self.speed / 10
            self.y += tab4[1] * self.speed / 10
            tabPaskow[3].hp= (self.hp/self.basehp)
        if self.y >= wysokoscOkna - 60:
            self.y = wysokoscOkna - 61
        if self.x < 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0
        if self.x >= szerokoscOkna - 60:
            self.x = szerokoscOkna - 61



        obraz.blit(self.image, [self.x, self.y])

    def shot(self):
        tab1 = ruch(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        tab2 = ruch(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
        tab3 = ruch(pygame.K_j, pygame.K_l, pygame.K_i, pygame.K_k)
        tab4 = ruch(pygame.K_KP4, pygame.K_KP6, pygame.K_KP8, pygame.K_KP5)
        if pygame.key.get_pressed()[pygame.K_f]:
            if self.player == 1:
                my_missile_list.append(
                    Projectile(self.x + self.pozycjaxshot, self.y + self.pozycjayshot, self.predkoscxshot,
                               self.predkoscyshot,
                               rozrzut * self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * tab1[1]),
                               self.rodzajpocisku))

        if pygame.key.get_pressed()[pygame.K_p]:
            if self.player == 2:
                my_missile_list.append(
                    Projectile(self.x + self.pozycjaxshot, self.y + self.pozycjayshot, self.predkoscxshot,
                               self.predkoscyshot,
                               rozrzut * self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * tab2[1]),
                               self.rodzajpocisku))

        if pygame.key.get_pressed()[pygame.K_u]:
            if self.player == 3:
                my_missile_list.append(
                    Projectile(self.x + self.pozycjaxshot, self.y + self.pozycjayshot, self.predkoscxshot,
                               self.predkoscyshot,
                               rozrzut * self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * tab3[1]),
                               self.rodzajpocisku))

        if pygame.key.get_pressed()[pygame.K_KP9]:
            if self.player == 4:
                my_missile_list.append(
                    Projectile(self.x + self.pozycjaxshot, self.y + self.pozycjayshot, self.predkoscxshot,
                               self.predkoscyshot,
                               rozrzut * self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * tab4[1]),
                               self.rodzajpocisku))


class paski():
    def __init__(self, grafa, x, y):
        self.grafa = grafa
        self.hp = 1
        self.x = x
        self.y = y
        self.xx = 0



    def rusuj(self):
        if self.x < szerokoscOkna/2:
            self.xx = self.x + 200*(self.hp+1)
        else:
            self.xx = self.x - 200*(self.hp+1)

        obraz.blit(self.grafa, [self.xx, self.y])


# NAJWAZNIEJSZA KLASA TUTAJ NIC NIE RUSZAC!!!

class Projectile():
    def __init__(self, x, y, vx, vy, rozrzut, rodzajpocisku):
        self.x = x
        self.y = y
        self.rozrzut = rozrzut
        self.vx = vx + (rozrzut / 50)
        self.vy = vy + (rozrzut / 50)
        self.image = rodzajpocisku
        self.istnieje = 1

    def missile(self):
        if (self.istnieje == 1):
            self.x += self.vx
            self.y += self.vy
            obraz.blit(self.image, [self.x, self.y])

    def trafienie(self):
        for b in lista_statków:
            if b.x < self.x < b.x + 60 and b.y < self.y < b.y + 60:
                b.hp -= 1
                self.istnieje = 0



    def outofmap(self):
        if self.x > szerokoscOkna or self.x < 0:
            self.istnieje = 0
        if self.y > wysokoscOkna or self.y < 0:
            self.istnieje = 0


def wynikNapis(killRed, killBlue):  # funckja od wyswietlania wyniku
    przesuniecieR = 0
    if killRed > 19:
        przesuniecieR += 10
    if killRed > 99:
        przesuniecieR += 25
    killRed = str(killRed)
    killBlue = str(killBlue)

    napis1 = killRed
    napis2 = " : "
    napis3 = killBlue

    label1 = czcionka.render(napis1, 1, kolorNapisu)
    label2 = czcionka.render(napis2, 1, kolorNapisu)
    label3 = czcionka.render(napis3, 1, kolorNapisu)

    obraz.blit(label1, (szerokoscOkna / 2 - 50 - przesuniecieR, 30))
    obraz.blit(label2, (szerokoscOkna / 2 - 20, 30))
    obraz.blit(label3, (szerokoscOkna / 2 + 20, 30))


def przyciski(y):
    if 172 < mouse[0] < 212 and y + ykoncowy < mouse[1] < y + 40 + ykoncowy:
        if click[0]:
            obraz.blit(przycisk4, [172, y + ykoncowy])
            return 1
        else:
            obraz.blit(przycisk2, [172, y + ykoncowy])
            return 0
    if 380 < mouse[0] < 420 and y + ykoncowy < mouse[1] < y + 40 + ykoncowy:
        if click[0]:
            obraz.blit(przycisk3, [380, y + ykoncowy])
            return -1
        else:
            obraz.blit(przycisk2, [380, y + ykoncowy])
            return 0
    else:
        return 0


################Pętla programu całego#######################
while True:
    ################################################################################
    # MODUŁ OD WCZYTYWANIA CONFIGU
    if opcjemenu == -1:
        file = open('config/parametry.txt', 'r').read()
        lines = file.split('\n')
        for line in lines:
            x = line
            x = int(x)
            parametryplayer1.append(x)
        file = open('config/parametry2.txt', 'r').read()
        lines = file.split('\n')
        for line in lines:
            x = line
            x = int(x)
            parametryplayer2.append(x)
        file = open('config/parametry3.txt', 'r').read()
        lines = file.split('\n')
        for line in lines:
            x = line
            x = int(x)
            parametryplayer3.append(x)
        file = open('config/parametry4.txt', 'r').read()
        lines = file.split('\n')
        for line in lines:
            x = line
            x = int(x)
            parametryplayer4.append(x)

        if liczbagraczy >= 1:
            lista_statków.append(Statek(*parametryplayer1))
            if liczbagraczy >= 2:
                lista_statków.append(Statek(*parametryplayer2))
                if liczbagraczy >= 3:
                    lista_statków.append(Statek(*parametryplayer3))
                    if liczbagraczy == 4:
                        lista_statków.append(Statek(*parametryplayer4))
        opcjemenu = 0

    #########################################################################################################
    # MENU GLOWNE
    if opcjemenu == 0:
        while True:
            obraz.blit(menu, [0, 0])
            obraz.blit(przyciskstart, [0, 0])
            obraz.blit(przycisksettings, [0, 40])
            obraz.blit(przycisksilnik, [0, 80])
            obraz.blit(przyciskexit, [szerokoscOkna - 220, wysokoscOkna - 76])
            mouse = pygame.mouse.get_pos()
            # obraz.blit(pocisk, [mouse[0], mouse[1]])
            click = pygame.mouse.get_pressed()
            if 0 < mouse[0] < 220 and 0 < mouse[1] < 36:
                if click[0]:
                    opcjemenu = 1
                    break
            if 0 < mouse[0] < 220 and 40 < mouse[1] < 76:
                if click[0]:
                    opcjemenu = 2
                    break
            if 0 < mouse[0] < 220 and 80 < mouse[1] < 116:
                if click[0]:
                    opcjemenu = 3
                    break
            if szerokoscOkna - 220 < mouse[0] < szerokoscOkna and wysokoscOkna - 76 < mouse[1] < wysokoscOkna - 40:
                if click[0]:
                    sys.exit(0)

            pygame.display.flip()
            off()

    #########################################################################################################
    drugafaza = 1  # <--------moje zmienne do setingsów
    lokalnytimer = 230
    startmouse = 0
    pozycjamouse = 0
    pozycjakoncowa = 0
    ykoncowy = -500
    step1 = 0
    step2 = -720
    step3 = -1440
    step4 = -2160
    ################################################################################
    # menu ustawienia
    if opcjemenu == 2:
        while True:
            obraz.blit(settings, [0, 0])

            lokalnytimer -= 1
            if lokalnytimer < 0:
                lokalnytimer = 0
            if drugafaza == 1:
                if ykoncowy < 0:
                    ykoncowy += lokalnytimer / 40
                else:
                    ykoncowy = 0
                    drugafaza = 2

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            ykoncowy += pozycjakoncowa / 50
            if 212 < mouse[0] < 382:
                if click[0] == True:
                    pozycjamouse = mouse[1] - startmouse
                else:
                    pozycjakoncowa = pozycjamouse
                    startmouse = mouse[1]

            obraz.blit(czaszka, [700, 0])
            obraz.blit(przyciskback, [szerokoscOkna - 220, wysokoscOkna - 36])
            obraz.blit(pasek, [219, -720 - (ykoncowy) / 4])
            obraz.blit(staty, [178, step1 + ykoncowy])
            obraz.blit(staty2, [178, step2 + ykoncowy])
            obraz.blit(staty3, [178, step3 + ykoncowy])
            obraz.blit(staty4, [178, step4 + ykoncowy])

            lista_statków[0].basehp += przyciski(80)
            lista_statków[0].energia += przyciski(160)
            lista_statków[0].firerate += przyciski(240)
            lista_statków[0].speed += przyciski(320)
            lista_statków[0].dmg += przyciski(400)
            lista_statków[0].predkoscyshot += przyciski(480)
            lista_statków[0].predkoscxshot += przyciski(560)
            lista_statków[0].modyfikatorrozrzutu += przyciski(640)
            hapeki1 = lista_statków[0].basehp
            hapeki1 = str(hapeki1)
            label2 = czcionka.render(hapeki1, 1, kolorNapisu)
            obraz.blit(label2, (260, 83 + ykoncowy))
            energie1 = lista_statków[0].energia
            energie1 = str(energie1)
            label2 = czcionka.render(energie1, 1, kolorNapisu)
            obraz.blit(label2, (260, 163 + ykoncowy))
            firerate1 = lista_statków[0].firerate
            firerate1 = str(firerate1)
            label2 = czcionka.render(firerate1, 1, kolorNapisu)
            obraz.blit(label2, (260, 243 + ykoncowy))
            speed1 = lista_statków[0].speed
            speed1 = str(speed1)
            label2 = czcionka.render(speed1, 1, kolorNapisu)
            obraz.blit(label2, (260, 323 + ykoncowy))
            dmg1 = lista_statków[0].dmg
            dmg1 = str(dmg1)
            label2 = czcionka.render(dmg1, 1, kolorNapisu)
            obraz.blit(label2, (260, 403 + ykoncowy))
            yshot1 = lista_statków[0].predkoscyshot
            yshot1 = str(yshot1)
            label2 = czcionka.render(yshot1, 1, kolorNapisu)
            obraz.blit(label2, (260, 483 + ykoncowy))
            xshot1 = lista_statków[0].predkoscxshot
            xshot1 = str(xshot1)
            label2 = czcionka.render(xshot1, 1, kolorNapisu)
            obraz.blit(label2, (260, 563 + ykoncowy))
            roz1 = lista_statków[0].modyfikatorrozrzutu
            roz1 = str(roz1)
            label2 = czcionka.render(roz1, 1, kolorNapisu)
            obraz.blit(label2, (260, 643 + ykoncowy))
            ############################################################################
            lista_statków[1].basehp += przyciski(80 + step2)
            lista_statków[1].energia += przyciski(160 + step2)
            lista_statków[1].firerate += przyciski(240 + step2)
            lista_statków[1].speed += przyciski(320 + step2)
            lista_statków[1].dmg += przyciski(400 + step2)
            lista_statków[1].predkoscyshot += przyciski(480 + step2)
            lista_statków[1].predkoscxshot += przyciski(560 + step2)
            lista_statków[1].modyfikatorrozrzutu += przyciski(640 + step2)
            hapeki2 = lista_statków[1].basehp
            hapeki2 = str(hapeki2)
            label2 = czcionka.render(hapeki2, 1, kolorNapisu)
            obraz.blit(label2, (260, 83 + step2 + ykoncowy))
            energie2 = lista_statków[1].energia
            energie2 = str(energie2)
            label2 = czcionka.render(energie2, 1, kolorNapisu)
            obraz.blit(label2, (260, 163 + step2 + ykoncowy))
            firerate2 = lista_statków[1].firerate
            firerate2 = str(firerate2)
            label2 = czcionka.render(firerate2, 1, kolorNapisu)
            obraz.blit(label2, (260, 243 + step2 + ykoncowy))
            speed2 = lista_statków[1].speed
            speed2 = str(speed2)
            label2 = czcionka.render(speed2, 1, kolorNapisu)
            obraz.blit(label2, (260, 323 + step2 + ykoncowy))
            dmg2 = lista_statków[1].dmg
            dmg2 = str(dmg2)
            label2 = czcionka.render(dmg2, 1, kolorNapisu)
            obraz.blit(label2, (260, 403 + step2 + ykoncowy))
            yshot2 = lista_statków[1].predkoscyshot
            yshot2 = str(yshot2)
            label2 = czcionka.render(yshot2, 1, kolorNapisu)
            obraz.blit(label2, (260, 483 + step2 + ykoncowy))
            xshot2 = lista_statków[1].predkoscxshot
            xshot2 = str(xshot2)
            label2 = czcionka.render(xshot2, 1, kolorNapisu)
            obraz.blit(label2, (260, 563 + step2 + ykoncowy))
            roz2 = lista_statków[1].modyfikatorrozrzutu
            roz2 = str(roz2)
            label2 = czcionka.render(roz2, 1, kolorNapisu)
            obraz.blit(label2, (260, 643 + step2 + ykoncowy))
            ####################################################################################################
            lista_statków[2].basehp += przyciski(80 + step3)
            lista_statków[2].energia += przyciski(160 + step3)
            lista_statków[2].firerate += przyciski(240 + step3)
            lista_statków[2].speed += przyciski(320 + step3)
            lista_statków[2].dmg += przyciski(400 + step3)
            lista_statków[2].predkoscyshot += przyciski(480 + step3)
            lista_statków[2].predkoscxshot += przyciski(560 + step3)
            lista_statków[2].modyfikatorrozrzutu += przyciski(640 + step3)
            hapeki3 = lista_statków[2].basehp
            hapeki3 = str(hapeki3)
            label2 = czcionka.render(hapeki3, 1, kolorNapisu)
            obraz.blit(label2, (260, 83 + step3 + ykoncowy))
            energie3 = lista_statków[2].energia
            energie3 = str(energie3)
            label2 = czcionka.render(energie3, 1, kolorNapisu)
            obraz.blit(label2, (260, 163 + step3 + ykoncowy))
            firerate3 = lista_statków[2].firerate
            firerate3 = str(firerate3)
            label2 = czcionka.render(firerate3, 1, kolorNapisu)
            obraz.blit(label2, (260, 243 + step3 + ykoncowy))
            speed3 = lista_statków[2].speed
            speed3 = str(speed3)
            label2 = czcionka.render(speed3, 1, kolorNapisu)
            obraz.blit(label2, (260, 323 + step3 + ykoncowy))
            dmg3 = lista_statków[2].dmg
            dmg3 = str(dmg3)
            label2 = czcionka.render(dmg3, 1, kolorNapisu)
            obraz.blit(label2, (260, 403 + step3 + ykoncowy))
            yshot3 = lista_statków[2].predkoscyshot
            yshot3 = str(yshot3)
            label2 = czcionka.render(yshot3, 1, kolorNapisu)
            obraz.blit(label2, (260, 483 + step3 + ykoncowy))
            xshot3 = lista_statków[2].predkoscxshot
            xshot3 = str(xshot3)
            label2 = czcionka.render(xshot3, 1, kolorNapisu)
            obraz.blit(label2, (260, 563 + step3 + ykoncowy))
            roz3 = lista_statków[2].modyfikatorrozrzutu
            roz3 = str(roz3)
            label2 = czcionka.render(roz3, 1, kolorNapisu)
            obraz.blit(label2, (260, 643 + step3 + ykoncowy))
            ##############################################################################
            lista_statków[3].basehp += przyciski(80 + step4)
            lista_statków[3].energia += przyciski(160 + step4)
            lista_statków[3].firerate += przyciski(240 + step4)
            lista_statków[3].speed += przyciski(320 + step4)
            lista_statków[3].dmg += przyciski(400 + step4)
            lista_statków[3].predkoscyshot += przyciski(480 + step4)
            lista_statków[3].predkoscxshot += przyciski(560 + step4)
            lista_statków[3].modyfikatorrozrzutu += przyciski(640 + step4)
            hapeki4 = lista_statków[3].basehp
            hapeki4 = str(hapeki4)
            label2 = czcionka.render(hapeki4, 1, kolorNapisu)
            obraz.blit(label2, (260, 83 + step4 + ykoncowy))
            energie4 = lista_statków[3].energia
            energie4 = str(energie4)
            label2 = czcionka.render(energie4, 1, kolorNapisu)
            obraz.blit(label2, (260, 163 + step4 + ykoncowy))
            firerate4 = lista_statków[3].firerate
            firerate4 = str(firerate4)
            label2 = czcionka.render(firerate4, 1, kolorNapisu)
            obraz.blit(label2, (260, 243 + step4 + ykoncowy))
            speed4 = lista_statków[3].speed
            speed4 = str(speed4)
            label2 = czcionka.render(speed4, 1, kolorNapisu)
            obraz.blit(label2, (260, 323 + step4 + ykoncowy))
            dmg4 = lista_statków[3].dmg
            dmg4 = str(dmg4)
            label2 = czcionka.render(dmg4, 1, kolorNapisu)
            obraz.blit(label2, (260, 403 + step4 + ykoncowy))
            yshot4 = lista_statków[3].predkoscyshot
            yshot4 = str(yshot4)
            label2 = czcionka.render(yshot4, 1, kolorNapisu)
            obraz.blit(label2, (260, 483 + step4 + ykoncowy))
            xshot4 = lista_statków[3].predkoscxshot
            xshot4 = str(xshot4)
            label2 = czcionka.render(xshot4, 1, kolorNapisu)
            obraz.blit(label2, (260, 563 + step4 + ykoncowy))
            roz4 = lista_statków[3].modyfikatorrozrzutu
            roz4 = str(roz4)
            label2 = czcionka.render(roz4, 1, kolorNapisu)
            obraz.blit(label2, (260, 643 + step4 + ykoncowy))


            # tutaj idzie kod do ustawien
            # tutaj idzie kod do ustawien
            # tutaj idzie kod do ustawien
            # tutaj idzie kod do ustawien

            if szerokoscOkna - 220 < mouse[0] < szerokoscOkna and wysokoscOkna - 36 < mouse[1] < wysokoscOkna:
                if click[0]:
                    opcjemenu = 0
                    break
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                opcjemenu = 0
                break
            pygame.display.flip()
            off()

    ################################################################################## ########################
    # puste menu
    if opcjemenu == 3:
        while True:
            obraz.blit(pustemenu, [0, 0])
            obraz.blit(przyciskback, [szerokoscOkna - 220, wysokoscOkna - 36])
            mouse = pygame.mouse.get_pos()
            obraz.blit(pocisk1, [mouse[0], mouse[1]])
            click = pygame.mouse.get_pressed()

            # tutaj idzie kod do pustego menu
            # tutaj idzie kod do pustego menu
            # tutaj idzie kod do pustego menu
            # tutaj idzie kod do pustego menu

            if szerokoscOkna - 220 < mouse[0] < szerokoscOkna and wysokoscOkna - 36 < mouse[1] < wysokoscOkna:
                if click[0]:
                    opcjemenu = 0
                    break
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                opcjemenu = 0
                break
            pygame.display.flip()
            off()

    tabPaskow.append(paski(life1, -400, 1))
    tabPaskow.append(paski(life1, szerokoscOkna +200, 1))
    tabPaskow.append(paski(life1, -400, wysokoscOkna - 21))
    tabPaskow.append(paski(life1, szerokoscOkna+200, wysokoscOkna - 21))
    ##########################################################################################################
    ##########################################################################################################
    # BODY GRY Głównej CALE!!!
    if opcjemenu == 1:
        while True:
            obraz.blit(background, [0, 0])
            if globalnytimer < 60:
                globalnytimer += 1
            else:
                globalnytimer = 0
            clock.tick(60)



            rozrzut = random.randint(-rozrzutmenu, rozrzutmenu)  # róra randomizacja rorzuty góra dół

            # Updatuje wszystkie pociski z clasy Projectile
            for b in my_missile_list:
                b.missile()
                b.trafienie()
                b.outofmap()
                if b.istnieje == 0:
                    my_missile_list.remove(b)

            for b in lista_statków:
                b.update()
                b.shot()
                if b.hp <= 0:
                    killBlue += 1
                    b.hp = b.basehp
            print(lista_statków[1].hp)


            y = len(lista_statków)
            for x in range(y):
                for i in range(x, y):
                    if i != x:
                        if hitBox(lista_statków[x].x, lista_statków[x].y, lista_statków[i].x, lista_statków[i].y,
                                  60) == 1:
                            lista_statków[x].hp -= 10
                            lista_statków[i].hp -= 10

            obraz.blit(tabelaplayer1, [-3, -2])
            obraz.blit(tabelaplayer2, [szerokoscOkna - 230, -2])
            obraz.blit(tabelaplayer3, [-2, wysokoscOkna - 47])
            obraz.blit(tabelaplayer4, [szerokoscOkna - 230, wysokoscOkna - 47])

            for x in tabPaskow:
                x.rusuj()

            pygame.display.flip()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:  # <------------Powrót do menu
                opcjemenu = 0
                break
            off()