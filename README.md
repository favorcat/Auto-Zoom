# Zoom 자동 실행

### Install
- [Chromedriver 설치](https://chromedriver.chromium.org/downloads)    
- 파이썬 설치 (MacOS)
```
brew install python3
```
- selenium 설치
```
pip3 install selenium
```

### 처리 가능한 경우
- e-강의동의 실시간 강의 메뉴를 통해 들어오는 경우
- Zoom ID를 통해 들어오는 경우

### 스케쥴러 설정 방법
- MacOS - [crontab](https://blog.favorcat.dev/11)
- Windows - 작업 스케쥴러

### 갑자기 실행이 되지 않을 때
버전이 맞지 않아 실행이 되지 않을 수 있으니,    
chrome 버전 확인 후, chromedriver 재설치하면 해결 가능

### 참고
[Zoom URL Schemes](https://medium.com/zoom-developer-blog/zoom-url-schemes-748b95fd9205)