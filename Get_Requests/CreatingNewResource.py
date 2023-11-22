import requests
import json
import jsonpath


url = "https://reqres.in/api/users"

file = open('C:/Users/Desktop/Desktop/Python/Requests/CreateUser.json','r')
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with input json body

response = requests.post(url, request_json)

# Validating response code
assert response.status_code == 201

# Fetch Header from response
print(response.headers.get('Content-Length'))

# Parse response to json format
responseJson = json.loads(response.text)

# Pick Id using jsonpath
id = jsonpath.jsonpath(responseJson,'id')
print(id[0])
