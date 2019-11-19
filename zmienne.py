import pygame
import sys
import random

#pygame.init()  # musi być
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.init()
pygame.font.init()
pygame.display.set_caption('Statki')
a = pygame.image.load('Grafa/Logo.png')
pygame.display.set_icon(a)
pygame.mixer.set_num_channels(30)
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
lista_enemy= []
lista_turet=[]
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
lista_odrzut= []
lista_eksplozji=[]




listakropekkordyx = []
listakropekkordyy = []
listakropekkordyx2 = []
listakropekkordyy2 = []



killRed = 0
killBlue = 0
kolorNapisu = (0, 255, 255)
czcionka = pygame.font.Font("Czcionki/digital-7.ttf", 40)
czcionka1 = pygame.font.Font("Czcionki/digital-7.ttf", 13)
background = pygame.image.load("Grafa/background2.jpg").convert()
menu = pygame.image.load("Grafa/backgroundmenu.jpg").convert()
settings = pygame.image.load('Grafa/settings.jpg').convert()
przyciskback = pygame.image.load('Grafa/przyciskback.png')
menuopcje1= pygame.image.load('Grafa/menuopcje1.png')
menuopcje2= pygame.image.load('Grafa/menuopcje2.png')
platform=pygame.image.load('Grafa/platform.png')
mapa1=pygame.image.load('Grafa/mapa1.png')
mapmaking=pygame.image.load('Grafa/mapmaking.png')
zium=pygame.mixer.Sound('Dźwięki/zium.ogg')
zium2=pygame.mixer.Sound('Dźwięki/zium2.ogg')
zium3=pygame.mixer.Sound('Dźwięki/zium3.ogg')
boom1=pygame.mixer.Sound('Dźwięki/boom1.ogg')
boom2=pygame.mixer.Sound('Dźwięki/boom2.ogg')
kick=pygame.mixer.Sound('Dźwięki/kick.ogg')
punch=pygame.mixer.Sound('Dźwięki/punch.ogg')

staty = pygame.image.load('Grafa/staty.png')
pasek = pygame.image.load('Grafa/pasek.png')
oko = pygame.image.load('Grafa/czaszkaoko.png')
energiaGraph=pygame.image.load('Grafa/energy.png')
czaszka = pygame.image.load('Grafa/czaszka4.png')
staty2 = pygame.image.load('Grafa/staty2.png')
staty3 = pygame.image.load('Grafa/staty3.png')
staty4 = pygame.image.load('Grafa/staty4.png')
przycisksettings = pygame.image.load('Grafa/przycisksettings.png')
przycisksettings1 = pygame.image.load('Grafa/przycisksettings1.png')
przyciskstart = pygame.image.load('Grafa/przyciskstart.png')
przyciskstart1 = pygame.image.load('Grafa/przyciskstart1.png')

