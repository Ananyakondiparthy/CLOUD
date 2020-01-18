#!/usr/bin/python3
from flask import Flask, request
import socket
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return "Hello world, {}".format(socket.gethostname())

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=80)

