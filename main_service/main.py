# coding: utf-8
from flask import Flask, request, jsonify
import re
import rpc


app = Flask(__name__)

def run_inner(ast):
    if type(ast) == int:
        return ast
    elif len(ast) == 1:
        ret = ast[0]
        if type(ret) != int:
            raise Exception('type error')
    else:
        left = run_inner(ast[0])
        right = run_inner(ast[2])
        op = ast[1]
        if op == '+':
            return rpc.add_service(left, right)
        elif op == '-':
            return rpc.sub_service(left, right)
        elif op == '*':
            return rpc.mul_service(left, right)
        elif op == '/':
            return rpc.div_service(left, right)
        else:
            raise Exception('no such function')


def run(qstr):
    tokens = rpc.lexer_service(qstr)
    ast = rpc.ast_service(tokens)
    return run_inner(ast)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return open('index.html').read()
    qstr = request.json['query']

    ret = run(qstr)
    return jsonify({'status': 'ok', 'result': ret})

@app.route('/main.js')
def mainjs():
    return open('main.js').read()


app.run(host='0.0.0.0', debug=True)
