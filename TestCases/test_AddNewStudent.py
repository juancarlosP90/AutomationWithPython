import requests
import json
import jsonpath


def test_addStudentData():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/Desktop/Desktop/Python/Requests/postRequest.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    print(response.text)

def test_updateStudentData():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/8441302"
    f = open('C:/Users/Desktop/Desktop/Python/Requests/postRequest.json', 'r')
    json_request = json.loads(f.read())
    response = requests.put(API_URL, json_request)
    print(response.text)

def test_getStudentData():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/8441302"
    response = requests.get(API_URL)
    json_response = response.json()
    print(json_response)
    id=jsonpath.jsonpath(json_response,'data.id')
    assert id[0] == 8441302
    #print(id)

def test_DeleteStudent():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/8441308"
    response= requests.delete(API_URL)
    print(response.text)