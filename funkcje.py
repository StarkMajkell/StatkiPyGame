import pygame
import sys
import random
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


def napisybloki(gracz,step):
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