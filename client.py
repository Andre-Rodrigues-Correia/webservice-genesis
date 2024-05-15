import requests
import json


def send_json(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://127.0.0.1:5000/pacientes', headers=headers, data=json.dumps(data))
    try:
        print(response.json())
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")


def send_xml(data):
    headers = {'Content-Type': 'application/xml'}
    response = requests.post('http://127.0.0.1:5000/pacientes', headers=headers, data=data)
    try:
        print(response.json())
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")


json_data = {
    "nome": "Joe Json",
    "data_nascimento": "2001-01-01",
    "sexo": "Masculino",
    "visitas": ["2008-07-07", "2009-08-18"]
}

xml_data = """
<paciente>
    <nome>Joe XML</nome>
    <data_nascimento>1956-05-08</data_nascimento>
    <sexo>Masculino</sexo>
    <visitas>
        <visita>2023-11-11</visita>
        <visita>2024-02-01</visita>
    </visitas>
</paciente>
"""


send_json(json_data)

send_xml(xml_data)
