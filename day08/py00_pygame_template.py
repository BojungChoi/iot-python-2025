import pygame 
from pygame.locals import QUIT
import sys

pygame.init()
Surface = pygame.display.set_mode((640, 400)) 
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame template')

def main():
    while True:
        Surface.fill(color='white')
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update() 
        FPSCLOCK.tick(30)
if __name__=='__main__':
    main()