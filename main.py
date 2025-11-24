from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from local server!"})

@app.route("/postdata", methods=["POST"])
def post_data():
    data = request.json
    print(data)
    return jsonify({"received": data})

app.run(host="0.0.0.0", port=5000)
