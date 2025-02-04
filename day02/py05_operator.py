# py05_operator.py
# 연산자

# 사칙연산 : + - * /
a, b = 15, 14
# Shift + Del 는 한줄삭제 (효율적!)
print(a + b)
print(a - b)
print(a * b)

# 나누기 연산자는 /, //, % 
a = 14
b = 4
print(a / b) # 나눈 결과는 float(실수)
print(a // b) # 나눈 몫, int(정수)
print(a % b) # 나머지, int

# 거듭제곱(Power)
print(2 ** 5)

# 연산자 우선순위
## 계단식이 복잡해서 연산자 우선순위를 잘 모르겠으면 () 사용
print((3 + 4) * 7) # 49
print(3 + 4 * 7) # 31


## 리스트연산
## index = len(list) - 1
ListSample = [1,3,5,7,9]
print(ListSample[0])
print(len(ListSample)) # 리스트의 길이 5

print(ListSample[1])
print(ListSample[2])
print(ListSample[3])
print(ListSample[4])

#여기까지는 마지막이 9 였다가
ListSample[4] = 11
#여기서부터 5번째가 11이 됨.

print(ListSample[len(ListSample) -1]) # 마지막출력 리스트의길이 - 1 => index의 마지막을 구하라라는 뜻. 고로 상단에 마지막 인덱스를 11로 바꿔서 11의 값이나옴
# print(listsample[5])

## 문자열 연산 : + * 만 존재
greeting = 'Hello'
target = 'World'
print(greeting, target) #문자를 순차적으로 출력해줘 # 문자열 연산X

print(greeting + target) #문자를 합쳐서 출력해줘 # 문자열 연산  # string concatenate
print(greeting + ' ' + target)
print('{0}{1}'.format(greeting, target))
print(f'{greeting}{target}')

print(greeting * 5) # 해당문자열을 *수로 반복

## 문자열(Charactor Array) == List 와 유사하지만 값 수정 불가
print(greeting[1]) # 리스트 연산 
# greeting[0] = 'C' # --> List 와는 다르게 값을 집어넣어서 바꾸는건 안됨.py02_datastruct.py 참조
print(greeting)

## 리스트 연산, 슬라이싱
ListSample = ['2', '0', '2', '5', '-', '0', '2', '-', '0', '4'] #2025-02-04 출력
current = '2025-02-04' # 2025-02-04 출력

for i in ListSample:
    print(i, end='')
print()

print(current)
# 준비 끝

#인덱싱, 인덱스에 있는 값을 가져오기
print(ListSample[-1]) # 마지막부터 (9번째) , 끝에서부터는 0 부터가아닌 -1 부터 순서대로 (Python에서만가능)
print(current[9]) # 9번째 

# 슬라이싱, 리스트를 자르기
## [start:end] : end - 1 까지만 추출
print(ListSample[0:3]) #0부터 3인데 '2','0','2','5' 가 나와야 할것같지만 2,0,2 까지만 추출됨.
print(ListSample[0:3 + 1]) # '2','0','2','5' 까지 나오려면 + 1 을 해줘야함
print(current[0:3 + 1]) 

# 2025-02-04
year = current[0:3 + 1]
month = current[5:6 + 1]
day = current[8:] # end 끝까지는 숫자 생각
print(year, month, day)
print(current[-2:])

## 문자열 연산 중 함수를 사용
full_name = "Bo jung. Choi"
#자르기 split
print(full_name.split())
print(full_name.split(' ')) #공백을 잘라서 스플릿 해줘줘

names = full_name.split('.')# . 를 잘라서 스플릿 해줘줘
print(type(names))
print(names)

#바꾸기 replace
print(full_name.replace('Bo', 'BBBO'))

#공백 제거
origin = '     Hello  ~     ' 
print(f'{origin}')
print(f'/{origin.lstrip()}/') # lstrip(왼쪽공백없애줘)
print(f'//{origin.rstrip()}//') # rstrip(오른쪽공백없애줘)
print(f'///{origin.strip()}///') # rstrip 양쪽 공백은은 없앴으나, 문장 사이에 공백은 안없어짐!

# 문자 제거
# '',"" == Empty(비어있다)
# ' '," " == Space(공백이존재)
origin = 'TESTSTING'
print(origin.split('T')) # T 를 자르고 나눈다 -> 앞단어에 출력값에 공백이 존재(Empty)


# 단어찾기
full_name = "Bo jung. Choi"
print(full_name.find('j'))
print(full_name.find('y')) # 출력값 => -1 : 찾을 수 없다는 뜻

print(full_name.count('o')) # full_name 중에 o 가 문장에 몇번 존재하는지? (2번)
# print(full_name.index('H')) # 오류발생!

print(full_name.upper()) # 모든 단어를 대문자로
print(full_name.lower()) # 모든 단어를 소문자로로

