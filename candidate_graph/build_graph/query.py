import json
import requests

uri = "http://localhost:9200/smart_address/_search"

def buildQuery(map_entity):
    project = map_entity.get("project","")
    street = map_entity.get("street","")
    ward = map_entity.get("ward","")
    district = map_entity.get("dist","")
    city = map_entity.get("city","")
    query = json.dumps({
        "from": 0, "size": 100,
        "query":{
            "bool":{
                "should":[
                    {"match":{"street" : street}},
                    {"match":{"project" : project}},
                    {"match":{ "ward" : ward}},
                    {"match":{"district" : district}},
                    {"match": {"city" : city} }
                ]
            }
        }
    })
    return query

def matchMultiFields(query):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(uri, data=query, headers=headers)
    results = json.loads(response.text)
    return results
