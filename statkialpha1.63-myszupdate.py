import pygame
import sys
import random
from zmienne import *
from funkcje import *


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
            tabPaskow[0].hp= (self.hp/self.basehp)
            tabPaskow[4].hp = (self.energia / self.baseenergia)/2
        #######################################
        if self.player == 2:
            self.x += tab2[0] * self.speed / 10
            self.y += tab2[1] * self.speed / 10
            tabPaskow[1].hp= (self.hp/self.basehp)
            tabPaskow[5].hp = (self.energia / self.baseenergia)/2
        ########################################
        if self.player == 3:
            self.x += tab3[0] * self.speed / 10
            self.y += tab3[1] * self.speed / 10
            tabPaskow[2].hp= (self.hp/self.basehp)
            tabPaskow[6].hp = (self.energia / self.baseenergia)/2
        #########################################
        if self.player == 4:
            self.x += tab4[0] * self.speed / 10
            self.y += tab4[1] * self.speed / 10
            tabPaskow[3].hp= (self.hp/self.basehp)
            tabPaskow[7].hp = (self.energia  / self.baseenergia )/2
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
        i=0
        while i < self.energiaregen:
            i+=1
            if globalnytimer == 34 and self.energia < self.baseenergia:
                self.energia+= 1
        if pygame.key.get_pressed()[pygame.K_f]:
            if self.player == 1:
                if self.energia > 0:
                    self.energia-=1
                    my_missile_list.append(
                        Projectile(self.x + self.pozycjaxshot, self.y + self.pozycjayshot, self.predkoscxshot,
                                   self.predkoscyshot,
                                   rozrzut * self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * tab1[1]),
                                   self.rodzajpocisku))

        if pygame.key.get_pressed()[pygame.K_p]:
            if self.player == 2:
                if self.energia > 0:
                    self.energia-=1
                    my_missile_list.append(
                        Projectile(self.x + self.pozycjaxshot, self.y + self.pozycjayshot, self.predkoscxshot,
                                   self.predkoscyshot,
                                   rozrzut * self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * tab2[1]),
                                   self.rodzajpocisku))

        if pygame.key.get_pressed()[pygame.K_u]:
            if self.player == 3:
                if self.energia > 0:
                    self.energia-=1
                    my_missile_list.append(
                        Projectile(self.x + self.pozycjaxshot, self.y + self.pozycjayshot, self.predkoscxshot,
                                   self.predkoscyshot,
                                   rozrzut * self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * tab3[1]),
                                   self.rodzajpocisku))

        if pygame.key.get_pressed()[pygame.K_KP9]:
            if self.player == 4:
                if self.energia > 0:
                    self.energia-=1
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
                b.x += self.vx/5
                b.y += self.vy/5




    def outofmap(self):
        if self.x > szerokoscOkna or self.x < 0:
            self.istnieje = 0
        if self.y > wysokoscOkna or self.y < 0:
            self.istnieje = 0

