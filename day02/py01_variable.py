# 변수와 자료형
# 변수는 => 변하는 수(Variable) <-> 상수 (Constant)
# 상수 예 Pi = 3.14159265727...... 

# 변수
a = None # 특수형, None타입
print(a) # a라는 변수에 무슨 값이 들어있는지 콘솔에 출력해줘
print(type(a))


a = 10      # 정수(소수점없는 수), integer
print(a) # 함수는 늘 괄호를 같이 사용
print(type(a))


a = 12.34   # 실수(소수점 있는 수), Float
print(a)
print(type(a))


a = 0b11111110  # 0과 1로 수를 표현(2진수), Binary
print(a)
print(type(a))


a = 0xFE    # 0~9,A~F(10~15)로 수를 표현하는 방식 (16진수), Hex
print(a)
print(type(a))

a = 1_000_000_000   # 천단위마다 쉼표와 같이 표현(팁)
print(a)
print(type(a))

a = "Life is short, You need Python"    # 문자열, String
print(a)
print(type(a))

a = 'life is short, You need Python'    # 문자열 ''  "" 상관없음
print(a)
print(type(a))

a = (3 > 1) # 불형 True | False, Boolean
print(a)
print(type(a))

