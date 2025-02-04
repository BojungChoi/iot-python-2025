# py04_stringfomat.py
# 문자열 포맷팅

loginTemp = '안녕하세요, %s님!'
# name = '보정'

# print(loginTemp % (name))
# name = input('로그인할 이름 입력 > ')
# print(loginTemp % (name))

## 구세대 문자열 포맷팅
intro = '나는 %s(이)고, %d살입니다. 몸무게 %fKg 입니다.'
print(intro % ('보정', 31, 79.5))

intro = '나는 %10s (이)고, %06d살입니다. 몸무게 %0.1fKg 입니다.'
print(intro % ('보정', 31, 79.5))

## 중간세대 문자열 포맷팅
## {0:>10s} 로 %10s와 동일하게 적용
intro = '나는 {0}(이)고, {1}살입니다. 몸무게 {2}Kg 입니다.'
print(intro.format('뽀룡', 8 , 8.1))

## 신세대 문자열 포맷팅
name = '보덩'
age = 30
weight = 77.7
print(f'나는 {name:>10s}(이)고, {age}살입니다. 몸무게 {weight}Kg입니다.') #f를 씀으로써, 더 간단하게 씀 (format)
# {name:>10s} 은 공백을 10칸띄움 