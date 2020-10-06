from flask import Flask
from flask import request
from time import sleep
import os

app = Flask(__name__)

@app.route('/endpoint')
def endpoint():
    app.logger.info(f"Received request from {request.remote_addr}")
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['APP_PORT'])
