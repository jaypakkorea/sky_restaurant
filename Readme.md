# Readme



### Getting Started

* `python -m venv venv`
* `source venv/Scripts/activate`
* `python manage.py runserver`





### 폴더 구조

전체 프로젝트 폴더 : **BUK2on_on**

맛집 추천 app : **recommends**

계정 app : **accounts**

CSS, JS, 프로필 및 고정 이미지 저장 폴더 : **static**

맛집 사진, 프로필 사진 저장 폴더 : **media**





### API

| HTTP verb | URL                                        | 설명             |
| --------- | ------------------------------------------ | ---------------- |
| GET       | localhost/buk2on_on/                       | 대문페이지       |
| GET       | localhost/buk2on_on/seoul/                 | 서울 지역 조회   |
| GET       | localhost/buk2on_on/busan/                 | 부산지역 조회    |
| GET       | localhost/buk2on_on/etc/                   | 기타 지역 조회   |
| POST      | localhost/buk2on_on/create/                | 맛집 추천        |
| GET       | localhost/buk2on_on/`<int:restaurant_pk>`/ | 맛집 상세 페이지 |





### Reference

superuser id : superuser

superuser pw : 1부터 연속된 증가 숫자 4개