##Klasa wroga
class Enemy():
    def __init__(self, pozycjax, pozycjay, obraz,hp,vx,vy,dmg):
        self.image = grafaStatków[obraz]
        self.x = pozycjax
        self.y = pozycjay
        self.hp=hp
        self.vx=vx
        self.vy=vy
        self.dmg=dmg

    def idz(self):
        if self.x >= 640:
            self.x -= self.vx
        if self.x <= 640 and self.y <=430 :
            self.y += self.vy
        if self.y > 430:
            self.x -= self.vx
        obraz.blit(self.image, [self.x, self.y])









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
        lokalnytimer=0
        blok1menu = -60
        blok2menu = -87
        while True:
            clock.tick(60)
            obraz.blit(background, [0, 0])
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if blok1menu < 0:
                blok1menu +=1.5
            if blok2menu < 0:
                blok2menu +=1.5
            if 350 < mouse[1] <430 and 0< mouse[0]<160 and blok2menu <175:
                blok2menu+=8
            if not(350 < mouse[1] <600) or not(0< mouse[0]<160):
                if blok2menu > 3:
                    blok2menu-=8



            obraz.blit(menuopcje2,[0,0+blok2menu])
            obraz.blit(menuopcje1,[0+blok1menu,0])
            tupala = mouse[0],mouse[1]
            tupala = str(tupala)
            label2 = czcionka1.render(tupala, 1, kolorNapisu)
            obraz.blit(label2, (mouse[0]+10, mouse[1]))




            if 4 < mouse[0] < 224 and 0 < mouse[1] <  40 :
                obraz.blit(przyciskstart1, [4+blok1menu, 6])
                if click[0]:
                    opcjemenu=1
                    break
            else:
                obraz.blit(przyciskstart, [4+blok1menu, 4])



            obraz.blit(przyciskdefence, [4+blok1menu, 84])
            obraz.blit(przyciskback, [szerokoscOkna - 220, wysokoscOkna - 76])




            if 4 < mouse[0] < 224 and 46 < mouse[1] < 82:
                obraz.blit(przycisksettings1, [4+blok1menu, 46])
                if click[0]:
                    opcjemenu = 2
                    break
            else:
                obraz.blit(przycisksettings, [4+blok1menu, 44])
            if 4 < mouse[0] < 224 and 86 < mouse[1] < 122:
                obraz.blit(przyciskdefence1, [4+blok1menu, 86])
                if click[0]:
                    opcjemenu = 3
                    break
            if szerokoscOkna - 220 < mouse[0] < szerokoscOkna and wysokoscOkna - 76 < mouse[1] < wysokoscOkna - 40:
                if click[0]:
                    sys.exit(0)

            pygame.display.flip()
            off()
    #########################################################################################################
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
            mnoznikx=(mouse[0]-1170)*0.1*(click[0]+0.02)
            mnozniky = (mouse[1] - 318)*0.26*(click[0]+0.02)
            obraz.blit(oko,[30+mnoznikx,-160+mnozniky])
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

            napisybloki(0,step1)
            napisybloki(1,step2)
            napisybloki(2,step3)
            napisybloki(3,step4)

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
            if globalnytimer < 60:
                globalnytimer += 1
            else:
                globalnytimer = 0
            clock.tick(60)
            losuj=random.randint(2,20)
            obraz.blit(przyciskback, [szerokoscOkna - 220, wysokoscOkna - 36])
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            tupala=mouse[0],mouse[1]
            tupala = str(tupala)
            label2 = czcionka1.render(tupala, 1, kolorNapisu)
            obraz.blit(label2, (mouse[0]+10, mouse[1]))
            # tutaj idzie kod do pustego menu
            # tutaj idzie kod do pustego menu
            # tutaj idzie kod do pustego menu
            # tutaj idzie kod do pustego menu

            if globalnytimer ==34:
                lista_enemy.append(Enemy(1200, 220, 0, 100, losuj, losuj, 10))
            for b in lista_enemy:
                b.idz()
                if b.x <0:
                    b.x=1200
                    b.y=217
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
                if b.x < mouse[0] < b.x+70 and b.y < mouse[1] <b.y+70:
                    if click[0]:
                        b.x=mouse[0]-30
                        b.y=mouse[1]-30


            y = len(lista_statków)
            for x in range(y):
                for i in range(x, y):
                    if i != x:
                        if hitBox(lista_statków[x].x, lista_statków[x].y, lista_statków[i].x, lista_statków[i].y,
                                  50) == 1:
                            lista_statków[x].hp -= 10
                            lista_statków[i].hp -= 10
                            lista_statków[i].x -= (lista_statków[x].x -lista_statków[i].x)/4
                            lista_statków[i].y -= (lista_statków[x].y -lista_statków[i].y)/4
                            lista_statków[x].x -= (lista_statków[i].x -lista_statków[x].x)/4
                            lista_statków[x].y -= (lista_statków[i].y -lista_statków[x].y)/4

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