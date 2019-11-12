import pygame
import sys
import random
from zmienne import *
from funkcje import *



file = open('mapaBetax.txt', 'r').read()
file = file.split('\n')
for line in file:
    listakropekkordyx2.append(line)

file = open('mapaBetay.txt', 'r').read()
file = file.split('\n')
for line in file:
    listakropekkordyy2.append(line)

y = len(listakropekkordyx2)
for i in range(0,y-1):
    listakropekkordyx.append(int(listakropekkordyx2[i]))

y = len(listakropekkordyy2)
for i in range(0,y-1):
    listakropekkordyy.append(int(listakropekkordyy2[i]))


def zasieg(pozycjax, pozycjay, pozycjax2, pozycjay2, range):
    x = ((pozycjax - pozycjax2) ** 2 + (pozycjay - pozycjay2) ** 2) ** (1 / 2)
    if x < range:
        return 1
    else:
        return 0

def poleTureta(x1, y1, x2, y2):
    if (mouse[0] > x1) and (mouse[0] < x2) and (mouse[1] > y1) and (mouse[1] < y2):
        return 1
    else:
        return 0

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


def napisysets(co, x, y, step):
    nazwa = str(co)
    label2 = czcionka.render(nazwa, 1, kolorNapisu)
    obraz.blit(label2, (x, y + step + ykoncowy))

def napis(co, x, y):
    nazwa = str(co)
    label2 = czcionka.render(nazwa, 1, kolorNapisu)
    obraz.blit(label2, (x, y))


def napisybloki(gracz, step):
    obraz.blit(staty, [178, step + ykoncowy])
    lista_statków[gracz].basehp += przyciski(80)
    lista_statków[gracz].baseenergia += przyciski(160)
    lista_statków[gracz].energiaregen += przyciski(240)
    lista_statków[gracz].speed += przyciski(320)
    lista_statków[gracz].dmg += przyciski(400)
    lista_statków[gracz].predkoscyshot += przyciski(480)
    lista_statków[gracz].predkoscxshot += przyciski(560)
    lista_statków[gracz].modyfikatorrozrzutu += przyciski(640)
    napisysets(lista_statków[gracz].basehp, 260, 83, step)
    napisysets(lista_statków[gracz].baseenergia, 260, 163, step)
    napisysets(lista_statków[gracz].energiaregen, 260, 243, step)
    napisysets(lista_statków[gracz].speed, 260, 323, step)
    napisysets(lista_statków[gracz].dmg, 260, 403, step)
    napisysets(lista_statków[gracz].predkoscyshot, 260, 483, step)
    napisysets(lista_statków[gracz].predkoscxshot, 260, 563, step)
    napisysets(lista_statków[gracz].modyfikatorrozrzutu, 260, 643, step)


def animacjaobrotutureta(góra, prawo, dół, lewo, lewo_góra, prawo_góra, prawo_dół, lewo_dół):
    kierunkowax = -((i.x - j.x) + j.vx * 10)
    kierunkoway = -((i.y - j.y) + j.vy * 10)
    if kierunkoway == 0:
        if kierunkowax <= 0:
            i.image = lewo  # wlewo
        else:
            i.image = prawo  # wprawo
    else:
        if kierunkowax < 0:
            if kierunkoway < 0:
                if 0.4 < (kierunkowax / kierunkoway) < 2.5:
                    i.image = lewo_góra  # lewo-góra
                elif (kierunkowax / kierunkoway) >= 2.5:
                    i.image = lewo  # wlewo
                elif (kierunkowax / kierunkoway) <= 0.4:
                    i.image = góra  # góra
            else:
                if -2.5 < (kierunkowax / kierunkoway) < -0.4:
                    i.image = lewo_dół  # lewo-doł
                elif (kierunkowax / kierunkoway) <= -2.5:
                    i.image = lewo  # wlewo
                elif (kierunkowax / kierunkoway) >= -0.4:
                    i.image = dół  # dół
        else:
            if kierunkoway > 0:
                if 2.5 > (kierunkowax / kierunkoway) > 0.4:
                    i.image = prawo_dół
                elif (kierunkowax / kierunkoway) >= 2.5:
                    i.image = prawo  # Wprawo
                elif (kierunkowax / kierunkoway) <= 0.4:
                    i.image = dół  # dół
            else:
                if (kierunkowax / kierunkoway) <= -2.5:
                    i.image = prawo  # wprawo
                elif (kierunkowax / kierunkoway) >= -0.4:
                    i.image = góra  # góra
                else:
                    i.image = prawo_góra

