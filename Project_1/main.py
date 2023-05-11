import pygame,sys
from setting import *

class Game:
       def __init__(self) -> None:
              pygame.init()
              self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))    # set screen with height and width
              self.clock = pygame.time.Clock()          # create clock
              pygame.display.set_caption("DEMO")        # set title screen
              
       def run(self) -> None:
              running = True
              while running:
                     for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                   running =  False
                                   sys.exit()

                     dt = self.clock.tick(60)           # make fps
                     pygame.display.update()
                     

if __name__ == "__main__":
       game = Game()
       game.run()