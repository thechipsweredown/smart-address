import json
import requests

uri = "http://localhost:9200/smart_address/_search"

def match(field,term):
    query = json.dumps({
        "query": {
            "match" : {
                field : term
            }
        }
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.get(uri, data=query,headers = headers)
    results = json.loads(response.text)
    return results['hits']['hits']

