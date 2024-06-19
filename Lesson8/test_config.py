import pytest
import requests
from Lesson8.constants import base_url

@pytest.fixture()
def get_token(username= 'raphael', password ='cool-but-crude'):
    log_pass = {'username': username, 'password': password}
    resp_token = requests.post(base_url + 'auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token