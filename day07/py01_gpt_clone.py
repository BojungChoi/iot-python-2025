# py01_gpt_clone.py
# GUI를 위한 모듈
from tkinter import * # tkinter 모듈에 있는 모든 클래스, 함수, 변수등을 다쓰겠다.
from tkinter.messagebox import * # 모듈 밑에 있는 모듈을 from tkinter import * 로 가져올 수 없음. 추가로 생성
from tkinter.scrolledtext import *
from tkinter.font import *
# 제미나이를 위한 모듈
import google.generativeai as genai

# 6. 제미나이 API용 구성
genai.configure(api_key='AIzaSyADf2vc14JKpvO-kUT5IGaIVWCudXxCMA8') # 신청한 API키

model = genai.GenerativeModel('gemini-1.5-flash') # AI 사전훈련된 훈련모델



# 4. 전송버튼 이벤트  6. 제미나이 실행 포함
def responseMessage():
    # showinfo('실행','API를 실행합니다!')
    inputText = textMessage.get('1.0', END).replace('\n','').strip()
    print(inputText)
    # showinfo('결과', inputText) # 다이얼로그, 모달(Modal)창->제어권을 갖는 창 

    if inputText:
        try:
            textResult.insert(END, '유저:', BOLD)
            textResult.insert(END,f'{inputText}\n\n', 'user') # 'user' 텍스트 아규먼트

            ai_response = model.generate_content(inputText)
            response = ai_response.text

            textResult.insert(END, '챗봇: ', 'bold')
            textResult.insert(END,f'{response}\n\n', 'ai') # 'ai' 텍스트 아규먼트

            textMessage.delete('1.0',END) # 입력창 글 지우기
            textResult.see(END) # 스크롤텍스트 마지막위치로 스크롤 다운   
        except Exception as e:
            textResult.insert(END,f'Error: {str(e)}\n\n','error')
        finally:
            textResult.see(END)

# 8-2. textMessage 위젯에서 엔터를 치면 전송버튼 클릭 
def KeyPress(event):
    # print(repr(event.char)) # repr 안쓰면 \r, \x80 표시안됨
    # \r(캐리지 리턴), \n(뉴라인) 혼용해서 사용\r\n, \n, \r 
    if event.char == '\r':
        responseMessage()
# 11. 종료시 이벤트처리 함수
def onClosing():
    if askyesno('종료확인','종료하시겠습니까?'):
        # askyesno , askokcancel 사용가능 예,아니오 / 확인, 취소
        root.destroy() # 완전 종료.

# 1. 메인윈도우 생성, 초기설정
root = Tk()
root.title('제미나이 챗봇')
root.geometry('730x450')
# 12. 아이콘 변경
# ./image/ 경로는 삭제
root.iconbitmap('chatbot.ico') # Pyinstaller로 설치할땐 해당폴더에 복사하고 경로를바꿔야함.

# 7. 전체에서 사용할 폰트 지정 -> 나눔고딕 : root = Tk() 하단에 넣어야함!

myFont = Font(family='NanumGothic', size=10)
boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)


# 2. UI화면 구성

inputFrame = Frame(root, width=730, height=30, bg='#EFEFEF')
inputFrame.pack(side=BOTTOM, fill=BOTH) # BOTOM,'bottom' 둘다 사용가능

# 3. inputFrame에 들어갈 Entry와 Button 구성
textMessage = Text(inputFrame, width=75, height=1, wrap=WORD, font=myFont) # wrap=word래핑, 글자단위로 줄바꿈.
# 8. 입력창에서 Enter 를 치면 Keypress 이벤트처리함수 발생 bind
textMessage.bind('<Key>', KeyPress)
textMessage.pack(side=LEFT, padx=15)

buttonSend = Button(inputFrame, text='전송',bg='Green', fg='white',
                    font=myFont,
                     command=responseMessage)
buttonSend.pack(side=RIGHT, padx=20, pady=5)

# 5. API호출 결과메시지 출력될 스크롤기능 텍스트위젯
textResult = ScrolledText(root, wrap=WORD, bg='#000000', fg='#ffffff', font=myFont) # bg='black' , fg='white'이랑 같음.
textResult.pack(fill=BOTH, expand=True)

# 10. 스크롤텍스트에 나올 메시지 Design
textResult.tag_configure('user', font=boldFont, foreground='yellow')
textResult.tag_configure('ai', font=myFont, foreground='limegreen') # 89F336
textResult.tag_configure('error', font=boldFont, foreground='red') 


# 9. 실행 후 입력창에 바로 포커스가 가도록
textMessage.focus_set()

# 11. 종료버튼(X)를 누르면 종료메시지 확인 후 종료
root.protocol('WM_DELETE_WINDOW', onClosing)

# 1. 종료시까지 계속 실행
root.mainloop()