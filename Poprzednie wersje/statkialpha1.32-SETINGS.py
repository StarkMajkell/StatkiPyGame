import pygame
import sys
import random
import linecache

pygame.init()  # musi być
pygame.display.set_caption('Statki')
a = pygame.image.load('Grafa/Logo.png')
pygame.display.set_icon(a)

clock = pygame.time.Clock()


#moduł ze zmiennymi
wysokoscOkna=720
szerokoscOkna=1280
rozmiarOkna=(szerokoscOkna,wysokoscOkna)
obraz = pygame.display.set_mode(rozmiarOkna)
zyciegracza1=0
zyciegracza2=szerokoscOkna-200
opcjemenu=-1
my_missile_list=[]
lista_statków=[]
parametryplayer1 = []
parametryplayer2 = []
parametryplayer3 = []
parametryplayer4 = []
globalnytimer=0
rozrzutmenu= 20
liczbagraczy=4


killRed = 0
killBlue = 0
kolorNapisu = (0, 255, 255)
czcionka = pygame.font.Font("Czcionki/digital-7.ttf", 40)
background = pygame.image.load("Grafa/background2.jpg").convert()
menu = pygame.image.load("Grafa/backgroundmenu.jpg").convert()
settings= pygame.image.load('Grafa/settings.jpg').convert()
przyciskback= pygame.image.load('Grafa/przyciskback.png')
przycisk= pygame.image.load('Grafa/przycisk.png')
staty=pygame.image.load('Grafa/staty.png')
przycisksettings=pygame.image.load('Grafa/przycisksettings.png')
przyciskstart=pygame.image.load('Grafa/przyciskstart.png')
przyciskexit=pygame.image.load('Grafa/przyciskexit.png')
przycisk2=pygame.image.load('Grafa/przycisk2.png')
przycisk3=pygame.image.load('Grafa/przycisk3.png')
przycisk4=pygame.image.load('Grafa/przycisk4.png')
pustemenu=pygame.image.load('Grafa/pustemenu.jpg')
tabela=pygame.image.load('Grafa/tabela.png')
przycisksilnik=pygame.image.load('Grafa/przycisksilnik.png')
statek1 = pygame.image.load("Grafa/Statek1-Blue1.png")
statek2 = pygame.image.load("Grafa/Statek3.png")
statek3 = pygame.image.load("Grafa/Statek1-Red1.png")
pocisk1=pygame.image.load('Grafa/pocisk.png')
pocisk2=pygame.image.load('Grafa/pocisk2.png')
pocisk4=pygame.image.load('Grafa/pocisk4.png')
pocisk3=pygame.image.load('Grafa/pocisk3.png')
life = pygame.image.load('Grafa/life.png')
music = pygame.mixer.music.load("Dźwięki/pif.mp3")
player1=pygame.image.load('Grafa/player1.png')
player2=pygame.image.load('Grafa/player2.png')
player3=pygame.image.load('Grafa/player3.png')
player4=pygame.image.load('Grafa/player4.png')
grafaStatków = [statek1,statek2,statek3]
pociski = [pocisk1,pocisk2,pocisk3,pocisk4]


#moduł resetowania pozycji
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

#moduł poruszania sie
def ruch(x,y,z,h):
    tab = [0,0]
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
def pifpaf():
    pygame.mixer.music.play(0)
    pygame.mixer.music.play(1)


