# pt06_exeception.py

# 예외처리
## 오류, Error, fault,
## 1. Error(문법적 오류) - 코딩하다가 빨간색 밑중생기는 거
##    오류표시가 안나는 코딩을 잘못한 오류 포함(!) mul(7, 6) -> 42예상. 결과13
## 2. Exception(실행중 발생 예외) - 문법오류 수정 후 실행하다가 비정상 종료되는 거
## 파이썬은 Error도 **Error고 Exception도 **Error
## 에디터 상에 오류표시가 나면 Error
## 실행중에 발생시 Exception
numbers = list(range(1, 11))
for i in numbers:
    # print(i)
    pass

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print('계산 시작')
while True:
    op = input('계산할 연산을 입력(*, /, q)')
    if op == 'q' : # 종료조건
        break
    elif op == '*': # 곱하기
        x, y = input('곱합 수 입력 > ').split()
        x = int(x)
        y = int(y)
        print(f'{x} x {y} 는 = {mul(x, y)} 입니다.')
    elif op == '/': # 나누기
        x, y = input('나눌 수 입력 > ').split()
        x = int(x)
        y = int(y)
        print(f'{x} % {y} 는 = {x / y} 입니다.')
    else:
        print('정확한 입력 요망')

print('프로그램 종료!')