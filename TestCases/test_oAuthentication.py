import requests
import json
import jsonpath

def test_oauth_api():
    token_url='https://thetestingworldapi.com/Token'
    data = {'grant_type':'password', 'username':'admin','password':'adminpass'}
    response = requests.post(token_url,data)
    tokenValue = jsonpath.jsonpath(response.json(),'access_token')

    auth = {'Authorization':'Bearer '+tokenValue[0]}
    API_URL='https://thetestingworldapi.com/api/StDetails/8468319'
    response = requests.get(API_URL,headers=auth)
    print(response.text)
