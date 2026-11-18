# boxoffice — KOBIS 박스오피스 조회 스킬

## 하는 일
날짜로 박스오피스 1위 제목, 날짜+제목으로 관객 수를 조회한다.

## 들어 있는 파일
- .claude/skills/boxoffice/SKILL.md
- .claude/skills/boxoffice/scripts/boxoffice.py
- .claude/skills/boxoffice/LICENSE

## 필요한 것
- `tools.py`, `secret.py` (같은 프로젝트 폴더)
- 파이썬 3, `requests`

## 설치
`boxoffice` 폴더를 스킬 폴더에 두고 Claude Code 를 실행한다.

## 바깥으로 요청하는 곳
`kobis.or.kr` (KOBIS 오픈 API) 한 곳

## 키
저장소에 없음. 자기 키를 `secret.py` 에 넣는다.

## 권한
`allowed-tools` 없음. 스크립트 실행 때마다 허용 여부를 묻는다.

## 라이선스
MIT (2026 김정협), LICENSE 파일 참고
