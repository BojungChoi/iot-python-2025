# py01_listop.py

# 리스트연산
# 리스트가 for, while 반복문에서 가장 많이 활용되는 구조
# interabel -> 반복할 수 있는 요소가 for, while문에 사용
listSample = [1,2,3,4,5,6,7,8,9,10] # 반복

sum = 0
for i in listSample:
    sum = sum + i # sum += i

print(f'합산결과 = {sum}')

# 리스트 연산
arr = [1,2,3,4,5]
arr2 = [2,4,6,8,10]
print(arr)
print(arr[4])
print(arr[0]+arr[2])
print(arr[-2])
print(arr[2:])

print(arr + arr2)
print(arr * 2)

## 리스트 길이
print(len(arr))

arr[2] = 9 # 데이터 할당
print(arr)

## 리스트 요소 삭제
arr[2] = None
print(len(arr), (arr))

del(arr[2])
print(len(arr), (arr))

## 리스트 요소 추가
arr.append(7) # 출력 끝에 추가
print(arr)

arr.insert(2, 100) # 지정된 자리에 값을 추가
print(arr)

# ## 리스트를 합칠 때
# arr.append(arr2)
# print(arr)

# arr.extend(arr2)
# print(arr)


## 리스트 정렬(쇼핑몰 낮은가격순, 높은가격순, 최신일자부터...)
arr = [6, 7, 1, 3, 9, 0, 2, 8, ]
print(arr)
arr.sort() # 오름차순 정렬
print(arr)
arr.sort(reverse=True) # 내림차순 정렬
print(arr)

## 요소의 위치파악
print(arr.index(6)) # 없는 데이터를 인덱스하면 오류발생

## 요소 꺼내기
print(arr.pop()) # 마지막 요소를 꺼냄
print(arr)

## 리스트컴프리핸션. 대량의 리스트를 쉽게 생성하는 방법!!
arr = [i for i in range(1, 100 + 1)] # 1 부터 100까지
print(arr)

sum = 0
for i in arr:
    sum = sum + i