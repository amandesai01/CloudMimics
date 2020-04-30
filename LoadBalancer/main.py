from flask import Flask, request, redirect
from .Register import register
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def balancer(path):
    print(path)
    return "<h1>Work in Progress</h1>"

if __name__ == '__main__':
    app.run(port=4999, debug=True)
    