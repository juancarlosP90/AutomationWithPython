import requests
from requests.auth import HTTPBasicAuth


def test_basicauthentication():
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth('juancarlosP90', 'Juancarlos90*'))
    print(response.text)
