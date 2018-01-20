#import requests
#import json

def handle(st):
    print('fn-b function')
    print(st)
    '''
    eve={"Message":"attach_accept", "UeId":1234, "UeIdType":"1"}
    payload=json.dumps(eve)
    url = "http://128.110.153.209:8001"
    headers = {
      'content-type': "application/json"
    }
    r = requests.post(url,headers=headers,data=payload)
    print(r)
    '''
    return "attach accepted"  # Echo back the first key value
