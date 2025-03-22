import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/mine_block', methods=['GET'])
def mine_block():
    return 'Mining block', 200

@app.route('/', methods=['GET'])
def is_server_running():
    return 'Server is Running Successfully', 200


# Run the app locally if not on Vercel
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
