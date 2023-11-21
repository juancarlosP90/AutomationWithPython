import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)
print(response)

# Display Response content
# print(response.content)
# print(response.headers)

# Validate Status Code
# print(response.status_code)

# assert response.status_code == 200

# Fetch response header
# print(response.headers)
# print(response.headers.get('Date'))
# print(response.headers.get('Server'))

# print(response.cookies)
# print(response.encoding)

# print(response.elapsed)

json_response = json.loads(response.text)
# print(json_response)

# Fetch value using json path
pages = jsonpath.jsonpath(json_response, 'total_pages')
# print(pages[0])
# assert pages[0] == 2

for i in range(0, 3):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print((first_name[0]))
