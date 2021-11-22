### docker desktop app 설치
```
brew install --cask install docker
```

### 가상환경 만들기
```
virtualenv venv
source venv/bin/activate
```


### 1. sprint로 branch 변경 & 필요한 거 설치 & vsc로 열기
```terminal
git checkout sprint
pip install -r requirements.txt #안되며 pip3로
code .
pytho3 run.py
```

### 2.2 docker로 열기
```terminal
docker build . -t docker-image
docker run --name docker-container -d -p 5000:5000 docker-image
localhost:5000로 접속
```
