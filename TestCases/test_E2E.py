import requests
import json
import jsonpath

def test_AddNewData():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('/Users/juan/Desktop/Python/requests/postRequest.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(API_URL, request_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_api = "https://thetestingworldapi.com/api/technicalskills"
    f = open('/Users/juan/Desktop/Python/requests/postTechDetails.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(tech_api, request_json)
    print(response.text)

    address_api = "https://thetestingworldapi.com/api/addresses"
    f = open('/Users/juan/Desktop/Python/requests/address.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(address_api, request_json)
    print(response.text)

    final_details = "https://thetestingworldapi.com/api/FinalStudentDetails/8442682"
    requests.get(final_details)
    print(response.text)