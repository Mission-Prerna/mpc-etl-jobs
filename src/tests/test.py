import json
from . import queries, conn_util
import requests
import time


def test_prerna_saathi():
    volunteer_endpoint = "http://localhost:8080/volunteer"
    f = open('prerna_saathi_final.json', 'r')
    request_json = json.dumps(json.loads(f.read()))
    json_obj = json.loads(request_json)
    headers = {'content-type': 'application/json'}
    response = requests.post(volunteer_endpoint, data=request_json, headers=headers, verify=False)
    assert str(response.text) == "success"
    assert str(response.status_code) == "200"
    time.sleep(3)
    for form_request in json_obj["data"]:
        form_request = form_request[0]
        form_request['instanceID'] = form_request['instanceID'].replace("uuid:", "")
        connection = conn_util.get_connection()
        cursor = connection.cursor()
        data = []
        cursor.execute(queries.GET_VOLUNTEER_COUNT.format(form_request['wanum']), data)
        results = cursor.fetchone()
        assert str(results[0]) == '1'


def test_prerna_saathi_duplicates():
    volunteer_endpoint = "http://localhost:8080/volunteer"
    f = open('prerna_saathi_final.json', 'r')
    request_json = json.dumps(json.loads(f.read()))
    json_obj = json.loads(request_json)
    headers = {'content-type': 'application/json'}
    response = requests.post(volunteer_endpoint, data=request_json, headers=headers, verify=False)
    assert str(response.text) == "success"
    assert str(response.status_code) == "200"
    time.sleep(3)
    for form_request in json_obj["data"]:
        form_request = form_request[0]
        form_request['instanceID'] = form_request['instanceID'].replace("uuid:", "")
        connection = conn_util.get_connection()
        cursor = connection.cursor()
        data = []
        cursor.execute(queries.GET_VOLUNTEER_COUNT.format(form_request['wanum']), data)
        results = cursor.fetchone()
        assert str(results[0]) == '1'

def test_ePathshala():
    epathshala_endpoint = "http://localhost:8080/epathshala-quiz"
    f = open('ePathshala_quiz.json', 'r')
    request_json = json.dumps(json.loads(f.read()))
    json_obj = json.loads(request_json)
    headers = {'content-type': 'application/json'}
    response = requests.post(epathshala_endpoint, data=request_json, headers=headers, verify=False)
    assert str(response.text) == "success"
    assert str(response.status_code) == "200"
    time.sleep(3)
    for form_request in json_obj["data"]:
        form_request = form_request[0]
        form_request['instanceID'] = form_request['instanceID'].replace("uuid:", "")
        connection = conn_util.get_connection()
        cursor = connection.cursor()
        data = []
        cursor.execute(queries.GET_EPATHSHALA_COUNT.format(form_request['instanceID']), data)
        results = cursor.fetchone()
        assert str(results[0]) == '1'


def test_ePathshala_duplicates():
    epathshala_endpoint = "http://localhost:8080/epathshala-quiz"
    f = open('ePathshala_quiz_duplicates.json', 'r')
    request_json = json.dumps(json.loads(f.read()))
    json_obj = json.loads(request_json)
    headers = {'content-type': 'application/json'}
    response = requests.post(epathshala_endpoint, data=request_json, headers=headers, verify=False)
    assert str(response.text) == "success"
    assert str(response.status_code) == "200"
    time.sleep(3)
    for form_request in json_obj["data"]:
        form_request = form_request[0]
        form_request['instanceID'] = form_request['instanceID'].replace("uuid:", "")
        connection = conn_util.get_connection()
        cursor = connection.cursor()
        data = []
        cursor.execute(queries.GET_EPATHSHALA_COUNT.format(form_request['instanceID']), data)
        results = cursor.fetchone()
        assert str(results[0]) == '1'

def test_purge_data():
    connection = conn_util.get_connection()
    cursor = connection.cursor()
    cursor.execute(queries.DELETE_VOLUNTEER)
    cursor.execute(queries.DELETE_VOLUNTEER_NORMALIZED)
    cursor.execute(queries.DELETE_EPATHSHALA)
    connection.commit()






