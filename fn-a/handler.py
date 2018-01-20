import requests

def handle(st):
    r = requests.post("http://128.110.153.209:8080/async-function/service1")

    print("service1 ran: " + r.text)
    print(st)
