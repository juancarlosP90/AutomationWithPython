import requests
import json
import jsonpath

def test_AddNewStudent():
    global id
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/Desktop/Desktop/Python/Requests/postRequest.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

def test_GetDetails():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(API_URL)
    print(response.text)