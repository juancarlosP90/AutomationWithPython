import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library

# DATA DRIVEN TESTING (Multiple Files)

def test_add_multiple_students():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('/Users/juan/Desktop/Python/requests/addNewStudent.json')
    json_request = json.loads(f.read())

    obj = Library.Common("/Users/juan/Desktop/Python/requests/testData.xlsx", "Sheet1")
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()


    for i in range (2, row+1):
        updated_json_request = obj.update_request_with_data(i,json_request, keyList)
        response = requests.post(API_URL,updated_json_request)
        print(response)
