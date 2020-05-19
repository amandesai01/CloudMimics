from flask import Flask, jsonify
from time import sleep
import threading
import sys

app = Flask(__name__)

@app.route('/')
def route():
    '''
    Here we assume that each server takes 0.5 seconds to respond.
    '''
    sleep(0.5)
    return jsonify({"status" : "served"})

if __name__ == '__main__':
    PORT = int(sys.argv[1])
    app.run(port=PORT)