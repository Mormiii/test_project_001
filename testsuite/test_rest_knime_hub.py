import pytest
from pytest_bdd import given,when,then,scenario, parsers
import requests as REST
from requests.structures import CaseInsensitiveDict

url_create_space ='https://api.hub.knime.com/repository/Users/test_knime_001/'
url_api ='https://api.hub.knime.com/'

#@pytest.mark.skip("reason=currently we dont want to test this")
@scenario("features/rest_knime_hub.feature","Create Space")
def test_create_space():
    pass

#@pytest.mark.skip("reason=currently we dont want to test this")
@scenario("features/rest_knime_hub.feature","Delete Space")
def test_delete_space():
    pass

body ={

    "private":"false",
    "type":"Space",
    "overwrite": "false",
    "move": "true",
    "from-repository": ""

}


"""

AUTH
Bearer Token
"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ2SHpuYUhTS3RMWmszcnczVlJBN2M4eThsUHlVazU3YndMejRvekFZT1o4In0.eyJqdGkiOiJkYzViNmE4Ny0zZDY4LTQ4ZDQtYTFhYi04YmI4ZTZmYmIzNjMiLCJleHAiOjE2NDYxOTA4NzcsIm5iZiI6MCwiaWF0IjoxNjQ2MTgwMDc3LCJpc3MiOiJodHRwczovL2F1dGguaHViLmtuaW1lLmNvbS9hdXRoL3JlYWxtcy9rbmltZSIsInN1YiI6IjBlY2UwMmY1LWFkZmItNDU3Yi1hMmFmLWJjOTNkYjc0NDdjMCIsInR5cCI6IkJlYXJlciIsImF6cCI6Imh1Yi11aSIsIm5vbmNlIjoib0JGUVJ0c2xUallyektQektoS200M3BwYmF6NWRpRjJIaGU1TV9qNUFmWSIsImF1dGhfdGltZSI6MTY0NjE4MDA3Niwic2Vzc2lvbl9zdGF0ZSI6ImI5ZWJmMTg5LWVhMDctNGYzYi04MmQxLThiMDVlNDI1ZWEwNiIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9zdGFnZS5odWIua25pbWUuY29tIiwiaHR0cHM6Ly9odWIua25pbWUuY29tIl0sInJlc291cmNlX2FjY2VzcyI6eyJicm9rZXIiOnsicm9sZXMiOlsicmVhZC10b2tlbiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZ3JvdXBzIHJvbGVzIGVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IlRlc3RfS25pbWVfMDAxIiwiZ3JvdXBzIjpbImh1YnVzZXIiXSwicHJlZmVycmVkX3VzZXJuYW1lIjoidGVzdF9rbmltZV8wMDEiLCJnaXZlbl9uYW1lIjoiVGVzdF9LbmltZV8wMDEiLCJlbWFpbCI6ImRvci5kZWthbnlAZ21haWwuY29tIn0.PAvqhc0SxdWb-yU16KBEHAd1m5WMuG5U7gFVIufEZD1hE7fnKFkSbPz8f180q92QE9FfEgMRjDE32dQ45aOP2dEKNW_QNbsDO--MRFFm7Lm4S7HBn1V32aVIRT7ZvL8ywiu3gKAZDEMJq8gHysSSSpjGLYAGB6Yrw9cFZ9eFZ5jwSRncHtRMZid7Ybg42kgR4MhPMGpmd87PFbA_5MlglgwjoT8_2nGf5eBygbDIr4T4EtmbWXO_i_CjmQbKz3W9wQQCOIsCsCx-N0TkkB28fYqPeAUxVscliXGFMkYrA5R_jZ6c2nnKwCYqTdHOCKkOJw9FMxBJelmFaC0JcwXMIg"

GET
https://api.hub.knime.com/repository/Users/test_knime_001/



PUT https://api.hub.knime.com/repository/Users/test_knime_001/New space

Body

{"private":false,"type":"Space"}


PUT 
https://api.hub.knime.com/repository//Users/test_knime_001/---test-003
Body
{
    "private":false,
    "type":"Space", 
    "overwrite": false,
    "move": true,
    "from-repository": "/Users/test_knime_001/New space"
}


DELETE
https://api.hub.knime.com/repository//Users/test_knime_001/---test-003



"""



@given("request with body and <spacename> which is a <test_type> test")
def arrange_requirements(spacename, test_type):
    print(f"\nThe name of the space is :{spacename}")
    print(f"This is a {test_type} test.")

token = {"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ2SHpuYUhTS3RMWmszcnczVlJBN2M4eThsUHlVazU3YndMejRvekFZT1o4In0"

}

@given("an existing space with name <spacename> which is a <test_type> test")
def arrange_requirements(spacename, test_type):
    print(f"\nThe name of the space which we try to delete is :{spacename}")
    print(f"This is a {test_type} test.")

@when("put request arrives to endpoint/<spacename>", target_fixture = "resp")
def create_request(spacename, body):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    resp = REST.get(url_create_space, headers=headers)
    print(resp.status_code)
    url_create_space_filled = url_create_space + spacename
    print("Sending a DELETE request to this url:",url_create_space_filled)
    body["from-repository"] = f"/Users/test_knime_001/{spacename}"
    print("with body :",body)
    resp = REST.put(url_create_space, data =body )
    print("The response is :", resp)
    return resp



@when("delete request arrives to endpoint", target_fixture = "resp")
def delete_request(spacename):
    url_create_space_filled = url_create_space + spacename
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    resp = REST.get(url_create_space, headers=headers)
    print(resp.status_code)

    print("Sending a DELETE request to this url:",url_create_space_filled)
#    body["from-repository"] = f"/Users/test_knime_001/{spacename}"
    resp = REST.put(url_create_space)
    print("The response is :", resp)
    return resp


@then("<expected_status> is responded")
def check_response(resp, expected_status):
    print("The response code is:",resp.status_code, "| and the expected status is:",expected_status )
    assert int(expected_status) == resp.status_code


#@then("in the response is a uniq Id for the space", target_fixture= "id")
#def get_blobId(resp):
#    response_id = resp['id']
#    print(f"In the response : {response_id} is found.")




