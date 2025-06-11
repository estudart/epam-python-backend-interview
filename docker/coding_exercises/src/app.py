from flask import Flask, request as req



app = Flask("my_api")

@app.route("/", methods=["GET"])
def index():
    return "Hello world"

@app.route("/print-message", methods=["POST"])
def print_message():
    data = req.get_json()
    return data.get("message")

app.run(host='0.0.0.0')