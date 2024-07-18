# Django_Insta_Crawling_API
* **개발 인원**: 2명

* **개발 환경**: Visual Studio Code, Python, Django, vue.js

* **개발 기간**: 2024.01 ~ 2024.02 (인턴쉽 2개월)

* **지원 플랫폼**: PC

* **프로젝트 개요**: 학교에서 2개월간 진행하는 인턴쉽 프로그램에서 웹개발 스타트업 회사에 합격하여 진행한 프로젝트. <br>vue.js와 django를 연동하여 인스타그램 인플루언서 정보 분석 웹페이지를 구현.

* **핵심 기능**
   - **Python 코드로 크롤링 기능 구현**
   <br>Python의 selenium 라이브러리를 이용하여 인스타그램 인플루언서의 정보를 크롤링하는 기능을 구현함.
   - **Django Rest Framework를 이용한 RESTful API 서버 구현**
   <br>Python의 Django 프레임워크를 이용하여 크롤링 데이터를 저장하고 웹페이지에 데이터를 보내줄 서버를 구현함.
   - **vue.js와 Django를 연동하여 인스타그램 인플루언서 정보 분석 웹페이지를 구현**
   <br>사용자가 보기 쉽도록 크롤링 데이터를 분석하여 정리한 데이터를 웹페이지에 보여주도록 구현함.


## 가상환경
### 가상환경 생성
```
python -m venv [가상환경 이름]
```

### 가상환경 실행
```
[가상환경 이름]/scripts/activate
```

### 가상환경 비활성화
```
deactivate
```

## 프로젝트 세팅 (가상환경 내부에 설치)
### Django 설치
```
pip install Django
```

### 패키지 설치
```
pip install djangorestframework
```

### Django 프로젝트 생성
```
django-admin startproject [프로젝트 이름] .
```

### Django 앱 생성
```
python manage.py startapp [앱이름]
```

## 서버 실행 (marge.py가 있는 디렉토리에서 작업)
### 모델 변경사항 감지 및 기록
```
python manage.py makemigrations
```

### 변경사항을 DB에 적용
```
python manage.py migrate
```

### 서버 실행
```
python manage.py runserver
```

## 패키지
### 설치한 패키지를 한번에 받기
```
pip install -r requirements.txt
```
