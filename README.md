
### sprint로 branch 변경 & 필요한 거 설치 & vsc로 열기
```terminal
git checkout sprint
pip install -r requirements.txt
code .
```

### docker로 열기
```terminal
docker build . -t docker-image
docker run --name docker-container -d -p 5000:5000 docker-image
localhost:5000로 접속
```