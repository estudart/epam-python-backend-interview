from flask import Flask, request as req, jsonify



app = Flask("my-api")

@app.route("/", methods=['GET'])
def say_hello():
    return jsonify({"message": "Hello World"})

app.run(host='0.0.0.0', port=5000)