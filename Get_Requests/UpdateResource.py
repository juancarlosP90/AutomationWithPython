import  requests
import json
import jsonpath


url = "https://reqres.in/api/users/2"

file = open('/Users/juan/Desktop/CreateUser.json','r')
json_input = file.read()
request_json = json.loads(json_input)

# Make PUT request
response = requests.put(url, request_json)

# Validating response code
assert response.status_code == 200

# Parse response content
responseJson = json.loads(response.text)
newResponse = jsonpath.jsonpath(responseJson, 'updatedAt')
print(newResponse[0])