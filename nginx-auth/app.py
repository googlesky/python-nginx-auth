from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/auth')
def auth():
    print(request.headers)
    print(request.headers.get("X-Original-Uri"))
    print(request.headers.get("Cookie"))
    return "OK", 200


@app.route('/')
def test():
    print(request.headers)
    return "OK", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
