# coding: utf-8
from flask import Flask, request, jsonify

app = Flask(__name__)

class Leaf:
    def __init__(self, c):
        self.c = c

    def to_list(s):
        return s.c


class BinTree:
    def __init__(self, op, t1, t2):
        self.op = op
        self.t1 = t1
        self.t2 = t2

    def to_list(s):
        ret = [s.t1.to_list(), s.op, s.t2.to_list()]
        return ret


def split_par(tokens):
    if len(tokens) == 0:
        raise Exception('invalid syntax')
    elif len(tokens) == 1:
        token = tokens[0]
        if type(token) != int:
            raise Exception('invalid syntax')
        return Leaf(token)

    st = -1
    cnt = 0
    left = None
    for i, token in enumerate(tokens):
        if cnt == 0 and token in ['*', '/']:
            if i == len(tokens) - 1 or i == 0:
                raise Exception('invalid syntax')
            token = tokens[i]
            left = split_par(tokens[:i])
            right = split_par(tokens[i + 1:])
            return BinTree(token, left, right)
        elif token == '(':
            if cnt == 0:
                st = i
            cnt += 1
        elif token == ')':
            cnt -= 1
            if cnt < 0:
                raise Exception('invalid syntax')
            elif cnt == 0:
                if i == len(tokens) - 1:
                    return split_add_sub(tokens[1:i])
                if i == len(tokens) - 2:
                    raise Exception('invalid syntax')
                token = tokens[i + 1]
                left = split_add_sub(tokens[1:i])
                right = split_par(tokens[i + 2:])
                return BinTree(token, left, right)
        elif type(token) == int:
            continue

    raise Exception('not supported')


def split_add_sub(tokens):
    if len(tokens) == 1:
        token = tokens[0]
        if type(token) != int:
            raise Exception('invalid syntax')
        return Leaf(token)

    par_cnt = 0
    for i, token in enumerate(tokens):
        if par_cnt == 0 and token in ['+', '-']:
            if i == len(tokens) - 1 or i == 0:
                raise Exception('invalid syntax')
            left = split_par(tokens[:i])
            right = split_add_sub(tokens[i + 1:])
            return BinTree(token, left, right)
        elif token == '(':
            par_cnt += 1
        elif token == ')':
            par_cnt -= 1
    return split_par(tokens)

def gen_ast(tokens):
    return split_add_sub(tokens).to_list()

print(gen_ast([1, '+', 2, '-', 3]))
print(gen_ast(['(', 1, '+', 2, ')',  '-', 3]))
print(gen_ast([1, '*', '(', 2, '+', 3, ')']))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return open('index.html').read()
    q = request.json['query']
    try:
        ret = gen_ast(q)
    except:
        return jsonify({'status': 'fail', 'error': 'ast error'})

    return jsonify({'status': 'ok', 'result': ret})

app.run(host='0.0.0.0')
