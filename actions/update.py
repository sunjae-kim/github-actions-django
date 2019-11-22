from movies.apis import fetch_movies
from datetime import datetime
from pprint import pprint

movies = fetch_movies()
print('Hello World at', datetime.now())
print()
pprint(movies)