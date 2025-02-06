# py03_module.py

# 모듈 - 레고
# 모듈사용 하려면
# inport 모듈명
# from 모듈명 import 상세...
import py02_car

hisCar = py02_car.Car('기아차', 'K8', '11어1111')
print(hisCar)

import py02_car as c

herCar = c.Car('페라리', 'GT911','11오1109')
print(herCar)

from py02_car import Car

thatCar = Car('람보르기니','이름몰라','55로1004')
