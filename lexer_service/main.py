# coding: utf-8
from flask import Flask, request, jsonify

app = Flask(__name__)

# 眠くて酒に酔っているので間違ってたらすんません
def lexer(qstr):
    ret = []
    current = ''
    for c in qstr:
        if ord(c) in range(48, 58):
            current += c
        elif c == ' ':
            if len(current) > 0:
                ret.append(int(current))
                current = ''
        elif c in ['(', ')', '+', '-', '*', '/']:
            if len(current) > 0:
                ret.append(int(current))
                current = ''
            ret.append(c)
        else:
            print(c)
            raise Exception('cannot interpret')
    if len(current) > 0:
        ret.append(int(current))
    return ret

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return open('index.html').read()
    qstr = request.json['query']
    try:
        ret = lexer(qstr)
    except:
        return jsonify({'status': 'fail', 'error': 'lexer error'})

    return jsonify({'status': 'ok', 'result': ret})

app.run(host='0.0.0.0')
