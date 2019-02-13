import json
import requests

uri = "http://localhost:9200/smart_address/_search"

def buildQuery(map_entity):
    project = map_entity["project"]
    street = map_entity["street"]
    ward = map_entity["ward"]
    district = map_entity["district"]
    city = map_entity["city"]

    query = json.dumps({

    })

def matchMultiFields(query):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(uri, data=query, headers=headers)
    results = json.loads(response.text)
    return results
