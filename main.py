import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/mine_block', methods=['GET'])
def mine_block():
    return 'Mining block', 200

@app.route('/', methods=['GET'])
def is_server_running():
    return 'Server is Running Successfully', 200

# Vercel serverless function handler
def handler(event, context):
    from flask import Request

    # Create a fake request object from the event
    with app.test_request_context(
        path=event['path'],
        method=event['httpMethod'],
        headers=event.get('headers', {}),
        data=event.get('body', '')
    ):
        # Dispatch the request to the Flask app
        response = app.full_dispatch_request()

        # Return the response in the format Vercel expects
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.data.decode('utf-8')
        }

# Run the app locally if not on Vercel
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)