##Klasa gracza
class Statek():
    def __init__(self,pozycjax,pozycjay,nrstatku,player,pozycjaxshot,pozycjayshot,predkoscxshot,predkoscyshot,modyfikatorrozrzutu,modyfikatorrozstrzalu,hp,rodzajpocisku,speed):
        self.image = grafaStatków[nrstatku]
        self.x = pozycjax
        self.y = pozycjay
        self.speed = speed
        self.player = player
        self.pozycjaxshot =pozycjaxshot
        self.pozycjayshot=pozycjayshot
        self.predkoscxshot=predkoscxshot
        self.predkoscyshot=predkoscyshot
        self.modyfikatorrozrzutu=modyfikatorrozrzutu
        self.modyfikatorrozstrzalu=modyfikatorrozstrzalu
        self.hp = hp
        self.basehp = hp
        self.rodzajpocisku = pociski[rodzajpocisku]

    def update(self):
        tab1 = ruch(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        tab2 = ruch(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
        tab3 = ruch(pygame.K_j, pygame.K_l, pygame.K_i, pygame.K_k)
        tab4 = ruch(pygame.K_KP4, pygame.K_KP6, pygame.K_KP8, pygame.K_KP5)
        if self.player == 1:
            self.x += tab1[0]*self.speed/10
            self.y += tab1[1]*self.speed/10
        #######################################
        if self.player == 2:
            self.x += tab2[0]*self.speed/10
            self.y += tab2[1]*self.speed/10
        ########################################
        if self.player == 3:
            self.x += tab3[0]*self.speed/10
            self.y += tab3[1]*self.speed/10
        #########################################
        if self.player == 4:
            self.x += tab4[0]*self.speed/10
            self.y += tab4[1]*self.speed/10
        if self.y >= wysokoscOkna-60:
            self.y = wysokoscOkna-61
        if self.x < 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0
        if self.x >= szerokoscOkna-60:
            self.x = szerokoscOkna-61

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
                pifpaf()
        if pygame.key.get_pressed()[pygame.K_p]:
            if self.player == 2:
                my_missile_list.append(
                    Projectile(self.x + self.pozycjaxshot, self.y + self.pozycjayshot, self.predkoscxshot,
                               self.predkoscyshot,
                               rozrzut * self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * tab2[1]),
                               self.rodzajpocisku))
                pifpaf()
        if pygame.key.get_pressed()[pygame.K_u]:
            if self.player == 3:
                my_missile_list.append(
                    Projectile(self.x + self.pozycjaxshot, self.y + self.pozycjayshot, self.predkoscxshot,
                               self.predkoscyshot,
                               rozrzut * self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * tab3[1]),
                               self.rodzajpocisku))
                pifpaf()
        if pygame.key.get_pressed()[pygame.K_KP9]:
            if self.player == 4:
                my_missile_list.append(
                    Projectile(self.x + self.pozycjaxshot, self.y + self.pozycjayshot, self.predkoscxshot,
                               self.predkoscyshot,
                               rozrzut * self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * tab4[1]),
                               self.rodzajpocisku))
                pifpaf()



#NAJWAZNIEJSZA KLASA TUTAJ NIC NIE RUSZAC!!!
class Projectile():
    def __init__(self,x,y,vx,vy,rozrzut, rodzajpocisku):
        self.x = x
        self.y = y
        self.rozrzut=rozrzut
        self.vx = vx +(rozrzut/50)
        self.vy = vy +(rozrzut/50)
        self.image = rodzajpocisku
        self.istnieje=1
    def missile(self):
        if (self.istnieje==1):
            self.x += self.vx
            self.y += self.vy
            obraz.blit(self.image, [self.x, self.y])
    def trafienie(self):
        for b in lista_statków:
            if b.x < self.x < b.x+60 and b.y < self.y < b.y+60:
                b.hp -= 1
                self.istnieje=0
    def outofmap(self):
        if self.x>szerokoscOkna or self.x<0:
            self.istnieje=0
        if self.y>wysokoscOkna or self.y<0:
            self.istnieje=0

