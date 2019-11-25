# actions/update.py
import requests

response = requests.get('http://github-actions-test.jvnsgh2u35.ap-northeast-2.elasticbeanstalk.com/movies/update-db/')
print(response.json())
