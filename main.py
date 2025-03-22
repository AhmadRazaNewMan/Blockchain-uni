import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/mine_block', methods=['GET'])
def mine_block():
    return 'Mining block', 200

@app.route('/', methods=['GET'])
def is_server_running():
    return 'Server is Running Successfully', 200









# Vercel requires a serverless function handler
def handler(event, context):
    from flask import request

    with app.app_context():
        # Simulate a Flask request
        path = event['path']
        method = event['httpMethod']
        headers = event.get('headers', {})
        body = event.get('body', '')

        # Create a Flask test client
        with app.test_client() as client:
            response = client.open(
                path=path,
                method=method,
                headers=headers,
                data=body
            )

            return {
                'statusCode': response.status_code,
                'headers': dict(response.headers),
                'body': response.data.decode('utf-8')
            }

# Run the app locally if not on Vercel
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)