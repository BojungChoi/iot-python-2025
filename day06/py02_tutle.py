# py02_tutle.py
# 터틀 라이브러리는 주피터노트북에서 실행 불가
import turtle as t

t.home()
t.shape('turtle') # 마우스커서 거북이모양

for i in range(3):
    t.forward(100) # 100만큼이동
    t.left(120) # 120도로 꺽음

t.done() # 반드시 필요
