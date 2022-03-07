import requests as REST
from json.decoder import JSONDecodeError
import pytest

token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ2SHpuYUhTS3RMWmszcnczVlJBN2M4eThsUHlVazU3YndMejRvekFZT1o4In0.eyJqdGkiOiI3OGJhYTlhZC0wODYzLTRiMzMtYTU5Yi01ZjljNDQxYjAwYjYiLCJleHAiOjE2NDY3MDQzMTcsIm5iZiI6MCwiaWF0IjoxNjQ2NjkzNTE3LCJpc3MiOiJodHRwczovL2F1dGguaHViLmtuaW1lLmNvbS9hdXRoL3JlYWxtcy9rbmltZSIsInN1YiI6IjBlY2UwMmY1LWFkZmItNDU3Yi1hMmFmLWJjOTNkYjc0NDdjMCIsInR5cCI6IkJlYXJlciIsImF6cCI6Imh1Yi11aSIsIm5vbmNlIjoiWGRoNHE0U3F0dXl6dmhMekxlUkJKYng5NTlSeUFraExBd0d5LU1Zc01OZyIsImF1dGhfdGltZSI6MTY0NjY0NDI0Mywic2Vzc2lvbl9zdGF0ZSI6Ijc3NmEwNTM0LWU0NjMtNGIwMS1iNDY2LWRkOGIxZDI2NTk0MCIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9zdGFnZS5odWIua25pbWUuY29tIiwiaHR0cHM6Ly9odWIua25pbWUuY29tIl0sInJlc291cmNlX2FjY2VzcyI6eyJicm9rZXIiOnsicm9sZXMiOlsicmVhZC10b2tlbiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZ3JvdXBzIHJvbGVzIGVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IlRlc3RfS25pbWVfMDAxIiwiZ3JvdXBzIjpbImh1YnVzZXIiXSwicHJlZmVycmVkX3VzZXJuYW1lIjoidGVzdF9rbmltZV8wMDEiLCJnaXZlbl9uYW1lIjoiVGVzdF9LbmltZV8wMDEiLCJlbWFpbCI6ImRvci5kZWthbnlAZ21haWwuY29tIn0.P6UeDIxy3g0GTTQlZRELDzSv4WFsaRj4KtIpJt7Pf6FBqog2ftXRqJnci7pC-a1iPf0880Lk0hRkszvhBCUhLpvcf7vF_Y3sr5u6YhuSbSMd2cgIrjZ14fNbCas81_RqXKA_hOQO8i5sm4VE0lAEWkF_u4KzKnawrCZUamcDSG6cz8pKpIAQwAlwVMPcyC-bf78gXLOiPMKIvSvG3UG5sqgVsuKNiq3APvBFwqq_lAeS1SwdGgLQ2erYndJcC3SptDoogNd5eS-AP4U6FklnuX9e_LLv9GFBSOmEiFwBcD2zb7mOT3Uw7dWzbVO8qzg7RhMgjMwoIE8nruMkFALQ_g"

# here pls give the User for the repository
@pytest.fixture
def user():
	return 'test_knime_001'

user_for_url= 'test_knime_001'



def user_rep_space_names(user):
	# user = 'test_knime_001'
	url_user_repo = f'https://api.hub.knime.com/repository//Users/{user}'
	#user_repo = f'/Users/{user}/'
	params_space_details = {"spaceDetails": "true", "contribSpaces": "children"}
	print(f"Information about this user: {user}'s repository")
	#print("Sending a GET request to this url:", url_user_repo)
	headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
	resp = REST.get(url_user_repo, params=params_space_details, headers=headers)
	try:
		resp_json = resp.json()
	except JSONDecodeError:
		print("You're token might be invalid/expired!")
		raise Exception

	print("Number of spaces existing in this repository: ", len(resp_json["children"]))
	spaces = resp_json["children"]
	paths = []
	for i in spaces:
		paths.append(i['path'])
	#print(f" User has following children paths:{paths}")
	space_names = []
	for p in paths:
		#space_names.append(p.lstrip(f"/Users/{user}/"))
		space_names.append(p[22:])
	#print(f"User has spaces with name: {space_names}")
	return space_names