Claude Code/ 확인 김정협

# week09/tools.py 함수 정리

## 개요

- KOBIS(영화진흥위원회) 일별 박스오피스 API를 호출하는 도구 모음임
- 함수 2개와 모듈 상수 1개로 구성됨

## 모듈 상수 및 의존성

- `BASE_URL`: 일별 박스오피스 조회 API 주소(`searchDailyBoxOfficeList.json`)이며 두 함수가 공유함
- `requests`: HTTP 요청에 사용함
- `secret.API_KEY`: API 인증 키이며 `secret.py`에서 import함 (키 값은 문서에 기재하지 않음)

## 함수 목록

### 1. `get_boxoffice_rank_1(date)`

- 기능: 해당 날짜의 박스오피스 1위 영화 제목 조회
- 입력: `date` (문자열) - 8자리 날짜. 예: `"20260824"`
- 반환: (문자열) 1위 영화 제목. 예: `"오디세이"`
- 동작: `dailyBoxOfficeList`의 첫 번째 항목에서 `movieNm`을 반환함

### 2. `get_movie_audience(date, title)`

- 기능: 일별 박스오피스에서 영화 제목에 해당하는 관객 수 조회
- 입력
  - `date` (문자열) - 8자리 조회 날짜
  - `title` (문자열) - 검색할 영화 제목
- 반환: 천 단위 쉼표와 '명'을 붙인 문자열. 예: `"186,587명"`
- 동작: 목록을 순회하며 `movieNm`이 `title`과 일치하면 `audiCnt`를 정수로 변환해 반환함
- 미발견 시: `'{title}' 은(는) {date} 순위에 없습니다.` 안내 문자열 반환

## 특이사항

- 두 함수 모두 `requests.get`을 timeout 10초로 호출함
- HTTP 오류, 응답 구조 이상(키 누락 등)에 대한 예외 처리가 없음
- 제목 비교는 완전 일치 방식임 (부분 일치 불가)
- 두 함수가 같은 API를 각각 호출하므로 동일 날짜 반복 조회 시 중복 요청이 발생함
