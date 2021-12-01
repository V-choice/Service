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

<details>
<summary>/join</summary>

| method | description | parameters |
|--------|-------------|------------|
| post | 회원의 회원가입 | <span dir="">'user_id', 'user_pw'</span> |

</details>
<details>
<summary>/login</summary>

| method | description | parameters |
|--------|-------------|------------|
| post | 회원의 로그인    | <span dir="">'user_id', 'user_pw'</span> |

</details>
<details>
<summary>/first_choice</summary>

| method | description | parameters |
|--------|-------------|------------|
| post | 첫번째 yes or no의 회원정보 | 'first_choice', 'user' |

</details>
<details>
<summary>/second_choice</summary>

| method | description | parameters |
|--------|-------------|------------|
| post | 두번째 yes or no의 회원정보 | 'second_choice', 'user' |

</details>
<details>
<summary>/post</summary>

| method | description | parameters |
|--------|-------------|------------|
| post | 게시판의 글 업로드 | 'content', 'author' |
| delete | 게시판의 글 삭제 | 'id', 'author' |
| patch | 게시판의 글 수정 | 'id', 'content' |

</details>
<details>
<summary>/like</summary>

| method | description | parameters |
|--------|-------------|------------|
| patch | 게시판의 좋아요 | 'id' |

</details>
<details>
<summary>/vid-cnt</summary>

| method | description | parameters |
|--------|-------------|------------|
| post | 카테고리 별 영상 수 변화 | 'category_id' |

</details>
<details>
<summary>

<span dir="">/comp-mean-views</span>

</summary>

| method | description | parameters |
|--------|-------------|------------|
| post | 평균 조회수 비교 | 'category_id' |

</details>
<details>
<summary>/ratio-ch-vid</summary>

| method | description | parameters |
|--------|-------------|------------|
| post | 코로나 전후 영상들의 카테고리 \
순위 및 비율 변화 | 'label_num' |

</details>
<details>
<summary>

<span dir="">/multi-analysis</span>

</summary>

| method | description | parameters |
|--------|-------------|------------|
| post | 멀티 분석 | 'selection_1_num', 'selection_2_num', 'category_id' |

</details>
<details>
<summary>

<span dir="">/corona-related-multi-analysis</span>

</summary>

| method | description | parameters |
|--------|-------------|------------|
| post | 코로나 영상 추출 후  \
멀티분석기능 | 'selection_1_num', 'selection_2_num' |

</details>
<details>
<summary>

<span dir="">/correlation-bokeh</span>

</summary>

| method | description | parameters |
|--------|-------------|------------|
| post | bokeh 상관관계 그래프 | 'category_id' |

</details>
<details>
<summary>

<span dir="">/sentiment-analysis</span>

</summary>

| method | description | parameters |
|--------|-------------|------------|
| post | 감정분석 결과 그래프 | 'user_want' |

</details>
