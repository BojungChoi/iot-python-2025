# iot-developer
IoT 개발자과정

## 개발환경 설치

### Visual Studio 2022 Community

세계에서 가장 강력한 디버깅을 할 수 있는 개발툴

- https://visualstudio.microsoft.com/ko/vs/community/

    1. 다운로드를 클릭하면 VisualStudioSetup.exe 자동 다운로드
    2. VisalStudio Installer 시작
        - https://learn.microsoft.com/ko-kr/visualstudio/install/install-visual-studio?view=vs-2022
        참조
        - 경로 변경
        - **ASP.NET 웹 개발**, **.NET 데스크톱 개발**, **C++ 를 사용한 데스크톱 개발 선택**
        - 설치 시작
        - 설치완료 후 Visual Studio Install 종료
        - Visual Studio 2022 실행
        - 테마 결정
        - MS 또는 Github 계정으로 로그인
    

### Docker
- 가상머신. 리눅스에서 응용 프로그램을 컨테이너(이미지) 형태로 실행하고 관리하는 오픈소스 프로젝트
    - VM(virtual Machine), Virtual-Box, VMware 부터 발전되어서 도커로 진화
    - 도커가 진화해서 쿠버네티스
    - 서버를 가상으로 운영하고 개발이후 운영환경을 체계적으로 관리하기위해서 생성

- https://www.docker.com/
    1. 사이트에서 Docker Personal 선택
    2. Docker Desktop AMD64 클릭 다운로드
    3. 설치 재부팅 후 아래의 메시지가 출력되면,

        <img src='./image/py010.png' width='600'>
    
    4. powershell에서 아래 명령어 실행

        ```shell
        > wsl --update
        ```