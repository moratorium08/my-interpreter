from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify({'status': 'ok'})
    params = request.json['params']
    if len(params) != 2:
        return jsonify({'status': 'fail', 'error': 'invalid args'})

    ret = params[0] - params[1]
    return jsonify({'status': 'ok', 'result': ret})


app.run(host='0.0.0.0')
