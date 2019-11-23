import requests
from datetime import datetime

response = requests.get('https://dog.ceo/api/breeds/image/random')

print('Hello World at', datetime.now())
print(response.json())
