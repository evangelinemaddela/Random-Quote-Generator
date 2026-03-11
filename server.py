from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/quote")
def get_quote():
    response = requests.get("https://api.quotable.io/random", verify=False)
    data = response.json()

    return jsonify({
        "content": data["content"],
        "author": data["author"]
    })

if __name__ == "__main__":
    app.run(debug=True)