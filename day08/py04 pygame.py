# py04pygame.py
# 마우스 이벤트
import pygame 
from pygame.locals import QUIT , MOUSEBUTTONDOWN, MOUSEBUTTONUP,MOUSEMOTION
import sys

pygame.init()
Surface = pygame.display.set_mode((640, 400)) 
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Mouse')

def main():
    pos = []
    check = mousebutton = False
    while True:
        Surface.fill(color='white')
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
               # pos.append(event.pos)
                check = True
                mousebutton = True
            elif event.type == MOUSEMOTION:
                if mousebutton: pos.append(event.pos)
            elif event.type == MOUSEBUTTONUP:
                mousebutton = False
                check = False
                pos.clear()

        # for mpos in pos:
        #     pygame.draw.circle(Surface, 'black', mpos, 5)

        if check:
            if len(pos) > 1:
                pygame.draw.lines(Surface, 'black', False, pos)


        pygame.display.update() 
        FPSCLOCK.tick(30)
if __name__=='__main__':
    main()