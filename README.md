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
pip install -r requirements.txt #안되면 pip3로
code .
python3 run.py
```

### 2.2 docker로 열기
```terminal
docker build . -t docker-image
docker run --name docker-container -d -p 5000:5000 docker-image
localhost:5000로 접속
```
### mysql database 구성
mysql 설치 후 
```terminal
mysql.server start #sql 서버 시작
or
mysql -uroot -p
['mysql 설치시 설정한 root pw입력'] #root로 mysql 로그인
mysql> connect #mysql에서 connect
```
```terminal
1.
mysql -uroot -p
['mysql 설치시 설정한 root pw입력'] #root로 mysql 로그인
2.
mysql> create database mydb;
3.
mysql> use mydb;
4.
mysql> exit;
5.
mysql -uroot -p mydb<['다운받은 mydb.sql파일의 위치'] #ex)/users/krc/downloads/mydb.sql
6.
mysql -uroot -p
mysql> show database;
mysql> use mydb;
```
local에서 실행 시 app.py의 14줄
```terminal
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:['자신의 local sqlserver root 비밀번호']@localhost:3306/mydb"
```
로 수정해서 실행

1. 원하는 곳에 git clone
```zsh
git clone https://yeardream-gitlab.elice.io/yeardream-project/project-9/service.git
```

2. 클론된 폴더로 이동 & sprint 브랜치로 변경
```zsh
cd service
git checkout sprint
(안되면) git chechout -t origin/sprint
```

3. terminal에서 바로 vsc열기
[설정하면 터미널에서 바로 vsc이동가능](https://velog.io/@hwang-eunji/vscode-code-%EB%AA%85%EB%A0%B9%EC%9C%BC%EB%A1%9C-vscode-%EC%97%B4%EA%B8%B0)
뒤에 점 꼭 찍어야함
```
code .
```