##Klasa gracza
class Statek():
    def __init__(self, pozycjax, pozycjay, nrstatku, player, pozycjaxshot, pozycjayshot, predkoscxshot, predkoscyshot,
                 modyfikatorrozrzutu, modyfikatorrozstrzalu, hp, rodzajpocisku, speed, energia, dmg, enegiaregen):
        self.image = grafaStatków[nrstatku]
        self.x = pozycjax
        self.y = pozycjay
        self.speed = speed
        self.energiaregen = enegiaregen
        self.player = player
        self.energia = energia
        self.baseenergia = energia
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
            tabPaskow[0].hp = (self.hp / self.basehp)
            tabPaskow[4].hp = (self.energia / self.baseenergia) / 2
        #######################################
        if self.player == 2:
            self.x += tab2[0] * self.speed / 10
            self.y += tab2[1] * self.speed / 10
            tabPaskow[1].hp = (self.hp / self.basehp)
            tabPaskow[5].hp = (self.energia / self.baseenergia) / 2
        ########################################
        if self.player == 3:
            self.x += tab3[0] * self.speed / 10
            self.y += tab3[1] * self.speed / 10
            tabPaskow[2].hp = (self.hp / self.basehp)
            tabPaskow[6].hp = (self.energia / self.baseenergia) / 2
        #########################################
        if self.player == 4:
            self.x += tab4[0] * self.speed / 10
            self.y += tab4[1] * self.speed / 10
            tabPaskow[3].hp = (self.hp / self.basehp)
            tabPaskow[7].hp = (self.energia / self.baseenergia) / 2
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
        i = 0
        while i < self.energiaregen:
            i += 1
            if globalnytimer == 34 and self.energia < self.baseenergia:
                self.energia += 1
        if pygame.key.get_pressed()[pygame.K_f]:
            if self.player == 1:
                if self.energia > 0:
                    self.energia -= 1
                    my_missile_list.append(
                        Projectile(self.x + self.pozycjaxshot, self.y + self.pozycjayshot, self.predkoscxshot,
                                   self.predkoscyshot,
                                   rozrzut * self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * tab1[1]),
                                   self.rodzajpocisku,self.dmg,0))

        if pygame.key.get_pressed()[pygame.K_p]:
            if self.player == 2:
                if self.energia > 0:
                    self.energia -= 1
                    my_missile_list.append(
                        Projectile(self.x + self.pozycjaxshot, self.y + self.pozycjayshot, self.predkoscxshot,
                                   self.predkoscyshot,
                                   rozrzut * self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * tab2[1]),
                                   self.rodzajpocisku,self.dmg,0))

        if pygame.key.get_pressed()[pygame.K_u]:
            if self.player == 3:
                if self.energia > 0:
                    self.energia -= 1
                    my_missile_list.append(
                        Projectile(self.x + self.pozycjaxshot, self.y + self.pozycjayshot, self.predkoscxshot,
                                   self.predkoscyshot,
                                   rozrzut * self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * tab3[1]),
                                   self.rodzajpocisku,self.dmg,0))

        if pygame.key.get_pressed()[pygame.K_KP9]:
            if self.player == 4:
                if self.energia > 0:
                    self.energia -= 1
                    my_missile_list.append(
                        Projectile(self.x + self.pozycjaxshot, self.y + self.pozycjayshot, self.predkoscxshot,
                                   self.predkoscyshot,
                                   rozrzut * self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * tab4[1]),
                                   self.rodzajpocisku,self.dmg,0))


class paski():
    def __init__(self, grafa, x, y):
        self.grafa = grafa
        self.hp = 1
        self.x = x
        self.y = y
        self.xx = 0

    def rusuj(self):
        if self.x < szerokoscOkna / 2:
            self.xx = self.x + 200 * (self.hp + 1)
        else:
            self.xx = self.x - 200 * (self.hp + 1)

        obraz.blit(self.grafa, [self.xx, self.y])


# NAJWAZNIEJSZA KLASA TUTAJ NIC NIE RUSZAC!!!

