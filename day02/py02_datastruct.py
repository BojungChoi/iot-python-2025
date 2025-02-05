# py02_datastruct.py
# 복합자료형
# 자료구조 및 알고리즘

# 리스트 사용이전 (변수가 계속많이나오니까..)
a = 1
b = 2
c = 3
d = 4
e = 5

sum = a + b + c + d + e
print(sum)

# 리스트(배열) 사용(간단하게) [] - 다른언어에선 리스트와 배열은 다른것, Python 에선 같다.
f = [1, 2, 3, 4, 5]
print(f)
print(type(f))

f = ['Life','is', True, 0, None,[1,2,3]]
print(f)
print(f[0]) # 첫번째 인덱스 값을 꺼낸다.
# 리스트의 한 요소에도 값을 집어넣을 수 있음
f[3] = 100 # f 라는 리스트에 4번째 (0) 값을 100으로 바꿔줘
print(f) #f 전체 출력

## 튜플 ()
# 리스트와 거의 흡사. 값을 변경할 수 없음!!
t = (1, 2, 3, 4)
print(t)
print(t[3])
# t[0] = 5 # 튜플은 값변경이 안됨 error
print(type(t))

##  딕셔러니(사전형){Key : value} 의 집합
Spiderman = { 'name' : 'perter parker', 'age': 20, 'Weapon': 'Web Shooter'}
print(Spiderman)
print(type(Spiderman))

print(Spiderman['name'])
Spiderman['age'] = 21
print(Spiderman)

## 집합(),{},[] 다 사용. 리스트처럼 인덱스가 없음.
s = set([1,3,5,7,9,5]) #마지막 5가 나오지않는다. 수학의 집합과 동일. 중복 제거
print(s)
print(type(s))

s = set('Hello world') # 중복 제거 후 표현 공백까지 포함해서 8자리
print(s)

## 변수명 지정 방식
## 의미있는 단어들의 조합으로 만들것
phoneNumber = '010-2758-0000'
salaryBankAcconut = '110-358-328533'

samsung = ''
samsung1 = ''
# 1samsung = '' # 숫자로 변수명 시작불가
_samsung = ''
samsung_ = '' 
# samsung! = '' # _이외의 특수문자는 사용불가
# samsung* = ''
# samsung-apple = '' # 파이썬 연산자는 사용불가