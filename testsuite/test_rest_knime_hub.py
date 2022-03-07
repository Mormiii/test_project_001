import pytest
from pytest_bdd import given,when,then,scenario, parsers
import requests as REST
import json
from conftest import token, user_rep_space_names, user, user_for_url



url_create_space =f'https://api.hub.knime.com/repository//Users/{user_for_url}/'
url_api ='https://api.hub.knime.com/'

#@pytest.mark.skip("reason=currently we dont want to test this")
@scenario("features/rest_knime_hub.feature","Create Space")
def test_create_space():
    pass

#@pytest.mark.skip("reason=currently we dont want to test this")
@scenario("features/rest_knime_hub.feature","Delete Space")
def test_delete_space():
    pass


@given("request with body and <spacename> which is a <test_type> test")
def arrange_requirements(spacename, test_type, user):
    print(f"\nCreate a public space with name :{spacename}")
    print(f"This is a {test_type} test.")
    print(user_rep_space_names(user))
    if spacename in user_rep_space_names(user):
        print(f"WARNING: The {spacename} that you're trying to create is already in use!")
        #raise Exception
    else:
        print(f"The {spacename} is not used.")





@given("an existing space with name <spacename> which is a <test_type> test")
def arrange_requirements(spacename, test_type,user):
    print(f"\nThe name of the space which we try to delete is :{spacename}")
    print(f"This is a {test_type} test.")
    print(user_rep_space_names(user))
    if spacename not in user_rep_space_names(user):
        print(f"WARNING: The {spacename} what you're trying to delete is not existing!")
        #raise Exception
    else:
        print(f"The {spacename} exist, so it can be deleted.")



@when("put request arrives to endpoint/<spacename>", target_fixture = "resp")
def create_request(spacename, user):
    body = {
        "private":"false" ,
        "type": "Space",
        "overwrite": "false",
        "move": "true",
        "from-repository": ""}

    headers = {"Accept":"application/json", "Authorization":f"Bearer {token}"}
    url_create_space_filled = url_create_space + spacename
    print("Sending a PUT request to this url:",url_create_space_filled)
    body["from-repository"] = f"/Users/{user}/New space"
    print(f'with body :{body} and header: {headers}')
    resp = REST.put(url_create_space_filled, data = json.dumps(body, indent =2) , headers=headers)
    print("The response is :", resp.text)
    return resp



@when("delete request arrives to endpoint", target_fixture = "resp")
def delete_request(spacename):
    url_create_space_filled = url_create_space + spacename + '/'
    headers = {"Accept":"application/json", "Authorization":f"Bearer {token}"}
    print("Sending a DELETE request to this url:",url_create_space_filled)
    print(f"with header: {headers}")
    resp = REST.delete(url_create_space_filled, headers=headers)
    print("The response is :", resp.text)
    return resp


@then("<expected_status> is responded")
def check_response(resp, expected_status):
    print("The response code is:",resp.status_code, "| and the expected status is:",expected_status )
    if resp.status_code == 200:
        print("It's possible that you're trying to create a space with a name that is already in use.")

    assert int(expected_status) == int(resp.status_code)
    if resp.status_code == 200:
        print("It's possible that you're trying to create a space with a name that is already in use.")


#@then("in the response is a uniq Id for the space", target_fixture= "id")
#def get_blobId(resp):
#    response_id = resp['id']
#    print(f"In the response : {response_id} is found.")




