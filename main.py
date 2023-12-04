import pygame 
import sys


W = 600
H = 400

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

rect = pygame.Rect((10, 0, 30, 30))
print(rect.bottomright)
print(rect.left)


while True:

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill((0, 255, 0))   
    pygame.draw.circle(sc, (0, 0, 255), (100, 100), 30)

    
    clock.tick(60)
    pygame.display.update()