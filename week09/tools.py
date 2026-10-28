
"""tools.py - 박스오피스 정보를 가져오는 도구 모음"""

import requests
from secret import API_KEY

BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/"
            "rest/boxoffice/searchDailyBoxOfficeList.json")


def get_boxoffice_rank_1(date):
    """
    그 날짜의 박스오피스 1위 영화 제목을 알려준다.

    받는 것: date (문자열) - 8자리 날짜. 예: "20260824"
    돌려주는 것: (문자열) 1위 영화 제목. 예: "오디세이"
    """

    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]
    return movies[0]["movieNm"]


def get_movie_audience(date, title):
    """일별 박스오피스에서 영화 제목에 해당하는 관객 수를 조회한다.

    date는 조회 날짜를 나타내는 8자리 문자열이고, title은 검색할 영화 제목이다.
    반환값은 관객 수에 천 단위 쉼표와 '명'을 붙인 문자열이며, 영화를 찾지 못하면
    해당 날짜 순위에 없다는 안내 문자열을 반환한다.

    사용 예시:
        get_movie_audience("20260824", "오디세이")
        # "186,587명"
    """

    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]

    for movie in movies:
        if movie["movieNm"] == title:
            audience = int(movie["audiCnt"])
            return f"{audience:,}명"

    return f"'{title}' 은(는) {date} 순위에 없습니다."
