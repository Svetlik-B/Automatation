import pytest
import requests
import json
from Lesson8.Employee import Employer, Company
from Lesson8.constants import base_url

employer = Employer()
company = Company()

def test_authorization(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token, str)
    
def test_getcompany_id():
    company_id = company.last_active_company_id()
    assert company_id is not None
    assert str(company_id).isdigit()
    
def test_add_employer(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer =  {
        "id": 0,
        "firstName": "Olga",
        "lastName": "QA",
        "middleName": "string",
        "companyId": com_id,
        "email": "string",
        "url": "string",
        "phone": "string",
        "birthdate": "2024-06-18T12:18:20.475Z",
        "isActive": 'true'}
    
    new_employer_id = (employer.add_new_employee(token, body_employer))['id']
    assert new_employer_id is not None
    assert str(new_employer_id).isdigit()
    
    info = employer.get_info_new_employee(new_employer_id)
    assert info.json()['id'] == new_employer_id
    assert info.status_code == 200 

def test_add_employer_non_token():
    token = ""
    com_id = company.last_active_company_id()
    body_employer =  {
        "id": 0,
        "firstName": "Olga",
        "lastName": "QA",
        "middleName": "string",
        "companyId": com_id,
        "email": "string",
        "url": "string",
        "phone": "string",
        "birthdate": "2024-06-18T12:18:20.475Z",
        "isActive": 'true'}
    
    new_employer = employer.add_new_employee(token, body_employer)
    assert new_employer['message'] == 'Unauthorized'
    
def test_add_employer_without_body(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {}
    new_employer = employer.add_new_employee(token, body_employer)
    assert new_employer ['message'] == 'Internal server error'
    
def test_get_employer():
    com_id = company.last_active_company_id()
    list_employers = employer.get_list(com_id)
    assert isinstance(list_employers, list)
    
def test_get_list_employers_missing_company_id():
    try:
        employer.get_list()
    except TypeError as e:
        assert str(e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"
        
def test_get_list_employers_invalid_company_id():
    try:
        employer.get_list('')
    except TypeError as e:
        assert str(e) == "Employer get list() missing 1 required positional argument: 'company_id'"
        
def test_change_employer_info(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer =  {
        "id": 0,
        "firstName": "Olga",
        "lastName": "QA",
        "middleName": "string",
        "companyId": com_id,
        "email": "string",
        "url": "string",
        "phone": "string",
        "birthdate": "2024-06-18T12:18:20.475Z",
        "isActive": 'true'}
    just_employer = employer.add_new_employee(token, body_employer)
    id = just_employer['id']
    body_change_employer = {
        'lastName': 'Kozlov',
        'email': 'test2@string',
        'url': 'string',
        'phone': 'string',
        'isActive': 'true'}
    employer_changed = employer.change_new_employee(token, id, body_change_employer)
    assert employer_changed.status_code == 200
    assert id == employer_changed.json()['id']
    assert (employer_changed.json()["email"]) == body_change_employer.get ("email")
    
def test_employers_missing_id_and_token():
    try:
        employer.change_new_employee()
    except TypeError as e:
        assert str(e) == "Employer.change_new_employee() missing 3 required positional arguments: 'token', 'employee_id', 'body'"
    