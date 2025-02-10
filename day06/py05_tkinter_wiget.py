# py05_tikinter_wiget.py
# Tkinter 위젯 학습용
from tkinter import *
from tkinter.messagebox import *

def buttonClick():    
    showinfo('위젯','버튼을 클릭했습니다!') # 다이얼로그(메시지)박스

root = Tk()
root.title('위젯 예제')

# 이미지 객체
img = PhotoImage(file='./day06/kitty.png')

# 레이블에 이미지 표시
label = Label(root, image=img)
label.pack() # 위젯위치 지정
# 버튼 위젯
button = Button(root, text='클릭', command=buttonClick)
button.pack()
# 엔트리 위젯 - 사용자 입력
entry = Entry(root)
entry.pack()
# 라디오버튼 # 단일선택
Label(root, text='가장 선호하는 프로그래밍 언어 선택').pack()

choice = IntVar()
Radiobutton(root, text='C',value=1, variable=choice).pack(anchor = W) # variable=choice -> 출력 때 체크가 되어있는데, 체크없애줌 / value=1 -> 안해놓으면 전체 선택 됨
Radiobutton(root, text='C#',value=2, variable=choice).pack(anchor = W)
Radiobutton(root, text='JAVA',value=3, variable=choice).pack(anchor = W)
Radiobutton(root, text='Python',value=4, variable=choice).pack(anchor = W)

# 체크박스 # 다중선택
Label(root, text='좋아하는 과일을 모두 선택').pack() 

orange = IntVar()
Checkbutton(root, text='오렌지', variable=orange).pack(anchor = W)
banana = IntVar()
Checkbutton(root, text='바나나', variable=banana).pack(anchor = W)
mango = IntVar()
Checkbutton(root, text='망고', variable=mango).pack(anchor = W)

# 리스트박스 위젯
lstbox = Listbox(root, height=4)
lstbox.pack()
lstbox.insert(END,'Python')
lstbox.insert(END,'JAVA')
lstbox.insert(END,'Ruby')
lstbox.insert(END,'PHP')

# 컨테이너 위젯 중(프레임)
frame = Frame(root, width=600, height=40, bg='pink')
frame.pack()

#프레임 위젯에 들어갈 위젯
button2 = Button(frame, text='버튼2' ,width=20)
button2.pack(side=LEFT)
button3 = Button(frame, text='버튼3',width=20)
button3.pack(side=LEFT)
button4 = Button(frame, text='버튼4',width=20)
button4.pack(side=LEFT)


root.mainloop()