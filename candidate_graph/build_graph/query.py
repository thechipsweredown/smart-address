import json
import requests

uri = "http://localhost:9200/smart_address/_search"

def buildQuery(str,field):
    query = json.dumps({
        "from": 0, "size": 100,
        "query":{
            "match":{field : str}
        }
    })
    return query

def match(query):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(uri, data=query, headers=headers)
    results = json.loads(response.text)
    return results
