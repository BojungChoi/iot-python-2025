# py02_car.py

# 객체지향 다시
class Car:
    ## __new__ 사용빈도 낮음 , __init__ 많이 사용
    ## Car() 호출하면 아래의 메서드가 실행
    ## company, name, plateNum 모를때는 None(뭔지몰라)
    def __init__(self, company=None, name=None, plateNum=None ):
        self.__company = company # self.멤버변수 이름앞에 __ 를쓰면 외부접근 불가 (24번줄 참조)
        self.__name = name
        self.__plateNum = plateNum
        print('Car 클래스를 새로 생성!')

    # 클래스 자체가 출력되는데, __str__ 문자열로 출력되도록 바꿔줌.
    def __str__(self):
        return f'제 차는 {self.__name} 이고, 차 번호는 {self.__plateNum} 입니다.'
    
    # 외부에서 잘못된 차번호를 넣으면 안들어감
    def setPlateNum(self, newplateNum):
        if type(newplateNum) is str:
            self.__plateNum = newplateNum 

    def setName(self, newName='글쎄요'): # 이름을 모를때 글쎄요로 대체.
        self.__name = newName

    def getName(self):
        return self.__name

# 모듈화 하려면 예제소스는 주석처리

# myCar = Car('현대', '산타페', '65머4960') # 순서대로 써야하나,
# 파라미터명 = 값 으로 매개변수 순서를 변경가능.
# myCar = Car(name='산타페', plateNum='65머4960', company='현대') # 이렇게하면 변수 순서상관없이 적용
# print(myCar) # 차의 번호를 출력하고 싶음

# myCar.__plateNum = 2018  # 클래스 외부에서 잘몬된 데이터를 넣어도 문제가 발생X (실수를 미연에 방지)
# print(myCar)

# myCar.setPlateNum('115우3089')
# print(myCar)

# yourCar = Car()
# print(yourCar)
# yourCar.setPlateNum('222노2222')
# print(yourCar)
# yourCar.setName('제네시스')
# print(yourCar)
