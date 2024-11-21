# MyTodo 프로젝트
이 프로젝트는 백엔드를 위한 Django REST Framework with 파이썬에 실린 Todo 목록 API 만들기 프로젝트를 기반으로 진행한 프로젝트입니다.   
할 일 목록과 각 목록에 대한 상세 내용을 조회하고, 할 일 생성하고, 수정하는 API를 구현하였습니다.   
추가적으로 개발 과정에서 테스트하는 코드를 적용해보면서 TDD에 대한 감을 키울 수 있는 프로젝트였습니다.

## 기간
2024.11.14 ~ 2024.11.16

## 주요 기능
1. Todo 목록 API 서비스 구현   
   - Todo 목록 및 상세 조회 기능
   - 새로운 Todo 생성 및 수정 기능
   - Todo 완료 기능
2. Test 코드 구현   
   - 각 API 기능에 대한 테스트 코드 작성
3. Docker 기반 개발 환경 구성
   - Docker Compose를 이용해 일관된 개발 환경 구성

## 기술 스택
    - 백엔드: Django REST Framework
    - 데이터베이스: Django ORM (SQLite3)
    - 컨테이너: Docker

## 설정 및 실행
1. 저장소 클론   
    ``` bash
    git clone https://github.com/rlozl15/mytodo.git
    cd pylog
      ```
2. Docker 환경 준비   
    - Docker Desktop을 실행합니다.
3. Docker 이미지 빌드 및 실행
    ```
    docker-compose up -d --build
    ```
4. Django 마이크레이션
    ```
    docker-compose exec app python manage.py migrate
    ```
5. Django API 문서 확인
    - Swagger 또는 API 문서를 확인할 수 있습니다:
        - Swagger: http://localhost:8000/swagger/
        - API Docs: http://localhost:8000/docs/
