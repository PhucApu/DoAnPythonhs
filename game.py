import pygame,sys


pygame.init()
screen = pygame.display.set_mode((500,500))


start = (0, 0)
size = (0, 0)
drawing = False

running = True

while running:
       for event in pygame.event.get():
              if event.type == pygame.QUIT:
                     running = False
              elif event.type == pygame.MOUSEBUTTONDOWN:
                     start = event.pos
                     size = 0, 0
                     drawing = True
              elif event.type == pygame.MOUSEBUTTONUP:
                     end = event.pos
                     size = end[0] - start[0], end[1] - start[1]
                     drawing = False
              elif event.type == pygame.MOUSEMOTION and drawing:
                     end = event.pos
                     size = end[0] - start[0], end[1] - start[1]
                     
       screen.fill("red")
       pygame.draw.rect(screen, "yellow", (start, size), 2)
       pygame.display.update()
