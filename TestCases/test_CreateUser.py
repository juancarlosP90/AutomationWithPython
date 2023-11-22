import  requests
import json
import jsonpath
import pytest

# API url
url = "https://reqres.in/api/users"
#a=100


# This method will be used before each test cases (fixture)

@pytest.fixture()
def start_exec():
    global file
    file = open('C:/Users/Desktop/Desktop/Python/Requests/CreateUser.json', 'r')
#@pytest.mark.skip("This is not valid for current build")
#@pytest.mark.skipif(a>10, reason="Condition is not satisfied")
def test_create_new_user(start_exec):
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201

def test_create_other_user(start_exec):
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    responseJson = json.loads(response.text)
    id = jsonpath.jsonpath(responseJson,'id')
    print(id[0])