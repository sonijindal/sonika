import requests

def handle(st):
    r = requests.post("http://128.110.153.209:8080/async-function/fn-b")

    print("b ran: " + r.text)

