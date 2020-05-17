from flask import Flask, jsonify
from time import sleep
import threading

app = Flask(__name__)

PORT = 5005

@app.route('/')
def route():
    '''
    Here we assume that each server takes 0.5 seconds to respond.
    '''
    sleep(0.5)
    return jsonify({"status" : "served"})

if __name__ == '__main__':
    app.run(port=PORT)