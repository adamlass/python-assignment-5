from flask import Flask, request, jsonify, abort, make_response
app = Flask(__name__)

SERVER_PASSWORD = "Xy"

@app.route('/', methods=['POST'])
def check_password():
    client_password = request.json["password"]
    
    if(client_password == SERVER_PASSWORD):
        return "Welcome!"
    else:
        abort(403)