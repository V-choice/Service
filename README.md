
 ### API 명세서

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
