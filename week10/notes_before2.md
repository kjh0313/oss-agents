# week09/tools.py 분석 노트 (notes_before2)

`tools.py`는 KOBIS(영화진흥위원회) 오픈 API의 **일별 박스오피스** 데이터를 조회하는 함수 2개를 담은 모듈입니다.

## 구성 요소

| 항목 | 내용 |
| --- | --- |
| 의존성 | `requests`, `secret.API_KEY` |
| `BASE_URL` | `.../boxoffice/searchDailyBoxOfficeList.json` |
| 요청 파라미터 | `key`(API 키), `targetDt`(8자리 날짜) |
| 타임아웃 | 10초 |
| 사용하는 응답 필드 | `boxOfficeResult.dailyBoxOfficeList` → 각 항목의 `movieNm`, `audiCnt` |

## 함수

### `get_boxoffice_rank_1(date)`

- 입력: `date` (str, 예: `"20260824"`)
- 반환: 1위 영화 제목 (str, 예: `"오디세이"`)
- 동작: 목록의 첫 항목 `movies[0]["movieNm"]`을 반환

### `get_movie_audience(date, title)`

- 입력: `date` (str, 8자리 날짜), `title` (str, 영화 제목)
- 반환: (str)
  - 찾은 경우: `"186,587명"` 형식 (천 단위 쉼표 + '명')
  - 못 찾은 경우: `"'{title}' 은(는) {date} 순위에 없습니다."`
- 동작: 목록을 순회하며 `movieNm == title`인 항목의 `audiCnt`를 `int`로 바꿔 포맷

## 개선이 필요한 점

1. **중복 코드**: API 호출·JSON 파싱·목록 추출 코드가 두 함수에 똑같이 있음 → 공통 헬퍼로 분리 가능
2. **에러 처리 없음**: 네트워크 오류, HTTP 오류 상태, 잘못된 날짜, 빈 목록이면 `KeyError`/`IndexError`/예외 발생
3. **제목 완전 일치**: 띄어쓰기·표기가 다르면 영화를 찾지 못함
4. **반환 타입**: 관객 수를 문자열로만 반환해 숫자로 재활용하기 어려움 (에이전트 도구용이라면 의도된 선택일 수 있음)
5. **docstring 스타일 불일치**: 첫 함수는 "받는 것/돌려주는 것" 형식, 둘째는 서술형 + 사용 예시
