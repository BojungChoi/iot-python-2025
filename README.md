# iot-python-2025
IoT 개발자 기초프로그래밍 언어 리포지토리

## 1일차
- 개발환경 설정
    - 압축, 폰트, 개발용 에디터 설치
        - 반디집(교육용,회사에서 전부 무료)
        - 나눔 글꼴 (2DCoding) 추후 나눔고딕코딩 필요 https://hangeul.naver.com/font
        - NotePad++ https://notepad-plus-plus.org/downloads/
    - Visual studio coed 설치
        - 확장 Korean
        - Font Family D2Coding 추가, Mouse Wheel Zoom 체크 설정정

- 프로그래밍 언어 종류
    - 컴파일러(exe파일 생성)
        - C, C++, C#, java, ...
    - 인터프리터(소스코드를 바로 실행, 실행파일 없음)
        - Python, javascript, ...
    
- 파이썬(Python)
    - 1990대경에 개발한 인터프리터 언어
    - 네덜란드 개발자 귀도 반 로썸
    - 객체지향 프로그래밍 언어(Object Oriented Program)
    - 쉽게 학습할 수 있는 언어

- 파이썬 개발환경 Pyenv
    - 파이썬 버전을 손쉽게 변경할 수 있는 툴
    - 설치 전, 파워셀 관리자모드 오픈, 아래의 명령어 실행
        ```Shell
        > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
        ```
    - https://pyenv-win.github.io/pyenv-win/ Quick Start 1번 실행
    - pyenv로 파이썬 버전 설치 및 전역설정

- Visual studio Code
    - 확장에서 Python 설치
    - *.py 파일 생성 후 코딩
    - Ctrl + F5 로 실행

## 2일차
- 파이썬 기초
    - 변수
        - `데이터`를 담아서서 딴데서 쓰기위해 사용
    - 자료형
        - None, int, float, str, bool, list, tuple, dict, set, ...
        - type() 함수로 <class 'str'> 확인가능
    - 화면입출력 - 콘솔에서 입력하고 결과 출력
        - input(), print()
    - 문자열 포맷팅
        - 문자열을 좀 더 깔끔하게 표현
        - %s, %d, %f, .....
        - {0}, {1}, {2}.format() ...
        - f'{name}...{age}"
    - 연산자
        - 사칙연산 : +, -, *, /, //, %, **, (, )
        - 리스트연산 : list[0], list[0:3 + 1]
        - 문자열연산 : split(), replace(), strip, find, ...


- 깃허브[데스크톱]
    1. **fetch orign** : 리모트 최신변경사항 확인(중요!)
    2. pull : 리모트에 변경사항을 내 로컬로 다운로드
    3. Commit : 로컬, 리모트에 변경사항을 확정
    4. push : 로컬에 변경사항을 리모트로 올리기
   
    
## 3일차
- 파이썬 기초
    - 흐름제어
    - 파일입출력
    - 함수
    - 객체지향
    - 모듈, 패키지
    - 예외처리
    - 디버깅
