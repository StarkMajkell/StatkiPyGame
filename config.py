#moduł ze zmiennymi
wysokoscOkna=600
szerokoscOkna=1280
rozmiargracza_1=50
rozmiargracza_2=50
kolorstatku1=255
kolorstatku2=255
rozmiarOkna=(szerokoscOkna,wysokoscOkna)
obraz = pygame.display.set_mode(rozmiarOkna)
statek_1 = pygame.Rect(0, wysokoscOkna/2, rozmiargracza_1, rozmiargracza_1)
statek_2 = pygame.Rect(szerokoscOkna-rozmiargracza_2-40, (wysokoscOkna/2), rozmiargracza_2, rozmiargracza_2)
my_missile_list=[]
zyciegracza1=0
zyciegracza2=szerokoscOkna-200
timer_strzalu=0
timer_strzalu2=0


killRed = 0
killBlue = 0
kolorNapisu = (255, 255, 0)
czcionka = pygame.font.SysFont("Comic Sans MS", 60)

background = pygame.image.load("background.jpg").convert()
statekGrafika_1 = pygame.image.load("Statek1-Blue.png")
statekGrafika_1_mask=pygame.mask.from_surface(statekGrafika_1)
statekGrafika_1_rect=statekGrafika_1.get_rect()
statekGrafika_2 = pygame.image.load("Statek1-Red.png")
statekGrafika_2_mask=pygame.mask.from_surface(statekGrafika_2)
pociskGrafika = pygame.image.load('pocisk.png').convert_alpha()
pociskikolor=[]
pociskikolor.append(pygame.image.load('pocisk.png'))
pociskikolor.append(pygame.image.load('pocisk2.png'))
pociskikolor.append(pygame.image.load('pocisk3.png'))


pociskGrafika_mask=pygame.mask.from_surface(pociskGrafika)
life = pygame.image.load('life.png')
music = pygame.mixer.music.load("pif.mp3")



