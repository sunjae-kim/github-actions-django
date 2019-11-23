import requests
from decouple import config
from datetime import datetime, timedelta
from pprint import pprint

def fetch_movies():
    API_KEY = config('MOVIE_API_KEY')
    API_URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
    REQUEST_URL = f'{API_URL}?key={API_KEY}&targetDt={datetime.strftime(datetime.now() - timedelta(1), "%Y%m%d")}'
    response = requests.get(REQUEST_URL)
    movies = response.json().get('boxOfficeResult').get('dailyBoxOfficeList')
    return movies

movies = fetch_movies()
print('Hello World at', datetime.now())
print()
pprint(movies)