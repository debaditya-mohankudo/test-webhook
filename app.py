from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    GET /hello
    POST /test-webhook
    '''

@app.route('/hello')
def hello():
     return 'Hello!'


@app.route('/test-webhook', methods = ['POST']) 
def test_webhook():
    res = {'status': 'ok'}
    return jsonify(res)



if __name__ == "__main__":
    app.run(debug=True)