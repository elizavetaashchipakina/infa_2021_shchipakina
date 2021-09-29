import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 800))
screen.fill((255,255,255))

# функция фона
def fon(a, b, c, i, j):
    polygon(screen, (a, b, c), [(0, i), (1200, i), (1200, j), (0, j)])
    
# фон
fon(255, 0, 0, 0, 100)
fon(255, 102, 0, 100, 200)
fon(255, 255, 0, 200, 300)
fon(0, 255, 0, 300, 400)
fon(0, 255, 255, 400, 500)
fon(0, 0, 255, 500, 600)
fon(128, 0, 128, 600, 700)
fon(255, 0, 255, 700, 800)

# функция гуся
def gus(a, b, c, i, j, d, e, f, g, k, l):
    
    # функция клюва гуся
    polygon(screen, (g, k, l), [(550+i, 560+j), (590+i, 580+j), (550+i, 580+j)])

    # функция тела гуся
    ellipse(screen, (a, b, c), (500+i, 550+j, 60, 40))
    ellipse(screen, (a, b, c), (420+i, 550+j, 90, 45))
    ellipse(screen, (a, b, c), (250+i, 550+j, 200, 80))
    
    # функция глаза гуся
    ellipse(screen, (d, e, f), (540+i, 560+j, 10, 10))
    
    # функция ног гуся
    ellipse(screen, (a, b, c), (300+i, 600+j, 50, 60))
    ellipse(screen, (a, b, c), (350+i, 600+j, 50, 60))
    polygon(screen, (a, b, c), [(310+i, 650+j), (380+i, 700+j), (400+i, 700+j), (340+i, 650+j)])
    polygon(screen, (a, b, c), [(360+i, 650+j), (440+i, 700+j), (460+i, 700+j), (390+i, 650+j)])
    
    # функция радужных лапок гуся
    line(screen, (255, 0, 0), (390+i, 700+j), (430+i, 710+j), 5)
    line(screen, (255, 255, 0), (390+i, 700+j), (430+i, 730+j), 5)
    line(screen, (0, 255, 0), (390+i, 700+j), (420+i, 740+j), 5)
    line(screen, (0, 0, 255), (390+i, 700+j), (410+i, 745+j), 5)

    line(screen, (255, 0, 0), (450+i, 700+j), (480+i, 710+j), 5)
    line(screen, (255, 255, 0), (450+i, 700+j), (480+i, 730+j), 5)
    line(screen, (0, 255, 0), (450+i, 700+j), (470+i, 740+j), 5)
    line(screen, (0, 0, 255), (450+i, 700+j), (460+i, 745+j), 5)

    # функция хвоста гуся
    polygon(screen, (a, b, c), [(200+i, 550+j), (150+i, 600+j), (310+i, 600+j)])
    
    # функция крыльев гуся
    polygon(screen, (a, b, c), [(360+i, 555+j), (300+i, 480+j), (200+i, 440+j), (100+i, 350+j), (150+i, 500+j), (300+i, 560+j)])
    polygon(screen, (a, b, c), [(400+i, 555+j), (340+i, 480+j), (240+i, 440+j), (140+i, 350+j), (190+i, 500+j), (340+i, 560+j)])
    line(screen, (0, 0, 0), (355+i, 555+j), (300+i, 480+j))
    line(screen, (0, 0, 0), (300+i, 480+j), (200+i, 440+j))
    line(screen, (128, 128, 128), (200+i, 440+j), (100+i, 350+j))
    
# функция рыбы
def fish(a, b, c, i, j, d, e, f):
    # тело рыбы
    arc(screen, (a, b, c), (600+i, 700+j, 80, 40), 3, 0, 100)
    arc(screen, (a, b, c), (600+i, 700+j, 80, 40), 0, 3, 100)
    
    # хвост рыбы
    polygon(screen, (a, b, c), [(610+i, 720+j), (550+i, 700+j), (550+i, 740+j)])
    
    # глаз рыбы
    circle(screen, (d, e, f), (670+i, 720+j), 4)
    
    # 1 плавник рыбы
    polygon(screen, (a, b, c), [(660+i, 710+j), (650+i, 680+j), (610+i, 680+j), (640+i, 710+j)])
    
    # 2 плавник рыбы
    polygon(screen, (a, b, c), [(660+i, 730+j), (680+i, 747+j), (650+i, 750+j), (650+i, 730+j)])
    
    # 3 плавник рыбы 
    polygon(screen, (a, b, c), [(630+i, 730+j), (620+i, 747+j), (600+i, 750+j), (620+i, 730+j)])

# розовые гуси
gus(255, 204, 255, 0, 0, 0, 51, 102, 204, 0, 0)
gus(255, 51, 153, 400, -300, 204, 255, 255, 153, 0, 51)

# рыбы
fish(204, 255, 0, 0, 0, 0, 0, 0)
fish(128, 0, 128, 400, -300, 255, 255, 255)

pygame.display.update()

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()