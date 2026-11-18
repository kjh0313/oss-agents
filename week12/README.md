# boxoffice — KOBIS 박스오피스 조회 스킬

## 하는 일
- 날짜(8자리)를 주면 영화진흥위원회(KOBIS) 일별 박스오피스의 1위 영화 제목을 알려 줌
- 날짜와 영화 제목을 주면 해당 영화의 관객 수를 알려 줌

## 들어 있는 파일
- .claude/skills/boxoffice/SKILL.md
- .claude/skills/boxoffice/scripts/boxoffice.py
- .claude/skills/boxoffice/LICENSE

## 필요한 것
- 스킬 폴더 밖에 있어야 하는 파일
  - `tools.py`: KOBIS API 를 호출하는 함수 모음. 스크립트가 불러 씀
  - `secret.py`: `API_KEY = "..."` 한 줄이 든 파일. 받는 사람이 직접 만들어야 함
- 파이썬 3 과 `requests` 패키지 (`pip install requests`)
- 스크립트는 현재 작업 폴더에서 `tools.py` 를 찾으므로 `tools.py`, `secret.py` 가 있는 폴더에서 실행해야 함

## 설치
1. `boxoffice` 폴더를 프로젝트 폴더의 `.claude/skills/` 아래에 둠 (`.claude/skills/boxoffice/`)
2. 같은 프로젝트 폴더에 `tools.py` 와 `secret.py` 를 둠
3. 프로젝트 폴더에서 Claude Code 를 실행함. 박스오피스를 물으면 스킬이 쓰임
4. 직접 확인할 때는 아래 명령을 실행함
   - `python .claude/skills/boxoffice/scripts/boxoffice.py rank 20261114`
   - `python .claude/skills/boxoffice/scripts/boxoffice.py audience 20261114 "영화 제목"`

## 바깥으로 요청하는 곳
- `https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json` 한 곳뿐임 (`tools.py` 에서 호출)
- 보내는 것은 API 키와 조회 날짜임. 다른 주소로 보내는 코드는 없음

## 키
- 키는 이 저장소에 없음
- 받는 사람은 자기 KOBIS API 키를 발급받아 자기 `secret.py` 에 넣을 것
- `secret.py` 는 커밋하지 말 것

## 권한
- `SKILL.md` 에 `allowed-tools` 가 없음. 권한을 따로 넓히지 않음
- Claude Code 가 스크립트를 실행할 때마다 `python .claude/skills/boxoffice/scripts/boxoffice.py ...` 명령 실행 허용 여부를 물음. Manual 모드에서는 명령 줄을 읽고 허용할 것
- 스킬의 지시는 스크립트 출력만 근거로 답하고, `tools.py` 와 `secret.py` 를 읽거나 고치지 말라는 것뿐임

## 라이선스
- MIT License (2026 김정협)
- 파일 위치: `.claude/skills/boxoffice/LICENSE`