class Projectile():
    def __init__(self, x, y, vx, vy, rozrzut, rodzajpocisku,dmg,range):
        self.x = x
        self.y = y
        self.rozrzut = rozrzut
        self.vx = vx + (rozrzut / 50)
        self.vy = vy + (rozrzut / 50)
        self.image = rodzajpocisku
        self.istnieje = 1
        self.dmg=dmg
        self.zasieg=0
        self.range=range

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
                b.x += self.vx / 5
                b.y += self.vy / 5

    def outofmap(self):
        if self.x > szerokoscOkna or self.x < 0:
            self.istnieje = 0
        if self.y > wysokoscOkna or self.y < 0:
            self.istnieje = 0


##Klasa wroga
class Enemy():
    def __init__(self, pozycjax, pozycjay, obraz, hp, vx, vy, dmg):
        self.image = grafaEnemy[obraz]
        self.x = pozycjax
        self.y = pozycjay
        self.hp = hp
        self.basehp = hp
        self.vx = vx
        self.vy = vy
        self.dmg = dmg
        self.zmiennai=0
        self.istnieje=1

    def zycieenemy(self):
        pygame.draw.rect(obraz,[0,0,0],([self.x + 4,self.y + 49],[52,7]))
        pygame.draw.rect(obraz,[255,0,0],([self.x + 5,self.y + 50],[50*(self.hp/self.basehp),5]))

    def trasa(self):
        self.vx = (self.x - listakropekkordyx[self.zmiennai])
        self.vy = (self.y - listakropekkordyy[self.zmiennai])
        self.x -= self.vx
        self.y -= self.vy
        if self.zmiennai < len(listakropekkordyx)-1:
            self.zmiennai += 1
        else:
            #self.istnieje = 0
            self.zmiennai = 0
        obraz.blit(self.image, [self.x,self.y])


class Turet():
    def __init__(self, pozycjax, pozycjay, obraz, firerate, vx, vy, dmg, range, wartosc):
        self.obraz = obraz
        self.image = grafaTuret[self.obraz]
        self.x = pozycjax
        self.y = pozycjay
        self.firerate = firerate
        self.vx = vx
        self.vy = vy
        self.dmg = dmg
        self.range = range
        self.postawiony = 0
        self.magazynek=1
        self.menupokaz=0
        self.wartosc = wartosc
        self.tier=0
        self.rodzaj=0

    def update(self):
        obraz.blit(self.image, [self.x, self.y])

