# py03_while_statement.py

# while 반복문 : for문으로 변경 가능
# while (조건이 참인동안):
#   구문안에서 반복

# 1 ~ 10까지의 수를 합산
sum = 0
i = 0

while i <= 10:
    sum += i  # sum = sum + i
    i += 1    # i = i + 1 같은 의미, i++
    # print(f'합은 {sum}') # print 문이 while문 안에있냐, 밖에있냐를 잘봐야함. 이때는 순차적으로 합이나옴.
print(f'합은 {sum}') # 이때는 55


sum = 0
for j in range(1, 10 + 1):   # 위에 while문과 같은 뜻, for 문으로 변경할때의 예
    sum += j

print(f'합은 {sum}')
