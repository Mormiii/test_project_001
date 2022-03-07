import pytest
from pytest_bdd import given,when,then,scenario, parsers
import requests as REST
from requests.structures import CaseInsensitiveDict
import json
from conftest import token



user = 'test_knime_001'
url_user_repo =f'https://api.hub.knime.com/repository//Users/{str(user)}'

url_api ='https://api.hub.knime.com/'
params_space_details = {"spaceDetails":"true","contribSpaces":"children" }

user_repo= '/Users/test_knime_001/'
headers = {"Accept":"application/json", "Authorization":f"Bearer {token}"}


print("Sending a GET request to this url:",url_user_repo)
print(f'with params :{params_space_details} and header: {headers}')
resp = REST.get(url_user_repo, params = params_space_details, headers=headers)
print("The response is :", resp.text)
resp_json= resp.json()
print("Number of spaces existing in this repository: ",len(resp_json["children"]))

spaces = resp_json["children"]
paths = []
for i in spaces:
    paths.append(i['path'])
print(f" User has following children paths:{paths}")
space_names = []
for p in paths:
    space_names.append(p.lstrip("/Users/test_knime_001/"))

print(f"User : {user_repo.lstrip('/Users/')} has following spaces: {space_names}")


def user_rep_space_names(user):
    #user = 'test_knime_001'
    url_user_repo =f'https://api.hub.knime.com/repository//Users/{str(user)}'
    user_repo= f'/Users/{user}/'
    params_space_details = {"spaceDetails": "true", "contribSpaces": "children"}
    print("Sending a GET request to this url:",url_user_repo)
    headers = {"Accept":"application/json", "Authorization":f"Bearer {token}"}
    resp = REST.get(url_user_repo, params = params_space_details, headers=headers)
    resp_json= resp.json()
    print("Number of spaces existing in this repository: ",len(resp_json["children"]))
    spaces = resp_json["children"]
    paths = []
    for i in spaces:
        paths.append(i['path'])
    print(f" User has following children paths:{paths}")
    space_names = []
    for p in paths:
        space_names.append(p.lstrip(f"/Users/{user}/"))

    print(f"User : {user_repo.lstrip('/Users/')} has following spaces: {space_names}")


