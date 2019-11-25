import requests
from decouple import config
from datetime import datetime, timedelta


def fetch_movies():
    API_KEY = config('MOVIE_API_KEY')
    API_URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
    REQUEST_URL = f'{API_URL}?key={API_KEY}&targetDt={datetime.strftime(datetime.now() - timedelta(10), "%Y%m%d")}'
    response = requests.get(REQUEST_URL)
    movies = response.json().get('boxOfficeResult').get('weeklyBoxOfficeList')
    return movies

if __name__ == "__main__":
    movies = fetch_movies()
    print(movies)
