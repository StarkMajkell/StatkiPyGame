import pygame
import sys
import random

pygame.init()  # musi być
pygame.display.set_caption('Statki')
a = pygame.image.load('Grafa/Logo.png')
pygame.display.set_icon(a)

#moduł ze zmiennymi
wysokoscOkna=720
szerokoscOkna=1280
rozmiargracza_1=50
rozmiargracza_2=50
rozmiarOkna=(szerokoscOkna,wysokoscOkna)
obraz = pygame.display.set_mode(rozmiarOkna)
statek_1 = pygame.Rect(0, wysokoscOkna/2, rozmiargracza_1, rozmiargracza_1)
statek_2 = pygame.Rect(szerokoscOkna-rozmiargracza_2-40, (wysokoscOkna/2), rozmiargracza_2, rozmiargracza_2)
zyciegracza1=0
zyciegracza2=szerokoscOkna-200
timer_strzalu=0
timer_strzalu2=0
opcjemenu=0
pociskikolor=[]
my_missile_list=[]
timer=0
rozrzutmenu= 20


killRed = 0
killBlue = 0
kolorNapisu = (0, 255, 255)
czcionka = pygame.font.Font("Czcionki/digital-7.ttf", 60)

background = pygame.image.load("Grafa/background2.jpg").convert()
menu = pygame.image.load("Grafa/backgroundmenu.jpg").convert()
background1920 = pygame.image.load("Grafa/background1920.png")
settings= pygame.image.load('Grafa/settings.jpg').convert()
przyciskback= pygame.image.load('Grafa/przyciskback.png')
przycisk= pygame.image.load('Grafa/przycisk.png')
przycisksettings=pygame.image.load('Grafa/przycisksettings.png')
przyciskstart=pygame.image.load('Grafa/przyciskstart.png')
przyciskexit=pygame.image.load('Grafa/przyciskexit.png')
pustemenu=pygame.image.load('Grafa/pustemenu.jpg')
tabela=pygame.image.load('Grafa/tabela.png')
przycisksilnik=pygame.image.load('Grafa/przycisksilnik.png')
statekGrafika_1 = pygame.image.load("Grafa/Statek1-Blue1.png")
statekGrafika_1_mask=pygame.mask.from_surface(statekGrafika_1)
statekGrafika_1_rect=statekGrafika_1.get_rect()
statekGrafika_2 = pygame.image.load("Grafa/Statek1-Red1.png")
statekGrafika_2_mask=pygame.mask.from_surface(statekGrafika_2)
pociskGrafika = pygame.image.load('Grafa/pocisk.png').convert_alpha()
pociskikolor.append(pygame.image.load('Grafa/pocisk.png'))
pociskikolor.append(pygame.image.load('Grafa/pocisk4.png'))
pociskikolor.append(pygame.image.load('Grafa/pocisk3.png'))


pociskGrafika_mask=pygame.mask.from_surface(pociskGrafika)
life = pygame.image.load('Grafa/life.png')
music = pygame.mixer.music.load("Dźwięki/pif.mp3")




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
def ruchy85():
    if pygame.key.get_pressed()[pygame.K_KP8]:
        return -1
    elif pygame.key.get_pressed()[pygame.K_KP5]:
        return 1
    else:
        return 0
def ruchx46():
    if pygame.key.get_pressed()[pygame.K_KP4]:
        return -1
    elif pygame.key.get_pressed()[pygame.K_KP6]:
        return 1
    else:
        return 0
def ruchyIK():
    if pygame.key.get_pressed()[pygame.K_i]:
        return -1
    elif pygame.key.get_pressed()[pygame.K_k]:
        return 1
    else:
        return 0
def ruchxJL():
    if pygame.key.get_pressed()[pygame.K_j]:
        return -1
    elif pygame.key.get_pressed()[pygame.K_l]:
        return 1
    else:
        return 0

def off():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
def pifpaf():
    pygame.mixer.music.play(0)
    pygame.mixer.music.play(1)


