import requests
param = {'name':'TestingWorld', 'email': 'juan@me.com', 'number': '+56 19-367-3644'}
response = requests.get('https://httpbin.org/get', params=param)
print(response.text)