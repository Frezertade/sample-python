from flask import Flask
import pymongo

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello there"


if __name__:
    app.run(port=8787, debug=True)
