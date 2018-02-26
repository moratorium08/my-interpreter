from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify({'status': 'ok'})
    params = request.json['params']
    if len(params) > 100:
        return jsonify({'status': 'fail', 'error': 'too much args'})

    ret = 0
    for param in params:
        ret += param
    return jsonify({'status': 'ok', 'result': ret})


app.run(host='0.0.0.0')
