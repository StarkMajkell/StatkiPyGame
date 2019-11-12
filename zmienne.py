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
mapa1=pygame.image.load('Grafa/mapa1.png')
mapmaking=pygame.image.load('Grafa/mapmaking.png')

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
pygame.mixer.music.load("Dźwięki/intel.mp3")
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
enemy1 = pygame.image.load('Grafa/enemy1.png')
enemy2 = pygame.image.load('Grafa/enemy2.png')
grafaStatków = [statek1, statek2, statek3]
grafaEnemy = [enemy1,enemy2]
pociski = [pocisk1, pocisk2, pocisk3, pocisk4]
grafaTuret= [turet1,turet2,turet3,turet2_1]
pygame.mixer.music.play(-1)