##Klasa gracza
class Statek():
    def __init__(self,pozycjax,pozycjay,nrstatku,player,pozycjaxshot,pozycjayshot,predkoscxshot,predkoscyshot,modyfikatorrozrzutu,modyfikatorrozstrzalu):
        self.image = nrstatku
        self.x = pozycjax
        self.y = pozycjay
        self.player = player
        self.pozycjaxshot =pozycjaxshot
        self.pozycjayshot=pozycjayshot
        self.predkoscxshot=predkoscxshot
        self.predkoscyshot=predkoscyshot
        self.modyfikatorrozrzutu=modyfikatorrozrzutu
        self.modyfikatorrozstrzalu=modyfikatorrozstrzalu
    def update(self):
        if ruchxAD() == 1 or -1:
            if self.player ==1:
                self.x += ruchxAD()
        if ruchyWS() == 1 or -1:
            if self.player ==1:
                self.y += ruchyWS()
        #######################################
        if ruchxLR() == 1 or -1:
            if self.player ==2:
                self.x += ruchxLR()
        if ruchyUD() == 1 or -1:
            if self.player ==2:
                self.y += ruchyUD()
        ########################################
        if ruchxJL() == 1 or -1:
            if self.player ==3:
                self.x += ruchxJL()
        if ruchyIK() == 1 or -1:
            if self.player == 3:
                self.y += ruchyIK()
        #########################################
        if ruchx46() == 1 or -1:
            if self.player==4:
                self.x += ruchx46()
        if ruchy85() == 1 or -1:
            if self.player==4:
                self.y += ruchy85()
        obraz.blit(self.image, [self.x, self.y])

    def shot(self):
        if pygame.key.get_pressed()[pygame.K_f]:
            if self.player == 1:
                my_missile_list.append(Projectile(self.x+self.pozycjaxshot, self.y+self.pozycjayshot, self.predkoscxshot, self.predkoscyshot, rozrzut*self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * ruchyWS())))
                pifpaf()
        if pygame.key.get_pressed()[pygame.K_p]:
            if self.player == 2:
                my_missile_list.append(Projectile(self.x+self.pozycjaxshot, self.y+self.pozycjayshot, self.predkoscxshot, self.predkoscyshot, rozrzut*self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * ruchyWS())))
                pifpaf()
        if pygame.key.get_pressed()[pygame.K_u]:
            if self.player == 3:
                my_missile_list.append(Projectile(self.x+self.pozycjaxshot, self.y+self.pozycjayshot, self.predkoscxshot, self.predkoscyshot, rozrzut*self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * ruchyWS())))
                pifpaf()
        if pygame.key.get_pressed()[pygame.K_KP7]:
            if self.player == 4:
                my_missile_list.append(Projectile(self.x+self.pozycjaxshot, self.y+self.pozycjayshot, self.predkoscxshot, self.predkoscyshot, rozrzut*self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * ruchyWS())))
                pifpaf()


czarek=Statek(50,50,statekGrafika_1,3,30,25,2.7,0,1,75)
czarek2=Statek(110,500,statekGrafika_2,4,-20,30,0,3,1,75)