przycisk2 = pygame.image.load('Grafa/przycisk2.png')
przycisk3 = pygame.image.load('Grafa/przycisk3.png')
przycisk4 = pygame.image.load('Grafa/przycisk4.png')
pustemenu = pygame.image.load('Grafa/pustemenu.jpg')
przyciskdefence = pygame.image.load('Grafa/przyciskdefence.png')
przyciskdefence1 = pygame.image.load('Grafa/przyciskdefence1.png')
statek1 = pygame.image.load("Grafa/statek1.png")
statek2 = pygame.image.load("Grafa/statek2.png")
statek3 = pygame.image.load("Grafa/statek3.png")
pocisk1 = pygame.image.load('Grafa/pocisk.png')
pocisk2 = pygame.image.load('Grafa/pocisk2.png')
pocisk4 = pygame.image.load('Grafa/pocisk4.png')
pocisk3 = pygame.image.load('Grafa/pocisk3.png')
pocisk5 = pygame.image.load('Grafa/pocisk5.png')
tabelaplayer1=pygame.image.load('Grafa/statyp1.png')
tabelaplayer2=pygame.image.load('Grafa/statyp2.png')
tabelaplayer3=pygame.image.load('Grafa/statyp3.png')
tabelaplayer4=pygame.image.load('Grafa/statyp4.png')
life1 = pygame.image.load('Grafa/life1.png')
sklepmenuturety = pygame.image.load('Grafa/sklepmenuturety.png')
pygame.mixer.music.load("Dźwięki/nutka1.ogg")
turet1=pygame.image.load('Grafa/turet1.png')
turet2=pygame.image.load('Grafa/turet2.png')
turet3=pygame.image.load('Grafa/turet3.png')
turet2_1=pygame.image.load('Grafa/turet2-1.png')
turet2_2=pygame.image.load('Grafa/turet2-2.png')
turet2_3=pygame.image.load('Grafa/turet2-3.png')
turet2_4=pygame.image.load('Grafa/turet2-4.png')
turet2_5=pygame.image.load('Grafa/turet2-5.png')
turet2_6=pygame.image.load('Grafa/turet2-6.png')
turet2_7=pygame.image.load('Grafa/turet2-7.png')
turet2_8=pygame.image.load('Grafa/turet2-8.png')
pocisk6_1=pygame.image.load('Grafa/pocisk6_1.png')
pocisk6_2=pygame.image.load('Grafa/pocisk6_2.png')
pocisk6_3=pygame.image.load('Grafa/pocisk6_3.png')
pocisk6_4=pygame.image.load('Grafa/pocisk6_4.png')
pocisk6_5=pygame.image.load('Grafa/pocisk6_5.png')
pocisk6_6=pygame.image.load('Grafa/pocisk6_6.png')
pocisk6_7=pygame.image.load('Grafa/pocisk6_7.png')
pocisk6_8=pygame.image.load('Grafa/pocisk6_8.png')
odrzut1_1=pygame.image.load('Grafa/odrzut1_1.png')
odrzut1_2=pygame.image.load('Grafa/odrzut1_2.png')
odrzut1_3=pygame.image.load('Grafa/odrzut1_3.png')
odrzut1_4=pygame.image.load('Grafa/odrzut1_4.png')
odrzut1_5=pygame.image.load('Grafa/odrzut1_5.png')
odrzut1_6=pygame.image.load('Grafa/odrzut1_6.png')
odrzut1_7=pygame.image.load('Grafa/odrzut1_7.png')
enemy1 = pygame.image.load('Grafa/enemy1.png')
enemy2 = pygame.image.load('Grafa/enemy2.png')
enemy5_1 = pygame.image.load('Grafa/enemy5_1.png')
enemy5_2 = pygame.image.load('Grafa/enemy5_2.png')
enemy5_3 = pygame.image.load('Grafa/enemy5_3.png')
enemy5_4 = pygame.image.load('Grafa/enemy5_4.png')
enemy5_5 = pygame.image.load('Grafa/enemy5_5.png')
enemy5_6 = pygame.image.load('Grafa/enemy5_6.png')
enemy5_7 = pygame.image.load('Grafa/enemy5_7.png')
enemy5_8 = pygame.image.load('Grafa/enemy5_8.png')
eksplosion1_1=pygame.image.load('Grafa/eksplosion1_1.png')
eksplosion1_2=pygame.image.load('Grafa/eksplosion1_2.png')
eksplosion1_3=pygame.image.load('Grafa/eksplosion1_3.png')
eksplosion1_4=pygame.image.load('Grafa/eksplosion1_4.png')
eksplosion2_1=pygame.image.load('Grafa/eksplosion2_1.png')
eksplosion2_2=pygame.image.load('Grafa/eksplosion2_2.png')
eksplosion2_3=pygame.image.load('Grafa/eksplosion2_3.png')
eksplosion2_4=pygame.image.load('Grafa/eksplosion2_4.png')
eksplosion2_5=pygame.image.load('Grafa/eksplosion2_5.png')
eksplosion2_6=pygame.image.load('Grafa/eksplosion2_6.png')
eksplosion2_7=pygame.image.load('Grafa/eksplosion2_7.png')
eksplosion2_8=pygame.image.load('Grafa/eksplosion2_8.png')
ludz=pygame.image.load('Grafa/ludz.png')
ludzlewo=pygame.image.load('Grafa/ludzlewo.png')
ludzprawo=pygame.image.load('Grafa/ludzprawo.png')
ludzgóra=pygame.image.load('Grafa/ludzgóra.png')
ludzskok=pygame.image.load('Grafa/ludzskok.png')
ludzskok1=pygame.image.load('Grafa/ludzskok1.png')
ludzskok2=pygame.image.load('Grafa/ludzskok2.png')
ludzskok3=pygame.image.load('Grafa/ludzskok3.png')
ludzkop1=pygame.image.load('Grafa/ludzkop1.png')
ludzkop3=pygame.image.load('Grafa/ludzkop3.png')
ludzpunch1=pygame.image.load('Grafa/ludzpunch1.png')
ludzpunch3=pygame.image.load('Grafa/ludzpunch3.png')
ludzkuc=pygame.image.load('Grafa/ludzkuc.png')
efekt1=pygame.image.load('Grafa/efekt1.png')
efekt2=pygame.image.load('Grafa/efekt2.png')
efekt3=pygame.image.load('Grafa/efekt3.png')
grafaStatków = [statek1, statek2, statek3]
grafaEnemy = [enemy1,enemy2,enemy5_1]
pociski = [pocisk1, pocisk2, pocisk3, pocisk4,pocisk5]
listaodrzutów = [odrzut1_1,odrzut1_2,odrzut1_3,odrzut1_4,odrzut1_5,odrzut1_6,odrzut1_7]
eksplozje = [eksplosion1_1,eksplosion1_2,eksplosion1_3,eksplosion1_4]
eksplozje2 = [eksplosion2_1,eksplosion2_2,eksplosion2_3,eksplosion2_4,eksplosion2_5,eksplosion2_6,eksplosion2_7,eksplosion2_8]
grafaTuret= [turet1,turet2,turet3,turet2_1]
listaefektów=[efekt1,efekt2,efekt2,efekt2,efekt3,efekt3]
#pygame.mixer.music.play(-1)

tabeleagrawitacji=[11,11,12,8,6,5,4.8,4.5,4.2,3.8,3,2.1,1,0.5,0.2,0.1,0.1,-0.1,-0.1,-0.2,-0.5,-1,-2.1,-3,-3.8,-4.2,-4.5,-4.8,-5,-6,-8,-12,-11,-11,]

