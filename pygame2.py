import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
screen.fill((255,255,255))

# фон
polygon(screen, (0, 0, 51), [(0, 0), (800, 0), (800, 100), (0, 100)])
polygon(screen, (153, 0, 255), [(0, 100), (800, 100), (800, 150), (0, 150)])
polygon(screen, (255, 102, 255), [(0, 150), (800, 150), (800, 250), (0, 250)])
polygon(screen, (255, 51, 153), [(0, 250), (800, 250), (800, 350), (0, 350)])
polygon(screen, (255, 204, 0), [(0, 350), (800, 350), (800, 450), (0, 450)])
polygon(screen, (0, 51, 102), [(0, 450), (800, 450), (800, 800), (0, 800)])

# птички
arc(screen, (255, 255, 255), (100, 50, 150, 100), 0, 3, 5)
arc(screen, (255, 255, 255), (250, 50, 150, 100), 0, 3, 5)
arc(screen, (255, 255, 255), (300, 200, 150, 100), 0, 3, 5)
arc(screen, (255, 255, 255), (450, 200, 150, 100), 0, 3, 5)
arc(screen, (255, 255, 255), (150, 350, 150, 100), 0, 3, 5)
arc(screen, (255, 255, 255), (300, 350, 150, 100), 0, 3, 5)

# клюв
polygon(screen, (255, 102, 0), [(550, 560), (590, 580), (550, 580)])

# тело гуся
ellipse(screen, (255, 255, 255), (500, 550, 60, 40))
ellipse(screen, (255, 255, 255), (420, 550, 90, 45))
ellipse(screen, (255, 255, 255), (250, 550, 200, 80))

# крылья
polygon(screen, (255, 255, 255), [(360, 555), (300, 480), (200, 440), (100, 350), (150, 500), (300, 560)])
polygon(screen, (255, 255, 255), [(400, 555), (340, 480), (240, 440), (140, 350), (190, 500), (340, 560)])
line(screen, (0, 0, 0), (355, 555), (300, 480))
line(screen, (0, 0, 0), (300, 480), (200, 440))
line(screen, (128, 128, 128), (200, 440), (100, 350))

# хвост
polygon(screen, (255, 255, 255), [(200, 550), (150, 600), (310, 600)] )

# лапы
ellipse(screen, (255, 255, 255), (300, 600, 50, 60))
ellipse(screen, (255, 255, 255), (350, 600, 50, 60))
polygon(screen, (255, 255, 255), [(310, 650), (380, 700), (400, 700), (340, 650)])
polygon(screen, (255, 255, 255), [(360, 650), (440, 700), (460, 700), (390, 650)])

# лапки
line(screen, (255, 102, 0), (390, 700), (430, 710), 5)
line(screen, (255, 102, 0), (390, 700), (430, 730), 5)
line(screen, (255, 102, 0), (390, 700), (420, 740), 5)
line(screen, (255, 102, 0), (390, 700), (410, 745), 5)

line(screen, (255, 102, 0), (450, 700), (480, 710), 5)
line(screen, (255, 102, 0), (450, 700), (480, 730), 5)
line(screen, (255, 102, 0), (450, 700), (470, 740), 5)
line(screen, (255, 102, 0), (450, 700), (460, 745), 5)

# глаз
ellipse(screen, (0, 0, 0), (540, 560, 10, 10))

# рыбка: тело
arc(screen, (128, 128, 128), (600, 700, 80, 40), 3, 0, 100)
arc(screen, (128, 128, 128), (600, 700, 80, 40), 0, 3, 100)

# рыбка: хвост
polygon(screen, (128, 128, 128), [(610, 720), (550, 700), (550, 740)])

# рыбка: плавники
polygon(screen, (128, 128, 128), [(660, 710), (650, 680), (610, 680), (640, 710)])
polygon(screen, (128, 128, 128), [(660, 730), (680, 747), (650, 750), (650, 730)])
polygon(screen, (128, 128, 128), [(630, 730), (620, 747), (600, 750), (620, 730)])

# рыбка: глаз
circle(screen, (0, 0, 0), (670, 720), 4)



pygame.display.update()

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
