import requests
import json
import jsonpath

def test_fetch_user_details():
    # API URL
    url = "https://reqres.in/api/users?page=2"

    # Send Get Request
    response = requests.get(url)
    print(response)
    # Parse response to Json format
    json_response = json.loads(response.text)

    for i in range(0, 3):
        first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
        print((first_name[0]))

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
    # print(json_response)
    # Fetch value using json path
    #pages = jsonpath.jsonpath(json_response, 'total_pages')
    # print(pages[0])
    # assert pages[0] == 2


