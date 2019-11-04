import pygame
import sys
import random
import linecache

pygame.init()  # musi być
pygame.display.set_caption('Statki')
a = pygame.image.load('Grafa/Logo.png')
pygame.display.set_icon(a)

#moduł ze zmiennymi
wysokoscOkna=720
szerokoscOkna=1280
rozmiarOkna=(szerokoscOkna,wysokoscOkna)
obraz = pygame.display.set_mode(rozmiarOkna)
zyciegracza1=0
zyciegracza2=szerokoscOkna-200
opcjemenu=0
my_missile_list=[]
lista_statków=[]
globalnytimer=0
rozrzutmenu= 20
liczbagraczy=2


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
statek3 = pygame.image.load("Grafa/Statek3.png")
statekGrafika_2 = pygame.image.load("Grafa/Statek1-Red1.png")
pocisk=pygame.image.load('Grafa/pocisk.png')
pocisk2=pygame.image.load('Grafa/pocisk2.png')
pocisk4=pygame.image.load('Grafa/pocisk4.png')
pocisk3=pygame.image.load('Grafa/pocisk3.png')
life = pygame.image.load('Grafa/life.png')
music = pygame.mixer.music.load("Dźwięki/pif.mp3")
wczytywanie=0
parametryplayer1=[]

file = open('config/parametry.txt', 'r').read()
lines = file.split('\n')
for line in lines:
    parametryplayer1.append(line)
    print(parametryplayer1)

def f(a, b, c,d,e,f,g,h,i,j,k,l):
    print("%s %s %s %s %s %s %s %s %s %s %s %s" % (a, b, c,d,e,f,g,h,i,j,k,l))

l = [1, 2, 3]
print(f(*parametryplayer1))







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
    def __init__(self,pozycjax,pozycjay,nrstatku,player,pozycjaxshot,pozycjayshot,predkoscxshot,predkoscyshot,modyfikatorrozrzutu,modyfikatorrozstrzalu,hp,rodzajpocisku):
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
        self.hp = hp
        self.basehp = hp
        self.rodzajpocisku=rodzajpocisku
    def update(self):
        if ruchxAD() == 1 or -1:
            if self.player ==1:
                self.x += ruchxAD()
        if ruchyWS() == 1 or -1:
            if self.player ==1:
                self.y += ruchyWS()
        #######################################
        if ruchxLR() == 1 or -1:
            if self.player == 2:
                self.x += ruchxLR()
        if ruchyUD() == 1 or -1:
            if self.player == 2:
                self.y += ruchyUD()
        ########################################
        if ruchxJL() == 1 or -1:
            if self.player == 3:
                self.x += ruchxJL()
        if ruchyIK() == 1 or -1:
            if self.player == 3:
                self.y += ruchyIK()
        #########################################
        if ruchx46() == 1 or -1:
            if self.player == 4:
                self.x += ruchx46()
        if ruchy85() == 1 or -1:
            if self.player == 4:
                self.y += ruchy85()
        obraz.blit(self.image, [self.x, self.y])

    def shot(self):
        if pygame.key.get_pressed()[pygame.K_f]:
            if self.player == 1:
                my_missile_list.append(Projectile(self.x+self.pozycjaxshot, self.y+self.pozycjayshot, self.predkoscxshot, self.predkoscyshot, rozrzut*self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * ruchyWS()),self.rodzajpocisku))
                pifpaf()
        if pygame.key.get_pressed()[pygame.K_p]:
            if self.player == 2:
                my_missile_list.append(Projectile(self.x+self.pozycjaxshot, self.y+self.pozycjayshot, self.predkoscxshot, self.predkoscyshot, rozrzut*self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * ruchyUD()),self.rodzajpocisku))
                pifpaf()
        if pygame.key.get_pressed()[pygame.K_u]:
            if self.player == 3:
                my_missile_list.append(Projectile(self.x+self.pozycjaxshot, self.y+self.pozycjayshot, self.predkoscxshot, self.predkoscyshot, rozrzut*self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * ruchyIK()),self.rodzajpocisku))
                pifpaf()
        if pygame.key.get_pressed()[pygame.K_KP7]:
            if self.player == 4:
                my_missile_list.append(Projectile(self.x+self.pozycjaxshot, self.y+self.pozycjayshot, self.predkoscxshot, self.predkoscyshot, rozrzut*self.modyfikatorrozrzutu + (self.modyfikatorrozstrzalu * ruchy85()),self.rodzajpocisku))
                pifpaf()




#lista_statków.append(Statek(50, 50, statek3, 3, 60, 25, 2.7, 0, 1, 75, 10, pocisk2))

lista_statków.append(Statek(50, 50, statek3, 1, 60, 25, 2.7, 0, 1, 75, 1000, pocisk2))

lista_statków.append(Statek(1100, 50, statek3, 2, 0, 25, -2.7, 0, 1, 75, 10, pocisk2))

#lista_statków.append(Statek(50, 50, statek3, 4, 60, 25, 2.7, 0, 1, 75, 10, pocisk2))

#NAJWAZNIEJSZA KLASA TUTAJ NIC NIE RUSZAC!!!
class Projectile():
    def __init__(self,x,y,vx,vy,rozrzut, rodzajpocisku):
        self.x = x
        self.y = y
        self.rozrzut=rozrzut
        self.vx = vx
        self.vy = vy +(rozrzut/150)
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
            obraz.blit(pocisk, [mouse[0], mouse[1]])
            click = pygame.mouse.get_pressed()


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
            obraz.blit(pocisk, [mouse[0], mouse[1]])
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

            rozrzut = random.randint(-rozrzutmenu, rozrzutmenu)#róra randomizacja rorzuty góra dół
            obraz.blit(tabela,[szerokoscOkna/2-100, 10])
            wynikNapis(killRed,killBlue)#wywołanie wyniku

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