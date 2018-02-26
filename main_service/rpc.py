import requests
import settings
import json

def call(endpoint, data):
    headers = {'Content-type': 'application/json'}
    res = requests.post(endpoint, data=json.dumps(data), headers=headers)
    return json.loads(res.text)['result']


def add_service(x, y):
    data = {'params': [x, y]}
    return call(settings.add_service, data)


def mul_service(x, y):
    data = {'params': [x, y]}
    return call(settings.mul_service, data)


def sub_service(x, y):
    data = {'params': [x, y]}
    return call(settings.sub_service, data)


def div_service(x, y):
    data = {'params': [x, y]}
    return call(settings.div_service, data)


def lexer_service(query):
    data = {'query': query}
    return call(settings.lexer_service, data)


def ast_service(tokens):
    data = {'query': tokens}
    return call(settings.ast_service, data)


# print(call('http://127.0.0.1:5000', {"query": [1, "*", 2, "+", 3]}))
