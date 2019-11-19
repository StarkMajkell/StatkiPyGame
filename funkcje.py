import pygame
import sys
import random
from zmienne import *

def zasieg(pozycjax, pozycjay, pozycjax2, pozycjay2, range):
    x = ((pozycjax - pozycjax2) ** 2 + (pozycjay - pozycjay2) ** 2) ** (1 / 2)
    if x < range:
        return 1
    else:
        return 0

def strzal():
    a = random.randint(0, 2)
    if a == 0:
        pygame.mixer.Sound.play(zium)
    elif a == 1:
        pygame.mixer.Sound.play(zium2)
    else:
        pygame.mixer.Sound.play(zium3)

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

