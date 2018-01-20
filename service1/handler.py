import requests

def handle(st):
    r = requests.post("http://gateway:8080/async-function/fn-b")

    print("b ran: " + r.text)

