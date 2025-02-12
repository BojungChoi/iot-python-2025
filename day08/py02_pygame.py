# py02_pygame.py
# Pygame 그래픽 표현 (선, 사각형, 원...)
import pygame 
from pygame.locals import QUIT
from pygame.draw import line
from pygame.draw import rect
from pygame.draw import * # * 을넣으면 line, rect 등 다른 메소드를 넣을필요없이 다 들어감
import pygame.image as image
import sys

pygame.init()
Surface = pygame.display.set_mode((400, 400)) 
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Graphic')

def main():
    # 이미지 로드
    smileman = image.load('./image/happy64px.png')
    #텍스트 변수
    myFont = pygame.font.SysFont('NanumGothic', 50)
    message1 = myFont.render('This is my message', True, (255, 180, 255)) # True -> antialias -> 그래픽 계단현상 부드럽게해주는것.
    message2 = myFont.render('This is PyGame', False, (255, 100, 255))

    while True:
        Surface.fill(color='black')
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()



        # 화면표현, start_pos=(x, y)

        # 선
        pygame.draw.line(Surface, color=(255,200,255), start_pos=(30, 30), end_pos=(150, 30), width=5)
        line(Surface, (0,255,0), (30, 60), (150, 70), 7) # 상단에 From pygame pygame.draw import line 을 설정해뒀으니 pygame.draw.을 넣을 필요없음.
        line(Surface, (0,0,255), (30, 90), (150, 150), 5)

        for x in range(10, 400, 20): 
            line(Surface, 'white', (x, 0),(x, 400))
        for y in range(10, 400, 20):
            line(Surface, 'white', (0, y),(400, y))

        
        # 사각형
        pygame.draw.rect(Surface, color='white', rect=(200, 30, 50, 50)) # x축 y축 시작, 50x50 크기
        rect(Surface, (255,0,0), (260, 30, 100, 50), 4)

        # 원, 타원
        pygame.draw.circle(Surface, (255,255, 0), (60, 160), 30) # 원의 중심이 시작점이라 왼쪽으로 밀려보일 수 있어 계산하고 땡겨줘야함
        circle(Surface, (255,255,255), (110, 170), 20)
        circle(Surface, (255, 112, 20), (150,170), 20, 10)

        # 타원
        pygame.draw.ellipse(Surface, color=(255,150,255), rect=(280, 320, 100, 50))
        # polygon 다각형(별 ...)

        # 이미지 flaticon.com
        Surface.blit(smileman, (150,272))
        Surface.blit(smileman, (0, 272), (0, 20, 32, 32)) #이미지 자르기 X,Y, X의길이 ,Y의길이

        # 텍스트
        Surface.blit(message1,(30, 210))
        Surface.blit(message2,(30, 240))


        pygame.display.update() 
        FPSCLOCK.tick(30)
if __name__=='__main__':
    main()