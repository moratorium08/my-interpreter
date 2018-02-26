# coding: utf-8
from flask import Flask, request, jsonify
import re


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return open('index.html').read()
    qstr = request.json['query']

    print(qstr);

    ret = 1
    return jsonify({'status': 'ok', 'result': ret})

@app.route('/main.js')
def mainjs():
    return open('main.js').read()


app.run(host='0.0.0.0', debug=True)
