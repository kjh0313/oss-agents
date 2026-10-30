# week09

## 1. 코드가 하는 일
KOBIS 일별 박스오피스 API에서 날짜별 1위 영화와 지정한 영화의 관객 수를 조회합니다. `main.py`는 `tools.py`를 사용해 결과를 출력합니다.

## 2. 설치할 것
Python 3와 `requirements.txt`의 패키지가 필요합니다. 폴더에서 다음 명령으로 설치합니다.

```bash
python3 -m pip install -r requirements.txt
```

## 3. 실행 방법
같은 폴더에 KOBIS API 키를 넣은 `secret.py` 파일을 준비합니다.

```python
API_KEY = "발급받은_API_키"
```

그다음 폴더에서 실행합니다.

```bash
python3 main.py
```
