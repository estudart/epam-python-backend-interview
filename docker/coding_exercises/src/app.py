from flask import Flask, request as req, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def say_hello():
    return jsonify({"message": "Hello world!"})

app.run(host='0.0.0.0', port=5000)