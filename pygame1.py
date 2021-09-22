import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255,255,255))


circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (255, 0, 0), (150, 160), 30)
circle(screen, (255, 0, 0), (250, 160), 25)
circle(screen, (0, 0, 0), (150, 160), 20)
circle(screen, (0, 0, 0), (250, 160), 15)
polygon(screen, (0, 0, 0), [(180, 160),  (100, 40), (110, 30), (190, 150)])
polygon(screen, (0, 0, 0), [(220, 160), (210, 150), (330, 40), (340, 50)])
polygon(screen, (0, 0, 0), [(150, 250), (250, 250), (250, 260), (150, 260)])
pygame.display.update()

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()