def wynikNapis(killRed, killBlue):#funckja od wyswietlania wyniku
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
    if opcjemenu ==0:
        while True:
            obraz.blit(menu, [0, 0])
            obraz.blit(przyciskstart, [0, 0])
            obraz.blit(przycisksettings, [0, 40])
            obraz.blit(przycisksilnik, [0, 80])
            obraz.blit(przyciskexit,[szerokoscOkna-220,wysokoscOkna-76])
            mouse = pygame.mouse.get_pos()
            #obraz.blit(pocisk, [mouse[0], mouse[1]])
            click = pygame.mouse.get_pressed()
            if 0<mouse[0]<220 and 0<mouse[1]<36:
                if click[0]:
                    opcjemenu = 1
                    break
            if 0<mouse[0]<220 and 40<mouse[1]<76:
                if click[0]:
                    opcjemenu = 2
                    break
            if 0<mouse[0]<220 and 80<mouse[1]<116:
                if click[0]:
                    opcjemenu = 3
                    break
            if szerokoscOkna-220 < mouse[0] < szerokoscOkna and wysokoscOkna-76 < mouse[1] < wysokoscOkna-40:
                if click[0]:
                    sys.exit(0)

            pygame.display.flip()
            off()

    #########################################################################################################
    #menu ustawienia
    if opcjemenu == 2:
        while True:
            obraz.blit(settings, [0, 0])
            obraz.blit(przyciskback,[szerokoscOkna-220,wysokoscOkna-36])
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            obraz.blit(player1, [213, 13])
            obraz.blit(staty, [213, 0])
            if 212 < mouse[0] < 252 and 80 < mouse[1] < 120:
                if click[0]:
                    obraz.blit(przycisk4, [212, 80])
                    lista_statków[0].basehp +=1
                else:
                    obraz.blit(przycisk2, [212, 80])
            if 338< mouse[0] < 378 and 80 < mouse[1] < 120:
                if click[0]:
                    obraz.blit(przycisk3, [338, 80])
                    lista_statków[0].basehp -= 1
                else:
                    obraz.blit(przycisk2, [338, 80])

            obraz.blit(przycisk4, [212, 160])
            obraz.blit(przycisk3, [338, 160])
            obraz.blit(przycisk4, [212, 240])
            obraz.blit(przycisk3, [338, 240])
            obraz.blit(przycisk4, [212, 320])
            obraz.blit(przycisk3, [338, 320])
            obraz.blit(przycisk4, [212, 400])
            obraz.blit(przycisk3, [338, 400])
            obraz.blit(przycisk4, [212, 480])
            obraz.blit(przycisk3, [338, 480])
            hapeki1 = lista_statków[0].basehp
            hapeki1 = str(hapeki1)
            label2 = czcionka.render(hapeki1, 1, kolorNapisu)
            obraz.blit(label2, (260 , 83))
            energie1=335
            energie1 = str(energie1)
            label2 = czcionka.render(energie1, 1, kolorNapisu)
            obraz.blit(label2, (260 , 163))




            #tutaj idzie kod do ustawien
            #tutaj idzie kod do ustawien
            #tutaj idzie kod do ustawien
            #tutaj idzie kod do ustawien


            if szerokoscOkna-220 < mouse[0] < szerokoscOkna and wysokoscOkna-36 < mouse[1] < wysokoscOkna:
                if click[0]:
                    opcjemenu=0
                    break
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                opcjemenu=0
                break
            pygame.display.flip()
            off()

    ################################################################################## ########################
    #puste menu
    if opcjemenu == 3:
        while True:
            obraz.blit(pustemenu, [0, 0])
            obraz.blit(przyciskback,[szerokoscOkna-220,wysokoscOkna-36])
            mouse = pygame.mouse.get_pos()
            obraz.blit(pocisk1, [mouse[0], mouse[1]])
            click = pygame.mouse.get_pressed()


            #tutaj idzie kod do pustego menu
            #tutaj idzie kod do pustego menu
            #tutaj idzie kod do pustego menu
            #tutaj idzie kod do pustego menu


            if szerokoscOkna-220 < mouse[0] < szerokoscOkna and wysokoscOkna-36 < mouse[1] < wysokoscOkna:
                if click[0]:
                    opcjemenu=0
                    break
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                opcjemenu=0
                break
            pygame.display.flip()
            off()




    ##########################################################################################################
    ##########################################################################################################
    #BODY GRY Głównej CALE!!!
    if opcjemenu == 1:
        while True:
            obraz.blit(background, [0, 0])
            if globalnytimer <=10:
                globalnytimer += 1
            if globalnytimer > 10:
                globalnytimer = 0
            clock.tick(60)

            rozrzut = random.randint(-rozrzutmenu, rozrzutmenu)#róra randomizacja rorzuty góra dół
            #wynikNapis(killRed,killBlue)#wywołanie wyniku

            #Updatuje wszystkie pociski z clasy Projectile
            for b in my_missile_list:
                b.missile()
                b.trafienie()
                b.outofmap()
                if b.istnieje==0:
                    my_missile_list.remove(b)

            for b in lista_statków:
                b.update()
                b.shot()
                if b.hp <= 0:
                    killBlue+=1
                    b.hp=b.basehp

            obraz.blit(life, [zyciegracza1, 0])
            obraz.blit(life, [zyciegracza2, 0])
            pygame.display.flip()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:#<------------Powrót do menu
                opcjemenu=0
                break
            off()