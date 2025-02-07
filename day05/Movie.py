# Movie.py - Movie이름의 모듈
class Movie:
    def __init__(self, title, year, company, rate):
        self.__title = title
        self.__year = year
        self.__company = company
        self.__rate = rate

    def __str__(self): # 문자열 포멧팅
        str_res = (f'제목: {self.__title} ({self.__year})\n'
                    f'제작사: {self.__company}\n'
                    f'평점: {self.__rate}')
        return str_res
    
    # 찾는 이름이 포함되어있으면, True : 검색할때 사용
    def isNameContain(self, name):
        if name in self.__title: # name = '어벤져스', __title = '어벤져스 : 인피니티워' | '어벤져스 : 엔드게임'  -> 어벤져스 검색 시 종류가많을 때
            return True
        else:
            return False
        
    # 찾는 이름이 완벽하게 일치하면 True : 삭제할때 사용용
    def isNameExist(self, title):
        if self.__title == title:
            return True
        else:
            return False
        
    # 변수값 가져오기 getter 함수
    def getTitle(self):
        return self.__title # __  외부에서 접근불가!!

    def getYear(self):
        return self.__year

    def getCompany(self):
        return self.__company

    def getRate(self):
        return self.__rate
    
