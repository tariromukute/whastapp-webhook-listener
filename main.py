from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json)
    return Response(status=200)

# @app.route('/webhook', methods=['GET'])
# def get_webhook():
#     # print(request.json)
#     return Response(status=200)

# Create route to handle webhook Get request
@app.route('/webhook', methods=['GET'])
def webhook():
    # Verify token
    if request.args.get('hub.verify_token') == 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZZNEc4VUxVM0RKZ1gwb3dVT2N':
        # Respond with challenge token from request
        return request.args.get('hub.challenge')
    else:
        # Respond with '403 Forbidden' if verify tokens do not match
        return '403 Forbidden'

@app.route('/webhookx', methods=['GET'])
def get_webhook():
    return Response(status=200)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
