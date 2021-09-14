import json
from . import queries
import requests

def test_prerna_saathi():
    volunteer_endpoint = "http://localhost:8080/volunteer"
    f = open('prerna_saathi_final.json', 'r')
    request_json = json.dumps(json.loads(f.read()))
    headers = {'content-type': 'application/json'}
    response = requests.post(volunteer_endpoint, data=request_json, headers=headers, verify=False)
    assert str(response.text) == "success"
    assert str(response.status_code) == "200"


def test_prerna_saathi_duplicates():
    volunteer_endpoint = "http://localhost:8080/volunteer"
    f = open('prerna_saathi_final.json', 'r')
    request_json = json.dumps(json.loads(f.read()))
    headers = {'content-type': 'application/json'}
    response = requests.post(volunteer_endpoint, data=request_json, headers=headers, verify=False)
    assert str(response.text) == "success"
    assert str(response.status_code) == "200"


def test_ePathshala():
    epathshala_endpoint = "http://localhost:8080/epathshala-quiz"
    f = open('ePathshala_quiz.json', 'r')
    request_json = json.dumps(json.loads(f.read()))
    headers = {'content-type': 'application/json'}
    response = requests.post(epathshala_endpoint, data=request_json, headers=headers, verify=False)
    assert str(response.text) == "success"
    assert str(response.status_code) == "200"


def test_ePathshala_duplicates():
    epathshala_endpoint = "http://localhost:8080/epathshala-quiz"
    f = open('ePathshala_quiz_duplicates.json', 'r')
    request_json = json.dumps(json.loads(f.read()))
    headers = {'content-type': 'application/json'}
    response = requests.post(epathshala_endpoint, data=request_json, headers=headers, verify=False)
    assert str(response.text) == "success"
    assert str(response.status_code) == "200"





