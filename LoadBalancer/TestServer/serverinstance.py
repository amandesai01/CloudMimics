from flask import Flask, jsonify
from time import sleep

app = Flask(__name__)

@app.route('/')
def route():
    sleep(0.5)
    return jsonify({"status" : "served"})