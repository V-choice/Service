

# 유튜브로 바라본 v-choice

바이러스가 바꿔놓은 우리의 유튜브 초이스

## 프로젝트 구성 안내

- 코로나 상황 관련 변수(일일확진자, 누적확진자, 일자별 확진자 등)와 유튜브 데이터(조회수, 카테고리, 제목, 좋아요 수/싫어요 수 등)와의 관계 시각화
  -  다른 변수가 아닌 코로나 상황과의 상관 관계 검증
- 사용자의 데이터 선택에 대한 인터렉티브 시각화(워드클라우드, matplotlib, seaborn, bokeh)
- 인사이트를 공유하고 피드백을 남길 수 있는 댓글창

## 1. 프로젝트 소개
  
- 사용 데이터
    1. 코로나 이후(20-21년도) 유튜브 데이터 : kaggle [YouTube Trending Video Dataset (updated daily)](https://www.kaggle.com/rsrishav/youtube-trending-video-dataset)
    2. 코로나 이전(17-19년도) 유튜브 데이터 : kaggle [Trending YouTube Video Statistics](https://www.kaggle.com/datasnaek/youtube-new)
    3. 코로나 관련 데이터 : 공공포털사이트(20년도부터 최근까지)
  </br>
- 스택
  - 백엔드 스택 : 
  <img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/Mysql-E6B91E?style=flat-square&logo=MySql&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/Flask-29B5E8?style=flat-square&logo=Flask&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/aws-333664?style=flat-square&logo=amazon-aws&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=Ubuntu&logoColor=white"/></a>
  - 프론트엔드 스택 :
  <img src="https://img.shields.io/badge/Jinja-B41717?style=flat-square&logo=Jinja&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/JQuery-0769AD?style=flat-square&logo=JQuery&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=white"/></a>
  - 라이브러리 : 
  <img src="https://img.shields.io/badge/Pandas-FF6600?style=flat-square&logo=Pandas&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/Numpy-013243?style=flat-square&logo=Numpy&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/matplotlib-125345?style=flat-square&logo=matplotlib&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/seaborn-00CCBB?style=flat-square&logo=seaborn&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/sweetalert2-FEC111?style=flat-square&logo=sweetalert2&logoColor=white"/></a>



## 2. 프로젝트 목표

코로나19 이후 OTT(온라인동영상서비스)는 1100% 이상의 성장세를 보였다. \
OTT 중에서도 유튜브는 66배의 폭발적인 성장과 국내 동영상 플랫폼 1위를 유지하고 있다. \
이러한 유튜브에서 데이터를 수집하고, 사람들은 팬데믹 시기를 어떻게 보내고 있는가를 키워드로 분석하려 한다.

## 3. 프로젝트 팀원 역할 분담

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/surdarla">
        <img src="https://github.com/V-choice/Service/blob/main/static/image/junsu.jpeg?raw=true" height="100px;" alt=""/><br />
          <sub><b>김준수 | 팀장</b></sub>
              </a><br />
    <td align="center">
      <a href="https://github.com/">
        <img src="https://github.com/V-choice/Service/blob/main/static/image/Dongsung.jpeg?raw=true" height="100px;" alt=""/><br />
          <sub><b>고동성</b></sub>
              </a><br />
    <td align="center">
      <a href="https://github.com/">
        <img src="https://github.com/V-choice/Service/blob/main/static/image/juyeon.jpeg?raw=true" height="100px;" alt=""/><br />
          <sub><b>고주연</b></sub>
              </a><br />
    <td align="center">
      <a href="https://github.com/">
        <img src="https://github.com/V-choice/Service/blob/main/static/image/Banghyun.jpeg?raw=true" height="100px;" alt=""/><br />
          <sub><b>김방현</b></sub>
              </a><br />
    <td align="center">
      <a href="https://github.com/LearninMC">
        <img src="https://github.com/V-choice/Service/blob/main/static/image/Sungkyu.jpeg?raw=true" height="100px;" alt=""/><br />
          <sub><b>김성규</b></sub>
              </a><br />
    <td align="center">
      <a href="https://github.com/">
        <img src="https://github.com/V-choice/Service/blob/main/static/image/Chunghyun.jpeg?raw=true" height="100px;" alt=""/><br />
          <sub><b>최청현</b></sub>
              </a><br />
  <tr>
</table>

## 4. how to start
    
    
    

## 5. API 명세서

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

## 5. 버전

- 1.0.0

### 참조

- [Top Trending Videos on YouTube in 2021](https://russelllim22.medium.com/d576fa1f4c34)
- [한국어 감성사전](https://github.com/park1200656/KnuSentiLex/find/c95a8a9bcb78ef92e3f8ddd277abaf31451d9f23)