#NAJWAZNIEJSZA KLASA TUTAJ NIC NIE RUSZAC!!!
class Projectile():
    def __init__(self,x,y,vx,vy,rozrzut):
        self.x = x
        self.kolizja1 = 0
        self.kolizja2 = 0
        self.y = y
        self.rozrzut=rozrzut
        self.vx = vx
        self.vy = vy +(rozrzut/150)
        #self.image = pociskGrafika
        self.image = pociskikolor[rand]
        self.istnieje=1
    def missile(self):
        if (self.istnieje==1):
            self.x += self.vx
            self.y += self.vy
            obraz.blit(self.image, [self.x, self.y])
    def siongracz1(self):
        if (self.istnieje == 1):
            if statek_1.x<(self.x+12)<(statek_1.x+rozmiargracza_1) and statek_1.y<(self.y)<(statek_1.y+rozmiargracza_1) and self.vx<0:
                self.kolizja1=1
    def siongracz2(self):
        if (self.istnieje == 1):
            if statek_2.x<(self.x)<(statek_2.x+rozmiargracza_2) and statek_2.y<(self.y)<(statek_2.y+rozmiargracza_2)and self.vx>0:
                self.kolizja2=1
    def outofmap(self):
        if self.x>szerokoscOkna or self.x<0:
            self.y = 2*wysokoscOkna+20
            self.istnieje=0
        if self.y>wysokoscOkna or self.y<0:
            self.y = 2*wysokoscOkna+20
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
            obraz.blit(pociskGrafika, [mouse[0], mouse[1]])
            click = pygame.mouse.get_pressed()
            pociskGrafika_rect = pociskGrafika.get_rect()
            przyciskstart_rect = przyciskstart.get_rect()
            if pygame.Rect.collidepoint(przyciskstart_rect, mouse[0], mouse[1]):
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
            obraz.blit(pociskGrafika, [mouse[0], mouse[1]])
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

    #########################################################################################################
    #puste menu
    if opcjemenu == 3:
        while True:
            obraz.blit(pustemenu, [0, 0])
            obraz.blit(przyciskback,[szerokoscOkna-220,wysokoscOkna-36])
            mouse = pygame.mouse.get_pos()
            obraz.blit(pociskGrafika, [mouse[0], mouse[1]])
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
            #obraz.blit(background1920, [0,0])
            obraz.blit(background, [0, 0])
            if timer <=10:
                timer += 1
            if timer > 10:
                timer = 0
            #timer strzalu gracza 1
            if timer_strzalu >0:
                timer_strzalu -=1

            #timer strzalu gracza2
            if timer_strzalu2 > 0:
                timer_strzalu2 -= 1

            rozrzut = random.randint(-rozrzutmenu, rozrzutmenu)#róra randomizacja rorzuty góra dół
            rand = random.randint(1, 1)#randomizacja koloru pocisków


            # poruszanie sie
            statek_1.x += ruchxAD()
            statek_1.y += ruchyWS()
            statek_2.x += ruchxLR()
            statek_2.y += ruchyUD()

            # teleportacja na granicach mapy na przeciwną stronę
            statek_1.x = granicePlanszyX(statek_1.x)
            statek_1.y = granicePlanszyY(statek_1.y)
            statek_2.x = granicePlanszyX(statek_2.x)
            statek_2.y = granicePlanszyY(statek_2.y)

            #moduł pod pozycje skąd mają wystrzelić pociski
            shotplayer1x = statek_1.x + 34
            shotplayer1y = statek_1.y + rozmiargracza_1 / 2
            shotplayer2x = statek_2.x - 5
            shotplayer2y = statek_2.y + rozmiargracza_2 / 2

            #sprawdzanie zderzenia statków
            #offset=(statek_1.x-statek_2.x,statek_1.y-statek_2.y)
            #kolizja=statekGrafika_1_mask.overlap(statekGrafika_2_mask, offset)
            #if kolizja:#<-------------co sie dzieje kiedy sie zderzą
                #zyciegracza1-=1
                #zyciegracza2+=1

            obraz.blit(tabela,[szerokoscOkna/2-100, 10])
            wynikNapis(killRed,killBlue)#wywołanie wyniku

            obraz.blit(statekGrafika_1, [statek_1.x, statek_1.y])#to tutaj sa nasze statki, pamiętaj
            obraz.blit(statekGrafika_2, [statek_2.x, statek_2.y])#to tutaj sa nasze statki, pamiętaj

            #czarek.shot()
            #Updatuje wszystkie pociski z clasy Projectile
            for b in my_missile_list:
                b.missile()
                b.siongracz1()
                if b.kolizja1==1:
                    zyciegracza1-=5
                    b.kolizja1=0
                    b.istnieje=0
                    #killRed += 1 #<-------------Odplala licznik kolizji
                b.siongracz2()
                if b.kolizja2 == 1:
                    zyciegracza2 += 5
                    b.kolizja2 = 0
                    b.istnieje=0
                    #killBlue += 1#<-------------Odplala licznik kolizji
                b.outofmap()
                if b.istnieje==0:
                    my_missile_list.remove(b)


            czarek.update()
            czarek.shot()
            czarek2.update()
            czarek2.shot()
            #zycie i co sie dzieje po smierci
            if zyciegracza1 <= -200:
                zyciegracza1 = 0
                killRed += 1
                statek_1 = pygame.Rect(0, 100, rozmiargracza_1, rozmiargracza_1)


            if zyciegracza2 >= szerokoscOkna:
                zyciegracza2 = szerokoscOkna - 200
                killBlue += 1
                statek_2 = pygame.Rect(szerokoscOkna - rozmiargracza_2 - 40, (wysokoscOkna - 100), rozmiargracza_2, rozmiargracza_2)

        #moduł wystrzeliwania pocisków, dźwięki, trajektorie ilości etc.
            #gracz 1
            if pygame.key.get_pressed()[pygame.K_f] and timer_strzalu < 2:
                my_missile_list.append(Projectile(shotplayer1x, shotplayer1y, 2.7, 0, rozrzut+(75*ruchyWS())))
                pygame.mixer.music.play(0)
                pygame.mixer.music.play(1)
                timer_strzalu += 23
            #gracz 2)
            if pygame.key.get_pressed()[pygame.K_p] and timer_strzalu2 < 2:
                rand = random.randint(0,2)
                my_missile_list.append(Projectile(shotplayer2x, shotplayer2y - 6, -2.6, 0, rozrzut+(75*ruchyUD())))
                my_missile_list.append(Projectile(shotplayer2x, shotplayer2y - 16, -2.54, 0, rozrzut-0.2+(75*ruchyUD())))
                my_missile_list.append(Projectile(shotplayer2x, shotplayer2y + 13, -2.6, 0, rozrzut+(75*ruchyUD())))
                my_missile_list.append(Projectile(shotplayer2x, shotplayer2y + 23, -2.54, 0, rozrzut+0.2+(75*ruchyUD())))
                pygame.mixer.music.play(0)
                pygame.mixer.music.play(1)
                timer_strzalu2 += 0

            obraz.blit(life, [zyciegracza1, 0])
            obraz.blit(life, [zyciegracza2, 0])
            pygame.display.flip()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:#<------------Powrót do menu
                opcjemenu=0
                break
            off()