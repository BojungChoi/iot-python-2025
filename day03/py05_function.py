# py05_function.py

# 함수, Fuction, Method, procedure....
# 인자, 파라미터, 매개변수 , Parameter, Argument...
# def 함수명(인자1 , 파라미터2, 매개변수3):
#    함수안으로 진입

def say_hi(): #괄호안에는 매개변수, (None)은 안적어도됨 , 돌려줄게 없는경우()
    print('안녕~ ') # 안녕~ 출력하고 끝내
    # return # return None 은 숨어있다. **돌려줄값이없으면 생략가능함.**

def say_hello(name):
    print(f'{name}아, 안녕!!')
    # return None

def get_age(birthYear):
    age = 2025 - birthYear
    return age

def closing():
    return '바이바이~'

print('인사하기:', end=' ')
say_hi() # 함수 호출(8번째줄) 출력이 끝나면 한줄내림(\n)
say_hi()

name = input('이름입력 > ')
print('이름으로 인사하기:', end='')
say_hello(name)

year = int(input('생일년도 > '))
real_age = get_age(year) #변수를 위로 던진게 아니라 함수를 던지기때문에 get_age로 올라간다.하단 변수year 와 상단변수birthYear가 다르다는걸 보여주기위해 다르게표현함
print(f'나이는: {real_age}세')

print('작별인사 : ',closing()) # 위로올라갔다가 내려가면서서 closing (함수) 는 '바이바이~'(21줄) 값이 들어감