class Kropka():
    def __init__(self,pozycjax,pozycjay):
        self.x = pozycjax
        self.y = pozycjay

    def update(self):
        pygame.draw.circle(obraz, [0, 0, 0], (self.x, self.y), 4, 0)


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
        tabPaskow.append(paski(life1, -400, 1))
        tabPaskow.append(paski(life1, szerokoscOkna + 200, 1))
        tabPaskow.append(paski(life1, -400, wysokoscOkna - 21))
        tabPaskow.append(paski(life1, szerokoscOkna + 200, wysokoscOkna - 21))
        tabPaskow.append(paski(energiaGraph, -302, 27))
        tabPaskow.append(paski(energiaGraph, szerokoscOkna + 204, 27))
        tabPaskow.append(paski(energiaGraph, -302, wysokoscOkna - 38))
        tabPaskow.append(paski(energiaGraph, szerokoscOkna + 204, wysokoscOkna - 38))
        opcjemenu = 0

    #########################################################################################################
    # MENU GLOWNE
    if opcjemenu == 0:
        lokalnytimer = 0
        blok1menu = -60
        blok2menu = -87
        while True:
            clock.tick(60)
            obraz.blit(background, [0, 0])
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if blok1menu < 0:
                blok1menu += 1.5
            if blok2menu < 0:
                blok2menu += 1.5
            if 350 < mouse[1] < 430 and 0 < mouse[0] < 160 and blok2menu < 175:
                blok2menu += 8
            if not (350 < mouse[1] < 600) or not (0 < mouse[0] < 160):
                if blok2menu > 3:
                    blok2menu -= 8

            obraz.blit(menuopcje2, [0, 0 + blok2menu])
            obraz.blit(menuopcje1, [0 + blok1menu, 0])
            # tupala = mouse[0],mouse[1]
            # tupala = str(tupala)
            # label2 = czcionka1.render(tupala, 1, kolorNapisu)
            # obraz.blit(label2, (mouse[0]+10, mouse[1]))

            if 4 < mouse[0] < 224 and 0 < mouse[1] < 40:
                obraz.blit(przyciskstart1, [4 + blok1menu, 6])
                if click[0]:
                    opcjemenu = 1
                    break
            else:
                obraz.blit(przyciskstart, [4 + blok1menu, 4])

            obraz.blit(przyciskdefence, [4 + blok1menu, 84])
            obraz.blit(przyciskback, [szerokoscOkna - 220, wysokoscOkna - 76])

            if 4 < mouse[0] < 224 and 46 < mouse[1] < 82:
                obraz.blit(przycisksettings1, [4 + blok1menu, 46])
                if click[0]:
                    opcjemenu = 2
                    break
            else:
                obraz.blit(przycisksettings, [4 + blok1menu, 44])
            if 4 < mouse[0] < 224 and 86 < mouse[1] < 122:
                obraz.blit(przyciskdefence1, [4 + blok1menu, 86])
                if click[0]:
                    opcjemenu = 3
                    break
            if szerokoscOkna - 220 < mouse[0] < szerokoscOkna and wysokoscOkna - 76 < mouse[1] < wysokoscOkna - 40:
                if click[0]:
                    sys.exit(0)
            if pygame.key.get_pressed()[pygame.K_o]:
                opcjemenu=4
                break

            pygame.display.flip()
            off()
    #########################################################################################################
    # mapmaking
    if opcjemenu == 4:
        listakropek = []
        listakropekkordyx = []
        listakropekkordyy = []
        while True:
            obraz.blit(mapmaking,[0,0])
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if click[0]:
                listakropek.append(Kropka(mouse[0],mouse[1]))
                listakropekkordyx.append(mouse[0])
                listakropekkordyy.append(mouse[1])
            for b in listakropek:
                b.update()

            tupala = mouse[0], mouse[1]
            tupala = str(tupala)
            label2 = czcionka1.render(tupala, 1, [255,0,0])
            obraz.blit(label2, (mouse[0] + 10, mouse[1]))

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                opcjemenu = 0
                break
            pygame.display.flip()
            off()

            iksy = open('mapaBetax.txt', 'w')
            for x in listakropekkordyx:
                iksy.write(str(x))
                iksy.write('\n')
            iksy.close()

            igreki = open('mapaBetay.txt', 'w')
            for x in listakropekkordyy:
                igreki.write(str(x))
                igreki.write('\n')
            igreki.close()

    # menu ustawienia
    if opcjemenu == 2:
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
        while True:
            obraz.blit(settings, [0, 0])
            clock.tick(60)

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
            mnoznikx = (mouse[0] - 1170) * 0.1 * (click[0] + 0.02)
            mnozniky = (mouse[1] - 318) * 0.26 * (click[0] + 0.02)
            obraz.blit(oko, [30 + mnoznikx, -160 + mnozniky])
            obraz.blit(czaszka, [370, -400])

            ykoncowy += pozycjakoncowa / 50
            if 212 < mouse[0] < 382:
                if click[0] == True:
                    pozycjamouse = mouse[1] - startmouse
                else:
                    pozycjakoncowa = pozycjamouse
                    startmouse = mouse[1]

            obraz.blit(przyciskback, [szerokoscOkna - 220, wysokoscOkna - 36])
            obraz.blit(pasek, [219, -720 - (ykoncowy) / 4])

            napisybloki(0, step1)
            napisybloki(1, step2)
            napisybloki(2, step3)
            napisybloki(3, step4)

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
        kasa = 120


        my_missile_list = []
        lista_enemy = []
        lista_turet = []
        zmiennatrzymaszturet = 0
        lokalnytimer2=0
        zmiennanablokowaniepola = 0
        while True:
            obraz.blit(mapmaking, [0, 0])
            if globalnytimer < 5:
                globalnytimer += 1
                for b in lista_turet:
                    if b.magazynek < b.firerate:
                        b.magazynek += 1
            else:
                globalnytimer = 0
            tabMiejsTuretow = []
            clock.tick(60)
            losuj = random.randint(2, 8)
            obraz.blit(przyciskback, [szerokoscOkna - 220, wysokoscOkna - 36])
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            tupala = mouse[0], mouse[1]
            tupala = str(tupala)
            label2 = czcionka1.render(tupala, 1, kolorNapisu)
            obraz.blit(label2, (mouse[0] + 10, mouse[1]))

            napis(kasa,20,0)

            if click[0] and 70 < mouse[0] < 120 and 615 < mouse[1] < 665 and zmiennatrzymaszturet == 0 and kasa >= 30:
                lista_turet.append(Turet(70, 615, 3, 30, 2, 2, 100,200,30))
                kasa-=30
            if click[0] and 203 < mouse[0] < 254 and 617 < mouse[1] < 663 and zmiennatrzymaszturet == 0 and kasa >= 40:
                lista_turet.append(Turet(203, 617, 3, 1, 2, 2, 10,700,40))
                kasa-=40
            if click[0] and 130 < mouse[0] < 180 and 617 < mouse[1] < 663 and zmiennatrzymaszturet == 0 and kasa >= 40:
                lista_turet.append(Turet(130, 617, 3, 1, 2, 2, 10,700,40))
                kasa-=40

            for b in lista_turet:
                if b.postawiony ==1:
                    tabMiejsTuretow.append([b.x - 50,b.y - 50, b.x + 50, b.y + 50])
                if zmiennatrzymaszturet == 1 and b.postawiony == 0:
                    b.x = mouse[0] - 25
                    b.y = mouse[1] - 25

                if zmiennatrzymaszturet == 1 and b.postawiony == 1:
                    pygame.draw.rect(obraz, [255, 0, 0],(b.x,b.y,50,50))

                if b.x < mouse[0] < b.x + 50 and b.y < mouse[1] < b.y + 50 and b.postawiony == 0:
                    if click[0]:
                        zmiennatrzymaszturet = 1

                if b.x < mouse[0] < b.x + 50 and b.y < mouse[1] < b.y + 50 and b.postawiony == 1 and b.menupokaz ==0 and zmiennatrzymaszturet==0:
                    if click[0]:
                        b.menupokaz =1

                if b.x+195 < mouse[0] < b.x + 215 and b.y < mouse[1] < b.y + 50 and b.postawiony == 1 and b.menupokaz ==1 and zmiennatrzymaszturet==0:
                    if click[0]:
                        b.menupokaz =0

                if b.x + 175 < mouse[0] < b.x + 195 and b.y < mouse[1] < b.y + 50 and b.postawiony == 1 and b.menupokaz == 1 and zmiennatrzymaszturet == 0:
                    if click[0]:
                        kasa+=b.wartosc/2
                        lista_turet.remove(b)

                if b.x + 155 < mouse[0] < b.x + 175 and b.y < mouse[1] < b.y + 50 and b.postawiony == 1 and b.menupokaz == 1 and zmiennatrzymaszturet == 0:
                    if click[0]:
                        b.firerate -=1


                if b.x + 135 < mouse[0] < b.x + 155 and b.y < mouse[1] < b.y + 50 and b.postawiony == 1 and b.menupokaz == 1 and zmiennatrzymaszturet == 0:
                    if click[0]:
                        b.range += 2



                if b.menupokaz ==1:
                    pygame.draw.rect(obraz, [0, 0, 0], (b.x - 5, b.y - 5, 220, 60))
                    pygame.draw.rect(obraz, [220, 0, 0], (b.x +195, b.y - 5, 20, 60))
                    pygame.draw.rect(obraz, [255, 255, 0], (b.x + 175, b.y - 5, 20, 60))
                    pygame.draw.rect(obraz, [0, 255, 0], (b.x + 155, b.y - 5, 20, 60))
                    pygame.draw.rect(obraz, [0, 50, 200], (b.x + 135, b.y - 5, 20, 60))
                    pygame.draw.circle(obraz, [0, 0, 0], (b.x+25, b.y +25), b.range, 2)

                b.update()
                suma = 0
                for i in range(len(tabMiejsTuretow)):
                    suma += (poleTureta(*tabMiejsTuretow[i]))
                if suma == 0:
                    if zmiennatrzymaszturet == 1 and b.postawiony==0:
                        pygame.draw.circle(obraz,[0,0,0],(mouse[0],mouse[1]),b.range,2)
                        obraz.blit(turet3, [mouse[0] - 25, mouse[1] - 25])

                    if not click[0] and b.postawiony==0:
                        zmiennatrzymaszturet = 0
                        b.postawiony = 1
                        zmiennanablokowaniepola=1
                    if zmiennanablokowaniepola==1:
                        tabMiejsTuretow.append([mouse[0]-50, mouse[1]-50, mouse[0]+50, mouse[1]+50])
                        zmiennanablokowaniepola=0


                if suma != 0:
                    if zmiennatrzymaszturet == 1 and b.postawiony==0:

                        pygame.draw.circle(obraz,[0,0,0],(mouse[0],mouse[1]),b.range,2)
                        obraz.blit(turet1, [mouse[0] - 25, mouse[1] - 25])
                        if not click[0] and not b.postawiony == 1:
                            lista_turet.remove(b)
                            kasa += 30
                            zmiennatrzymaszturet = 0
            for j in lista_enemy:
                for i in lista_turet:
                    if zasieg(i.x, i.y, j.x, j.y, i.range) == 1:
                        if i.magazynek>=i.firerate:
                            animacjaobrotutureta(turet2_1,turet2_2,turet2_3,turet2_4,turet2_5,turet2_6,turet2_7,turet2_8)
                            my_missile_list.append(Projectile(i.x+25,i.y+25,-((i.x - j.x)*0.1)-j.vx,-((i.y - j.y)*0.1)-j.vy,random.randint(-9,9),pocisk5,i.dmg,i.range))
                            i.magazynek=0


            for b in my_missile_list:
                b.missile()
                b.outofmap()
                b.zasieg+=((b.vx**2 + b.vy**2 )**0.5)*1.1
                if b.zasieg > b.range:
                    b.istnieje=0

                for bb in lista_enemy:
                    if bb.x <b.x+5 < bb.x + 60 and bb.y <b.y+5 < bb.y + 60:
                        b.istnieje=0
                        bb.hp -= b.dmg
                        if bb.hp <= 0:
                            bb.istnieje=0
                if b.istnieje ==0:
                    my_missile_list.remove(b)






            # tutaj idzie kod do pustego menu
            # tutaj idzie kod do pustego menu
            print(lista_turet)
            print(tabMiejsTuretow)

            if globalnytimer == 5:
                if lokalnytimer2 < 1:
                    lokalnytimer2 += 1
                else:
                    lokalnytimer2 = 0
                    lista_enemy.append(Enemy(listakropekkordyx[0], listakropekkordyy[0], 1, 500, 0, 0, 10))
            for b in lista_enemy:
                b.trasa()
                b.zycieenemy()
                if b.x < 0:
                    b.istnieje=0
                if b.istnieje == 0:
                    kasa += 5
                    lista_enemy.remove(b)

            if szerokoscOkna - 220 < mouse[0] < szerokoscOkna and wysokoscOkna - 36 < mouse[1] < wysokoscOkna:
                if click[0]:
                    opcjemenu = 0
                    break
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                opcjemenu = 0
                break
            pygame.display.flip()
            off()

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
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

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
                    b.hp = b.basehp
                if b.x < mouse[0] < b.x + 70 and b.y < mouse[1] < b.y + 70:
                    if click[0]:
                        b.x = mouse[0] - 30
                        b.y = mouse[1] - 30

            y = len(lista_statków)
            for x in range(y):
                for i in range(x, y):
                    if i != x:
                        if hitBox(lista_statków[x].x, lista_statków[x].y, lista_statków[i].x, lista_statków[i].y,
                                  50) == 1:
                            lista_statków[x].hp -= 10
                            lista_statków[i].hp -= 10
                            lista_statków[i].x -= (lista_statków[x].x - lista_statków[i].x) / 4
                            lista_statków[i].y -= (lista_statków[x].y - lista_statków[i].y) / 4
                            lista_statków[x].x -= (lista_statków[i].x - lista_statków[x].x) / 4
                            lista_statków[x].y -= (lista_statków[i].y - lista_statków[x].y) / 4

            for x in tabPaskow:
                x.rusuj()

            obraz.blit(tabelaplayer1, [-3, -2])
            obraz.blit(tabelaplayer2, [szerokoscOkna - 230, -2])
            obraz.blit(tabelaplayer3, [-2, wysokoscOkna - 47])
            obraz.blit(tabelaplayer4, [szerokoscOkna - 230, wysokoscOkna - 47])

            pygame.display.flip()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:  # <------------Powrót do menu
                opcjemenu = 0
                break
            off()