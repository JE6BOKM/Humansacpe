# 휴먼스케이프

- 과제 출제 기업 정보
  - 기업명 : 휴먼스케이프
  - [휴먼스케이프](https://humanscape.io/kr/index.html)
  - [wanted 채용공고 링크](https://www.wanted.co.kr/wd/41413)
  - 과제 수행 기간(2021.11.15 ~ 2021.11.17)

## 💁‍♀️ Members

| 이름   | github                                    | 담당 기능    |
| ------ | ----------------------------------------- | ------------ |
| 신재민 | [shinjam](https://github.com/shinjam)     | 테스트 코드  |
| 신우주 | [shinwooju](https://github.com/shinwooju) | 상품 CRUD    |
| 최혜림 | [rimi0108](https://github.com/rimi0108)   | 로그인       |
| 강성묵 | [miranaky](https://github.com/miranaky)   | 임상정보수집 |
| 김민규 | [SkyStar-K](https://github.com/SkyStar-K) | 상품 CRUD    |

## ⭐ 과제 내용

### [필수 포함 사항]

- READ.ME 작성
  - 프로젝트 빌드, 자세한 실행 방법 명시
  - 구현 방법과 이유에 대한 간략한 설명
  - 완료된 시스템이 배포된 서버의 주소
  - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

### [확인 사항]

- **ORM 사용 필수**
- **데이터베이스는 SQLite로 구현**
- **secret key, api key 등을 레포지토리에 올리지 않도록 유의**
  - README.md 에 관련 설명 명시 필요

### [도전 과제]

- 배포하여 웹에서 사용 할 수 있도록 제공
- 임상정보 검색 API 제공

### [과제 안내]

다음 사항들을 충족하는 서비스를 구현해주세요.

- 임상정보를 수집하는 batch task
  - 참고: [공공데이터](https://www.data.go.kr/data/3074271/fileData.do#/API%20%EB%AA%A9%EB%A1%9D/GETuddi%3Acfc19dda-6f75-4c57-86a8-bb9c8b103887)
- 수집한 임상정보에 대한 API
  - 특정 임상정보 읽기(키 값은 자유)
- 수집한 임상정보 리스트 API
  - 최근 일주일내에 업데이트(변경사항이 있는) 된 임상정보 리스트
    - pagination 기능
- **Test 구현시 가산점이 있습니다.**

## 사용 기술 및 tools

> - Back-End : <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/mysql 8.0-1b9e41?style=for-the-badge&logo=Mysql&logoColor=white"/>
> - Deploy : <img src="https://img.shields.io/badge/AWS_EC2-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC : <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

## 🏄‍♀️ 모델링

![스크린샷 2021-11-16 오후 1 00 17](https://user-images.githubusercontent.com/5153352/141899305-f6638fbc-0319-477c-ba30-818363133291.png)

## API

[링크-postman document](https://documenter.getpostman.com/view/16042359/UVBzmpLX)

## 구현 기능

### 임상정보를 수집하는 batch task

[질병관리청\_임상연구 과제정보](https://www.data.go.kr/tcs/dss/selectFileDataDetailView.do?publicDataPk=3074271) 에서 제공하는 데이터를 수집합니다.

- 공공데이터API에서 임상연구 과제정보를 받아옵니다.
  - 새로운 데이터가 발견되면 저장합니다.
  - 기존 데이터가 변경되면 업데이트 합니다.
- 주기적으로 데이터를 받아옵니다.
  - [django-crontab](https://github.com/kraiz/django-crontab)을 활용하여 주기적으로 데이터를 확인합니다.(매주 일요일 0시15분,12시15분)
  - 확인 시 데이터가 변경되면 그에 맞게 생성/업데이트 합니다.

### 수집한 임상정보에 대한 API

- 공공데이터API에서 DB로 받아온 데이터를 불러옵니다.
- pk값 : project_number (과제번호)를 pathParameter로 받아와서 데이터를 불러옵니다.

### 수집한 임상정보 리스트 API

### 수집한 임상정보 리스트 API

### 임상정보 검색 API 제공
- query parameter로 'trail_name'을 받아 과제명을 검색하면 필터링해줍니다.
- 검색결과 값이없다면 전체 리스트를 불러옵니다.

## API TEST 방법

...

## 설치 및 실행 방법

### Local 개발 및 테스트용

```bash
git clone https://github.com/JE6BOKM/Humanscape.git && cd Humanscape
poetry install
#원하는 secret key 넣어서 사용.
export DJANGO_SECRET_KEY=a4+-6ld_4l2-fig_6j4ecr8xtxkf6y@9p%569ejaid**0
#data.go.kr 에서 받은 secretKey사용
export DATA_SECRET_KEY={your_secretKey}
poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
poetry run python manage.py api
poetry run python manage.py runserver
```

### 배포용

...

## 폴더 구조

# Reference

이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 휴먼스케이프에서 출제한 과제를 기반으로 만들었습니다.
